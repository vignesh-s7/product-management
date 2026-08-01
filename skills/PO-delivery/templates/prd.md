---
domain: {{domain}}
stage: delivery
type: prd
compliance-regime: {{compliance-regime}}
generated: {{date}}
synthetic-data: true
---

# PRD — {{feature_name}}

**Domain:** {{domain}} · **Author:** {{author}} · **Status:** Draft
**Linked:** {{linked_artifacts}}

---

## Problem
{{problem_statement}}

## Target Users
| Persona | Job-to-be-done | Frequency |
|---------|------------------|-----------|
| {{persona_1}} | {{persona_1_jtbd}} | {{persona_1_frequency}} |
| {{persona_2}} | {{persona_2_jtbd}} | {{persona_2_frequency}} |

## Success Metrics
| Metric | Type | Baseline | Target | Instrumentation |
|--------|------|----------|--------|-----------------|
| {{metric_1}} | Leading | {{metric_1_baseline}} | {{metric_1_target}} | {{metric_1_instrumentation}} |
| {{metric_2}} | Lagging | {{metric_2_baseline}} | {{metric_2_target}} | {{metric_2_instrumentation}} |

## Constraints
- **Latency:** {{latency_constraint}}
- **Cost:** {{cost_constraint}}
- **Data residency:** {{data_residency}}
- **Compliance:** {{compliance_constraints}}

## User Stories & Acceptance Criteria

### Story 1: {{story_1_title}}
**As a** {{story_1_persona}}, **I want** {{story_1_want}}, **so that** {{story_1_benefit}}.

```gherkin
Given {{story_1_given}}
When {{story_1_when}}
Then {{story_1_then}}
```

### Story 2: {{story_2_title}}
**As a** {{story_2_persona}}, **I want** {{story_2_want}}, **so that** {{story_2_benefit}}.

```gherkin
Given {{story_2_given}}
When {{story_2_when}}
Then {{story_2_then}}
```

## Out of Scope
- {{out_of_scope_1}}
- {{out_of_scope_2}}

## Compliance & Eval Plan
| Requirement | Status | Notes |
|-------------|--------|-------|
| {{compliance_req_1}} | {{compliance_req_1_status}} | {{compliance_req_1_notes}} |
| Eval golden set | {{eval_status}} | {{eval_notes}} |
| Rollback / kill switch | {{rollback_status}} | {{rollback_notes}} |

## Rollback Plan
- **Trigger:** {{rollback_trigger}}
- **Comms:** {{rollback_comms}}
- **Data recovery RTO:** {{rollback_rto}}

> Synthetic personas and metrics only. No real PII/PHI.
