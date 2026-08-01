# Phase 1 Brainstorm — 6-Persona Deep Session (Outcomes-First)

**Date:** 2026-08-01 (revised)  
**Author:** Vignesh AIPM  
**Purpose:** Reconcile technical, product, business, security, engineering, and UX views — anchored on **what users want and the outcomes they need** — to produce a revised Phase 1 scope.  
**Inputs:** `ROADMAP.md`, `prds/00-pm-os-platform.md`, `planning/meta_agent_swot_analysis.md`, `planning/cybersecurity_trust_plan.md`, `planning/persona_skills_roadmap.md`, `planning/rice_prioritization_matrix.md`, `planning/reusable_skills_plan.md`

---

## What Users Want — Outcomes First

Features are means. Phase 1 is scoped by **user outcomes**, not integration checkboxes.

### User segments and desired outcomes

| User | What they want (outcome) | How Phase 1 delivers it |
|------|--------------------------|-------------------------|
| **Product Owner** | Stop rewriting the same PRD/SWOT from scratch every sprint | Discovery + delivery skills + templates + local memory |
| **Product Owner** | Ship features that are launch-ready, not "almost done" | Y-Score gate + Gherkin AC + DoR checks |
| **Product Owner** | Reuse what the org already knows without searching 5 tools | Local `artifacts/` + `PO-kb-research` (API search in Phase 2) |
| **PO Lead / Manager** | See team output quality, not just velocity | Persona swarm gates (security + UX + QA) on every artifact |
| **Designer / Frontend Dev** | UI that passes WCAG and matches design system without manual audit loops | `ux-pro-skill` — a11y + design tokens + flow simplification |
| **Engineer** | Clear AC, edge cases, and security boundaries before coding | `qa-tester-skill` + `cybersec-skill` + Gherkin from PO skill |
| **InfoSec / Compliance** | Proof the tool won't leak PII or run arbitrary code | Declarative skills only, PII blocker, no executables |
| **Consulting PO** | Client-ready deliverables that look professional and are accessible | UX-reviewed demo + artifact templates + trust package |
| **Client Stakeholder** | Understand programme status without a Jira licence | Static client workspace demo (full tenant in Phase 4) |
| **Admin / P&T Ops** | Install in minutes, pass security review, no new infra | Plugin install guide + SECURITY.md + CI validation |

### Outcome statements (Phase 1 success in user language)

1. *"I opened a new repo, filled in memory, and had a compliant discovery pack in under an hour."*
2. *"My PRD came back with acceptance criteria I can hand straight to engineering."*
3. *"Security flagged PII before it hit the repo — I didn't have to remember the rules."*
4. *"The onboarding UI passed accessibility review without a separate audit sprint."*
5. *"I installed the plugin in 5 minutes — no Docker, no API keys, no ticket to IT."*
6. *"My demo looks enterprise-grade: accessible, consistent, trustworthy."*

### Outcome → skill mapping

```
User outcome                          Skill(s) responsible
─────────────────────────────────────────────────────────────
Fast, reusable discovery              PO-discovery + memory
Launch-ready delivery artifacts       PO-delivery + Y-Score
Safe, compliant outputs               cybersec-skill
Testable, complete requirements       qa-tester-skill
Accessible, consistent UI             ux-pro-skill
Repo-aware context                    .agent/memory.md
Professional first impression         docs/ demo + ux-pro-skill
```

---

## Session Setup

Six personas debated the current Phase 1 goal against what is built (static demo + planning docs) and what users actually need (outcomes above).

**Verdict:** Phase 1 = **"Trustworthy Plugin Foundation"** — ship a persona swarm (PO + Security + QA + **UX**) that delivers user outcomes, with local memory and templates, before enterprise API integrations.

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

### Gate model (persona swarm — see revised model at end)

```
User request → productowner-skill → cybersec-skill (BLOCK) → ux-pro-skill (BLOCK/WARN) → qa-tester-skill (WARN) → output
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
| E-05 | **GitHub Actions PRD Pipeline** | On PRD commit → Y-Score check + schema validation | 🟡 Stretch |
| E-07 | **OpenHands / MetaGPT Wiring** | Live code generation loops | ❌ Phase 5 |
| E-08 | **Promptfoo Eval Gate** | Mandatory eval before deploy | ❌ Phase 5 |

### Engineering recommendation
> Phase 1 = **skills as code**. Add CI that treats `SKILL.md` like source files. Defer autonomous coding loops to Phase 5.

---

## Persona 6 — UX/UI Designer (Design Systems & Accessibility)

**Lens:** User experience, WCAG compliance, cognitive load, design consistency.

### What users want from UX (not features)

| User pain | Desired outcome |
|-----------|-----------------|
| "Our demo failed an accessibility audit" | Ship UI that passes WCAG 2.1 AA without a separate audit sprint |
| "Every PO builds screens differently" | Enforce design tokens and component patterns from memory |
| "Users abandon the onboarding wizard" | Reduce steps, add clear progress, fix keyboard/screen-reader gaps |
| "Stakeholders don't trust the UI" | Consistent visual language, loading states, error boundaries |
| "I don't know if this flow is too complex" | Cognitive load review with step-reduction recommendations |

### Feature proposals

| ID | Feature | Description | Phase 1? |
|----|---------|-------------|----------|
| U-01 | **Accessibility (a11y) Enforcer** | Scan HTML/React for missing `aria-*`, contrast, focus order, keyboard traps | ✅ Must |
| U-02 | **Design System Adherence** | Reject inline styles; enforce tokens from `.agent/memory.md` design section | ✅ Must |
| U-03 | **Cognitive Load Reduction** | Review flows (onboarding, wizard, forms); suggest step merges and autofill | ✅ Must |
| U-04 | **Micro-Interaction Mapping** | Recommend hover, loading skeleton, error boundary for new components | 🟡 Stretch |
| U-05 | **Portfolio Demo UX Pass** | Run `ux-pro-skill` on `docs/` before every release | ✅ Must |
| U-06 | **UX Outcome Report** | Output: pass/fail per WCAG criterion + fix list + flow score | ✅ Must |

### UX recommendation
> Users judge the whole product by the demo UI. `ux-pro-skill` is not polish — it is **trust**. Enterprise buyers equate inaccessible UI with immature product. Promote from stretch to **P1 core**.

### UX intensity levels (like caveman modes)

| Mode | Scope |
|------|-------|
| `lite` | a11y scan on changed files only |
| `full` | **Default.** a11y + design tokens + flow review |
| `ultra` | Full + micro-interactions + responsive breakpoints |

---

## Cross-Persona Debate — Key Tensions Resolved

| Tension | Resolution |
|---------|------------|
| Product wants KB search now vs Architect says defer APIs | **Defer live integrations to Phase 2.** Phase 1 uses local `artifacts/` + `prds/` as mock KB. |
| Business wants monetisation vs Security wants zero telemetry | **No billing in Phase 1.** Trust narrative + OSS distribution first. |
| PO wants AI generation vs Security wants zero LLM cost | **Phase 1 skills work with any model the user's agent already has.** No bundled API calls. |
| Engineer wants E2E codegen vs Architect wants no scripts | **qa-tester outputs test *definitions* in markdown.** Playwright files are generated by agent on demand, not shipped as scripts. |
| Original Phase 1 listed Rovo/M365/Google | **Moved to Phase 2** — requires backend OAuth, violates current zero-network skill rule. |
| UX was "stretch" but users judge product by demo UI | **`ux-pro-skill` promoted to P1 core.** Outcome: accessible, consistent demo without separate audit. |
| Features vs outcomes | **Scope by outcome statements first.** Every Tier A item maps to a user outcome above. |

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
| 8 | `skills/ux-pro-skill/SKILL.md` | UX | a11y enforcer + design tokens + cognitive load review |
| 9 | Upgrade `skills/productowner-skill/SKILL.md` | Product | Read memory first; delegate to sub-skills |
| 10 | Template library under `skills/*/templates/` | Technical | Generic PRD, SWOT, ROI, KPI templates |
| 11 | Trust package update | Business | README + SECURITY.md + landing page trust badge |
| 12 | Plugin install guide | Business | `docs/INSTALL.md` — 5-minute setup |
| 13 | Portfolio demo UX pass (`docs/`) | UX | ux-pro-skill run on onboarding + landing before release |
| 14 | CI skill lint (`check-source.mjs` extension) | Engineering | Ban executables + validate SKILL structure |

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
| 23 | Micro-Interaction Mapping (ux-pro ultra) | UX |
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

**New goal:** Any PO can install the skill plugin, point it at any repository, and get **launch-ready outcomes** — discovery pack, delivery pack, accessible UI, security-cleared artifacts — without backend infrastructure, OAuth, or live enterprise integrations.

**Tagline:** *Outcomes users want. Skills that deliver. Zero scripts. Zero telemetry.*

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
| **`ux-pro-skill` (a11y + design tokens + flow review)** | 🔲 Next | P1 |
| **Portfolio demo UX pass (`docs/` onboarding + landing)** | 🔲 Next | P1 |
| **Template library (`skills/*/templates/`)** | 🔲 Next | P1 |
| **Plugin install guide (`docs/INSTALL.md`)** | 🔲 Next | P1 |
| **CI skill validation** | 🔲 Next | P2 |
| **Trust badge on landing page** | 🔲 Next | P2 |
| ~~Atlassian Rovo KB search~~ | ⏭️ Phase 2 | — |
| ~~Microsoft 365 Graph search~~ | ⏭️ Phase 2 | — |
| ~~Google Workspace API search~~ | ⏭️ Phase 2 | — |

### Phase 1 exit criteria (outcome-based)

| # | User outcome | Verification |
|---|--------------|--------------|
| 1 | Discovery pack in one session | Fresh repo + `.agent/memory.md` → SWOT + TAM/SAM/SOM + compliance map |
| 2 | Launch-ready delivery artifacts | PRD → delivery pack + Y-Score score + Gherkin AC |
| 3 | Safe outputs | `cybersec-skill` blocks sample PII injection |
| 4 | Testable requirements | `qa-tester-skill` produces edge-case matrix for sample API |
| 5 | Accessible demo UI | `ux-pro-skill` passes WCAG review on `docs/onboarding` + `docs/index.html` |
| 6 | Consistent design | No inline styles on demo pages; design tokens documented in memory |
| 7 | Fast install | Install guide verified on clean machine in < 5 minutes |
| 8 | CI trust | No executables; all SKILL.md files valid |

---

## Recommended Build Order (Next 4 Sessions)

| Session | Focus | User outcome delivered |
|---------|-------|------------------------|
| **Session 1** | Memory + Security | Repo-aware, safe outputs |
| **Session 2** | Discovery + Delivery | Fast PRD/discovery without starting from scratch |
| **Session 3** | QA + UX | Testable requirements + accessible demo |
| **Session 4** | Pipeline + Polish | End-to-end skill chain + install guide + CI |

### Session deliverables detail

| Session | Deliverables |
|---------|--------------|
| **1** | `.agent/memory.md`, `cybersec-skill`, update `productowner-skill` |
| **2** | `PO-discovery`, `PO-delivery`, templates |
| **3** | `qa-tester-skill`, `ux-pro-skill`, portfolio UX pass on `docs/` |
| **4** | `PO-kb-research`, `PO-code-pipeline`, INSTALL.md, CI lint |

---

## Persona Swarm Gate Model (revised)

```
User request
  → productowner-skill (PRD / AC / prioritization)
  → cybersec-skill (PII + OWASP) — BLOCK if fail
  → ux-pro-skill (a11y + design tokens + flow) — BLOCK on critical a11y; WARN on style
  → qa-tester-skill (edge cases) — WARN if gaps
  → output released to repo / demo
```

---

## Persona Vote Summary

| Persona | Phase 1 priority | User outcome owned |
|---------|------------------|-------------------|
| Technical Architect | Plugin contract + memory standard | "Works in any repo in 5 min" |
| Product Owner | Discovery + delivery + Y-Score | "PRD ready for engineering" |
| Business Strategist | Trust narrative + OSS distribution | "Passes InfoSec review" |
| Cybersecurity | `cybersec-skill` as mandatory gate | "No PII leaks" |
| Engineering Lead | Skills-as-code + CI validation | "Maintainable, testable" |
| UX/UI Designer | `ux-pro-skill` + demo UX pass | "Accessible, professional UI" |

**Unanimous:** Defer enterprise API integrations to Phase 2. Ship the full persona swarm (PO + Security + QA + UX) first — scoped by user outcomes, not feature count.
