# ROADMAP — productowner-skill Platform

**Author:** Vignesh AIPM
**Status:** Active
**Last updated:** 2026-08-01
**Linked PRD:** prds/00-pm-os-platform.md
**Phase 1 brainstorm:** planning/phase1_brainstorm_5_personas.md

---

## Vision

productowner-skill becomes the default PO operating layer for product teams and consulting engagements —
the system that connects every knowledge source, generates every artifact, and learns from every product.

---

## Phase 1 — Trustworthy Plugin Foundation (Current)

**Goal:** Any PO can install the skill plugin and get **launch-ready outcomes** — discovery pack, delivery pack, accessible UI, security-cleared artifacts — without backend infrastructure, OAuth, or live enterprise integrations.

**Tagline:** *Outcomes users want. Skills that deliver. Zero scripts. Zero telemetry.*

| Deliverable | Status | Priority |
|-------------|--------|----------|
| Master PRD (v0.4) | ✅ Done | — |
| SRS + FRD (v0.4) | ✅ Done | — |
| PO Onboarding UI (6-step wizard) | ✅ Done | — |
| GitHub Pages deployment | ✅ Done | — |
| Microsoft Teams tab + manifest | ✅ Done | — |
| CuCP 90-day rollout slide deck | ✅ Done | — |
| Playwright security + a11y test suite | ✅ Done | — |
| Local Memory Standard (`.agent/memory.md`) | ✅ Done | — |
| `cybersec-skill` (PII blocker + OWASP auditor) | ✅ Done | — |
| `PO-discovery` skill (SWOT, TAM/SAM/SOM, compliance map) | ✅ Done | — |
| `PO-delivery` skill (RICE backlog, KPI plan, rollout) | ✅ Done | — |
| `PO-kb-research` skill (local artifact search) | ✅ Done | — |
| `PO-code-pipeline` skill (declarative PRD → SDLC) | ✅ Done | — |
| `qa-tester-skill` (edge-case / boundary matrix) | ✅ Done | — |
| `ux-pro-skill` (a11y + design tokens + flow review) | ✅ Done | — |
| Portfolio demo UX pass (`docs/` onboarding + landing) | ✅ Done | — |
| Template library (`skills/*/templates/`) | ✅ Done | — |
| Plugin install guide (`docs/INSTALL.md`) | ✅ Done | — |
| CI skill validation (extend `check-source.mjs`) | ✅ Done | — |
| Trust badge on landing page | 🔲 Next | P2 |

**Exit criteria (outcomes):** Discovery pack in one session · PRD with Y-Score + Gherkin AC · PII blocked · edge-case matrix · WCAG pass on demo UI · install < 5 min.

> Enterprise KB integrations (Rovo / M365 / Google) moved to **Phase 2** per 6-persona brainstorm (`planning/phase1_brainstorm_5_personas.md`).

---

## Phase 2 — KB & Standard Reporting

**Goal:** Federated search live across all sources. Standard tier fully usable.

| Deliverable | Target |
|-------------|--------|
| Atlassian Rovo KB search integration (Jira + Confluence) | Q3 2026 |
| Microsoft 365 Graph search integration (SharePoint + Yammer) | Q3 2026 |
| Google Workspace API search integration | Q3 2026 |
| Unified search UI (Rovo + M365 + Google) | Q3 2026 |
| Artifact tagging: domain · stage · type · compliance | Q3 2026 |
| "Clone to KB" action from any search result | Q3 2026 |
| Shared Library (anonymised cross-org templates) | Q3 2026 |
| PowerBI standard embed (4 pre-built PO templates) | Q3 2026 |
| Looker embed integration | Q3 2026 |
| PO Lead team dashboard (release health, reuse rate) | Q3 2026 |

---

## Phase 3 — AI Tier

**Goal:** Chat, artifact generation, and PowerBI AI interpretation live for AI-tier PMs.

| Deliverable | Target |
|-------------|--------|
| Rovo Chat integration (Jira + Confluence Q&A) | Q4 2026 |
| Claude API chat (cross-tool synthesis, cited responses) | Q4 2026 |
| Gemini integration (Google Workspace Q&A) | Q4 2026 |
| AI artifact generation: SWOT · ROI · PRD · KPI plan | Q4 2026 |
| Jira AI epic-to-story breakdown | Q4 2026 |
| Confluence AI "save to page" from chat output | Q4 2026 |
| PowerBI Copilot: screenshot interpret + dataset query | Q4 2026 |
| Deep research engine (Quick / Standard / Deep) | Q4 2026 |

---

## Phase 4 — Client Workspace

**Goal:** Consulting and delivery teams can package work for clients. Client views without licences.

| Deliverable | Target |
|-------------|--------|
| Client Workspace tenant isolation | Q1 2027 |
| Per-artifact visibility toggle (PO controls what client sees) | Q1 2027 |
| Client dashboard: milestones · KPIs · AI status summary | Q1 2027 |
| Client invite link (no Atlassian/M365/Google licence required) | Q1 2027 |
| Workspace archive on engagement close (ZIP + audit log) | Q1 2027 |
| Admin audit log: who viewed what, when | Q1 2027 |

---

## Phase 5 — Full Pipeline Integration

**Goal:** End-to-end: idea → discovery → PRD → code → deploy → KB archival.

| Deliverable | Target |
|-------------|--------|
| Discovery Engine: problem statement → full research pack | Q2 2027 |
| Delivery Engine: PRD → backlog · KPI plan · Y-Score gate · rollout plan | Q2 2027 |
| Code Pipeline: PRD → MetaGPT → OpenHands → Promptfoo → Cloudflare | Q2 2027 |
| `orchestrate.sh` updated: `--stage discovery|delivery|release|all` | Q2 2027 |
| GitHub Actions full pipeline trigger on PRD commit | Q2 2027 |
| KB archival: all artifacts tagged, versioned, indexed post-launch | Q2 2027 |

---

## Phase 6 — Scale & Monetisation

**Goal:** Multi-tenant SaaS. Billing. White-label for enterprise clients.

| Deliverable | Target |
|-------------|--------|
| Multi-tenant SaaS architecture | Q3 2027 |
| Usage-based billing (Standard tier · AI tier · Client workspaces) | Q3 2027 |
| White-label for enterprise clients (custom domain + branding) | Q3 2027 |
| Jira / Confluence / SharePoint write-back (v2) | Q3 2027 |
| Native mobile app (iOS + Android) | Q4 2027 |
| API for third-party integrations | Q4 2027 |

---

## Principles of Proportional Delivery

Borrowed from the Coupa CuCP framework — applied to productowner-skill itself:

- Each phase ships something usable before the next begins
- Standard tier always ships before AI tier (cost-safe, broader adoption)
- Client features ship only after internal org use is stable
- Mandate nothing — earn adoption through value at each phase
