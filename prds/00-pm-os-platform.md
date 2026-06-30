# PRD 00 — pm-os Platform: AI-Native PM Operating System

**Domain:** PM tooling · platform
**Author:** Vignesh Vignesh S
**Status:** Active · v0.3
**Linked:** docs/product/SRS.md · docs/product/FRD.md

---

## Problem

Product managers carry the full cognitive load of a product from first idea to post-launch review.
Every artifact — market research, SWOT, competitor matrix, PRD, prioritisation backlog, KPI plan,
release strategy — is produced manually, from scratch, for every product.

Most PMs use Jira for task tracking. Jira does not generate the thinking.
Tools like Confluence, SharePoint, and Yammer hold institutional knowledge — but PMs search
each one separately, rarely reuse what exists, and have no AI layer to synthesise it.

The compounding cost: 60–80% of a PM's working week on documentation and re-work.

---

## Target User

Product managers and product owners across domains (BFSI, Healthcare, SaaS, Telecom, Consumer) who:
- Use Jira, Confluence, SharePoint, or Yammer as their knowledge sources
- Spend >50% of their time on documentation and stakeholder artifacts
- Work in regulated or compliance-heavy environments
- Want AI assistance but need audit-ready, cited outputs

---

## Two-Tier Product Model

| | Standard Tier | AI Tier |
|--|--------------|---------|
| Access | Web UI | Web UI + Chat |
| Search | Federated KB search across Jira, Confluence, SharePoint, Yammer | Same + AI answers over KB |
| Reporting | Embedded PowerBI standard templates | PowerBI AI interpretation (screenshot, CSV, or dataset query) |
| Research | Browse + reuse artifact URLs | Deep research: internal KB + web, structured report |
| Artifact generation | Templates | AI-generated drafts grounded in KB |

---

## Solution: Four Engines

### 1. Discovery Engine
Input: problem statement
Output: market sizing, SWOT, competitor matrix, ROI model, compliance risk map, GTM brief

### 2. Delivery Engine
Input: PRD
Output: prioritised backlog (RICE/WSJF/MoSCoW), KPI plan, Y-Score gate, beta + rollout strategy

### 3. KB Layer (Reuse Core)
- Federated index across Jira, Confluence, SharePoint, Yammer
- Every artifact tagged: domain · stage · product-type · compliance-regime
- Standard tier: search + URL reuse
- AI tier: RAG-powered chat + cited responses

### 4. Reporting & Interpret Layer
- Standard: embedded PowerBI reports (Release Velocity, KPI, CuCP Status, PM Time)
- AI: interpret screenshots, CSVs, or query datasets directly in natural language

---

## Workflow

```
PM enters problem statement
    ↓
[Discovery Engine] → Research pack (SWOT, competitor, ROI, compliance)
    ↓
[KB Search] → Find and reuse prior artifacts from Jira/Confluence/SharePoint/Yammer
    ↓
[Strategy + PRD] → Human review gate
    ↓
[Delivery Engine] → Backlog, KPIs, rollout plan, Y-Score gate
    ↓
[Code Pipeline] → MetaGPT → OpenHands → Promptfoo → Cloudflare (existing pm-os)
    ↓
[Reporting Layer] → PowerBI dashboards + AI interpretation
    ↓
[KB Archival] → All artifacts tagged, versioned, indexed for reuse
```

---

## Success Metrics

| KPI | Baseline | Target |
|-----|----------|--------|
| Time to first discovery pack | 2–3 days | < 2 hours |
| KB artifact reuse rate (product #3+) | 0% | > 60% |
| PM documentation time | ~60% of week | < 20% |
| PowerBI insight time (manual read → AI interpret) | 30–60 min | < 2 min |
| Compliance coverage per artifact | Patchy | 100% for known regimes |

---

## Deliverables (Phased)

| Phase | Deliverable |
|-------|-------------|
| 1 | Discovery Engine: SWOT, ROI, competitor, compliance generators |
| 2 | KB Layer: federated search (Jira + Confluence + SharePoint + Yammer) + reuse |
| 3 | Standard Reporting: PowerBI embed + 4 pre-built templates |
| 4 | AI Tier: chat over KB + PowerBI AI interpret + deep research |
| 5 | Full pipeline integration: Discovery → PRD → Delivery → Code → KB archival |

---

## Constraints

- LLM cost < $0.50 per full discovery pack (Claude Sonnet 4.6 with prompt caching)
- All outputs human-editable markdown (no lock-in)
- AI outputs must cite sources with URL (EU AI Act Art. 13 explainability)
- Standard tier requires zero LLM — search + retrieval only (cost-safe for broad rollout)
- Data stays within tenant — no LLM training on user content

---

## Out of Scope (v1)

- Write-back to Jira / Confluence / SharePoint
- Native mobile app
- Multi-tenant (single org in v1)
- Real-time sync (15-minute polling interval)
