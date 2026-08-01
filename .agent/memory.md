# Local Memory Standard

> **All skills MUST read this file first** before generating artifacts, searching the KB, or delegating to sub-skills. Adapt all templates and outputs to the values below. Do not hardcode repository-specific context in skill files — read it here.

---

## product_name

```yaml
name: productowner-skill
display_name: productowner-skill — AI-Native PO Operating System
tagline: Outcomes users want. Skills that deliver. Zero scripts. Zero telemetry.
version: 0.4
repository: productowner-skill
author: Vignesh AIPM
```

---

## domain

```yaml
primary: generic
secondary:
  - bfsi
  - healthcare
rationale: >
  Platform is domain-agnostic PO tooling. Reference PRDs and templates
  include BFSI (credit risk, regulated RAG) and healthcare (FHIR, wellness IoT)
  examples. Skills must adapt compliance checks to the active engagement domain.
```

---

## target_users

```yaml
internal:
  - role: Product Owner
    jtbd: Produce launch-ready PRDs, discovery packs, and delivery artifacts without starting from scratch each sprint
    frequency: daily
  - role: PO Lead / Manager
    jtbd: Enforce quality gates (Y-Score, security, UX, QA) across team output
    frequency: weekly
  - role: Admin / P&T Ops
    jtbd: Install plugin in < 5 min; pass InfoSec review with no new infra
    frequency: per onboarding
external:
  - role: Consulting PO / Engagement Lead
    jtbd: Package client deliverables into reusable, compliant artifact sets
    frequency: per engagement
  - role: Client Stakeholder
    jtbd: View programme status and artifacts without Jira/Confluence licences
    frequency: weekly
```

---

## compliance_regimes

```yaml
baseline:
  - SOC 2 Type II (target posture)
  - GDPR (EU data subjects in demo/mock data only)
  - EU AI Act (high-risk AI system documentation patterns)
bfsi:
  - PCI-DSS (no cardholder data in artifacts)
  - FATF / BSA (AML reference patterns in credit-risk PRDs)
  - Fair lending (model bias review in eval plans)
  - EU AI Act high-risk (credit scoring use cases)
healthcare:
  - HIPAA (no PHI in artifacts — synthetic data only)
  - FHIR R4 (interop patterns in reference PRDs)
  - FDA SaMD (class I/II awareness for wellness IoT PRDs)
enforcement: >
  cybersec-skill BLOCKS any PII/PHI in generated output.
  All personas use mock personas from docs/mock-data.json.
```

---

## constraints

```yaml
technical:
  - Declarative skills only — no bash scripts, no orchestrate.sh
  - No network calls from skills (no curl, wget, web search for KB)
  - No bundled LLM API keys — uses the user's IDE agent model
  - Outputs written to artifacts/ with tagging schema
  - Phase 1 local KB only — enterprise API integrations deferred to Phase 2
operational:
  - Install time target: < 5 minutes
  - First PRD from cold repo target: < 45 minutes
  - Security review: 100% pass (no executables in skills/)
data:
  - Synthetic / mock data only in all templates and demos
  - No PII, PHI, or real client identifiers
  - No cross-session profiling or telemetry
sla:
  - Static portfolio demo — no authentication, no live integrations
  - GitHub Pages hosting for docs/
```

---

## integrations

```yaml
planned:
  phase_2:
    - name: Atlassian Rovo
      scope: Jira + Confluence federated search
      status: deferred
    - name: Microsoft 365 Graph
      scope: SharePoint, Yammer, Teams search
      status: deferred
    - name: Google Workspace API
      scope: Drive + Docs search
      status: deferred
    - name: PowerBI Embed
      scope: PO dashboard templates
      status: deferred
  phase_3:
    - name: Rovo Chat + Claude
      scope: AI chat grounded in org KB
      status: deferred
  phase_5:
    - name: MetaGPT
      scope: Architecture generation from PRD
      status: deferred
    - name: OpenHands
      scope: Sandboxed code generation
      status: deferred
    - name: Promptfoo
      scope: Eval harness gate
      status: deferred
current:
  - name: Local filesystem KB
    scope: artifacts/, prds/, skills/*/templates/
    status: active
  - name: GitHub Pages
    scope: Static portfolio demo (docs/)
    status: active
  - name: Microsoft Teams tab
    scope: Onboarding manifest (docs/onboarding/manifest.json)
    status: active
```

---

## design_tokens

```yaml
colors:
  bg: "#fafafa"
  surface: "#ffffff"
  surface_2: "#f4f4f5"
  border: "#e4e4e7"
  border_strong: "#d4d4d8"
  text: "#18181b"
  text_2: "#52525b"
  muted: "#71717a"
  accent: "#3f3f46"
  accent_text: "#fafafa"
  ok: "#15803d"
  warn: "#a16207"
  bad: "#b91c1c"
  info: "#1e40af"
  dark_mode: auto via prefers-color-scheme and data-theme attribute
fonts:
  family: "ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
  base_size: "14px"
  line_height: 1.5
  heading_weight: 600
  heading_tracking: "-0.01em"
spacing:
  radius: "0.5rem"
  card_padding: "1rem"
  grid_gap: "0.85rem"
  button_padding: "0.4rem 0.9rem"
  input_padding: "0.45rem 0.65rem"
components:
  - .btn / .btn-primary / .btn-ghost
  - .card
  - .badge (.b-ok, .b-warn, .b-bad, .b-info)
  - .banner / .banner-ok
  - .input / .select / .textarea
source: docs/style.css
rules:
  - No inline styles on demo pages
  - ux-pro-skill enforces token adherence from this section
  - WCAG 2.1 AA minimum for all docs/ UI
```

---

## glossary

```yaml
Y-Score: >
  7-dimension launch-readiness rubric (problem clarity, target user,
  success metric, constraints, compliance, eval plan, rollback).
  Gate threshold: score ≥ 70 to proceed.
DoR: Definition of Ready — PRD meets Y-Score + Gherkin AC + compliance tags.
Gherkin AC: Given/When/Then acceptance criteria required on every PRD and story.
Four Engines: Discovery, Delivery, KB Layer, Code Pipeline — core product modules.
Persona Swarm: productowner-skill → cybersec-skill → ux-pro-skill → qa-tester-skill gate chain.
Discovery Pack: SWOT + TAM/SAM/SOM + competitor matrix + compliance risk map.
Delivery Pack: RICE backlog + KPI plan + rollout phases + Y-Score report.
Artifact Tagging: domain · stage · type · compliance-regime on every generated file.
CuCP: Change User Change Programme — enterprise rollout methodology (90-day deck in docs/cucp/).
Standard Tier: Templates + local KB search — zero bundled LLM cost.
AI Tier: Generation + chat grounded in org KB — requires user's agent model.
Local Memory: This file (.agent/memory.md) — repo-specific context for all skills.
KB Layer: Knowledge base — Phase 1 local only; Phase 2 federated enterprise search.
RICE: Reach × Impact × Confidence / Effort — backlog prioritisation framework.
WSJF: Weighted Shortest Job First — alternative prioritisation method.
MoSCoW: Must / Should / Could / Won't — scope framing for delivery packs.
PII: Personally Identifiable Information — blocked by cybersec-skill.
PHI: Protected Health Information — blocked by cybersec-skill.
SaMD: Software as a Medical Device — FDA classification context for healthcare PRDs.
```
