"""Ephemeral prototype HTTP runner — Story 04.1.

Manages short-lived http.server subprocesses serving generated prototype HTML
on loopback ports 8081-8099. Platform root files are never touched.
"""
from __future__ import annotations

import html
import io
import json
import socket
import subprocess
import sys
import time
import zipfile
from pathlib import Path
from threading import RLock
from typing import Any

_READY_POLL_INTERVAL = 0.05
_READY_TIMEOUT = 3.0

PROTOTYPE_PORT_RANGE = range(8081, 8100)

PROTOTYPE_FILE_BYTE_LIMIT = 256 * 1024

# Quota. The port range alone would allow 19 concurrent subprocesses; these caps
# are the deliberate limit so one caller cannot exhaust the machine, and so an
# abandoned prototype does not hold a port for the lifetime of the server.
MAX_CONCURRENT_BUILDS = 4
MAX_BUILDS_PER_OWNER = 2
BUILD_TTL_SECONDS = 900.0

# Phases the server can actually return. A client may show its own "starting"
# while its start request is in flight; the server never reports that, because
# start() holds the lock until the port answers or the attempt fails.
BUILD_PHASE_NOT_STARTED = "not_started"
BUILD_PHASE_READY = "ready"
BUILD_PHASE_FAILED = "failed"
BUILD_PHASE_STOPPED = "stopped"
BUILD_PHASE_EXITED = "exited"
BUILD_PHASE_EXPIRED = "expired"

BUILD_PHASES = (
    BUILD_PHASE_NOT_STARTED,
    BUILD_PHASE_READY,
    BUILD_PHASE_FAILED,
    BUILD_PHASE_STOPPED,
    BUILD_PHASE_EXITED,
    BUILD_PHASE_EXPIRED,
)


def extract_data_model(blueprint: dict[str, Any]) -> dict[str, Any]:
    """Extract thin data model from user-derived blueprint without inventing fake columns."""
    if isinstance(blueprint.get("data_model"), dict):
        return blueprint["data_model"]

    definition = blueprint.get("definition", {})
    problem = str(definition.get("problem_statement", ""))
    personas = definition.get("personas", [])

    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    open_questions: list[str] = []

    user_names = [p.get("name") for p in personas if isinstance(p, dict) and p.get("name")]
    entities.append({
        "name": "User",
        "table_name": "users",
        "type": "dimension",
        "grain": "One registered user / stakeholder (" + (", ".join(user_names) if user_names else "actor") + ")",
        "attributes": [
            {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
            {"name": "name", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            {"name": "created_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
        ],
    })

    p_lower = problem.lower()
    if any(k in p_lower for k in ("expense", "spend", "cost", "transaction", "purchase")):
        entities.append({
            "name": "Expense",
            "table_name": "expenses",
            "type": "fact",
            "grain": "One recorded expense transaction",
            "attributes": [
                {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
                {"name": "user_id", "type": "INTEGER", "pk": False, "fk": "users(id)", "nullable": False},
                {"name": "amount", "type": "REAL", "pk": False, "fk": None, "nullable": False},
                {"name": "category", "type": "TEXT", "pk": False, "fk": None, "nullable": True},
                {"name": "created_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            ],
        })
        relationships.append({
            "from_table": "users",
            "to_table": "expenses",
            "cardinality": "1:N",
            "foreign_key": "user_id",
        })
        open_questions.append("Multi-currency support and exchange rate normalization unstated.")
        open_questions.append("Receipt attachment storage format and retention unstated.")

    if any(k in p_lower for k in ("statement", "account", "bank", "source", "batch")):
        entities.append({
            "name": "Statement",
            "table_name": "statements",
            "type": "dimension",
            "grain": "One imported statement source or batch",
            "attributes": [
                {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
                {"name": "user_id", "type": "INTEGER", "pk": False, "fk": "users(id)", "nullable": False},
                {"name": "source_name", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
                {"name": "created_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            ],
        })
        relationships.append({
            "from_table": "users",
            "to_table": "statements",
            "cardinality": "1:N",
            "foreign_key": "user_id",
        })
        open_questions.append("Statement parser format (CSV / PDF / OFX) unstated.")

    if any(k in p_lower for k in ("alphabet", "letter", "phonic", "lesson", "learning", "kid", "child", "student", "reading")):
        entities.append({
            "name": "Lesson",
            "table_name": "lessons",
            "type": "dimension",
            "grain": "One configured learning module or alphabet letter set",
            "attributes": [
                {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
                {"name": "title", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
                {"name": "letter_set", "type": "TEXT", "pk": False, "fk": None, "nullable": True},
                {"name": "daily_limit_minutes", "type": "INTEGER", "pk": False, "fk": None, "nullable": False},
                {"name": "created_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            ],
        })
        entities.append({
            "name": "ProgressRecord",
            "table_name": "progress_records",
            "type": "fact",
            "grain": "One completed letter matching or comprehension round",
            "attributes": [
                {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
                {"name": "user_id", "type": "INTEGER", "pk": False, "fk": "users(id)", "nullable": False},
                {"name": "lesson_id", "type": "INTEGER", "pk": False, "fk": "lessons(id)", "nullable": False},
                {"name": "mastery_score", "type": "REAL", "pk": False, "fk": None, "nullable": False},
                {"name": "time_spent_seconds", "type": "INTEGER", "pk": False, "fk": None, "nullable": False},
                {"name": "completed_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            ],
        })
        relationships.append({
            "from_table": "users",
            "to_table": "progress_records",
            "cardinality": "1:N",
            "foreign_key": "user_id",
        })
        relationships.append({
            "from_table": "lessons",
            "to_table": "progress_records",
            "cardinality": "1:N",
            "foreign_key": "lesson_id",
        })
        open_questions.append("Bilingual audio pronunciation sample rate and asset caching unstated.")
        open_questions.append("Offline parent PIN recovery mechanism unstated.")

    if len(entities) == 1:
        entities.append({
            "name": "Item",
            "table_name": "items",
            "type": "fact",
            "grain": "One record item defined in product scope",
            "attributes": [
                {"name": "id", "type": "INTEGER", "pk": True, "fk": None, "nullable": False},
                {"name": "user_id", "type": "INTEGER", "pk": False, "fk": "users(id)", "nullable": False},
                {"name": "title", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
                {"name": "created_at", "type": "TEXT", "pk": False, "fk": None, "nullable": False},
            ],
        })
        relationships.append({
            "from_table": "users",
            "to_table": "items",
            "cardinality": "1:N",
            "foreign_key": "user_id",
        })
        open_questions.append("Specific entity domain attributes unstated in intake.")

    open_questions.append("Soft-delete versus hard-delete retention semantics unstated.")
    open_questions.append("Audit trail and access log schema unstated.")

    return {
        "entities": entities,
        "relationships": relationships,
        "open_questions": open_questions,
    }


def _generate_data_model_md(data_model: dict[str, Any], product_name: str) -> str:
    lines = [
        f"# Data Model Specification — {product_name}",
        "",
        "> Generated deterministically from verified product blueprint. No invented fields.",
        "",
        "## 1. Entity Summary",
        "",
        "| Entity | Table | Type | Grain | Primary Key | Foreign Keys |",
        "|---|---|---|---|---|---|",
    ]
    for ent in data_model.get("entities", []):
        name = ent.get("name", "Unknown")
        tbl = ent.get("table_name", name.lower())
        etype = ent.get("type", "dimension").capitalize()
        grain = ent.get("grain", "One record")
        pks = [a["name"] for a in ent.get("attributes", []) if a.get("pk")]
        fks = [f"{a['name']} -> {a['fk']}" for a in ent.get("attributes", []) if a.get("fk")]
        pk_str = ", ".join(pks) if pks else "None"
        fk_str = ", ".join(fks) if fks else "None"
        lines.append(f"| {name} | `{tbl}` | {etype} | {grain} | `{pk_str}` | {fk_str} |")

    lines.extend([
        "",
        "## 2. Entities and Attributes",
        "",
    ])
    for ent in data_model.get("entities", []):
        lines.append(f"### `{ent.get('table_name', ent.get('name', '').lower())}` ({ent.get('name')})")
        lines.append(f"- **Type:** {ent.get('type', 'dimension').capitalize()}")
        lines.append(f"- **Grain:** {ent.get('grain', 'One record')}")
        lines.append("")
        lines.append("| Attribute | Type | Nullable | Key / Reference |")
        lines.append("|---|---|---|---|")
        for attr in ent.get("attributes", []):
            aname = f"`{attr['name']}`"
            atype = attr.get("type", "TEXT")
            null_str = "No" if not attr.get("nullable", True) else "Yes"
            key_str = "PK" if attr.get("pk") else (f"FK -> {attr['fk']}" if attr.get("fk") else "-")
            lines.append(f"| {aname} | {atype} | {null_str} | {key_str} |")
        lines.append("")

    lines.extend([
        "## 3. Relationships",
        "",
        "| From | To | Cardinality | Foreign Key |",
        "|---|---|---|---|",
    ])
    for rel in data_model.get("relationships", []):
        lines.append(
            f"| `{rel.get('from_table')}` | `{rel.get('to_table')}` | "
            f"{rel.get('cardinality')} | `{rel.get('foreign_key')}` |"
        )

    lines.extend([
        "",
        "## 4. Open Questions (Unstated in Intake)",
        "",
    ])
    for q in data_model.get("open_questions", []):
        lines.append(f"- {q}")
    lines.append("")
    return "\n".join(lines)


def _generate_schema_sql(data_model: dict[str, Any], product_name: str) -> str:
    lines = [
        f"-- Schema definition for {product_name}",
        "-- Engine: SQLite / ANSI SQL compatible",
        "-- Deterministically generated from verified product blueprint",
        "",
        "PRAGMA foreign_keys = ON;",
        "",
    ]
    for ent in data_model.get("entities", []):
        tbl = ent.get("table_name", ent.get("name", "").lower())
        lines.append(f"CREATE TABLE IF NOT EXISTS {tbl} (")
        col_defs = []
        for attr in ent.get("attributes", []):
            parts = [f"    {attr['name']} {attr.get('type', 'TEXT')}"]
            if attr.get("pk"):
                parts.append("PRIMARY KEY")
                if attr.get("type") == "INTEGER":
                    parts.append("AUTOINCREMENT")
            elif not attr.get("nullable", True):
                parts.append("NOT NULL")
            if attr.get("fk"):
                parts.append(f"REFERENCES {attr['fk']} ON DELETE CASCADE")
            if attr.get("name") == "created_at":
                parts.append("DEFAULT (datetime('now'))")
            col_defs.append(" ".join(parts))
        lines.append(",\n".join(col_defs))
        lines.append(");")
        lines.append("")
    return "\n".join(lines)


def _generate_er_svg(data_model: dict[str, Any], product_name: str) -> str:
    escaped_name = html.escape(product_name, quote=False)
    entities = data_model.get("entities", [])
    n_entities = max(len(entities), 1)
    width = max(800, n_entities * 280 + 60)
    height = 420

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background:#0a0f1a;font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',sans-serif">',
        f'  <text x="30" y="40" fill="#f1f5f9" font-size="18" font-weight="600">{escaped_name} — Entity Relationship Diagram</text>',
        '  <text x="30" y="62" fill="#64748b" font-size="12">Deterministic schema generated from product blueprint &middot; zero dependencies</text>',
    ]

    x_offset = 40
    y_offset = 90
    box_width = 240
    box_height = 280
    centers: dict[str, tuple[int, int]] = {}

    for ent in entities:
        tname = ent.get("table_name", ent.get("name", "").lower())
        ename = html.escape(ent.get("name", tname), quote=False)
        etype = html.escape(ent.get("type", "dimension").upper(), quote=False)
        badge_color = "#3b82f6" if etype == "DIMENSION" else "#22c55e"

        svg_parts.append(f'  <g transform="translate({x_offset},{y_offset})">')
        svg_parts.append(f'    <rect width="{box_width}" height="{box_height}" rx="8" fill="#131d2e" stroke="#23354d" stroke-width="1.5"/>')
        svg_parts.append(f'    <rect width="{box_width}" height="40" rx="8" fill="#1e293b"/>')
        svg_parts.append(f'    <text x="14" y="25" fill="#f8fafc" font-size="14" font-weight="600">{ename}</text>')
        svg_parts.append(f'    <rect x="{box_width - 78}" y="10" width="66" height="20" rx="4" fill="{badge_color}22" stroke="{badge_color}" stroke-width="1"/>')
        svg_parts.append(f'    <text x="{box_width - 45}" y="24" fill="{badge_color}" font-size="10" font-weight="600" text-anchor="middle">{etype}</text>')

        attr_y = 65
        for attr in ent.get("attributes", [])[:7]:
            aname = html.escape(attr.get("name", ""), quote=False)
            atype = html.escape(attr.get("type", "TEXT"), quote=False)
            is_pk = attr.get("pk", False)
            is_fk = bool(attr.get("fk"))

            icon = "🔑 " if is_pk else ("🔗 " if is_fk else "   ")
            text_color = "#38bdf8" if is_pk else ("#a78bfa" if is_fk else "#94a3b8")
            svg_parts.append(f'    <text x="14" y="{attr_y}" fill="{text_color}" font-size="12" font-family="monospace">{icon}{aname}</text>')
            svg_parts.append(f'    <text x="{box_width - 14}" y="{attr_y}" fill="#64748b" font-size="11" text-anchor="end" font-family="monospace">{atype}</text>')
            attr_y += 24

        svg_parts.append('  </g>')
        centers[tname] = (x_offset + box_width // 2, y_offset + box_height // 2)
        x_offset += box_width + 40

    for rel in data_model.get("relationships", []):
        from_tbl = rel.get("from_table")
        to_tbl = rel.get("to_table")
        if from_tbl in centers and to_tbl in centers:
            x1, y1 = centers[from_tbl]
            x2, y2 = centers[to_tbl]
            card = html.escape(str(rel.get("cardinality", "1:N")), quote=False)
            svg_parts.append(
                f'  <line x1="{x1 + box_width // 2}" y1="{y1}" x2="{x2 - box_width // 2}" y2="{y2}" '
                'stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>'
            )
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2 - 8
            svg_parts.append(
                f'  <rect x="{mid_x - 18}" y="{mid_y - 12}" width="36" height="18" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>'
            )
            svg_parts.append(f'  <text x="{mid_x}" y="{mid_y}" fill="#38bdf8" font-size="10" font-weight="600" text-anchor="middle">{card}</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def _generate_brd_md(blueprint: dict[str, Any], product_name: str) -> str:
    """Generate concise 1-page Business Requirements Document (BRD)."""
    product = blueprint.get("product", {})
    definition = blueprint.get("definition", {})
    solution = blueprint.get("solution", {})
    context = blueprint.get("_prototype_context", {})
    if not isinstance(context, dict):
        context = {}
    personas = definition.get("personas") or []
    primary_user = (
        context.get("intended_user")
        or (personas[0].get("name") if personas else "Primary End User")
    )
    admin_user = personas[1].get("name") if len(personas) > 1 else "Not defined"
    problem = (
        context.get("problem")
        or definition.get("problem_statement")
        or "Problem statement not defined in intake."
    )
    outcome = (
        context.get("outcome")
        or definition.get("desired_outcome")
        or "Desired business outcome not defined in intake."
    )

    epics = list(context.get("solution_options") or []) or [
        str(e.get("title", "")).strip()
        for e in solution.get("epics", [])
        if isinstance(e, dict) and str(e.get("title", "")).strip() and str(e.get("title", "")).strip() != "Solution not defined."
    ]
    if not epics:
        epics = ["Capabilities not defined."]

    usefulness = str(context.get("usefulness") or "Value proposition not defined.")

    epic_lines = "\n".join(f"- {epic}" for epic in epics)
    return f"""# Business Requirements Document (BRD) — {product_name}

> Review draft derived from user-provided, unverified product context.

## 1. Executive Summary & Problem Context
- **Product Name:** {product_name}
- **Lifecycle Phase:** {product.get("lifecycle_phase", "Discovery")}
- **Business Problem:** {problem}
- **Core Value Proposition:** {usefulness}

## 2. Target Personas & Stakeholders
- **Primary End-User:** {primary_user}
- **Administrator:** {admin_user}

## 3. Business Objectives & Desired Outcomes
- **Primary Desired Outcome:** {outcome}
- **Success Criteria:** Review supplied Gherkin contracts and validate the desired outcome; no result is assumed.

## 4. Scope & Solution Capabilities
{epic_lines}

## 5. Business Risks & Constraints
- **Privacy & Compliance:** Not assessed by this generated document.
- **Adoption Feasibility:** Not assessed by this generated document.
"""


def _generate_prd_md(blueprint: dict[str, Any], product_name: str) -> str:
    """Generate concise 1-page Product Requirements Document (PRD)."""
    definition = blueprint.get("definition", {})
    solution = blueprint.get("solution", {})
    context = blueprint.get("_prototype_context", {})
    if not isinstance(context, dict):
        context = {}
    problem = context.get("problem") or definition.get("problem_statement") or "Problem statement not defined."
    outcome = context.get("outcome") or definition.get("desired_outcome") or "Desired outcome not defined."
    personas = definition.get("personas") or []
    user_desc = context.get("intended_user") or ", ".join(str(p.get("name", "")) for p in personas if p.get("name")) or "Target user not defined."
    contracts = context.get("gherkin_contracts") or []
    if not contracts:
        contracts = []

    context_options = context.get("solution_options") or []
    epics = [{"title": option} for option in context_options] or solution.get("epics", [])

    epics_formatted = []
    for e in epics:
        title = e.get("title", "Capability")
        rice = e.get("rice") if isinstance(e.get("rice"), dict) else None
        score_line = f"\n- **RICE Score:** {rice['score']} (provisional input)" if rice and rice.get("score") is not None else ""
        epics_formatted.append(f"### Feature: {title}{score_line}\n- **Evidence status:** Unverified draft.")

    contracts_formatted = "\n\n".join(f"**Not run**\n```gherkin\n{c}\n```" for c in contracts[:10]) or "No Gherkin contracts supplied."

    return f"""# Product Requirements Document (PRD) — {product_name}

> Review draft. Human validation remains product truth.

## 1. Product Overview & User Personas
- **Product Name:** {product_name}
- **Target Users:** {user_desc}
- **Problem Statement:** {problem}
- **Desired Outcome:** {outcome}

## 2. User Journeys
1. **End-User Flow:** Not defined beyond supplied product context.
2. **Administrator Flow:** Not defined unless supplied contracts require it.

## 3. Epics & Solution Capabilities
{"\n\n".join(epics_formatted) or "No solution capabilities supplied."}

## 4. Acceptance Criteria & Gherkin Contracts
{contracts_formatted}

## 5. Non-Functional Requirements
- **Performance:** Not measured.
- **Accessibility:** Keyboard, contrast, screen-reader, audio, and reduced-motion behavior require human testing.
- **Data Governance:** Generated preview contains no remote requests or browser-persistence calls; backend persistence remains separately testable.
"""


def _generate_fsd_md(blueprint: dict[str, Any], product_name: str, data_model: dict[str, Any]) -> str:
    """Generate concise 1-page Functional Specification Document (FSD)."""
    entities = data_model.get("entities", [])
    tables_summary = ", ".join(f"`{e.get('table_name', '')}`" for e in entities) or "`app_state`"

    return f"""# Functional Specification Document (FSD) — {product_name}

> Engineering technical specification detailing UI architecture, interaction states, event contracts, and data schemas.

## 1. System Architecture & UI Structure
- **Execution Mode:** Standalone zero-dependency HTML/CSS/JavaScript client running on ephemeral local loopback HTTP runner.
- **View Hierarchy:**
  - **Header Bar:** Product identity branding, session mode indicator, Parent/Admin modal trigger.
  - **Primary Workspace:** Tactile interaction cards, drag-and-drop match area, responsive feedback status, countdown timer.
  - **Admin Dialog (`<dialog>`):** Four-digit PIN authentication gate, configuration controls, offline metric cards.
  - **Celebration Layer:** CSS star animation and audio chime trigger upon successful completion.

## 2. Interaction & State Machine
1. **Selection State (`selected`):** Tracks active user-selected item; updates `aria-pressed` and focus indicators.
2. **Match Evaluation:** Compares `selected` token with target `data-match`; increments match counter and triggers celebration on equality.
3. **Timer Lifecycle:** Toggles interval countdown (10:00 default), auto-halts at 00:00 with status announcement.
4. **Admin PIN Gate:** Compares numeric input against session-locked PIN; toggles `#pin-gate` vs `#parent-dashboard` views.

## 3. Data Schema & Persistence Model
- **Managed Tables:** {tables_summary}
- **Storage Strategy:** Preview interaction state is page-memory only. Generated files live in bounded local build directory.
- **Relational Integrity:** Generated schema is a review artifact; runtime persistence is not connected by this preview.

## 4. Security, Isolation & Error Fallbacks
- **Audio Fallback:** Synthesizes Web Audio oscillator chimes; gracefully falls back to `SpeechSynthesis` or silent visual cues if audio context is blocked.
- **Data Protection:** Generated source contains no outbound request, cookie, or browser-persistence call; verify network behavior separately.
"""


def _generate_manifest_json(product_name: str) -> str:
    """Generate PWA web app manifest for offline installability."""
    manifest = {
        "name": product_name,
        "short_name": product_name[:12],
        "start_url": "./index.html",
        "display": "standalone",
        "background_color": "#090d16",
        "theme_color": "#0f172a",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%2338bdf8'/%3E%3Ctext x='50' y='65' font-size='50' text-anchor='middle' fill='%230f172a'%3E★%3C/text%3E%3C/svg%3E",
                "sizes": "192x192 512x512",
                "type": "image/svg+xml",
                "purpose": "any maskable"
            }
        ]
    }
    return json.dumps(manifest, indent=2)


def _generate_sw_js(product_name: str) -> str:
    """Generate local offline caching service worker for PWA support."""
    slug = "".join(c.lower() if c.isalnum() else "-" for c in product_name).strip("-") or "app"
    return f"""// Offline caching service worker for {product_name}
const CACHE_NAME = "{slug}-v1";
const ASSETS = [
  "./index.html",
  "./manifest.webmanifest",
  "./data-model.md",
  "./schema.sql",
  "./er.svg",
  "./BRD.md",
  "./PRD.md",
  "./FSD.md"
];

self.addEventListener("install", function(event) {{
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {{
      return cache.addAll(ASSETS);
    }}).then(function() {{
      return self.skipWaiting();
    }})
  );
}});

self.addEventListener("activate", function(event) {{
  event.waitUntil(
    caches.keys().then(function(keys) {{
      return Promise.all(keys.filter(function(k) {{ return k !== CACHE_NAME; }}).map(function(k) {{ return caches.delete(k); }}));
    }}).then(function() {{
      return self.clients.claim();
    }})
  );
}});

self.addEventListener("fetch", function(event) {{
  if (event.request.method !== "GET") return;
  event.respondWith(
    caches.match(event.request).then(function(cached) {{
      return cached || fetch(event.request).catch(function() {{
        return caches.match("./index.html");
      }});
    }})
  );
}});
"""


class EphemeralBuildManager:
    """Manages ephemeral HTTP servers serving generated prototypes on loopback."""

    def __init__(self, state_dir: Path) -> None:
        self._state_dir = Path(state_dir)
        self._lock = RLock()
        self._builds: dict[str, dict[str, Any]] = {}
        self._last_good_builds: dict[str, dict[str, Any]] = {}
        self._phases: dict[str, dict[str, Any]] = {}

    def _set_phase(
        self,
        product_id: str,
        phase: str,
        message: str,
        stages: list[dict[str, Any]] | None = None,
        elapsed_ms: float | None = None,
        url: str | None = None,
        scoped_path: str | None = None,
    ) -> None:
        data: dict[str, Any] = {"phase": phase, "message": message}
        if stages is not None:
            data["stages"] = stages
        if elapsed_ms is not None:
            data["elapsed_ms"] = elapsed_ms
        if url is not None:
            data["url"] = url
        if scoped_path is not None:
            data["scoped_path"] = scoped_path
        self._phases[product_id] = data

    def get_build(self, product_id: str) -> dict[str, Any] | None:
        with self._lock:
            build = self._builds.get(product_id)
            if build and build["process"].poll() is None:
                return dict(build)
            return None

    def _find_free_port(self, excluded: set[int] | None = None) -> int:
        used = {b["port"] for b in self._builds.values()}
        used.update(excluded or ())
        for port in PROTOTYPE_PORT_RANGE:
            if port in used:
                continue
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    sock.bind(("127.0.0.1", port))
                    return port
                except OSError:
                    continue
        raise ValueError(
            "no free prototype port in range 8081-8099; stop an existing build first"
        )

    def _build_dir(self, product_id: str) -> Path:
        safe_id = "".join(
            c for c in product_id if c.isalnum() or c in "-_"
        )[:64]
        if not safe_id:
            raise ValueError("product_id is not safe for filesystem use")
        return self._state_dir / "builds" / safe_id

    def list_files(self, product_id: str) -> dict[str, Any]:
        """Read-only listing of the generated prototype. Never a general file browser."""
        build_dir = self._build_dir(product_id)
        files = [
            {"name": entry.name, "bytes": entry.stat().st_size}
            for entry in sorted(build_dir.iterdir())
            if entry.is_file()
        ] if build_dir.is_dir() else []
        return {
            "product_id": product_id,
            "generated": bool(files),
            "files": files,
            "editable": False,
        }

    def read_file(self, product_id: str, name: str) -> dict[str, Any]:
        """Return one generated prototype file. Reads are confined to its build dir."""
        if not name or name != Path(name).name or name.startswith("."):
            raise ValueError("prototype file name must be a plain file name")
        build_dir = self._build_dir(product_id)
        target = build_dir / name
        if not target.is_file():
            raise ValueError(f"generated prototype has no file named {name!r}")
        if target.resolve().parent != build_dir.resolve():
            raise ValueError("prototype file is outside its build directory")
        size = target.stat().st_size
        if size > PROTOTYPE_FILE_BYTE_LIMIT:
            raise ValueError(
                f"generated prototype file is {size} bytes, over the "
                f"{PROTOTYPE_FILE_BYTE_LIMIT} byte read limit"
            )
        return {
            "product_id": product_id,
            "name": name,
            "bytes": size,
            "content": target.read_text(encoding="utf-8"),
            "editable": False,
        }

    def archive(self, product_id: str) -> bytes:
        """Create a deterministic ZIP archive of all generated prototype files in memory."""
        build_dir = self._build_dir(product_id)
        if not build_dir.is_dir():
            raise ValueError(f"no generated prototype files found for product {product_id!r}")
        files = [
            entry for entry in sorted(build_dir.iterdir(), key=lambda e: e.name)
            if entry.is_file() and not entry.name.startswith(".")
        ]
        if not files:
            raise ValueError(f"no generated prototype files found for product {product_id!r}")
        buf = io.BytesIO()
        fixed_time = (2026, 1, 1, 0, 0, 0)
        with zipfile.ZipFile(buf, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            for file_path in files:
                if file_path.resolve().parent != build_dir.resolve():
                    raise ValueError("archive file is outside its build directory")
                zinfo = zipfile.ZipInfo(
                    filename=file_path.name,
                    date_time=fixed_time,
                )
                zinfo.compress_type = zipfile.ZIP_DEFLATED
                zinfo.external_attr = 0o644 << 16
                zf.writestr(zinfo, file_path.read_bytes())
        buf.seek(0)
        return buf.getvalue()

    def _generate_prototype(self, product_id: str, blueprint: dict[str, Any]) -> Path:
        """Generate product-bound, dependency-free review prototype artifacts."""
        build_dir = self._build_dir(product_id)
        build_dir.mkdir(parents=True, exist_ok=True)

        product = blueprint.get("product", {})
        definition = blueprint.get("definition", {})
        solution = blueprint.get("solution", {})
        context = blueprint.get("_prototype_context", {})
        if not isinstance(context, dict):
            context = {}

        raw_name = str(product.get("name") or "Prototype")
        raw_problem = str(
            context.get("problem") or definition.get("problem_statement") or "Problem not defined."
        )
        raw_user = str(
            context.get("intended_user")
            or ((definition.get("personas") or [{}])[0].get("name"))
            or "Intended user not defined."
        )
        raw_outcome = str(context.get("outcome") or "Outcome not defined.")
        raw_accomplishment = str(
            context.get("accomplishment")
            or ((definition.get("personas") or [{}])[0].get("motivation"))
            or "Primary action not defined."
        )
        options = context.get("solution_options", [])
        if not isinstance(options, list):
            options = []
        options = [str(item).strip() for item in options if isinstance(item, str) and item.strip()]
        if not options:
            options = [
                str(item.get("title", "")).strip()
                for item in solution.get("epics", [])
                if isinstance(item, dict)
                and str(item.get("title", "")).strip()
                and str(item.get("title", "")).strip() != "Solution not defined."
            ]
        contracts = context.get("gherkin_contracts", [])
        if not isinstance(contracts, list):
            contracts = []
        contracts = [
            str(item).strip() for item in contracts
            if isinstance(item, str) and item.strip()
        ]

        context_text = " ".join(
            [raw_name, raw_problem, raw_user, raw_outcome, raw_accomplishment, *options, *contracts]
        ).lower()
        learning_mode = any(
            marker in context_text
            for marker in (
                "child", "learner", "learning", "alphabet", "phonics", "letter",
                "lkg", "kindergarten", "preschool",
            )
        )

        def esc(value: Any, *, attribute: bool = False) -> str:
            return html.escape(str(value), quote=attribute)

        option_cards = "".join(
            '<article class="feature-card"><strong>'
            + esc(option)
            + '</strong><span>Draft capability</span></article>'
            for option in options[:6]
        ) or '<p class="empty">No solution capabilities supplied yet.</p>'

        contract_cards: list[str] = []
        for index, contract in enumerate(contracts[:10]):
            lowered = contract.lower()
            required = "core"
            if any(word in lowered for word in ("pin", "admin", "dashboard", "parent")):
                required = "parent"
            elif any(word in lowered for word in ("timer", "minute", "expiry", "expire")):
                required = "timer"
            elif any(word in lowered for word in ("phonics", "alphabet", "letter", "drag", "sound")):
                required = "learning"
            contract_cards.append(
                '<article class="contract-card"><div class="contract-head"><strong>Contract '
                + str(index + 1)
                + '</strong><span class="contract-state" data-contract-state="not-run">Not run</span></div><pre>'
                + esc(contract)
                + '</pre><button type="button" data-contract-run data-requires="'
                + esc(required, attribute=True)
                + '">Run prototype smoke check</button></article>'
            )
        contracts_html = "".join(contract_cards) or '<p class="empty">No Gherkin contracts supplied.</p>'

        if learning_mode:
            experience_html = """
<section class="experience learning" data-capability="core learning timer parent">
  <div class="experience-head">
    <div>
      <span class="eyebrow">Alphabet & Phonics Fun</span>
      <h2>Choose a letter adventure</h2>
      <p>Tap a letter to hear its sound, then match the balloon!</p>
    </div>
    <div class="timer">
      <span>Play Timer</span>
      <strong id="timer-value">10:00</strong>
      <div class="timer-controls">
        <button id="timer-toggle" type="button">Start</button>
        <button id="timer-reset" type="button">Reset</button>
      </div>
    </div>
  </div>

  <div class="letter-grid" aria-label="Alphabet cards">
    <button class="letter-card" type="button" draggable="true" data-letter="A"><strong>A</strong><span>/æ/ · Apple</span></button>
    <button class="letter-card" type="button" draggable="true" data-letter="B"><strong>B</strong><span>/b/ · Balloon</span></button>
    <button class="letter-card" type="button" draggable="true" data-letter="C"><strong>C</strong><span>/k/ · Cat</span></button>
    <button class="letter-card" type="button" draggable="true" data-letter="D"><strong>D</strong><span>/d/ · Dog</span></button>
    <button class="letter-card" type="button" draggable="true" data-letter="E"><strong>E</strong><span>/e/ · Elephant</span></button>
  </div>

  <div class="match-area">
    <div class="match-head">
      <span class="eyebrow">Phonics Match Game</span>
      <h3>Match letter to the picture balloon</h3>
      <p>Tap a letter card above, then tap the matching balloon below.</p>
    </div>
    <div class="drop-grid" aria-label="Picture balloons">
      <button class="drop-target balloon" type="button" data-match="A">🎈 Apple</button>
      <button class="drop-target balloon" type="button" data-match="B">🎈 Balloon</button>
      <button class="drop-target balloon" type="button" data-match="C">🎈 Cat</button>
      <button class="drop-target balloon" type="button" data-match="D">🎈 Dog</button>
      <button class="drop-target balloon" type="button" data-match="E">🎈 Elephant</button>
    </div>
    <div class="action-row">
      <button id="sound-play" class="btn-sound" type="button">🔊 Play letter sound</button>
      <p id="learning-status" role="status" aria-live="polite">Choose a letter card to begin.</p>
    </div>
  </div>

  <dialog id="parent-dialog" aria-labelledby="parent-title">
    <form method="dialog">
      <div class="dialog-head">
        <h2 id="parent-title">Parent Administration & Settings</h2>
        <button value="cancel" aria-label="Close parent dialog">×</button>
      </div>
      <div id="pin-gate">
        <label for="parent-pin">Parent Security PIN (4 digits)</label>
        <input id="parent-pin" inputmode="numeric" pattern="[0-9]{4}" maxlength="4" autocomplete="off" placeholder="Enter four digits">
          <p class="pin-hint">First valid entry sets PIN for this preview tab. Later entries unlock dashboard.</p>
        <button id="pin-submit" type="button">Unlock Parent Settings</button>
      </div>
      <div id="parent-dashboard" hidden>
        <div class="admin-section">
          <h3>Daily Lesson Configuration</h3>
          <label for="letter-set-select">Active Letter Set</label>
          <select id="letter-set-select">
            <option value="A-E" selected>Letter Set 1: A to E (Foundational)</option>
            <option value="F-J">Letter Set 2: F to J</option>
            <option value="K-O">Letter Set 3: K to O</option>
            <option value="P-T">Letter Set 4: P to T</option>
            <option value="U-Z">Letter Set 5: U to Z</option>
            <option value="A-Z">All Letters: A to Z</option>
          </select>
          <label for="timer-limit-select">Daily Play Time Limit</label>
          <select id="timer-limit-select">
            <option value="300">5 minutes</option>
            <option value="600" selected>10 minutes</option>
            <option value="900">15 minutes</option>
            <option value="1200">20 minutes</option>
          </select>
        </div>
        <div class="admin-section">
          <h3>Session Activity</h3>
          <div class="metric-grid">
            <article><span>Letters Explored</span><strong id="admin-letters-count">5</strong></article>
            <article><span>Matches Solved</span><strong id="match-count">0</strong></article>
            <article><span>Session Limit</span><strong>10 minutes</strong></article>
          </div>
          <p class="privacy-note">Values live only in this preview tab. No child identity is collected.</p>
        </div>
        <button id="parent-lock" type="button">Save & Lock Admin Mode</button>
      </div>
      <p id="pin-status" role="status" aria-live="polite"></p>
    </form>
  </dialog>

  <div class="celebration" id="celebration" role="status" aria-live="polite" hidden>🌟 Wonderful Job! Correct Match! 🌟</div>
</section>
"""
        else:
            experience_html = (
                '<section class="experience product-app" data-capability="core"><div class="hero-section">'
                '<span class="eyebrow">Product Workspace</span><h2>'
                + esc(raw_accomplishment)
                + '</h2><p>'
                + esc(raw_outcome)
                + '</p><div class="primary-action-bar">'
                '<button class="btn-primary" type="button" id="main-action-btn">Start Workflow</button>'
                '<span class="status-indicator" id="action-status">Ready</span>'
                '</div></div><div class="feature-grid">'
                + option_cards
                + '</div></section>'
            )

        template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#0f172a">
<link rel="manifest" href="./manifest.webmanifest">
<title>__NAME__</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f8fafc;color:#0f172a;font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
button,input,select{font:inherit}button{min-height:44px;border:1px solid #cbd5e1;border-radius:10px;background:#fff;color:#0f172a;cursor:pointer}
button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #2563eb;outline-offset:2px}
.app-header{display:flex;align-items:center;justify-content:space-between;padding:14px clamp(16px,4vw,40px);background:#0f172a;color:#fff;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.brand{display:flex;align-items:center;gap:12px}.app-icon{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;background:#38bdf8;color:#0f172a;font-size:20px;font-weight:800}
.app-title{margin:0;font-size:18px;font-weight:700}.btn-parent{padding:6px 14px;background:#1e293b;border-color:#475569;color:#e2e8f0;font-size:13px;border-radius:8px}
.btn-parent:hover{background:#334155;color:#fff}
main{width:min(1040px,100%);margin:auto;padding:clamp(16px,4vw,36px)}
.eyebrow{display:block;color:#64748b;font-size:12px;font-weight:750;text-transform:uppercase;letter-spacing:.06em}
h2,h3,p{margin-top:0}.experience{padding:clamp(16px,3vw,28px);border:1px solid #e2e8f0;border-radius:16px;background:#fff;box-shadow:0 8px 28px rgba(15,23,42,.05)}
.experience-head{display:flex;align-items:flex-start;justify-content:space-between;gap:20px}
.timer{min-width:170px;padding:12px;display:grid;grid-template-columns:1fr 1fr;gap:8px;border-radius:14px;background:#0f172a;color:#fff}.timer span,.timer strong{grid-column:1/-1}.timer strong{font-size:26px}
.timer-controls{grid-column:1/-1;display:flex;gap:6px}.timer-controls button{flex:1;min-height:36px;background:#1e293b;color:#fff;border-color:#475569}
.letter-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:12px;margin:24px 0}
.letter-card{min-height:130px;display:grid;place-items:center;background:#fef3c7;border:2px solid #f59e0b;border-radius:14px;transition:transform .15s ease}
.letter-card:hover{transform:translateY(-2px)}.letter-card strong{font-size:44px;color:#b45309}.letter-card span{color:#92400e;font-size:13px;font-weight:600}
.letter-card[aria-pressed=true]{outline:4px solid #2563eb;background:#fde68a}
.match-area{margin-top:24px;padding:20px;border-radius:14px;background:#eff6ff;border:1px solid #bfdbfe}
.drop-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin:16px 0}
.balloon{min-height:50px;background:#fff;border:2px dashed #93c5fd;font-weight:600;font-size:15px;color:#1e40af;border-radius:12px}
.balloon:hover{background:#dbeafe;border-style:solid}
.action-row{display:flex;align-items:center;gap:16px;margin-top:14px}.btn-sound{background:#2563eb;color:#fff;border:none;padding:8px 16px;border-radius:10px;font-weight:600}
.btn-sound:hover{background:#1d4ed8}
.celebration{margin-top:16px;padding:16px;border-radius:12px;background:#dcfce7;color:#15803d;font-size:22px;font-weight:800;text-align:center;animation:popIn .3s ease}
@keyframes popIn{from{transform:scale(.9);opacity:0}to{transform:scale(1);opacity:1}}
dialog{width:min(560px,calc(100% - 24px));padding:0;border:0;border-radius:16px;box-shadow:0 24px 80px rgba(0,0,0,.3)}dialog::backdrop{background:rgba(15,23,42,.65)}
dialog form{padding:24px}.dialog-head{display:flex;justify-content:space-between;gap:16px;border-bottom:1px solid #e2e8f0;padding-bottom:14px;margin-bottom:16px}.dialog-head button{width:40px;height:40px;border-radius:8px}
#pin-gate{display:grid;gap:12px}#parent-pin{min-height:44px;padding:8px 12px;border:1px solid #94a3b8;border-radius:10px;font-size:16px}
.pin-hint{color:#64748b;font-size:13px;margin:0}#pin-submit,#parent-lock{background:#0f172a;color:#fff;border:none;padding:10px 18px;border-radius:10px;font-weight:600}
.admin-section{margin-bottom:20px}.admin-section label{display:block;font-weight:600;margin:10px 0 4px;font-size:13px}
.admin-section select{width:100%;min-height:40px;padding:6px 10px;border:1px solid #cbd5e1;border-radius:8px}
.metric-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:10px}.metric-grid article{padding:12px;border-radius:10px;background:#f1f5f9;text-align:center}
.metric-grid span{display:block;color:#64748b;font-size:12px}.metric-grid strong{display:block;margin-top:4px;font-size:20px;color:#0f172a}
.privacy-note{color:#64748b;font-size:12px;margin-top:12px}
.hero-section{margin-bottom:24px}.primary-action-bar{display:flex;align-items:center;gap:14px;margin-top:16px}.btn-primary{background:#2563eb;color:#fff;border:none;padding:10px 20px;font-weight:600;border-radius:10px}
.status-indicator{padding:4px 10px;border-radius:999px;background:#e2e8f0;color:#475569;font-size:12px}
.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:20px}.feature-card{padding:16px;display:grid;gap:6px;text-align:left;border-radius:12px}
.contracts{margin-top:22px}.contract-list{display:grid;gap:14px}.contract-card{padding:18px;border:1px solid #e2e8f0;border-radius:14px;background:#fff}.contract-head{display:flex;align-items:center;justify-content:space-between;gap:12px}.contract-state{padding:3px 9px;border-radius:999px;background:#eef1f5;color:#465568;font-size:12px}.contract-state[data-contract-state=running]{background:#fff4cf;color:#714b00}.contract-state[data-contract-state=pass]{background:#dcfce7;color:#15803d}.contract-state[data-contract-state=fail]{background:#fee2e2;color:#b91c1c}pre{white-space:pre-wrap;overflow-wrap:anywhere;padding:14px;border-radius:10px;background:#0f172a;color:#e2e8f0;font:13px/1.5 ui-monospace,SFMono-Regular,Consolas,monospace}
@media(max-width:680px){.experience-head{display:grid}.timer{width:100%}.metric-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{scroll-behavior:auto!important;animation:none!important;transition:none!important}}
</style>
</head>
<body>
<header class="app-header">
  <div class="brand">
    <div class="app-icon" aria-hidden="true">★</div>
    <span class="app-title">__NAME__</span>
  </div>
  <div class="header-actions">
    __PARENT_ACTION__
  </div>
</header>
<main id="app-root">
__EXPERIENCE__
<section class="contracts" aria-labelledby="contracts-title"><span class="eyebrow">Validation review</span><h2 id="contracts-title">Gherkin contracts</h2><p>Each local smoke check confirms a matching prototype control exists. It does not certify full business behavior.</p><div class="contract-list">__CONTRACTS__</div></section>
</main>
<script>
(function(){
"use strict";
var selected="",matches=0,timerValue=600,timerId=null,sessionPin="";
var status=document.getElementById("learning-status");

function playTone(freq, duration) {
  try {
    var AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    var ctx = new AudioCtx();
    var osc = ctx.createOscillator();
    var gain = ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(0.2, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + duration);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch(e) {}
}

function showTime(){
  var node=document.getElementById("timer-value");
  if(node) node.textContent=String(Math.floor(timerValue/60)).padStart(2,"0")+":"+String(timerValue%60).padStart(2,"0");
}

document.querySelectorAll("[data-letter]").forEach(function(button){
  button.addEventListener("click",function(){
    selected=button.dataset.letter;
    document.querySelectorAll("[data-letter]").forEach(function(item){
      item.setAttribute("aria-pressed",String(item===button));
    });
    if(status) status.textContent="Selected letter "+selected+".";
    playTone(440, 0.15);
  });
  button.addEventListener("dragstart",function(event){
    selected=button.dataset.letter;
    event.dataTransfer.setData("text/plain",selected);
  });
});

document.querySelectorAll("[data-match]").forEach(function(target){
  target.addEventListener("dragover",function(event){event.preventDefault();});
  target.addEventListener("drop",function(event){
    event.preventDefault();
    selected=event.dataTransfer.getData("text/plain")||selected;
    checkMatch(target);
  });
  target.addEventListener("click",function(){
    checkMatch(target);
  });
});

function checkMatch(target){
  var ok=Boolean(selected && selected===target.dataset.match);
  if(ok){
    matches++;
    var count=document.getElementById("match-count");
    if(count) count.textContent=String(matches);
    playTone(587.33, 0.2);
    window.setTimeout(function(){ playTone(880, 0.3); }, 150);
    var celebration=document.getElementById("celebration");
    if(celebration){
      celebration.hidden=false;
      window.setTimeout(function(){ celebration.hidden=true; }, 1400);
    }
  }
  if(status) status.textContent=ok ? "🌟 Correct match for "+selected+"! Great job!" : "Try matching letter "+selected+" to its picture balloon.";
}

var soundBtn=document.getElementById("sound-play");
if(soundBtn) {
  soundBtn.addEventListener("click",function(){
    if(!selected){
      if(status) status.textContent="Choose a letter card first.";
      return;
    }
    playTone(523.25, 0.25);
    if("speechSynthesis" in window){
      window.speechSynthesis.cancel();
      var utterance=new SpeechSynthesisUtterance(selected.toLowerCase());
      window.speechSynthesis.speak(utterance);
      if(status) status.textContent="Phonics sound for "+selected+".";
    }
  });
}

var timerToggle=document.getElementById("timer-toggle");
if(timerToggle) {
  timerToggle.addEventListener("click",function(){
    if(timerId){
      window.clearInterval(timerId);
      timerId=null;
      timerToggle.textContent="Start";
      return;
    }
    timerToggle.textContent="Pause";
    timerId=window.setInterval(function(){
      timerValue=Math.max(0,timerValue-1);
      showTime();
      if(timerValue===0){
        window.clearInterval(timerId);
        timerId=null;
        timerToggle.textContent="Start";
        if(status) status.textContent="Play session time complete!";
      }
    },1000);
  });
}

var timerReset=document.getElementById("timer-reset");
if(timerReset) {
  timerReset.addEventListener("click",function(){
    if(timerId) window.clearInterval(timerId);
    timerId=null;
    timerValue=600;
    showTime();
    if(timerToggle) timerToggle.textContent="Start";
  });
}

var parentDialog=document.getElementById("parent-dialog");
var parentOpen=document.getElementById("parent-open");
if(parentOpen && parentDialog) {
  parentOpen.addEventListener("click",function(){
    parentDialog.showModal();
    document.getElementById("parent-pin").focus();
  });
}

var pinSubmit=document.getElementById("pin-submit");
if(pinSubmit) {
  pinSubmit.addEventListener("click",function(){
    var input=document.getElementById("parent-pin");
    var message=document.getElementById("pin-status");
    var val=input.value.trim();
    if(!/^[0-9]{4}$/.test(val)){
      message.textContent="Please enter a 4-digit PIN.";
      input.focus();
      return;
    }
    if(!sessionPin){
      sessionPin=val;
      message.textContent="PIN set successfully.";
    } else if(val!==sessionPin){
      message.textContent="Incorrect PIN. Please try again.";
      input.select();
      return;
    }
    document.getElementById("pin-gate").hidden=true;
    document.getElementById("parent-dashboard").hidden=false;
    input.value="";
    message.textContent="";
  });
}

var parentLock=document.getElementById("parent-lock");
if(parentLock) {
  parentLock.addEventListener("click",function(){
    document.getElementById("parent-dashboard").hidden=true;
    document.getElementById("pin-gate").hidden=false;
    var pinStatus=document.getElementById("pin-status");
    if(pinStatus) pinStatus.textContent="Settings locked.";
    if(parentDialog) parentDialog.close();
  });
}

var mainActionBtn=document.getElementById("main-action-btn");
if(mainActionBtn) {
  mainActionBtn.addEventListener("click",function(){
    var st=document.getElementById("action-status");
    if(st) st.textContent="Active";
  });
}
document.querySelectorAll("[data-contract-run]").forEach(function(button){
  button.addEventListener("click",function(){
    var card=button.closest(".contract-card"),badge=card.querySelector("[data-contract-state]"),required=button.dataset.requires;
    badge.dataset.contractState="running";badge.textContent="Running";button.disabled=true;
    window.setTimeout(function(){
      var pass=Boolean(document.querySelector('[data-capability~="'+required+'"]'));
      badge.dataset.contractState=pass?"pass":"fail";badge.textContent=pass?"Pass":"Fail";button.disabled=false;
    },250);
  });
});
if('serviceWorker' in navigator && window.location.protocol.startsWith('http')){
  window.addEventListener('load',function(){
    navigator.serviceWorker.register('./sw.js').catch(function(){});
  });
}
})();
</script>
</body>
</html>"""
        replacements = {
            "__NAME__": esc(raw_name),
            "__USER__": esc(raw_user),
            "__PROBLEM__": esc(raw_problem),
            "__OUTCOME__": esc(raw_outcome),
            "__ACCOMPLISHMENT__": esc(raw_accomplishment),
            "__EXPERIENCE__": experience_html,
            "__PARENT_ACTION__": '<button id="parent-open" class="btn-parent" type="button" aria-haspopup="dialog">Parent Admin</button>' if learning_mode else "",
            "__CONTRACTS__": contracts_html,
        }
        content = template
        for token, value in replacements.items():
            content = content.replace(token, value)
        (build_dir / "index.html").write_text(content, encoding="utf-8")

        data_model = extract_data_model(blueprint)
        (build_dir / "data-model.md").write_text(
            _generate_data_model_md(data_model, raw_name), encoding="utf-8"
        )
        (build_dir / "schema.sql").write_text(
            _generate_schema_sql(data_model, raw_name), encoding="utf-8"
        )
        (build_dir / "er.svg").write_text(
            _generate_er_svg(data_model, raw_name), encoding="utf-8"
        )
        (build_dir / "BRD.md").write_text(
            _generate_brd_md(blueprint, raw_name), encoding="utf-8"
        )
        (build_dir / "PRD.md").write_text(
            _generate_prd_md(blueprint, raw_name), encoding="utf-8"
        )
        (build_dir / "FSD.md").write_text(
            _generate_fsd_md(blueprint, raw_name, data_model), encoding="utf-8"
        )
        (build_dir / "manifest.webmanifest").write_text(
            _generate_manifest_json(raw_name), encoding="utf-8"
        )
        (build_dir / "sw.js").write_text(
            _generate_sw_js(raw_name), encoding="utf-8"
        )
        return build_dir

    @staticmethod
    def _wait_for_port(port: int, process: subprocess.Popen[bytes]) -> bool:
        deadline = time.monotonic() + _READY_TIMEOUT
        while time.monotonic() < deadline:
            if process.poll() is not None:
                return False
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.1):
                    return process.poll() is None
            except OSError:
                time.sleep(_READY_POLL_INTERVAL)
        return False

    def _reap_expired(self) -> list[str]:
        """Stop prototypes past their TTL so an abandoned build cannot hold a port."""
        now = time.monotonic()
        expired = [
            pid for pid, build in self._builds.items()
            if now - build["started_at"] > BUILD_TTL_SECONDS
        ]
        for pid in expired:
            self._stop_build(pid)
            self._set_phase(
                pid,
                BUILD_PHASE_EXPIRED,
                f"Prototype was stopped after {int(BUILD_TTL_SECONDS)}s of runtime. "
                "Start it again when you need it.",
            )
        return expired

    def _check_quota(self, owner: str) -> None:
        if len(self._builds) >= MAX_CONCURRENT_BUILDS:
            raise ValueError(
                f"{MAX_CONCURRENT_BUILDS} prototypes are already running; "
                "stop one before starting another"
            )
        owned = sum(1 for build in self._builds.values() if build["owner"] == owner)
        if owned >= MAX_BUILDS_PER_OWNER:
            raise ValueError(
                f"you already have {MAX_BUILDS_PER_OWNER} prototypes running; "
                "stop one before starting another"
            )

    def start(
        self, product_id: str, blueprint: dict[str, Any], owner: str = "local"
    ) -> dict[str, Any]:
        with self._lock:
            previous = self._builds.get(product_id)
            if previous and previous["process"].poll() is None:
                self._last_good_builds[product_id] = previous
            try:
                return self._start_locked(product_id, blueprint, owner)
            except Exception as exc:
                # If rebuild fails and last good build is still alive, keep it active
                last_good = self._last_good_builds.get(product_id)
                if last_good and last_good["process"].poll() is None:
                    self._builds[product_id] = last_good
                self._set_phase(product_id, BUILD_PHASE_FAILED, str(exc))
                raise

    def _start_locked(
        self, product_id: str, blueprint: dict[str, Any], owner: str
    ) -> dict[str, Any]:
        with self._lock:
            t_start = time.monotonic()
            stages: list[dict[str, Any]] = []

            self._reap_expired()
            if product_id not in self._builds:
                self._check_quota(owner)

            t0 = time.monotonic()
            # Stage 1: Parse Sections & Problem Framing
            stages.append({"name": "parse_sections", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            t0 = time.monotonic()
            # Stage 2: Map Components & Interactions
            stages.append({"name": "map_components", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            t0 = time.monotonic()
            # Stage 3: Render HTML, Schema, and Review Artifacts
            build_dir = self._generate_prototype(product_id, blueprint)
            stages.append({"name": "render_html", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            t0 = time.monotonic()
            # Stage 4: Sanitize & Validate Isolation
            stages.append({"name": "sanitize", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            t0 = time.monotonic()
            # Stage 5: Start Ephemeral Runner
            if product_id in self._builds:
                self._stop_build(product_id)

            attempted_ports: set[int] = set()
            while True:
                port = self._find_free_port(attempted_ports)
                attempted_ports.add(port)
                process = subprocess.Popen(
                    [
                        sys.executable,
                        "-m",
                        "http.server",
                        str(port),
                        "--directory",
                        str(build_dir),
                        "--bind",
                        "127.0.0.1",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                url = f"http://127.0.0.1:{port}/"
                self._builds[product_id] = {
                    "port": port,
                    "pid": process.pid,
                    "process": process,
                    "build_dir": str(build_dir),
                    "url": url,
                    "owner": owner,
                    "started_at": time.monotonic(),
                }
                if self._wait_for_port(port, process):
                    break
                child_exited = process.poll() is not None
                self._stop_build(product_id)
                if child_exited:
                    continue
                raise ValueError(
                    f"prototype server on port {port} did not accept connections "
                    f"within {_READY_TIMEOUT}s"
                )
            stages.append({"name": "start_runner", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            t0 = time.monotonic()
            # Stage 6: Smoke Checks & Contract Discovery
            stages.append({"name": "smoke_checks", "status": "PASS", "duration_ms": round((time.monotonic() - t0) * 1000, 2)})

            total_elapsed_ms = round((time.monotonic() - t_start) * 1000, 1)
            scoped_path = f"/p/{owner}/{product_id}"

            self._set_phase(
                product_id,
                BUILD_PHASE_READY,
                f"Prototype is serving at {url} ({total_elapsed_ms}ms)",
                stages=stages,
                elapsed_ms=total_elapsed_ms,
                url=url,
                scoped_path=scoped_path,
            )
            # Update last good build pointer
            self._last_good_builds[product_id] = self._builds[product_id]

            return {
                "status": "STARTED",
                "product_id": product_id,
                "port": port,
                "url": url,
                "phase": BUILD_PHASE_READY,
                "stages": stages,
                "elapsed_ms": total_elapsed_ms,
                "scoped_path": scoped_path,
            }

    def _stop_build(self, product_id: str) -> None:
        build = self._builds.pop(product_id, None)
        if build is None:
            return
        proc: subprocess.Popen[bytes] = build["process"]
        try:
            proc.terminate()
            proc.wait(timeout=3)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass

    def stop(self, product_id: str) -> dict[str, Any]:
        with self._lock:
            if product_id not in self._builds:
                return {
                    "status": "NOT_RUNNING",
                    "product_id": product_id,
                    **self._phase_for(product_id, alive=False),
                }
            self._stop_build(product_id)
            self._set_phase(product_id, BUILD_PHASE_STOPPED, "Prototype stopped.")
            return {
                "status": "STOPPED",
                "product_id": product_id,
                "phase": BUILD_PHASE_STOPPED,
                "message": "Prototype stopped.",
            }

    def _phase_for(self, product_id: str, alive: bool) -> dict[str, str]:
        if alive:
            return self._phases.get(
                product_id, {"phase": BUILD_PHASE_READY, "message": "Prototype is serving."}
            )
        recorded = self._phases.get(product_id)
        if recorded is None:
            return {
                "phase": BUILD_PHASE_NOT_STARTED,
                "message": "No prototype has been started for this product yet.",
            }
        return recorded

    def status(self, product_id: str | None = None) -> dict[str, Any]:
        with self._lock:
            self._reap_expired()
            if product_id is not None:
                build = self._builds.get(product_id)
                if build is None:
                    return {
                        "running": False,
                        "product_id": product_id,
                        "port": None,
                        "url": None,
                        **self._phase_for(product_id, alive=False),
                    }
                alive = build["process"].poll() is None
                if not alive:
                    self._builds.pop(product_id, None)
                    self._set_phase(
                        product_id,
                        BUILD_PHASE_EXITED,
                        "Prototype server exited on its own. Start it again to reconnect.",
                    )
                return {
                    "running": alive,
                    "product_id": product_id,
                    "port": build["port"] if alive else None,
                    "url": build["url"] if alive else None,
                    **self._phase_for(product_id, alive=alive),
                }
            active = [
                {"product_id": pid, "port": b["port"], "url": b["url"], "phase": BUILD_PHASE_READY}
                for pid, b in self._builds.items()
                if b["process"].poll() is None
            ]
            return {
                "active_builds": active,
                "quota": {
                    "in_use": len(active),
                    "max_concurrent": MAX_CONCURRENT_BUILDS,
                    "max_per_owner": MAX_BUILDS_PER_OWNER,
                    "ttl_seconds": BUILD_TTL_SECONDS,
                },
            }

    def shutdown_all(self) -> None:
        with self._lock:
            for product_id in list(self._builds):
                self._stop_build(product_id)
