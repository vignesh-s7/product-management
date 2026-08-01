# Phase 1 Brainstorm — 5-Persona Deep Session

**Date:** 2026-08-01  
**Author:** Vignesh AIPM  
**Purpose:** Reconcile technical, product, and business views; produce a revised Phase 1 scope that ships trust + reuse before enterprise integrations.  
**Inputs:** `ROADMAP.md`, `prds/00-pm-os-platform.md`, `planning/meta_agent_swot_analysis.md`, `planning/cybersecurity_trust_plan.md`, `planning/persona_skills_roadmap.md`, `planning/rice_prioritization_matrix.md`, `planning/reusable_skills_plan.md`

---

## Session Setup

Five personas debated the current Phase 1 goal (*"Org Workspace live. PMs can onboard, connect tools, search KB, reuse artifacts"*) against what is actually built (static demo + planning docs) and what the brainstorming corpus recommends (markdown plugin + persona swarm + local memory).

**Verdict:** Phase 1 was over-indexed on enterprise API integrations (Rovo / M365 / Google) before the reusable skill foundation exists. Revised Phase 1 = **"Trustworthy Plugin Foundation"** — ship skills any repo can import, with security gates and repo memory, while keeping the portfolio demo as proof-of-concept UX.

---

## Persona 1 — Technical Architect

**Lens:** System design, portability, zero-overengineering.

### What Phase 1 must prove
- Global PO skills run in any IDE agent (Cursor, Antigravity, Claude Code) without Docker or Python orchestration.
- Repo-specific context loads from a standard local memory file — not hardcoded to this repository.
- Four Engines exist as independent `SKILL.md` modules, not README prose.

### Feature proposals

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| T-01 | **Local Memory Standard** | `.agent/memory.md` schema: domain, users, constraints, compliance, integrations, glossary | ✅ Must |
| T-02 | **Skill Plugin Layout** | `skills/{PO-discovery,PO-delivery,PO-kb-research,PO-code-pipeline}/SKILL.md` with YAML triggers | ✅ Must |
| T-03 | **Cross-Repo Skill Contract** | Every skill starts: read `.agent/memory.md` → adapt templates → write outputs to `artifacts/` | ✅ Must |
| T-04 | **Declarative Pipeline** | Replace `orchestrate.sh` with markdown stage instructions (`discovery → delivery → release`) | ✅ Must |
| T-05 | **Template Library** | Move reference PRDs to `skills/*/templates/` as copy-and-fill starters | ✅ Must |
| T-06 | **MCP Gateway (read-only)** | Thin MCP for Jira/Confluence search only — deferred | ❌ Phase 2 |
| T-07 | **Multi-tenant Backend** | Auth, tenant isolation, OAuth token store | ❌ Phase 4+ |

### Architect recommendation
> Ship the plugin contract first. Integrations without memory + skills = pretty demo, no portable value.

---

## Persona 2 — Product Owner (Internal PO User)

**Lens:** Day-to-day PO workflows, time saved, adoption.

### Jobs-to-be-done in Phase 1
1. Open any repo → agent already knows how to write a PRD for *this* product.
2. Run discovery (SWOT, ROI, competitor scan) in < 30 min with cited templates.
3. Run delivery (RICE backlog, Y-Score gate, KPI plan) from an existing PRD.
4. Reuse prior artifacts instead of starting from blank Confluence pages.

### Feature proposals

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| P-01 | **PO Onboarding Wizard (demo)** | 6-step static UX — already done; keep as portfolio entry | ✅ Done |
| P-02 | **Y-Score Readiness Gate** | 7-dimension launch check before any feature ships | ✅ Must |
| P-03 | **Gherkin AC Enforcer** | Every PRD/story gets Given/When/Then acceptance criteria | ✅ Must |
| P-04 | **Discovery Pack Generator** | SWOT + TAM/SAM/SOM + competitor matrix + compliance map from memory context | ✅ Must |
| P-05 | **Delivery Pack Generator** | RICE-scored backlog + KPI instrumentation plan + rollout phases | ✅ Must |
| P-06 | **Artifact Tagging Schema** | domain · stage · type · compliance-regime on every generated file | ✅ Must |
| P-07 | **KB Federated Search UI** | Unified Rovo + M365 + Google results | ❌ Phase 2 |
| P-08 | **Client Workspace** | Read-only client tenant | ❌ Phase 4 |
| P-09 | **Story Slicing (Epic → Stories)** | Break epics into deployable stories | 🟡 Stretch |
| P-10 | **DoR Gate (Analytics)** | Reject PRDs missing tracking requirements | 🟡 Stretch |

### PO recommendation
> Phase 1 wins when a PO says: *"I pointed the agent at my repo and got a compliant PRD + Y-Score report in one session."*

---

## Persona 3 — Business Strategist (GTM / Monetisation)

**Lens:** Differentiation, pricing tiers, enterprise sales motion.

### Competitive position (from `top_5_competitors.md`)
- OpenHands, MetaGPT, GPT-Engineer, ChatDev, SuperAGI = heavy Python apps, opaque execution, InfoSec blockers.
- **Our wedge:** Declarative markdown plugin, zero data retention, runs on approved local agent.

### Business features for Phase 1

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| B-01 | **Two-Tier Positioning Doc** | Standard (zero LLM, templates + search) vs AI (generation + chat) — live in README | ✅ Must |
| B-02 | **Trust Handshake Package** | `SECURITY.md` + signed releases + "no scripts, no telemetry" badge on landing page | ✅ Must |
| B-03 | **Case Study Narrative** | `CASE_STUDY.md` updated with plugin + persona swarm story | ✅ Must |
| B-04 | **CuCP Rollout Deck** | Enterprise change-management asset — already done | ✅ Done |
| B-05 | **Open-Source Plugin Distribution** | Install instructions: copy `skills/` to agent config or submodule | ✅ Must |
| B-06 | **Usage-Based Billing** | Standard / AI / Client workspace metering | ❌ Phase 6 |
| B-07 | **White-Label** | Custom domain + branding for consultancies | ❌ Phase 6 |
| B-08 | **Shared Library (cross-client)** | Anonymised template marketplace | ❌ Phase 2 |

### Business recommendation
> Phase 1 is a **trust + distribution** milestone, not a revenue milestone. Sell "InfoSec-approved PO plugin" before selling "connected KB search."

### Phase 1 success metrics (revised)

| KPI | Target |
|-----|--------|
| Skills installable in < 5 min | ✅ |
| First PRD generated from cold repo | < 45 min |
| Security review pass (no executables) | 100% |
| GitHub stars / fork as distribution proxy | Track |
| Enterprise pilot conversations enabled | ≥ 1 deck + 1 case study |

---

## Persona 4 — Cybersecurity / InfoSec Architect

**Lens:** Enterprise approval, regulated domains (BFSI, healthcare), zero-trust.

### Non-negotiables (from `cybersecurity_trust_plan.md`)

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| S-01 | **PII/PHI Blocker Skill** | `cybersec-skill` hard-stops extraction/transmission of sensitive data | ✅ Must |
| S-02 | **OWASP Top 10 Auditor** | Scan generated code/docs for SQLi, XSS, SSRF patterns | ✅ Must |
| S-03 | **No Executable Policy** | Zero `.sh` / `.bat`; CI enforces via `check-source.mjs` | ✅ Done |
| S-04 | **No Network in Skills** | Skills ban curl, wget, web search for data exfiltration | ✅ Must |
| S-05 | **Synthetic Data Only** | All templates use mock personas, no real client data | ✅ Must |
| S-06 | **Session Isolation** | No cross-session profiling; no `localStorage` identity in prod path | ✅ Must |
| S-07 | **Dependency Risk Assessor** | Flag unvetted npm/pip additions | 🟡 Stretch |
| S-08 | **Zero-Trust AuthZ Reviewer** | Demand permission checks on every new API endpoint | 🟡 Phase 2 |
| S-09 | **Immutable Signed Releases** | Cryptographic release verification | 🟡 Stretch |

### Security recommendation
> `cybersec-skill` is not optional — it is the **license to operate** in BFSI/healthcare. Build it in Phase 1 alongside PO skills, not after.

### Gate model (persona swarm)

```
User request
  → productowner-skill (writes PRD / AC)
  → cybersec-skill (PII + OWASP gate) — BLOCK if fail
  → qa-tester-skill (edge cases) — WARN if gaps
  → output released to repo
```

---

## Persona 5 — Engineering Lead (Builder / DX)

**Lens:** Developer experience, CI, testability, maintainability.

### What engineers need in Phase 1

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| E-01 | **`qa-tester-skill`** | Boundary/edge-case matrix generator for any function or API | ✅ Must |
| E-02 | **Playwright Security Suite** | XSS, open-redirect, auth-demo tests — already exist | ✅ Done |
| E-03 | **Skill Trigger YAML** | Consistent frontmatter: name, description, triggers, intensity levels | ✅ Must |
| E-04 | **CI Skill Validation** | Lint `SKILL.md` files: required sections, no banned commands | ✅ Must |
| E-05 | **`ux-pro-skill` (a11y)** | WCAG scan on `docs/` HTML — extends existing a11y tests | 🟡 Stretch |
| E-06 | **GitHub Actions PRD Pipeline** | On PRD commit → Y-Score check + schema validation | 🟡 Stretch |
| E-07 | **OpenHands / MetaGPT Wiring** | Live code generation loops | ❌ Phase 5 |
| E-08 | **Promptfoo Eval Gate** | Mandatory eval before deploy | ❌ Phase 5 |

### Engineering recommendation
> Phase 1 = **skills as code**. Add CI that treats `SKILL.md` like source files. Defer autonomous coding loops to Phase 5.

---

## Cross-Persona Debate — Key Tensions Resolved

| Tension | Resolution |
|---------|------------|
| Product wants KB search now vs Architect says defer APIs | **Defer live integrations to Phase 2.** Phase 1 uses local `artifacts/` + `prds/` as mock KB. |
| Business wants monetisation vs Security wants zero telemetry | **No billing in Phase 1.** Trust narrative + OSS distribution first. |
| PO wants AI generation vs Security wants zero LLM cost | **Phase 1 skills work with any model the user's agent already has.** No bundled API calls. |
| Engineer wants E2E codegen vs Architect wants no scripts | **qa-tester outputs test *definitions* in markdown.** Playwright files are generated by agent on demand, not shipped as scripts. |
| Original Phase 1 listed Rovo/M365/Google | **Moved to Phase 2** — requires backend OAuth, violates current zero-network skill rule. |

---

## Consolidated Feature Backlog (Phase 1)

### Tier A — Must Ship (Phase 1 Core)

| # | Feature | Owner Persona | Output |
|---|---------|---------------|--------|
| 1 | Local Memory Standard (`.agent/memory.md`) | Technical | Schema + example file |
| 2 | `skills/PO-discovery/SKILL.md` | Product | SWOT, TAM/SAM/SOM, competitor, compliance map |
| 3 | `skills/PO-delivery/SKILL.md` | Product | RICE backlog, KPI plan, rollout phases |
| 4 | `skills/PO-kb-research/SKILL.md` | Product | Local artifact search instructions (no API) |
| 5 | `skills/PO-code-pipeline/SKILL.md` | Technical | Declarative PRD → SDLC stage map |
| 6 | `skills/cybersec-skill/SKILL.md` | Security | PII/PHI blocker + OWASP auditor |
| 7 | `skills/qa-tester-skill/SKILL.md` | Engineering | Edge-case / boundary matrix generator |
| 8 | Upgrade `skills/productowner-skill/SKILL.md` | Product | Read memory first; delegate to sub-skills |
| 9 | Template library under `skills/*/templates/` | Technical | Generic PRD, SWOT, ROI, KPI templates |
| 10 | Trust package update | Business | README + SECURITY.md + landing page trust badge |
| 11 | Plugin install guide | Business | `docs/INSTALL.md` — 5-minute setup |
| 12 | CI skill lint (`check-source.mjs` extension) | Engineering | Ban executables + validate SKILL structure |

### Tier B — Already Done (Keep, Don't Rebuild)

| # | Feature | Status |
|---|---------|--------|
| 13 | Master PRD v0.4 | ✅ |
| 14 | SRS + FRD v0.4 | ✅ |
| 15 | PO Onboarding UI (6-step) | ✅ |
| 16 | GitHub Pages deployment | ✅ |
| 17 | Microsoft Teams tab + manifest | ✅ |
| 18 | CuCP 90-day rollout deck | ✅ |
| 19 | Playwright security + a11y tests | ✅ |
| 20 | `caveman` + `y-score-readiness` + `prd-to-sdlc` skills | ✅ |

### Tier C — Stretch (Phase 1 if capacity)

| # | Feature | Persona |
|---|---------|---------|
| 21 | Story Slicing (Epic → Stories) | Product |
| 22 | DoR Gate (analytics tracking) | Product |
| 23 | `ux-pro-skill` a11y enforcer | Engineering |
| 24 | GitHub Actions PRD validation pipeline | Engineering |
| 25 | Signed immutable releases | Security |

### Tier D — Explicitly Deferred

| # | Feature | New Phase |
|---|---------|-----------|
| 26 | Atlassian Rovo KB search | Phase 2 |
| 27 | Microsoft 365 Graph search | Phase 2 |
| 28 | Google Workspace API search | Phase 2 |
| 29 | PowerBI / Looker embed | Phase 2 |
| 30 | AI chat (Rovo + Claude + Gemini) | Phase 3 |
| 31 | Client Workspace | Phase 4 |
| 32 | MetaGPT / OpenHands / Promptfoo live pipeline | Phase 5 |
| 33 | Billing + white-label SaaS | Phase 6 |

---

## Revised Phase 1 — "Trustworthy Plugin Foundation"

**New goal:** Any PO can install the skill plugin, point it at any repository, and generate compliant discovery + delivery artifacts with security gates — without backend infrastructure, OAuth, or live enterprise integrations.

**Tagline:** *Write once. Run anywhere. Zero scripts. Zero telemetry.*

### Revised deliverable table

| Deliverable | Status | Priority |
|-------------|--------|----------|
| Master PRD (v0.4) | ✅ Done | — |
| SRS + FRD (v0.4) | ✅ Done | — |
| PO Onboarding UI (6-step wizard) | ✅ Done | — |
| GitHub Pages deployment | ✅ Done | — |
| Microsoft Teams tab + manifest | ✅ Done | — |
| CuCP 90-day rollout slide deck | ✅ Done | — |
| Playwright security + a11y test suite | ✅ Done | — |
| **Local Memory Standard (`.agent/memory.md`)** | 🔲 Next | P0 |
| **`cybersec-skill` (PII blocker + OWASP)** | 🔲 Next | P0 |
| **`PO-discovery` skill** | 🔲 Next | P0 |
| **`PO-delivery` skill** | 🔲 Next | P0 |
| **`PO-kb-research` skill (local artifacts)** | 🔲 Next | P1 |
| **`PO-code-pipeline` skill (declarative)** | 🔲 Next | P1 |
| **`qa-tester-skill` (edge-case generator)** | 🔲 Next | P1 |
| **Template library (`skills/*/templates/`)** | 🔲 Next | P1 |
| **Plugin install guide (`docs/INSTALL.md`)** | 🔲 Next | P1 |
| **CI skill validation** | 🔲 Next | P2 |
| **Trust badge on landing page** | 🔲 Next | P2 |
| ~~Atlassian Rovo KB search~~ | ⏭️ Phase 2 | — |
| ~~Microsoft 365 Graph search~~ | ⏭️ Phase 2 | — |
| ~~Google Workspace API search~~ | ⏭️ Phase 2 | — |

### Phase 1 exit criteria

- [ ] Fresh repo + `.agent/memory.md` → agent produces discovery pack in one session
- [ ] PRD input → delivery pack with Y-Score score and Gherkin AC
- [ ] `cybersec-skill` blocks sample PII injection attempt
- [ ] `qa-tester-skill` produces edge-case matrix for a sample API
- [ ] CI passes: no executables, all SKILL.md files valid
- [ ] Install guide verified on clean machine in < 5 minutes

---

## Recommended Build Order (Next 3 Sessions)

| Session | Focus | Deliverables |
|---------|-------|--------------|
| **Session 1** | Memory + Security | `.agent/memory.md`, `cybersec-skill`, update `productowner-skill` |
| **Session 2** | Discovery + Delivery | `PO-discovery`, `PO-delivery`, templates |
| **Session 3** | QA + Polish | `qa-tester-skill`, `PO-kb-research`, `PO-code-pipeline`, INSTALL.md, CI lint |

---

## Persona Vote Summary

| Persona | Phase 1 priority |
|---------|------------------|
| Technical Architect | Plugin contract + memory standard |
| Product Owner | Discovery + delivery generators with Y-Score |
| Business Strategist | Trust narrative + OSS distribution |
| Cybersecurity | `cybersec-skill` as mandatory gate |
| Engineering Lead | Skills-as-code + CI validation |

**Unanimous:** Defer enterprise API integrations to Phase 2. Ship the persona skill swarm foundation first.
