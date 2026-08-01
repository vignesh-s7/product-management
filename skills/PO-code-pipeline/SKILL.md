---
name: PO-code-pipeline
description: Declarative SDLC pipeline that routes a PRD through discovery, delivery, security, UX, QA, and release stages. Each stage delegates to a named skill. No bash scripts — markdown instructions only.
triggers:
  - "run the pipeline"
  - "PRD to SDLC"
  - "full SDLC from PRD"
  - "execute code pipeline"
  - "discovery to release"
---

# PO-code-pipeline — Declarative SDLC Pipeline

End-to-end Product Owner workflow from problem statement to release-ready artifact set. Each stage is a named skill delegation with explicit gate rules.

## Mandatory first step

**Read `.agent/memory.md`** before initiating any pipeline stage. Adapt domain, compliance, and constraints to the active repository.

## When to trigger

- User says "run the pipeline", "PRD to SDLC", or "full SDLC from PRD"
- After a PRD is drafted and needs the full persona swarm review
- When onboarding a new product in a regulated domain

## Pipeline overview

```
Input: problem statement OR existing PRD
  │
  ▼
┌─────────────┐
│  discovery  │  PO-discovery
└──────┬──────┘
       ▼
┌─────────────┐
│  delivery   │  PO-delivery (+ y-score-readiness gate)
└──────┬──────┘
       ▼
┌─────────────┐
│  security   │  cybersec-skill          ← BLOCK on critical
└──────┬──────┘
       ▼
┌─────────────┐
│     ux      │  ux-pro-skill              ← BLOCK on critical a11y
└──────┬──────┘
       ▼
┌─────────────┐
│     qa      │  qa-tester-skill           ← WARN on gaps
└──────┬──────┘
       ▼
┌─────────────┐
│   release   │  artifact packaging
└─────────────┘
       │
       ▼
Output: tagged artifacts in artifacts/
```

## Inputs

| Field | Required | Notes |
|-------|----------|-------|
| `input` | ✅ | Problem statement (text) OR path to existing PRD in `prds/` or `artifacts/` |
| `domain` | optional | Override domain from `.agent/memory.md` — `bfsi` / `healthcare` / `generic` |
| `intensity` | optional | `lite` / `full` (default) / `ultra` — controls UX and QA depth |

## Stage definitions

### Stage 1 — Discovery

| Property | Value |
|----------|-------|
| **Delegate to** | `PO-discovery` |
| **Input** | Problem statement + domain from memory |
| **Output** | Discovery pack → `artifacts/{date}-discovery-pack-{slug}.md` |
| **Contents** | SWOT · TAM/SAM/SOM · competitor matrix · compliance risk map · GTM brief |
| **Prerequisite** | Run `PO-kb-research` first to check for reusable prior artifacts |
| **Gate** | Proceed if discovery pack complete. WARN if compliance map missing for regulated domain. |

### Stage 2 — Delivery

| Property | Value |
|----------|-------|
| **Delegate to** | `PO-delivery` |
| **Sub-gate** | `y-score-readiness` — score PRD ≥ 70 to proceed |
| **Input** | Discovery pack + draft PRD |
| **Output** | Delivery pack → `artifacts/{date}-delivery-pack-{slug}.md` |
| **Contents** | RICE-scored backlog · KPI instrumentation plan · Gherkin AC · rollout phases |
| **Gate** | **BLOCK** if Y-Score < 70. Return findings and halt pipeline. |

### Stage 3 — Security

| Property | Value |
|----------|-------|
| **Delegate to** | `cybersec-skill` |
| **Input** | All artifacts produced in stages 1–2 |
| **Checks** | PII/PHI blocker · OWASP Top 10 patterns in generated code/docs · synthetic data enforcement |
| **Output** | Security report → `artifacts/{date}-security-report-{slug}.md` |
| **Gate** | **BLOCK** on critical findings (PII/PHI detected, hardcoded secrets, SQLi/XSS patterns). Pipeline halts. Non-critical → WARN and continue. |

### Stage 4 — UX

| Property | Value |
|----------|-------|
| **Delegate to** | `ux-pro-skill` |
| **Input** | Any UI artifacts (`docs/`, generated HTML/React) + design tokens from `.agent/memory.md` |
| **Checks** | WCAG 2.1 AA · design token adherence · cognitive load review |
| **Output** | UX report → `artifacts/{date}-ux-report-{slug}.md` |
| **Gate** | **BLOCK** on critical accessibility failures (missing alt text on functional images, keyboard traps, contrast < 4.5:1 on body text). WARN on style/token deviations. |

### Stage 5 — QA

| Property | Value |
|----------|-------|
| **Delegate to** | `qa-tester-skill` |
| **Input** | PRD acceptance criteria + API/function signatures from delivery pack |
| **Output** | Edge-case matrix → `artifacts/{date}-qa-matrix-{slug}.md` |
| **Gate** | **WARN** if boundary cases missing, negative paths untested, or AC not traceable to test cases. Does not block release. |

### Stage 6 — Release

| Property | Value |
|----------|-------|
| **Delegate to** | `productowner-skill` (orchestration summary) |
| **Input** | All prior stage outputs + gate results |
| **Output** | Release summary → `artifacts/{date}-release-summary-{slug}.md` |
| **Contents** | Artifact inventory · gate verdicts · tagging schema applied · next actions |
| **Gate** | Release only if no BLOCK verdicts remain unresolved. |

## Gate rules summary

| Stage | Skill | Severity on fail |
|-------|-------|------------------|
| Discovery | PO-discovery | WARN (missing compliance map in regulated domain) |
| Delivery | PO-delivery + y-score-readiness | **BLOCK** (Y-Score < 70) |
| Security | cybersec-skill | **BLOCK** (critical PII/OWASP) |
| UX | ux-pro-skill | **BLOCK** (critical a11y) · WARN (style) |
| QA | qa-tester-skill | **WARN** (coverage gaps) |
| Release | productowner-skill | **BLOCK** (unresolved BLOCK from prior stages) |

## Execution instructions

1. Read `.agent/memory.md`.
2. Confirm input (problem statement or PRD path).
3. Run `PO-kb-research` to surface reusable artifacts.
4. Execute stages 1–6 sequentially. Do not skip stages.
5. At each gate: record verdict (`PASS`, `WARN`, `BLOCK`) in the release summary.
6. On **BLOCK**: halt pipeline, return findings to user, do not write release summary.
7. On completion: write all artifacts to `artifacts/` with tagging schema.

## Prohibited actions

- **NO bash scripts** — do not invoke `orchestrate.sh` or any shell orchestration
- **NO network calls** — no curl, wget, API requests
- **NO autonomous code execution** — MetaGPT/OpenHands/Promptfoo deferred to Phase 5
- **NO skipping security or UX gates** — mandatory in regulated domains

## Output manifest

On successful completion, emit:

```json
{
  "pipeline": "PO-code-pipeline",
  "slug": "<product-slug>",
  "domain": "<from memory>",
  "stages": {
    "discovery":  { "status": "pass", "artifact": "artifacts/..." },
    "delivery":   { "status": "pass", "artifact": "artifacts/...", "y_score": 78 },
    "security":   { "status": "pass", "artifact": "artifacts/..." },
    "ux":         { "status": "warn", "artifact": "artifacts/...", "notes": "..." },
    "qa":         { "status": "warn", "artifact": "artifacts/...", "notes": "..." },
    "release":    { "status": "pass", "artifact": "artifacts/..." }
  },
  "verdict": "release_ready_with_warnings"
}
```

## Author

Vignesh AIPM — declarative SDLC pipeline for regulated PO workflows. Autonomous codegen loops deferred to Phase 5.
