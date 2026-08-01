# Local Memory — Fintech POC Example

> Copy to `.agent/memory.md` in your target repo and customise. All skills read this file first.

## product_name

```yaml
name: payflow-assist-poc
display_name: PayFlow Assist — SME Payment Reminder POC
tagline: Reduce late B2B payments for UK SMEs without adding bank integrations in v1
version: 0.1-poc
repository: client-repo
author: Client PO Team
```

## product_model

```yaml
what_we_are: Skills-driven POC built by client's local AI agent
domain_focus: bfsi
distribution: Skills copied from productowner-skill; no vendor runtime
```

## domain

```yaml
primary: bfsi
secondary:
  - generic
rationale: UK SME payments — PCI-DSS awareness, no card data in POC scope
```

## target_users

```yaml
internal:
  - role: Product Owner
    jtbd: Define POC scope, accept gated PRD and delivery pack
  - role: Engineering Lead
    jtbd: Review security gate and implement from Gherkin AC
external:
  - role: SME Finance Manager
    persona: "Sarah — 12-person logistics firm, chases invoices in spreadsheets"
    jtbd: See overdue invoices and send one-click reminder emails
    frequency: weekly
```

## compliance_regimes

```yaml
active:
  - GDPR
  - PCI-DSS  # no PAN storage in POC — reminders only
constraints:
  - Synthetic customer data only in all artifacts
  - EU data residency for any future hosted tier
```

## constraints

```yaml
technical:
  - POC: static HTML + local markdown artifacts only
  - No OAuth to banks in v1
operational:
  - POC timeline: 2 weeks
  - LLM cost cap: $50/month for agent usage (client budget)
```

## glossary

```yaml
POC: Proof of concept — discovery + gated PRD, no production deploy
Gherkin AC: Given/When/Then acceptance criteria on every story
Y-Score: Launch readiness gate — score ≥ 70 to proceed
```
