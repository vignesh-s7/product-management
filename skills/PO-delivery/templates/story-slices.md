---
domain: {{domain}}
stage: delivery
type: story-slices
compliance-regime: {{compliance-regime}}
generated: {{date}}
synthetic-data: true
---

# Story Slices — {{epic_name}}

**Domain:** {{domain}} · **Epic ID:** {{epic_id}} · **Author:** {{author}}
**Linked PRD:** {{linked_prd}} · **Deploy strategy:** {{deploy_strategy}}

---

## Epic Summary

{{epic_summary}}

### Epic-level success criteria
| Metric | Baseline | Target | Instrumentation |
|--------|----------|--------|-----------------|
| {{epic_metric_1}} | {{epic_metric_1_baseline}} | {{epic_metric_1_target}} | {{epic_metric_1_instrumentation}} |

### Slicing principles applied
- Each story is **independently deployable** behind a feature flag or safe default
- Stories are ordered by **risk reduction** and **learning value**
- No story depends on a later story for basic functionality

---

## Slice map

| Slice | Story ID | Title | Deployable alone? | Depends on | RICE | Flag / rollout |
|-------|----------|-------|-------------------|------------|------|----------------|
| 1 | {{story_1_id}} | {{story_1_title}} | Yes | — | {{story_1_rice}} | {{story_1_flag}} |
| 2 | {{story_2_id}} | {{story_2_title}} | Yes | {{story_2_depends}} | {{story_2_rice}} | {{story_2_flag}} |
| 3 | {{story_3_id}} | {{story_3_title}} | Yes | {{story_3_depends}} | {{story_3_rice}} | {{story_3_flag}} |
| 4 | {{story_4_id}} | {{story_4_title}} | Yes | {{story_4_depends}} | {{story_4_rice}} | {{story_4_flag}} |

---

## Story 1: {{story_1_title}}

**ID:** {{story_1_id}} · **Persona:** {{story_1_persona}} · **Effort:** {{story_1_effort}}

**As a** {{story_1_persona}}, **I want** {{story_1_want}}, **so that** {{story_1_benefit}}.

### Independent deployability
- **Ship alone:** {{story_1_deployable_rationale}}
- **Feature flag:** {{story_1_flag}}
- **Rollback:** {{story_1_rollback}}

### Acceptance criteria

```gherkin
Feature: {{story_1_title}}

  Scenario: {{story_1_scenario_1_name}}
    Given {{story_1_scenario_1_given}}
    When {{story_1_scenario_1_when}}
    Then {{story_1_scenario_1_then}}

  Scenario: {{story_1_scenario_2_name}}
    Given {{story_1_scenario_2_given}}
    When {{story_1_scenario_2_when}}
    Then {{story_1_scenario_2_then}}
```

---

## Story 2: {{story_2_title}}

**ID:** {{story_2_id}} · **Persona:** {{story_2_persona}} · **Effort:** {{story_2_effort}}

**As a** {{story_2_persona}}, **I want** {{story_2_want}}, **so that** {{story_2_benefit}}.

### Independent deployability
- **Ship alone:** {{story_2_deployable_rationale}}
- **Feature flag:** {{story_2_flag}}
- **Rollback:** {{story_2_rollback}}

### Acceptance criteria

```gherkin
Feature: {{story_2_title}}

  Scenario: {{story_2_scenario_1_name}}
    Given {{story_2_scenario_1_given}}
    When {{story_2_scenario_1_when}}
    Then {{story_2_scenario_1_then}}

  Scenario: {{story_2_scenario_2_name}}
    Given {{story_2_scenario_2_given}}
    When {{story_2_scenario_2_when}}
    Then {{story_2_scenario_2_then}}
```

---

## Story 3: {{story_3_title}}

**ID:** {{story_3_id}} · **Persona:** {{story_3_persona}} · **Effort:** {{story_3_effort}}

**As a** {{story_3_persona}}, **I want** {{story_3_want}}, **so that** {{story_3_benefit}}.

### Independent deployability
- **Ship alone:** {{story_3_deployable_rationale}}
- **Feature flag:** {{story_3_flag}}
- **Rollback:** {{story_3_rollback}}

### Acceptance criteria

```gherkin
Feature: {{story_3_title}}

  Scenario: {{story_3_scenario_1_name}}
    Given {{story_3_scenario_1_given}}
    When {{story_3_scenario_1_when}}
    Then {{story_3_scenario_1_then}}

  Scenario: {{story_3_scenario_2_name}}
    Given {{story_3_scenario_2_given}}
    When {{story_3_scenario_2_when}}
    Then {{story_3_scenario_2_then}}
```

---

## Deferred / out of scope

| Item | Reason |
|------|--------|
| {{deferred_1}} | {{deferred_1_reason}} |
| {{deferred_2}} | {{deferred_2_reason}} |

---

## Open questions

| # | Question | Owner | Resolution by |
|---|----------|-------|---------------|
| 1 | {{open_question_1}} | {{open_question_1_owner}} | {{open_question_1_date}} |
| 2 | {{open_question_2}} | {{open_question_2_owner}} | {{open_question_2_date}} |
