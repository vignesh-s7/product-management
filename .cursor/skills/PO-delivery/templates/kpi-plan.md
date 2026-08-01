---
domain: {{domain}}
stage: delivery
type: kpi-plan
compliance-regime: {{compliance-regime}}
generated: {{date}}
synthetic-data: true
---

# KPI Instrumentation Plan — {{feature_name}}

**Domain:** {{domain}} · **Launch target:** {{launch_date}}

## North Star Metric
**{{north_star_metric}}** — {{north_star_definition}}

## Metric Hierarchy
```
North Star: {{north_star_metric}}
├── Leading: {{leading_metric_1}}
├── Leading: {{leading_metric_2}}
└── Lagging: {{lagging_metric_1}}
```

## KPI Dashboard
| KPI | Type | Baseline | Target ({{target_period}}) | Owner | Instrumentation |
|-----|------|----------|---------------------------|-------|-----------------|
| {{kpi_1}} | Leading | {{kpi_1_baseline}} | {{kpi_1_target}} | {{kpi_1_owner}} | {{kpi_1_instrumentation}} |
| {{kpi_2}} | Leading | {{kpi_2_baseline}} | {{kpi_2_target}} | {{kpi_2_owner}} | {{kpi_2_instrumentation}} |
| {{kpi_3}} | Lagging | {{kpi_3_baseline}} | {{kpi_3_target}} | {{kpi_3_owner}} | {{kpi_3_instrumentation}} |
| {{kpi_4}} | Guardrail | {{kpi_4_baseline}} | {{kpi_4_target}} | {{kpi_4_owner}} | {{kpi_4_instrumentation}} |

## Event Taxonomy
| Event name | Trigger | Properties (synthetic) | Privacy class |
|------------|---------|------------------------|---------------|
| {{event_1}} | {{event_1_trigger}} | {{event_1_properties}} | {{event_1_privacy}} |
| {{event_2}} | {{event_2_trigger}} | {{event_2_properties}} | {{event_2_privacy}} |
| {{event_3}} | {{event_3_trigger}} | {{event_3_properties}} | {{event_3_privacy}} |

## Eval & Quality Metrics (AI features)
| Metric | Method | Threshold | Regression suite |
|--------|--------|-----------|------------------|
| {{eval_metric_1}} | {{eval_method_1}} | {{eval_threshold_1}} | {{eval_suite_1}} |
| {{eval_metric_2}} | {{eval_method_2}} | {{eval_threshold_2}} | {{eval_suite_2}} |

## Compliance Instrumentation
| Regime | Required telemetry | Retention | Anonymisation |
|--------|-------------------|-----------|---------------|
| {{compliance_regime}} | {{compliance_telemetry}} | {{compliance_retention}} | {{compliance_anonymisation}} |

## Alerting & Review Cadence
| Alert | Condition | Channel | Review cadence |
|-------|-----------|---------|----------------|
| {{alert_1}} | {{alert_1_condition}} | {{alert_1_channel}} | {{alert_1_cadence}} |
| {{alert_2}} | {{alert_2_condition}} | {{alert_2_channel}} | {{alert_2_cadence}} |

## Rollback Triggers (metric-based)
- {{rollback_trigger_1}}
- {{rollback_trigger_2}}

> All event properties use synthetic IDs. No PII/PHI in telemetry payloads.
