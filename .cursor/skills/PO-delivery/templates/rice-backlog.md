---
domain: {{domain}}
stage: delivery
type: rice-backlog
compliance-regime: {{compliance-regime}}
generated: {{date}}
synthetic-data: true
---

# RICE-Scored Backlog — {{product_name}}

**Domain:** {{domain}} · **Sprint/Quarter:** {{planning_period}}

## Scoring Formula
**RICE = (Reach × Impact × Confidence) / Effort**

| Factor | Scale |
|--------|-------|
| Reach | {{reach_unit}} per quarter |
| Impact | 0.25 (minimal) → 3 (massive) |
| Confidence | 0–100% |
| Effort | person-months |

## Prioritised Backlog
| Rank | Epic / Story | Reach | Impact | Confidence | Effort | RICE | Notes |
|------|--------------|-------|--------|------------|--------|------|-------|
| 1 | {{item_1}} | {{item_1_reach}} | {{item_1_impact}} | {{item_1_confidence}}% | {{item_1_effort}} | {{item_1_rice}} | {{item_1_notes}} |
| 2 | {{item_2}} | {{item_2_reach}} | {{item_2_impact}} | {{item_2_confidence}}% | {{item_2_effort}} | {{item_2_rice}} | {{item_2_notes}} |
| 3 | {{item_3}} | {{item_3_reach}} | {{item_3_impact}} | {{item_3_confidence}}% | {{item_3_effort}} | {{item_3_rice}} | {{item_3_notes}} |
| 4 | {{item_4}} | {{item_4_reach}} | {{item_4_impact}} | {{item_4_confidence}}% | {{item_4_effort}} | {{item_4_rice}} | {{item_4_notes}} |
| 5 | {{item_5}} | {{item_5_reach}} | {{item_5_impact}} | {{item_5_confidence}}% | {{item_5_effort}} | {{item_5_rice}} | {{item_5_notes}} |

## Deferred (Low RICE / High Uncertainty)
| Item | RICE | Reason deferred |
|------|------|-----------------|
| {{deferred_1}} | {{deferred_1_rice}} | {{deferred_1_reason}} |
| {{deferred_2}} | {{deferred_2_rice}} | {{deferred_2_reason}} |

## Dependencies & Risks
| Item | Depends on | Risk |
|------|------------|------|
| {{item_1}} | {{item_1_dep}} | {{item_1_risk}} |
| {{item_2}} | {{item_2_dep}} | {{item_2_risk}} |

## Assumptions
1. {{assumption_1}}
2. {{assumption_2}}
3. {{assumption_3}}

> Reach figures are synthetic estimates from memory personas. Re-score after discovery validation.
