# PRD 09 — CuCP 90-Day Rollout: Customer Collaboration Program Operationalisation

**Domain:** P&T Operations · Program Management
**Author:** Vignesh Vignesh S
**Status:** MVP · Case Study · Coupa Sr. Lead P&T Operations
**Program:** Customer Collaboration Program (CuCP) — Coupa Software

---

## Problem

Coupa's pre-release customer engagement has been ad-hoc. EAP and Limited Availability
phases lack standardised governance, creating three compounding failure modes:

1. **Definition drift** — scope and exit criteria shift during pre-GA phases, causing
   misaligned customer expectations and delayed or risky GA decisions.
2. **Fragmented execution** — each PM runs their own engagement model, producing
   inconsistent customer experience and zero institutional learning.
3. **PM resistance** — new structured processes are perceived as administrative overhead
   that slows release velocity rather than accelerating it.

The CuCP v1.0 framework has been drafted and approved by leadership. The gap is
**adoption** — turning a paper framework into operational reality across the PM org.

---

## Target User

**Primary:** Product Managers at Coupa shipping Standard or AI capabilities through
EAP → Pre-GA → GA phases.

**Secondary:** P&T Leadership who need visibility and confidence in release readiness.

**Resistance persona (the adoption blocker):** The sceptical PM who sees CuCP as
compliance tax. This persona must be converted through evidence, not mandate.

---

## Solution: 90-Day Rollout Plan

Adoption is **earned, not mandated.** The rollout follows a Pilot → Learn → Scale model.

### The Framing Shift (Change Management Core)

The single message to land with every PM:

> "CuCP is your evidence kit — not a compliance checklist."

Structured EAP/LA phases protect PMs at GA. They answer "how do we know this is ready?"
with customer data instead of gut feel. For AI capabilities especially, this evidence
is what separates a clean launch from a rollback. CuCP = launch accelerator, not gatekeeper.

Tactics to shift perception:
- Lead with PM pain, not programme goals: "You've been asked to justify GA readiness
  with no data. CuCP gives you that data."
- Find proto-champions — PMs already doing informal EAP governance well. Their story
  converts sceptics faster than any top-down message.
- Make the first experience ridiculously easy: templates pre-filled, I handle admin,
  PM just runs their programme.

---

## Phase 1: Listen & Align — Days 1–30

**Goal:** Understand real friction before imposing solutions.

| Action | Output |
|--------|--------|
| 1:1 listening sessions with 8–10 PMs | Friction map: where time is lost, where trust is low |
| Shadow 2 live EAP/LA cycles | Ground truth on actual workflow vs. perceived workflow |
| Identify proto-champions (good informal EAP managers) | Pilot PM shortlist |
| Select pilot cohort: 1 Standard, 1 AI, 1 sceptic-but-persuadable | Pilot confirmed with rationale |
| Playbook v0.1 adjusted from v1.0 draft based on listening | Playbook ready for pilot |
| Day 30 read-out to P&T Leadership | Friction map + pilot plan + adjusted framework |

**Decision gate:** Do pilot PMs feel the adjusted playbook addresses their concerns?
If no → iterate before proceeding.

---

## Phase 2: Pilot & Refine — Days 31–60

**Goal:** Run CuCP with pilot PMs, prove the value proposition, build the playbook.

| Action | Output |
|--------|--------|
| Launch 2–3 live CuCP pilots (Standard + AI + edge case) | Real programmes running |
| Act as embedded CuCP Concierge for pilot PMs | PM learns process; I absorb admin overhead |
| Weekly retros with pilot PMs: what saved time, what added time | Playbook v1.0 |
| Capture "before/after" evidence: EAP→GA cycle time, customer feedback quality, drift incidents | Proof points for scaling |
| PM Champion activation: pilot PMs tell their own story | Internal advocacy (more credible than me) |
| "CuCP in 5 minutes" cheat sheet — Standard version + AI version | Self-serve onboarding asset |

**Capability-specific playbook differences:**

| | Standard Capability | AI Capability |
|---|---|---|
| Phase 2 trigger | Optional — PM decides based on risk/complexity | Default for Copilot/Agent Studio (needs telemetry) |
| Customer cohort | 5–10 curated, $0 order form | All eligible, frictionless UI toggle |
| Primary goal | Operational readiness + support enablement | Model tuning + trust/safety guardrails + telemetry |
| PM workload | Moderate (controlled cohort comms) | Lower admin (broad open beta self-serves) |

**Decision gate:** Do pilot PMs say CuCP saved them time or reduced launch risk?
If yes → scale. If no → fix playbook before scaling.

---

## Phase 3: Scale & Institutionalise — Days 61–90

**Goal:** Expand CuCP to full PM org with structured enablement and self-serve support.

| Action | Output |
|--------|--------|
| All-hands PM enablement: led by pilot champions, not by me | Peer-to-peer credibility |
| Tiered training: 30-min onboarding all PMs + deep-dive for AI capabilities | Everyone enabled |
| Self-serve KB: playbook, templates, decision trees, pilot examples | Zero dependency on me for basics |
| #cucp-support Slack channel + weekly office hours | Live support without bottleneck |
| Automate admin: customer invitation templates, $0 order form workflow, exit criteria tracker | < 2 hrs PM overhead per release |
| Leadership dashboard: CuCP coverage %, PM confidence, customer participation rate | Visibility without asks |

---

## Proportional Governance Principle

The rollout applies the same principle as the CuCP Phase Matrix itself:
**adoption pressure must be proportional to the evidence available.**

| Window | Approach |
|--------|----------|
| Days 1–30 | No mandate. Observe and listen only. |
| Days 31–60 | Voluntary pilot. Earn trust through service. |
| Days 61–90 | Structured enablement. Clear expectation for eligible releases. |
| Day 90+ | Data-backed mandate discussion with leadership — only after PM satisfaction confirms value. |

---

## Success Metrics

| KPI | Baseline | Day 90 Target | Measured By |
|-----|----------|--------------|-------------|
| % eligible releases using CuCP | 0% (ad-hoc) | ≥ 50% | Release tracker |
| PM satisfaction score (is CuCP helping?) | — | ≥ 4.0 / 5.0 | Post-pilot + post-scale survey |
| EAP → GA cycle time | Measure in Days 1–30 | No regression; target 10% faster | Release logs |
| Definition drift incidents | Unmeasured | Tracked; target 0 in pilots | EAP/LA retros |
| Customer participation rate | — | ≥ 70% of invited customers engage | CuCP programme tracker |
| PM time on CuCP admin per release | — | < 2 hours | PM self-report |

**Leading indicator — most important in Days 1–90:**
PM satisfaction score. If PMs feel CuCP helps, scaling is pull, not push.
If they feel it hurts, fix the playbook — mandate never replaces trust.

---

## Deliverables

### Days 1–30
- Friction map (listening session synthesis)
- Pilot PM cohort with selection rationale
- Playbook v0.1 (adjusted from v1.0 draft)
- Day 30 leadership read-out

### Days 31–60
- 2–3 live pilot CuCP programmes
- Weekly retro outputs + playbook iterations
- "CuCP in 5 minutes" cheat sheets (Standard + AI)
- Champion story documentation

### Days 61–90
- Playbook v1.0 (validated, self-serve)
- All-PM enablement session delivered
- #cucp-support channel + weekly office hours live
- Leadership tracking dashboard live
- Day 90 read-out: metrics, learnings, Phase 2 scale plan

---

## Slide Mapping (Interview Deck)

| Slide | Section in this PRD |
|-------|---------------------|
| 1 | Title |
| 2 | Problem → The Framing Shift (change management strategy) |
| 3 | Phase 1–2–3 table (90-day phased rollout) |
| 4 | Enablement & Support model (Phase 3 actions + cheat sheet + KB) |
| 5 | Success Metrics table |
| 6 | What Day 90 looks like + my ask of leadership |

---

## Out of Scope (90-day window)

- Jira / tooling integration for CuCP tracking (v2 — after playbook is stable)
- Mandatory compliance gate before any release (requires established trust first)
- Retroactive CuCP documentation for in-flight releases
- External customer-facing CuCP communications (PM-facing only in 90 days)
- Standard capability Phase 2 mandate (proportional governance — PM-decided)
