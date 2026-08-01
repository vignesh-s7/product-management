---
name: productowner-skill
description: Core Product Owner orchestration. Defines PRD acceptance criteria, manages the SDLC lifecycle, and delegates tasks safely to persona swarm skills (PO-discovery, PO-delivery, cybersec, UX, QA, Y-Score) without raw execution. Regulated-domain aware (BFSI/healthcare). Synthetic data only.
triggers:
  - "Act as Product Owner"
  - "Write a PRD"
  - "Groom the backlog"
  - "Run PO workflow"
  - "Discovery to delivery"
---

# Product Owner Orchestration (Safe Mode)

## 0. Read Local Memory First
**Before any output**, read `.agent/memory.md` in the current repository (create from schema if missing).
Adapt all artifacts — domain, users, constraints, compliance regime, glossary, design tokens — to repo context.
Never hardcode product names, client data, or compliance assumptions from this skill repo.

## 1. Y-Score Readiness Check (MANDATORY)

**MANDATORY:** Whenever writing or finalizing a PRD or any launch-bound artifact, you **MUST** invoke the `y-score-readiness` skill before release. No exceptions.

1. Read and score the artifact via `y-score-readiness` (7-dimension rubric).
2. Validate the gate output against `schemas/gates/y-score-gate.schema.json`.
3. **If Y-Score < 70:** **BLOCK** release — output the full score, per-dimension findings, `blockers`, and `recommendations`; do **not** write to `artifacts/` or commit.
4. **If Y-Score ≥ 70:** proceed to the release step in the gate flow (§4).

This check enforces Definition of Ready (DoR) for every launch-bound deliverable.

### DoR — Analytics / telemetry check (WARN only)

Before releasing a PRD or launch-bound artifact, verify an **analytics / telemetry** section exists covering:

| Required element | What to look for |
|------------------|------------------|
| **Events** | Named user/system events to track (e.g. `onboarding_completed`, `order_submitted`) |
| **Properties** | Event payload fields and dimensions (user segment, feature flag, error code) |
| **Success metrics** | Leading/lagging KPIs tied to events with baseline and target |

**If any element is missing:** emit a **WARN** (not BLOCK) and append to the **DoR findings list**:

```markdown
## DoR findings

| # | Dimension | Severity | Finding | Recommendation |
|---|-----------|----------|---------|----------------|
| DOR-001 | analytics | WARN | No telemetry events defined for core user flows | Add events + properties table before GA |
```

Proceed with release when Y-Score ≥ 70; surface WARN findings for human review. Do not block on missing analytics alone.

## 2. Gherkin Acceptance Criteria (Given/When/Then)
Always enforce strict BDD/Gherkin acceptance criteria in every PRD and user story.
* **Given** [context]
* **When** [action]
* **Then** [outcome]

## 3. Persona Swarm Delegation
Do **NOT** execute bash scripts to orchestrate other agents. Use declarative instructions and safe integrations:

| Stage | Skill | Responsibility |
|-------|-------|----------------|
| Discovery | `PO-discovery` | SWOT, TAM/SAM/SOM, competitor matrix, compliance risk map, GTM brief |
| Delivery | `PO-delivery` | RICE backlog, KPI plan, rollout phases, PRD drafting |
| Architecture | `system-architect-skill` | Mermaid.js C4, schema, API contracts |
| Engineering | `builder-skill` | Sandboxed OpenHands wrapper |
| Readiness gate | `y-score-readiness` | 7-dimension launch check (≥ 70 to proceed) |
| Security gate | `cybersec-skill` | PII/PHI blocker + OWASP audit |
| UX gate | `ux-pro-skill` | a11y (WCAG), design tokens, cognitive load review |
| QA gate | `qa-tester-skill` | Edge-case / boundary matrix, Playwright definitions |
| SDLC bundle | `prd-to-sdlc` | PRD → architecture + code + evals (Phase 5) |

## 4. Gate Flow (Write → Release)
Every artifact passes through the persona swarm before release:

```
write artifact
  → DoR analytics check   (WARN if events/properties/success metrics missing — see §1)
  → cybersec-skill      (BLOCK on PII/PHI or critical OWASP findings)
  → ux-pro-skill        (BLOCK on critical a11y; WARN on style/token drift)
  → qa-tester-skill     (WARN on missing edge cases or untestable AC)
  → y-score-readiness   (MANDATORY for PRDs and launch-bound artifacts)
      · invoke y-score-readiness skill
      · validate against schemas/gates/y-score-gate.schema.json
      · BLOCK if score < 70 — output findings; do not release
      · proceed only if score ≥ 70
  → release to artifacts/
```

**DoR WARN** = write with `> ⚠️ DoR finding:` callout in the artifact; include row in DoR findings list.

**BLOCK** = do not write or commit until resolved. For Y-Score failures, always surface score, dimension notes, `blockers`, and `recommendations`.
**WARN** = write with `> ⚠️ QA/UX finding:` callout; flag for human review.

## 5. Artifact Conventions
- Discovery outputs → `artifacts/discovery/`
- Delivery outputs → `artifacts/delivery/`
- Tag every file: `domain` · `stage` · `type` · `compliance-regime`
- Use templates from `skills/*/templates/` — fill `{{placeholders}}` from memory context
- **Synthetic data only** — mock personas, anonymised metrics, no real client identifiers

## 6. Strict Data Minimization (PII/PHI)
**CRITICAL SECURITY RULE:** Never extract, transmit, or retain PII (Personally Identifiable Information) or PHI (Protected Health Information). Always use synthetic, mock data in PRDs and test cases.

## Regulated Domain Awareness
When `.agent/memory.md` declares `domain: bfsi` or `domain: healthcare`:
- Inject HIPAA / PCI-DSS / GDPR / EU-AI-Act checklists into discovery compliance maps
- Require eval plan + rollback in delivery KPI plans
- Escalate any data-residency or consent gaps to BLOCK via `cybersec-skill`
