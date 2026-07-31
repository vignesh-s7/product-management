# PRD 00 — productowner-skill Platform: AI-Native PO Persona Swarm

**Domain:** PO tooling · platform · B2B SaaS
**Author:** Vignesh AIPM
**Status:** Active · v0.4
**Linked:** docs/product/SRS.md · docs/product/FRD.md · docs/product/ARCHITECTURE.md

---

## Problem

Product Owners carry the full cognitive load of a product from first idea to post-launch review.
Every artifact — market research, SWOT, competitor matrix, PRD, prioritisation backlog, KPI plan,
release strategy — is produced manually, from scratch, for every product.

Tools like WikiBoard, DocRepo, AgileBoard, and SocialBoard hold institutional knowledge — but:
- PMs search each tool separately with no unified view
- Nothing is reused across products, teams, or clients
- AI exists in each tool in isolation (AgileVendor Rovo, M365 Copilot) but is not orchestrated into a PO workflow
- When a consulting team delivers a product for a client, all that knowledge disappears — not packaged, not reusable

The compounding cost: 60–80% of a PO's working week on documentation and re-work,
multiplied across every PO in the organisation.

---

## Target Users

### Internal (Org Use)
| Role | Need |
|------|------|
| Product Owner | Find and reuse artifacts; AI-assisted research and drafting |
| PO Lead / Manager | Team-level KB visibility; release health dashboards |
| Admin / P&T Ops | Connect tools, manage tiers, monitor adoption |

### External (Client Delivery)
| Role | Need |
|------|------|
| Consulting PO / Engagement Lead | Package deliverables into reusable client KB |
| Client PO | Access shared artifacts; track programme status |
| Client Stakeholder | Read-only dashboards and summary views |

---

## Two-Tier, Multi-Tenant Product Model

### Deployment Modes
| Mode | Who Uses It | Description |
|------|------------|-------------|
| **Org Workspace** | Internal PO team | Shared KB across all PMs in the org; role-based access |
| **Client Workspace** | Consulting delivery | Separate tenant per client; PO team creates, client views |
| **Shared Library** | Cross-org / cross-client | Reusable template library (anonymised, tagged by domain) |

### User Tiers
| | Standard | AI |
|--|----------|----|
| Search | Federated: AgileBoard + WikiBoard + DocRepo + SocialBoard via AgileVendor Rovo + M365 Copilot | Same + AI chat (Rovo Chat + AIAssistant) |
| Reporting | Embedded AnalyticsDashboard standard templates | AnalyticsDashboard Copilot interpretation + natural language queries |
| Research | Browse + reuse artifact URLs from KB | Deep research: internal KB + web, structured report |
| Artifact generation | Templates (clone + edit) | AI-generated drafts grounded in org KB |
| Client sharing | Read-only client view of selected artifacts | Client workspace with AI-summarised status |

---

## Build-on-Existing-AI Strategy

productowner-skill does NOT rebuild what already exists. It orchestrates:

| Layer | Existing Tool Used | productowner-skill Adds |
|-------|-------------------|-----------|
| WikiBoard + AgileBoard search & AI | **AgileVendor Rovo** (Rovo Search + Rovo Chat) | PO-specific query templates, KB tagging, cross-product patterns |
| DocRepo + SocialBoard + Teams search | **EnterpriseCloud 365 Copilot / Graph API** | Unified result view alongside AgileVendor sources |
| AnalyticsDashboard reporting | **AnalyticsDashboard Embed API + AnalyticsDashboard Copilot** | Pre-built PO templates, cross-org aggregation |
| AI chat | **Rovo Chat (AgileVendor)** + **AIAssistant API** for productowner-skill-specific reasoning | PO workflow context, KB citations, artifact generation |
| Document generation | **WikiBoard AI** (create page from prompt) | Structured PO templates (PRD, SWOT, ROI, release plan) |
| Backlog + stories | **AgileBoard AI** (epic breakdown, story generation) | Domain-specific acceptance criteria, compliance tags |

---

## Solution: Four Engines

### 1. Discovery Engine
Input: problem statement + domain selector
Output (AI-generated, grounded in org KB + Rovo + web):
- Market sizing: TAM / SAM / SOM
- SWOT (reuses prior org SWOTs via KB search)
- Competitor matrix (web research + internal benchmarks)
- ROI model (cloned from closest prior org template)
- Compliance risk map (domain-aware: HIPAA / PCI-DSS / GDPR / EU AI Act / FATF)
- GTM brief

### 2. Delivery Engine
Input: PRD
Output:
- Prioritised backlog via AgileBoard AI (RICE / WSJF / MoSCoW)
- KPI instrumentation plan
- Y-Score launch readiness gate (7 dimensions)
- Beta strategy + phased rollout plan

### 3. KB Layer — Org + Client Reuse Core
- Indexed across: AgileBoard, WikiBoard (via Rovo), DocRepo, SocialBoard (via M365 Graph)
- Every artifact tagged: domain · stage · product-type · compliance-regime · client/internal
- Standard tier: search results with source URLs — click to reuse
- AI tier: Rovo Chat + AIAssistant answers from KB, every response cites source URL
- Client workspace: selected artifacts shared with client view (read-only, configurable)
- Shared Library: anonymised org templates available across client engagements

### 4. Reporting & Interpret Layer
- Standard: AnalyticsDashboard embed, 4 pre-built PO templates
- AI: AnalyticsDashboard Copilot for natural language queries + screenshot interpretation
- Multi-PO view: PO Lead sees team-level release health, KB coverage, adoption metrics
- Client dashboard: programme status, milestone tracking, shared KPIs

---

## Multi-PO Workflow

```
PO Lead sets up Org Workspace
    → connects AgileBoard + WikiBoard (Rovo) + DocRepo + SocialBoard (M365)
    → assigns Standard / AI tier per PO

PO starts new product
    → Discovery Engine: AI searches org KB for prior similar work
    → Surfaces: "3 prior BFSI products found — reuse their SWOT and compliance map?"
    → PO accepts / edits → saves to org KB tagged to this product

PO ships artifact to client
    → Creates Client Workspace
    → Selects artifacts to share (PRD summary, KPI dashboard, release plan)
    → Client PO sees read-only view + AI summary of programme status

PO Lead monitors
    → Team dashboard: which products are in flight, KB reuse rate, release velocity
    → Surfaces patterns: "BFSI products avg 3 weeks longer in EAP — investigate"
```

---

## Reuse Model (Org + Client)

| Artifact | Reuse Within Org | Reuse Across Clients |
|----------|-----------------|---------------------|
| SWOT template | Yes — tagged by domain | Yes — anonymised in Shared Library |
| ROI model | Yes — clone + adjust | Yes — anonymised |
| Compliance checklist | Yes — versioned by regime | Yes — regime-tagged |
| KPI framework | Yes | Yes |
| PRD template | Yes | Yes |
| Client deliverables | No (client-confidential) | No |

---

## Success Metrics

| KPI | Baseline | Target |
|-----|----------|--------|
| Time to first discovery pack | 2–3 days | < 2 hours |
| KB artifact reuse rate (product #3+) | 0% | > 60% |
| PO documentation time | ~60% of week | < 20% |
| Cross-PO KB contributions per month | 0 | > 5 per PO |
| Client workspace adoption | N/A | ≥ 1 per engagement |
| Shared Library template reuse across clients | 0 | > 40% of engagements |

---

## Phased Deliverables

| Phase | What Ships | Who Benefits |
|-------|-----------|-------------|
| 1 | Org Workspace + Rovo KB search (AgileBoard + WikiBoard) | Internal PO team |
| 2 | M365 search (DocRepo + SocialBoard) + AnalyticsDashboard embed | Full org Standard tier |
| 3 | AI tier: Rovo Chat + AIAssistant + AnalyticsDashboard Copilot | AI-tier PMs |
| 4 | Client Workspace + client sharing | Consulting / delivery teams |
| 5 | Shared Library + cross-client reuse | Org-wide + client portfolio |

---

## Constraints

- LLM cost < $0.50 per discovery pack (AIAssistant Sonnet 4.6 prompt caching)
- All outputs human-editable markdown (no lock-in)
- AI outputs cite sources with URL (EU AI Act Art. 13)
- Standard tier: zero LLM cost (Rovo + M365 search only)
- Client data isolation: client workspaces are separate tenants, never cross-contaminated
- Rovo / M365 Copilot licences required for AI search (productowner-skill doesn't replace, it orchestrates)

---

## Out of Scope (v1)

- Write-back to AgileBoard / WikiBoard / DocRepo
- Native mobile app
- Real-time sync (15-min polling)
- White-label for clients (v2)
- Revenue/billing module for client workspaces (v2)
