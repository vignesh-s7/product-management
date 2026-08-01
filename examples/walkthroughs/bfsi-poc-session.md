# BFSI POC Session — Synthetic Credit-Risk Pilot

**Domain:** BFSI · **Compliance:** PCI-DSS (no PAN in scope), GDPR, fair lending awareness  
**Data:** 100% synthetic — no real customer records, scores, or account numbers  
**Runtime:** Client-side AI agent only — no vendor execution

This walkthrough shows how a human PO triggers their local agent to produce a gated credit-risk POC artifact set using productowner-skill.

---

## Scenario

**Product:** RiskLens Assist — SME credit-risk pre-screen POC  
**Problem:** Relationship managers at a regional bank spend 2+ hours per SME loan application manually gathering financial signals before underwriting review. POC validates a **pre-screen dashboard** that surfaces synthetic risk indicators from uploaded CSV — no core banking integration in v1.  
**Persona:** **Marcus** — SME Relationship Manager, 8–15 loan applications per week.

**Fair lending note:** POC scope excludes automated approve/deny decisions. All outputs are "signals for human review" — no disparate impact testing in v1 (flagged as Phase 2 deliverable).

---

## Prerequisites

1. Skills copied per [docs/INSTALL.md](../../docs/INSTALL.md)
2. `.agent/memory.md` configured for BFSI domain (see memory stub below)
3. Client agent running in Cursor, Claude Code, or compatible IDE

### Memory stub (copy to `.agent/memory.md`)

```yaml
product_name:
  name: risklens-assist-poc
  display_name: RiskLens Assist — SME Credit Pre-Screen POC
  version: 0.1-poc

domain:
  primary: bfsi
  rationale: SME lending — PCI-DSS awareness, fair lending guardrails, no PAN storage

compliance_regimes:
  active: [GDPR, PCI-DSS]
  constraints:
    - Synthetic applicant data only
    - No automated credit decisions in POC
    - Fair lending — signals for human review only

constraints:
  technical:
    - POC: static HTML dashboard + markdown artifacts
    - No core banking API in v1
  operational:
    - POC timeline: 2 weeks
```

---

## Session flow

```
Human intent
    → Discovery (PO-discovery)
    → Delivery (PO-delivery)
    → Persona swarm gates (local JSON verdicts)
    → POC build (client agent codegen)
    → Human review & approve
```

---

## Step 1 — Human sets intent

**Human prompt (IDE agent chat):**

> Act as Product Owner — run discovery for an SME credit-risk pre-screen POC. Domain BFSI. Use synthetic data only. No core banking integration. Fair lending: signals for human review, no auto approve/deny.

**What the human does not do:** Call any productowner-skill API, run `orchestrate.sh`, or upload data to a vendor service.

---

## Step 2 — Client agent reads skills + memory

| Source | Purpose |
|--------|---------|
| `.agent/memory.md` | Product name, domain, compliance, constraints |
| `productowner-skill/SKILL.md` | Orchestration + gate flow |
| `PO-discovery/SKILL.md` | Discovery pack templates |
| `PO-delivery/SKILL.md` | PRD + RICE + KPI templates |

Agent delegates declaratively — no shell orchestration.

---

## Step 3 — Discovery artifacts

**Agent action:** Run `PO-discovery` — SWOT, market sizing, competitor matrix, compliance risk map.

| Artifact | Path | Notes |
|----------|------|-------|
| SWOT | `artifacts/discovery/risklens-swot.md` | Strengths include no core banking dependency |
| Market sizing | `artifacts/discovery/risklens-tam-sam-som.md` | UK SME lending segment — synthetic figures |
| Competitor matrix | `artifacts/discovery/risklens-competitors.md` | Manual spreadsheet tools vs. embedded analytics |
| Compliance map | `artifacts/discovery/risklens-compliance-map.md` | GDPR, PCI-DSS scope, fair lending guardrails |

**Sample compliance map excerpt (synthetic):**

| Regime | POC scope | Out of scope |
|--------|-----------|--------------|
| PCI-DSS | No PAN, no card data | Payment card processing |
| GDPR | Synthetic names only in fixtures | Production customer PII |
| Fair lending | Human-in-loop signals only | Automated adverse action notices |

---

## Step 4 — Delivery artifacts

**Human prompt:**

> Write a PRD with Gherkin acceptance criteria for the credit pre-screen dashboard. Include non-goals for auto-decisioning and core banking integration.

| Artifact | Path | Notes |
|----------|------|-------|
| PRD | `artifacts/delivery/risklens-prd.md` | Gherkin AC on every story |
| RICE backlog | `artifacts/delivery/risklens-rice-backlog.md` | POC stories ranked |
| KPI plan | `artifacts/delivery/risklens-kpi-plan.md` | Leading: time-to-first-signal |
| Rollout phases | `artifacts/delivery/risklens-rollout.md` | POC → pilot → production |

**Sample Gherkin AC (synthetic data):**

```gherkin
Given I have uploaded a CSV with columns applicant_id, business_name, revenue_gbp, debt_ratio, synthetic_risk_score
When I open the pre-screen dashboard
Then I see applicants sorted by synthetic_risk_score descending
And each row shows business_name, revenue_gbp, and a "Review signals" action
And no production applicant IDs from live systems appear in the POC dataset
And the UI displays "Human review required — not a credit decision"
```

**Non-goals (POC):**

- No automated approve/deny or adverse action generation
- No Open Banking or core banking API calls
- No storage of real financial account numbers

---

## Step 5 — Persona swarm gates

Gates run **on the client agent** before artifacts are committed. Example verdict JSONs below mirror the structure in [examples/golden-run/gates/](../../golden-run/gates/).

### 5a — cybersec-skill

**Reference:** [cybersec-pass.json](../../golden-run/gates/cybersec-pass.json) (adapt paths to `risklens-prd.md`)

```json
{
  "verdict": "pass",
  "artifact": "artifacts/delivery/risklens-prd.md",
  "checks": {
    "pii_phi_scan": "pass",
    "owasp_review": "pass",
    "synthetic_data_only": "pass"
  },
  "notes": "POC excludes PAN and live account numbers. CSV fixture uses synthetic business names only."
}
```

### 5b — ux-pro-skill

**Reference:** [ux-warn.json](../../golden-run/gates/ux-warn.json)

```json
{
  "verdict": "warn",
  "scope": ["docs/poc/risklens-dashboard.html"],
  "style_violations": [
    {
      "severity": "warn",
      "issue": "Risk score badge uses hard-coded red instead of design token --risk-high",
      "fix": "Use var(--risk-high) from .agent/memory.md design_tokens"
    }
  ],
  "flow_notes": "Fair lending disclaimer visible on dashboard load — good"
}
```

### 5c — qa-tester-skill

**Reference:** [qa-warn.json](../../golden-run/gates/qa-warn.json)

```json
{
  "verdict": "warn",
  "coverage_gaps": [
    {
      "id": "QA-GAP-BFSI-001",
      "message": "No AC for CSV with missing debt_ratio column",
      "suggestion": "Add Gherkin: Given CSV missing required column When upload Then inline error"
    },
    {
      "id": "QA-GAP-BFSI-002",
      "message": "No boundary case for duplicate applicant_id",
      "suggestion": "Second row with same applicant_id rejected with clear message"
    }
  ],
  "warnings": [
    "Add explicit test that no automated credit decision text appears in POC UI"
  ]
}
```

### 5d — y-score-readiness

**Reference:** [y-score.json](../../golden-run/gates/y-score.json)

```json
{
  "score": 76,
  "verdict": "go",
  "artifact": "artifacts/delivery/risklens-prd.md",
  "dimensions": {
    "problem_clarity": { "score": 100, "note": "Time-to-signal target stated" },
    "target_user": { "score": 100, "note": "Marcus persona with weekly frequency" },
    "success_metric": { "score": 50, "note": "Leading metric defined; portfolio risk lagging metric deferred" },
    "constraints": { "score": 100, "note": "No core banking API, fair lending guardrails documented" },
    "compliance_posture": { "score": 50, "note": "GDPR + PCI scope stated; fair lending testing plan not attached" },
    "eval_plan": { "score": 50, "note": "Gherkin AC present; golden eval set for risk signals not yet defined" },
    "rollback_plan": { "score": 50, "note": "POC non-goals clear; production kill switch not drafted" }
  },
  "recommendations": [
    "Attach fair lending review checklist before external pilot",
    "Define 5 golden synthetic applicants for regression eval"
  ]
}
```

**Gate rule:** BLOCK verdicts stop commit. WARN verdicts write with `> ⚠️ finding:` callout.

---

## Step 6 — POC build (client agent)

**Human prompt:**

> Build the POC pre-screen dashboard from the gated PRD. Static HTML + synthetic CSV fixture. No backend. Label all data as synthetic.

| Output | Path | Owner |
|--------|------|-------|
| Dashboard HTML | `docs/poc/risklens-dashboard.html` | Client repo |
| Synthetic CSV fixture | `fixtures/synthetic-sme-applicants.csv` | Client repo |
| Reminder / audit log | `artifacts/delivery/risklens-audit-log.md` | Client repo |

**Phase 5 note:** Full `prd-to-sdlc` bundle (MetaGPT architecture, OpenHands scaffold, Promptfoo evals) is **not** part of this POC session. The client agent generates POC code directly from Gherkin AC.

---

## Step 7 — Human review

| Review item | Action |
|-------------|--------|
| Gate JSONs | Confirm no BLOCK verdicts open |
| Fair lending disclaimer | Visible on every POC screen |
| Synthetic data labels | Present in CSV and UI |
| WARN findings | Triage ux-pro and qa-tester items |
| InfoSec | Share [INFOSEC-ONEPAGER.md](../../docs/INFOSEC-ONEPAGER.md) if first install |

---

## Artifact summary

| Stage | Artifacts | Gate refs |
|-------|-----------|-----------|
| Discovery | SWOT, TAM/SAM/SOM, competitors, compliance map | — |
| Delivery | PRD, RICE, KPI, rollout | cybersec-pass pattern |
| Gates | Verdict JSONs in session or `gates/` | See Step 5 |
| POC | HTML dashboard, synthetic CSV | ux-warn, qa-warn patterns |
| Readiness | Y-Score report | y-score.json pattern |

---

## Reproduce this session

1. Copy skills per [INSTALL.md](../../docs/INSTALL.md)
2. Configure `.agent/memory.md` for BFSI domain
3. Trigger: **"Act as Product Owner — run discovery for SME credit-risk pre-screen POC"**
4. Continue through delivery and gates per [productowner-skill/SKILL.md](../../skills/productowner-skill/SKILL.md)

All data in this walkthrough is fictional. Replace with validated research before external distribution.
