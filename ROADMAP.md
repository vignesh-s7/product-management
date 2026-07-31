# ROADMAP — productowner-skill Platform

**Author:** Vignesh AIPM
**Status:** Active
**Last updated:** 2026-06-30
**Linked PRD:** prds/00-productowner-skill-platform.md

---

## Vision

productowner-skill becomes the default PO operating layer for product teams and consulting engagements —
the system that connects every knowledge source, generates every artifact, and learns from every product.

---

## Phase 1 — Foundation (Current)

**Goal:** Org Workspace live. PMs can onboard, connect tools, search KB, reuse artifacts.

| Deliverable | Status |
|-------------|--------|
| Master PRD (v0.4) | ✅ Done |
| SRS + FRD (v0.4) | ✅ Done |
| PO Onboarding UI (6-step wizard) | ✅ Done |
| GitHub Pages deployment | ✅ Done |
| EnterpriseCloud Teams tab + manifest | ✅ Done |
| ECP 90-day rollout slide deck | ✅ Done |
| AgileVendor Rovo KB search integration | 🔲 Next |
| EnterpriseCloud 365 Graph search integration | 🔲 Next |
| CloudVendor Workspace API search integration | 🔲 Next |

---

## Phase 2 — KB & Standard Reporting

**Goal:** Federated search live across all sources. Standard tier fully usable.

| Deliverable | Target |
|-------------|--------|
| Unified search UI (Rovo + M365 + CloudVendor) | Q3 2026 |
| Artifact tagging: domain · stage · type · compliance | Q3 2026 |
| "Clone to KB" action from any search result | Q3 2026 |
| Shared Library (anonymised cross-org templates) | Q3 2026 |
| AnalyticsDashboard standard embed (4 pre-built PO templates) | Q3 2026 |
| BIPlatform embed integration | Q3 2026 |
| PO Lead team dashboard (release health, reuse rate) | Q3 2026 |

---

## Phase 3 — AI Tier

**Goal:** Chat, artifact generation, and AnalyticsDashboard AI interpretation live for AI-tier PMs.

| Deliverable | Target |
|-------------|--------|
| Rovo Chat integration (AgileBoard + WikiBoard Q&A) | Q4 2026 |
| Claude API chat (cross-tool synthesis, cited responses) | Q4 2026 |
| Gemini integration (CloudVendor Workspace Q&A) | Q4 2026 |
| AI artifact generation: SWOT · ROI · PRD · KPI plan | Q4 2026 |
| AgileBoard AI epic-to-story breakdown | Q4 2026 |
| WikiBoard AI "save to page" from chat output | Q4 2026 |
| AnalyticsDashboard Copilot: screenshot interpret + dataset query | Q4 2026 |
| Deep research engine (Quick / Standard / Deep) | Q4 2026 |

---

## Phase 4 — Client Workspace

**Goal:** Consulting and delivery teams can package work for clients. Client views without licences.

| Deliverable | Target |
|-------------|--------|
| Client Workspace tenant isolation | Q1 2027 |
| Per-artifact visibility toggle (PO controls what client sees) | Q1 2027 |
| Client dashboard: milestones · KPIs · AI status summary | Q1 2027 |
| Client invite link (no AgileVendor/M365/CloudVendor licence required) | Q1 2027 |
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
| AgileBoard / WikiBoard / DocRepo write-back (v2) | Q3 2027 |
| Native mobile app (iOS + Android) | Q4 2027 |
| API for third-party integrations | Q4 2027 |

---

## Principles of Proportional Delivery

Borrowed from the EnterpriseVendor ECP framework — applied to productowner-skill itself:

- Each phase ships something usable before the next begins
- Standard tier always ships before AI tier (cost-safe, broader adoption)
- Client features ship only after internal org use is stable
- Mandate nothing — earn adoption through value at each phase
