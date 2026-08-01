---
name: y-score-readiness
description: Score a PRD or pilot against the 7-dimension Y-Score launch-readiness rubric (problem clarity, target user, success metric, constraints, compliance, eval plan, rollback). Returns a 0-100 score plus per-dimension findings and a go / no-go recommendation. Use when a PO is deciding whether a pilot is ready to launch, especially in BFSI / healthcare / regulated domains.
---

# y-score-readiness

The PO gate that runs before `prd-to-sdlc` produces any artifacts. Refuses to proceed if score < 70.

## When to trigger
- `/y-score <prd.md>`
- User says "is this ready to launch?", "readiness check", "score this PRD"
- Auto-invoked by `prd-to-sdlc` orchestrator stage 1

## The 7 dimensions

| # | Dimension | Weight | Anchor for full marks |
|---|---|---|---|
| 1 | Problem clarity | 15 | One-sentence statement, measurable, user-visible |
| 2 | Target user | 10 | Named persona + JTBD + frequency |
| 3 | Success metric | 20 | Leading + lagging metric with baseline + target |
| 4 | Constraints | 10 | Latency / cost / data residency / SLA defined |
| 5 | Compliance posture | 15 | Domain checklist done (HIPAA / PCI / GDPR / EU-AI-Act) |
| 6 | Eval plan | 20 | Golden set + judge + regression suite + drift monitor |
| 7 | Rollback plan | 10 | Kill switch + comms + data-recovery RTO defined |

## Scoring
- Per dimension: 0 (missing) / 50 (partial) / 100 (full)
- Weighted total = sum(dim_score × weight) / 100
- **Gate:** total ≥ 70 → proceed. < 70 → return findings, block downstream stages.

## Output format
```json
{
  "score": 78,
  "verdict": "go",
  "dimensions": {
    "problem_clarity": {"score": 100, "note": "..."},
    "target_user":     {"score": 50,  "note": "Persona named but JTBD missing"},
    ...
  },
  "blockers": [],
  "recommendations": ["Add LLM-as-judge calibration step to eval plan"]
}
```

## Domain-aware compliance dimension
Compliance dimension auto-checks against domain:
- `bfsi` → PCI-DSS, FATF, BSA, fair-lending, EU-AI-Act high-risk
- `healthcare` → HIPAA, FHIR consent, FDA SaMD class (if applicable)
- `eu` → GDPR DPIA, EU-AI-Act risk tier
- `generic` → baseline SOC 2 + privacy review

## Author
Vignesh AIPM — distilled from 10 years shipping AI in regulated BFSI / healthcare environments.
