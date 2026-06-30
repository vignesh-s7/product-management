# PRD 09 — CuCP 90-Day Rollout: Customer Collaboration Program Operationalisation

**Domain:** P&T Operations · Program Management
**Author:** Vignesh Vignesh S
**Status:** MVP · Coupa Sr. Lead P&T Operations — Case Study
**Live Deck:** [docs/cucp/presentation.html](../docs/cucp/presentation.html)

---

## Case Study Brief (Preserved from Coupa Assignment)

**Role:** Sr. Lead, P&T Operations — Coupa Software
**Programme:** Customer Collaboration Program (CuCP)
**Mandate:** Lead, execute, and scale the CuCP across the Product Management organisation.

### The Scenario
Coupa is institutionalising how it partners with customers throughout the product lifecycle,
particularly during pre-release phases. The foundational framework is drafted and approved.

**Challenge:** The framework exists on paper but has not been implemented or adopted by the PM org.
Historically, customer engagement prior to GA has been ad-hoc. PMs perceive CuCP as
"administrative overhead" that will slow release velocity rather than enable success.

### The Assignment
Create a plan to successfully implement and scale CuCP across the organisation in the first 90 days.

**Four pillars required:**
1. Change Management & Adoption Strategy
2. Rollout Execution (phased approach)
3. Enablement & Support
4. Measuring Initial Success

### Provided Context: Coupa CuCP Framework

**Core Problem:** Fragmented Execution — lack of standardised governance for EAP/LA phases
causes "definition drift", creating operational risk and a compromised path to GA.

**Opportunity:** A Predictable Engine — a unified operating model that aligns cross-functional
teams, standardises launch phases, builds customer trust, de-risks the roadmap, and accelerates
time-to-value.

**Capability Classifications:**

| Type | Definition | Pre-GA Focus | Release Characteristics |
|------|-----------|-------------|------------------------|
| Standard | Deterministic logic, no AI. e.g. sourcing dashboards, workflow routing, UI redesigns | Validate operational readiness, scalability, support enablement | Readiness + enablement primary; controlled customer cohorts sufficient |
| AI | Powered by AI/ML/LLMs. Probabilistic models. e.g. Copilot (AI-Assisted), Agent Studio (Agentic) | Model tuning, trust/safety guardrails, real-world telemetry | Learning + usage patterns primary; benefits from broad customer interaction |

**The Coupa Phase Matrix:**

| Phase | Standard Capability | AI Capability |
|-------|--------------------|--------------------|
| Phase 1: EAP (Closed Beta) | Goal: validate core UX, value, workflow. 5–10 customers max. $0 order form. | Free (AI Credits). High-touch PM/Eng engagement. |
| Phase 2: Pre-GA (Variable) | Goal: validate operational readiness. Explicitly approved cohorts. $0 order form. Readiness gate with commercial alignment. | Early Access (Open Beta). Goal: learn, ingest telemetry, tune models at scale. Available to all eligible. Frictionless UI toggle. No $0 forms. Free (AI Credits). |
| Phase 3: GA | Production-ready, fully supported, meets all standard SLAs. Complete GTM enablement and fully monetised. | Same. |

**Principle of Proportional Governance:** The level of release gating must be proportional
to the risk, complexity, and impact of the feature. Phase 2 is optional — PM decides based
on risk/complexity/operational impact.

---

## Slide Deck: 90-Day Rollout Plan

*Live interactive version: `docs/cucp/presentation.html` (keyboard navigable)*

---

### Slide 1 — Title
**"Turning the CuCP Framework into Adopted Reality"**
A 90-day plan to implement and scale the Customer Collaboration Program — from paper
framework to predictable launch engine.

**Presented by:** Vignesh Vignesh S · Sr. Lead, P&T Operations · Coupa

---

### Slide 2 — The Challenge & The Reframe

**The Problem: Fragmented Execution**
- Ad-hoc EAP/LA engagement with no standard process
- "Definition drift" — scope shifts before GA
- No exit criteria → risky launch decisions
- PMs see CuCP as admin overhead slowing velocity

**Strategy: Earn Adoption, Don't Mandate It**
- Lead with PM pain — not programme goals
- Find proto-champions already doing good EAP work
- Make the first experience frictionless — I absorb the admin
- Their story converts sceptics; mine doesn't

> **The message that lands:**
> *"CuCP is your evidence kit — not a compliance checklist."*
> Structured EAP data protects PMs at GA. It answers "how do we know this is ready?"
> with customer signal, not gut feel.

---

### Slide 3 — 90-Day Rollout: Pilot → Learn → Scale

No big-bang mandate. Build trust through service, then scale on proven evidence.

**Phase 1: Listen & Align (Days 1–30)**

Goal: Understand real friction before imposing solutions.

| Action | Output |
|--------|--------|
| 1:1 listening sessions with 8–10 PMs | Friction map: where time is lost, where trust is low |
| Shadow 2 live EAP/LA cycles | Ground truth on actual workflow vs. perceived |
| Identify proto-champions | Pilot PM shortlist |
| Select pilot: 1 Standard + 1 AI + 1 sceptic | Pilot cohort confirmed |
| Adjust playbook v0.1 from v1.0 draft | Playbook ready for pilot |

Output: **Friction map + pilot cohort confirmed**

**Phase 2: Pilot & Refine (Days 31–60)**

Goal: Run CuCP with pilot PMs, prove value, build the playbook.

| Action | Output |
|--------|--------|
| Launch 2–3 live CuCP pilots | Real programmes running |
| Act as embedded CuCP Concierge | PM learns; I absorb admin overhead |
| Weekly retros — cut what adds time | Playbook v1.0 |
| Capture before/after evidence | Proof points for scaling |
| Activate PM champions | Internal advocacy |
| "CuCP in 5 minutes" cheat sheets (Standard + AI) | Self-serve onboarding asset |

Output: **Playbook v1.0 + champion stories**

**Phase 3: Scale & Institutionalise (Days 61–90)**

Goal: Expand CuCP to full PM org with structured enablement.

| Action | Output |
|--------|--------|
| All-hands enablement — led by pilot champions, not me | Peer-to-peer credibility |
| Self-serve KB: playbook, templates, decision trees | Zero dependency on me for basics |
| #cucp-support Slack + weekly office hours | Live support without bottleneck |
| Automate admin: invites, order forms, exit criteria tracker | < 2 hrs PM overhead per release |
| Leadership dashboard: CuCP coverage %, PM confidence, customer participation | Visibility without asks |

Output: **All PMs enabled · tracking dashboard live**

---

### Slide 4 — Enablement & Support Model

Four pillars that make CuCP stupidly easy to run — before it becomes expected.

| Pillar | What It Is | Timing |
|--------|-----------|--------|
| **CuCP Concierge** | I act as operational support for pilot PMs. They learn the process; I handle templates, invites, and exit criteria tracking. PM overhead: near zero. | Days 1–60, high-touch |
| **Playbook + Cheat Sheets** | Two 1-page cheat sheets: Standard path and AI path. Separate because their pre-GA goals, cohort sizes, and exit criteria differ meaningfully. | Live Day 45 |
| **#cucp-support + Office Hours** | Live Slack channel for real-time questions. Weekly 30-min open office hours for first 90 days. PMs get answers in minutes, not days. | Day 60 onwards, async + sync |
| **Champion-Led Rollout** | Pilot PMs present at the all-hands enablement session — not me. Peer stories are far more credible than top-down messaging for converting sceptics. | Day 65 all-hands |

---

### Slide 5 — Measuring Initial Success

Six metrics prove the rollout is working. One leading indicator matters most in first 90 days.

| KPI | Baseline | Day 90 Target | How Measured | Type |
|-----|----------|--------------|-------------|------|
| ⭐ **PM Satisfaction — "Is CuCP helping?"** | — | ≥ 4.0 / 5.0 | Post-pilot + post-scale survey | **Leading** |
| % eligible releases using CuCP | 0% (ad-hoc) | ≥ 50% | Release tracker | Lagging |
| EAP → GA cycle time | Measure Days 1–30 | No regression; –10% | Release logs | Lagging |
| Definition drift incidents | Unmeasured | Tracked; 0 in pilots | EAP/LA retros | Leading |
| Customer participation rate | — | ≥ 70% invited engage | CuCP tracker | Lagging |
| PM admin time per release | — | < 2 hours | PM self-report | Leading |

> ⭐ If PMs feel CuCP helps — scaling is pull, not push.
> If they feel it hurts — fix the playbook before mandating.

---

### Slide 6 — Day 90 Vision + Ask of Leadership

**Evidence of Success at Day 90:**
- ≥ 50% eligible releases running CuCP
- PM satisfaction ≥ 4.0 / 5.0
- 2–3 champion PMs advocating internally
- Self-serve KB live — zero dependency on me
- Leadership dashboard showing programme health

**Proportional Governance Principle (applied to the rollout itself):**

| Window | Approach |
|--------|----------|
| Days 1–30 | Observe only — no mandate |
| Days 31–60 | Voluntary pilot — earn trust |
| Days 61–90 | Clear expectation for eligible releases |
| Day 90+ | Data-backed mandate discussion — only after PM satisfaction confirmed |

**My Ask of P&T Leadership:**
- Air cover during pilot — no forced mandate before data exists
- Exec sponsor for the all-hands enablement session
- Access to 2–3 willing pilot PMs in Week 1
- Release log access for baseline measurement

---

## Success Metrics

| KPI | Baseline | Day 90 Target | Measured By |
|-----|----------|--------------|-------------|
| % eligible releases using CuCP | 0% | ≥ 50% | Release tracker |
| PM satisfaction score | — | ≥ 4.0 / 5.0 | Survey |
| EAP → GA cycle time | TBD Days 1–30 | No regression; –10% | Release logs |
| Definition drift incidents | Unmeasured | 0 in pilots | Retros |
| Customer participation rate | — | ≥ 70% | CuCP tracker |
| PM admin time per release | — | < 2 hours | Self-report |

---

## Out of Scope (90-day window)

- Jira/tooling integration for CuCP tracking (v2)
- Mandatory gate before any release (requires trust first)
- Retroactive documentation for in-flight releases
- External customer-facing CuCP communications
