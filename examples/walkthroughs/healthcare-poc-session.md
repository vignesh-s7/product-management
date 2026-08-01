# Healthcare POC Session — Synthetic FHIR Wellness Pilot

**Domain:** Healthcare · **Compliance:** HIPAA (skills instructional only), synthetic PHI rules  
**Data:** 100% synthetic — no real patient records, MRNs, or clinical identifiers  
**Runtime:** Client-side AI agent only — no vendor execution

This walkthrough shows how a human PO triggers their local agent to produce a gated FHIR wellness POC artifact set using productowner-skill. Structure mirrors the [BFSI walkthrough](./bfsi-poc-session.md).

---

## Scenario

**Product:** WellPath Assist — FHIR wellness check-in POC  
**Problem:** Care coordinators at a regional health network spend 30+ minutes per patient manually reconciling wellness survey responses across spreadsheets before scheduling follow-up calls. POC validates a **wellness dashboard** that displays synthetic FHIR Patient and Observation resources from a local JSON bundle — no EHR integration in v1.  
**Persona:** **Elena** — Care Coordinator, 20–30 wellness patients per week.

**HIPAA note:** POC uses synthetic PHI only. No real MRNs, dates of birth tied to real individuals, or production FHIR endpoints. Skills instruct the agent to BLOCK commits that contain detected PHI patterns.

---

## Prerequisites

1. Skills copied per [docs/INSTALL.md](../../docs/INSTALL.md)
2. `.agent/memory.md` configured for healthcare domain (see memory stub below)
3. Client agent running in Cursor, Claude Code, or compatible IDE

### Memory stub (copy to `.agent/memory.md`)

```yaml
product_name:
  name: wellpath-assist-poc
  display_name: WellPath Assist — FHIR Wellness Check-In POC
  version: 0.1-poc

domain:
  primary: healthcare
  rationale: Wellness coordination — HIPAA awareness, synthetic PHI only, no EHR in v1

compliance_regimes:
  active: [HIPAA]
  constraints:
    - Synthetic patient data only in all artifacts
    - No production FHIR server URLs
    - Minimum necessary — wellness fields only, no full chart export

constraints:
  technical:
    - POC: static HTML dashboard + local FHIR JSON bundle
    - No EHR API or SMART on FHIR in v1
  operational:
    - POC timeline: 2 weeks
    - Agent usage in client's HIPAA-compliant dev environment
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

> Act as Product Owner — run discovery for a FHIR wellness check-in POC. Domain healthcare. Use synthetic PHI only. No EHR integration. HIPAA minimum necessary — wellness observations only.

**What the human does not do:** Call any productowner-skill API, run `orchestrate.sh`, or upload patient data to a vendor service.

---

## Step 2 — Client agent reads skills + memory

| Source | Purpose |
|--------|---------|
| `.agent/memory.md` | Product name, domain, HIPAA constraints |
| `productowner-skill/SKILL.md` | Orchestration + gate flow |
| `PO-discovery/SKILL.md` | Discovery pack templates |
| `PO-delivery/SKILL.md` | PRD + RICE + KPI templates |
| `cybersec-skill/SKILL.md` | PHI blocker — BLOCK on detected PHI |

Agent delegates declaratively — no shell orchestration.

---

## Step 3 — Discovery artifacts

**Agent action:** Run `PO-discovery` — SWOT, market sizing, competitor matrix, compliance risk map.

| Artifact | Path | Notes |
|----------|------|-------|
| SWOT | `artifacts/discovery/wellpath-swot.md` | Strengths include no EHR certification delay |
| Market sizing | `artifacts/discovery/wellpath-tam-sam-som.md` | US wellness program segment — synthetic figures |
| Competitor matrix | `artifacts/discovery/wellpath-competitors.md` | Portal vendors vs. coordinator-built tools |
| Compliance map | `artifacts/discovery/wellpath-compliance-map.md` | HIPAA, synthetic PHI rules, minimum necessary |

**Sample compliance map excerpt (synthetic):**

| Regime | POC scope | Out of scope |
|--------|-----------|--------------|
| HIPAA | Synthetic Patient/Observation JSON only | Production PHI, real MRNs |
| Minimum necessary | Wellness score, last check-in date | Full clinical chart, diagnoses export |
| BAA | Not applicable — no vendor hosted service | Third-party PHI storage by us |

---

## Step 4 — Delivery artifacts

**Human prompt:**

> Write a PRD with Gherkin acceptance criteria for the wellness dashboard. Include non-goals for EHR integration and real PHI. Flag synthetic data requirements on every story.

| Artifact | Path | Notes |
|----------|------|-------|
| PRD | `artifacts/delivery/wellpath-prd.md` | Gherkin AC on every story |
| RICE backlog | `artifacts/delivery/wellpath-rice-backlog.md` | POC stories ranked |
| KPI plan | `artifacts/delivery/wellpath-kpi-plan.md` | Leading: time-to-identify-at-risk patient |
| Rollout phases | `artifacts/delivery/wellpath-rollout.md` | POC → pilot → production |

**Sample Gherkin AC (synthetic PHI):**

```gherkin
Given I have loaded the synthetic FHIR bundle at fixtures/synthetic-wellness-bundle.json
When I open the wellness dashboard
Then I see Patient resources with synthetic names only (e.g. "Synth Patient A")
And each row shows wellness_score and days_since_last_checkin
And no real MRNs, SSNs, or production patient identifiers appear in the POC dataset
And the UI displays "Synthetic data — not for clinical use"
```

**Non-goals (POC):**

- No SMART on FHIR or production EHR connectivity
- No storage of real PHI in repo or agent session logs
- No clinical decision support or diagnosis suggestions

---

## Step 5 — Persona swarm gates

Gates run **on the client agent** before artifacts are committed. Example verdict JSONs below mirror the structure in [examples/golden-run/gates/](../../golden-run/gates/).

### 5a — cybersec-skill (PHI blocker)

**Reference:** [cybersec-pass.json](../../golden-run/gates/cybersec-pass.json) (adapt paths to `wellpath-prd.md`)

```json
{
  "verdict": "pass",
  "artifact": "artifacts/delivery/wellpath-prd.md",
  "checks": {
    "pii_phi_scan": "pass",
    "owasp_review": "pass",
    "synthetic_data_only": "pass"
  },
  "notes": "POC excludes real MRNs and clinical identifiers. FHIR bundle uses Synth Patient A/B/C only."
}
```

**If PHI detected:** verdict becomes `block` — agent must not commit until synthetic replacements are applied.

### 5b — ux-pro-skill

**Reference:** [ux-warn.json](../../golden-run/gates/ux-warn.json)

```json
{
  "verdict": "warn",
  "scope": ["docs/poc/wellpath-dashboard.html"],
  "wcag_failures": [],
  "style_violations": [
    {
      "severity": "warn",
      "issue": "At-risk badge uses hard-coded orange instead of design token --alert-medium",
      "fix": "Use var(--alert-medium) from .agent/memory.md design_tokens"
    }
  ],
  "flow_notes": "Synthetic data banner visible on load — good. Consider larger touch targets for coordinator tablet use."
}
```

### 5c — qa-tester-skill

**Reference:** [qa-warn.json](../../golden-run/gates/qa-warn.json)

```json
{
  "verdict": "warn",
  "scope": ["wellness dashboard", "synthetic FHIR bundle import"],
  "coverage_gaps": [
    {
      "id": "QA-GAP-HC-001",
      "message": "No AC for FHIR bundle missing Observation resource",
      "suggestion": "Add Gherkin: Given Patient without Observation When load Then show 'No wellness data' state"
    },
    {
      "id": "QA-GAP-HC-002",
      "message": "No boundary case for wellness_score at clinical threshold edge (e.g. score = 0)",
      "suggestion": "Add boundary: score 0 displays at-risk styling without implying diagnosis"
    }
  ],
  "warnings": [
    "Add explicit test that no production FHIR server URL is referenced in POC code",
    "Verify agent session logs do not persist synthetic bundle contents to external tools"
  ]
}
```

### 5d — y-score-readiness

**Reference:** [y-score.json](../../golden-run/gates/y-score.json)

```json
{
  "score": 72,
  "verdict": "go",
  "artifact": "artifacts/delivery/wellpath-prd.md",
  "dimensions": {
    "problem_clarity": { "score": 100, "note": "Coordinator time-saving target stated" },
    "target_user": { "score": 100, "note": "Elena persona with weekly patient volume" },
    "success_metric": { "score": 50, "note": "Leading metric defined; readmission lagging metric deferred" },
    "constraints": { "score": 100, "note": "No EHR API, synthetic PHI only documented" },
    "compliance_posture": { "score": 50, "note": "HIPAA scope stated; BAA checklist for future hosted tier not attached" },
    "eval_plan": { "score": 50, "note": "Gherkin AC present; golden FHIR fixture set not yet defined" },
    "rollback_plan": { "score": 50, "note": "POC non-goals clear; production de-identification policy not drafted" }
  },
  "recommendations": [
    "Attach HIPAA minimum-necessary worksheet before external pilot",
    "Define 5 golden synthetic patients for regression eval",
    "Document agent log retention policy for coordinator workstations"
  ]
}
```

**Gate rule:** BLOCK verdicts stop commit. WARN verdicts write with `> ⚠️ finding:` callout.

---

## Step 6 — POC build (client agent)

**Human prompt:**

> Build the POC wellness dashboard from the gated PRD. Static HTML + synthetic FHIR JSON bundle. No backend. No EHR calls. Label all data as synthetic and not for clinical use.

| Output | Path | Owner |
|--------|------|-------|
| Dashboard HTML | `docs/poc/wellpath-dashboard.html` | Client repo |
| Synthetic FHIR bundle | `fixtures/synthetic-wellness-bundle.json` | Client repo |
| Check-in audit log | `artifacts/delivery/wellpath-audit-log.md` | Client repo |

**Sample synthetic Patient resource (fixture only):**

```json
{
  "resourceType": "Patient",
  "id": "synth-patient-a",
  "name": [{ "family": "Synth", "given": ["Patient A"] }],
  "meta": { "tag": [{ "code": "synthetic", "display": "Synthetic PHI — not real" }] }
}
```

**Phase 5 note:** Full `prd-to-sdlc` bundle (MetaGPT architecture, OpenHands scaffold, Promptfoo evals) is **not** part of this POC session. The client agent generates POC code directly from Gherkin AC.

---

## Step 7 — Human review

| Review item | Action |
|-------------|--------|
| Gate JSONs | Confirm no BLOCK verdicts open |
| Synthetic PHI labels | Present in FHIR bundle, UI, and artifact frontmatter |
| HIPAA minimum necessary | Only wellness fields in POC — no full chart |
| WARN findings | Triage ux-pro and qa-tester items |
| InfoSec / Compliance | Share [INFOSEC-ONEPAGER.md](../../docs/INFOSEC-ONEPAGER.md); confirm POC runs in compliant dev environment |

---

## Artifact summary

| Stage | Artifacts | Gate refs |
|-------|-----------|-----------|
| Discovery | SWOT, TAM/SAM/SOM, competitors, compliance map | — |
| Delivery | PRD, RICE, KPI, rollout | cybersec-pass pattern |
| Gates | Verdict JSONs in session or `gates/` | See Step 5 |
| POC | HTML dashboard, synthetic FHIR bundle | ux-warn, qa-warn patterns |
| Readiness | Y-Score report | y-score.json pattern |

---

## Synthetic PHI rules (quick reference)

| Rule | POC behavior |
|------|--------------|
| Patient names | `Synth Patient A`, `Synth Patient B` — never real names |
| MRNs / identifiers | `synth-patient-a` — never production IDs |
| Dates | Fixed synthetic dates — not tied to real individuals |
| FHIR endpoints | Local file paths only — no `https://ehr.hospital.org` |
| Agent logs | Do not paste real PHI into IDE chat |
| Commits | cybersec-skill BLOCK if PHI patterns detected |

---

## Reproduce this session

1. Copy skills per [INSTALL.md](../../docs/INSTALL.md)
2. Configure `.agent/memory.md` for healthcare domain
3. Trigger: **"Act as Product Owner — run discovery for FHIR wellness check-in POC"**
4. Continue through delivery and gates per [productowner-skill/SKILL.md](../../skills/productowner-skill/SKILL.md)

All data in this walkthrough is fictional. Replace with validated research and compliance sign-off before external distribution or any contact with real PHI.
