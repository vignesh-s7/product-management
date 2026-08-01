---
domain: bfsi
stage: delivery
type: prd-excerpt
compliance-regime: GDPR, PCI-DSS
generated: 2026-08-01
synthetic-data: true
---

# PRD Excerpt — PayFlow Assist POC

## Problem

UK SME finance managers spend 3–5 hours per week manually identifying overdue invoices and sending reminder emails. POC validates a **reminder workflow** without bank integrations.

## Target user

**Sarah** — Finance Manager at a 12-person logistics SME. JTBD: see overdue invoices and send one-click reminder emails. Frequency: weekly.

## User story 1 — View overdue list

**As a** finance manager, **I want** to see a list of overdue invoices imported from CSV, **so that** I know which customers to chase.

### Acceptance criteria (Gherkin)

```gherkin
Given I have uploaded a valid CSV with columns invoice_id, customer_name, amount_gbp, due_date
When I open the overdue dashboard
Then I see only invoices where due_date is before today
And each row shows customer_name, amount_gbp, and days_overdue
And no real PII from production systems appears in the POC dataset
```

## User story 2 — Send reminder email

**As a** finance manager, **I want** to send a reminder email for one overdue invoice, **so that** I can chase payment without copying fields manually.

### Acceptance criteria (Gherkin)

```gherkin
Given I am viewing an overdue invoice for customer "Synth Logistics Ltd"
When I click "Send reminder"
Then a preview modal shows subject and body with customer_name and amount_gbp filled
And when I confirm send
Then the UI shows status "Reminder queued (POC — no mail sent)"
And an audit row is appended to artifacts/delivery/reminder-log.md with timestamp and invoice_id
```

## Non-goals (POC)

- No card data, PAN, or bank OAuth
- No actual SMTP send in POC — simulated queue only
- No multi-tenant admin or SaaS login

## Success metrics

| Metric | Baseline | POC target |
|--------|----------|------------|
| Time to send one reminder | ~8 min manual | &lt; 2 min in UI walkthrough |
| PRD gate readiness (Y-Score) | — | ≥ 70 |

> Synthetic personas and metrics only. No real PII/PHI.
