---
name: PO-delivery
description: Generate a delivery pack — RICE-scored backlog, KPI instrumentation plan, rollout phases, and PRD — from repo memory and an input PRD. Invokes y-score-readiness gate. Regulated-domain aware (BFSI/healthcare). Synthetic data only. Writes to artifacts/delivery/.
triggers:
  - "prioritize backlog"
  - "RICE score"
  - "KPI plan"
  - "delivery pack"
  - "rollout plan"
  - "write delivery artifacts"
---

# PO-delivery — Backlog, KPI & Rollout Pack

## Step 0 — Read Local Memory + Input PRD
1. Read `.agent/memory.md` — adapt domain, users, constraints, compliance.
2. Read input PRD from user-provided path (e.g. `prds/*.md`, `artifacts/delivery/prd.md`) or draft from `templates/prd.md`.
3. If no PRD exists, generate `artifacts/delivery/prd.md` first using the template, then continue.

## Inputs
| Field | Required | Source |
|-------|----------|--------|
| Repo context | ✅ | `.agent/memory.md` |
| PRD | ✅ | User path or `templates/prd.md` |
| Discovery pack | optional | `artifacts/discovery/` (for market context) |

## Outputs (write to `artifacts/delivery/`)
| File | Template | Description |
|------|----------|-------------|
| `prd.md` | `templates/prd.md` | Problem, users, Gherkin AC, constraints |
| `rice-backlog.md` | `templates/rice-backlog.md` | RICE-scored epics/stories |
| `kpi-plan.md` | `templates/kpi-plan.md` | Leading/lagging metrics + instrumentation |
| `rollout-phases.md` | *(inline)* | Phased rollout with gates and rollback |

### Artifact frontmatter (required on every file)
```yaml
---
domain: {{domain}}
stage: delivery
type: {{prd|rice-backlog|kpi-plan|rollout-phases}}
compliance-regime: {{hipaa|pci-dss|gdpr|eu-ai-act|generic}}
generated: {{ISO-date}}
synthetic-data: true
---
```

## Workflow
1. Read memory + PRD → ensure every story has Gherkin AC (Given/When/Then).
2. Copy templates from `skills/PO-delivery/templates/` → fill `{{placeholders}}`.
3. Score backlog with RICE: **Reach × Impact × Confidence / Effort** — document assumptions.
4. Build KPI plan: leading + lagging metrics, baseline, target, instrumentation owner.
5. Define rollout phases: pilot → limited → GA — each with entry/exit criteria and rollback.
6. **Invoke `y-score-readiness` gate** on the PRD — BLOCK delivery pack if score < 70.
7. Run persona swarm gates:
   - `cybersec-skill` — BLOCK on PII/PHI
   - `ux-pro-skill` — BLOCK on critical a11y; WARN on style
   - `qa-tester-skill` — WARN on untestable AC or missing edge cases
8. Write final pack to `artifacts/delivery/`.

## RICE Scoring Guide
| Factor | Scale | Notes |
|--------|-------|-------|
| Reach | users/quarter | Synthetic estimate from memory personas |
| Impact | 0.25–3 | 0.25=minimal, 1=medium, 2=high, 3=massive |
| Confidence | 0–100% | Lower if based on assumptions |
| Effort | person-months | Include design + eng + QA |

Sort descending by RICE score. Flag items with Confidence < 50% for discovery follow-up.

## Y-Score Gate (mandatory)
Delegate to `y-score-readiness` before marking delivery complete.
- Score ≥ 70 → proceed to release
- Score < 70 → return per-dimension findings; do not write rollout-phases until blockers resolved

## Regulated Domain Rules
| Domain | Delivery pack must include |
|--------|---------------------------|
| `bfsi` | Fair-lending checks, model explainability, audit trail KPIs |
| `healthcare` | HIPAA eval plan, consent flows in AC, PHI-free test data |
| `eu` | GDPR lawful basis, DPIA reference, EU-AI-Act risk tier |
| `generic` | Privacy review checkpoint, rollback RTO |

## Data Rules
- **Synthetic data only** — mock user IDs, anonymised metrics, fictional company names.
- Gherkin AC must use synthetic personas from memory glossary.
- Never embed API keys, real endpoints, or production credentials in rollout plans.

## Gate Verdict
Return a summary:
```
Delivery pack: artifacts/delivery/
Files: prd.md, rice-backlog.md, kpi-plan.md, rollout-phases.md
Y-Score: {{score}} ({{go|no-go}})
Gates: cybersec {{PASS|BLOCK}} · ux {{PASS|WARN|BLOCK}} · qa {{PASS|WARN}}
```
