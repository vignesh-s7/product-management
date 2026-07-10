# SRS — pm-os Platform (v0.4)

**Author:** Vignesh AIPM
**Status:** Draft v0.4
**Linked PRD:** prds/00-pm-os-platform.md

---

## 1. System Overview

Multi-tenant, two-tier web platform for product managers to discover, reuse, and generate
PM artifacts — within their org and across client engagements.
Built on top of Atlassian Rovo, Microsoft 365 Copilot, and PowerBI. pm-os orchestrates;
it does not replace these tools.

| Deployment Mode | Who | Description |
|----------------|-----|-------------|
| Org Workspace | Internal PM team | Shared KB, role-based access, team dashboards |
| Client Workspace | Consulting delivery | Separate tenant per client; PM creates, client views |
| Shared Library | Cross-org / cross-client | Anonymised, domain-tagged reusable templates |

| User Tier | Access |
|-----------|--------|
| Standard | Federated search + KB reuse + PowerBI standard reports |
| AI | Chat over KB + PowerBI AI interpretation + deep research + artifact generation |

---

## 2. Integrations (Build-on-Existing-AI)

| Source | Tool Used | Protocol | Access | Data Retrieved |
|--------|-----------|----------|--------|---------------|
| Jira | Atlassian Rovo Search | Rovo API / OAuth2 | Read-only | Epics, issues, comments, attachments |
| Confluence | Atlassian Rovo Search + Confluence AI | Rovo API / OAuth2 | Read-only + AI generate | Pages, spaces, labels, AI summaries |
| SharePoint | Microsoft Graph API / M365 Copilot | OAuth2 / Graph | Read-only | Documents, sites, lists |
| Yammer / Viva Engage | Microsoft Graph API | OAuth2 / Graph | Read-only | Posts, groups, announcements |
| PowerBI | PowerBI Embed API + PowerBI Copilot API | OAuth2 | Read + Embed + AI query | Reports, datasets, dashboards |
| AI Chat (Jira+Confluence) | Atlassian Rovo Chat | Rovo API | Query | Conversational answers from Atlassian content |
| AI Chat (pm-os reasoning) | Claude Sonnet 4.6 (Anthropic API) | REST | Generate | Artifact drafts, research, synthesis |

---

## 3. Multi-Tenant Architecture

- SR-T01 Each org gets an isolated Workspace — data never crosses tenant boundaries
- SR-T02 Client Workspaces are sub-tenants of the org; client data isolated from internal KB
- SR-T03 Shared Library contains only anonymised, admin-approved templates — no client or internal PII
- SR-T04 Admin connects source integrations per Workspace (Org or Client)
- SR-T05 Role hierarchy per Workspace: Admin · PM Lead · PM · Client Viewer

---

## 4. Search Requirements (Standard Tier)

- SR-S01 Federated search via Rovo Search (Jira + Confluence) + M365 Graph (SharePoint + Yammer) in one query
- SR-S02 Results: title, source icon, URL, artifact type tag, domain tag, last updated, author
- SR-S03 Filters: source, artifact type, domain (BFSI/Healthcare/SaaS/Telecom/Consumer), date range, PM owner
- SR-S04 "Reuse" action: open source URL in new tab or copy shareable link
- SR-S05 "Clone to KB" action: copies artifact into org KB with new metadata tag
- SR-S06 Search latency < 3 seconds p95 (Rovo + M365 Graph parallel query)
- SR-S07 Shared Library search: returns anonymised templates from cross-org pool

---

## 5. Reporting Requirements (Standard Tier)

- SR-R01 Embedded PowerBI reports via PowerBI Embed API (read-only)
- SR-R02 Pre-built PM templates: Release Velocity · KPI Dashboard · CuCP Status · PM Time Allocation
- SR-R03 PM Lead view: team-level aggregation across all active products
- SR-R04 Client dashboard: milestone tracking, shared KPIs, programme status (client-visible)
- SR-R05 Filters: date range, PM, product area, domain, client workspace
- SR-R06 Export: PDF, PNG per report

---

## 6. AI Chat Requirements (AI Tier)

- SR-A01 Rovo Chat handles Jira + Confluence questions natively (Atlassian-grounded)
- SR-A02 Claude API handles pm-os-specific reasoning: artifact generation, cross-tool synthesis, deep research
- SR-A03 Every AI response cites source: name, type, URL, confidence level
- SR-A04 Multi-turn context within session; resets on new session
- SR-A05 Suggested prompts on load (domain + role aware)
- SR-A06 Response latency < 8 seconds p95
- SR-A07 Prompt caching enabled on Claude API calls (cost control)
- SR-A08 Fallback: if Rovo unavailable → Claude searches org KB index directly

---

## 7. AI PowerBI Interpretation (AI Tier)

- SR-P01 Screenshot paste/upload → PowerBI Copilot interprets, pm-os surfaces narrative + actions
- SR-P02 CSV upload → Claude parses and answers natural language questions
- SR-P03 Direct dataset query: PowerBI Copilot API → natural language answer
- SR-P04 PM Lead: "Summarise team release health across all products" → aggregated AI narrative
- SR-P05 Output exportable: markdown, PDF

---

## 8. Deep Research (AI Tier)

- SR-DR01 /research command → Claude synthesises internal KB (via Rovo + M365) + web
- SR-DR02 Output structure: Summary · Key Findings · Gaps · Recommended Next Steps
- SR-DR03 All sources cited: internal (URL) + web (URL)
- SR-DR04 Depth selector: Quick (30s) · Standard (2min) · Deep (5min)
- SR-DR05 Export: markdown, PDF, Confluence page draft (via Confluence AI create)

---

## 9. Client Workspace Requirements

- SR-C01 PM creates Client Workspace; client receives invite link (no Atlassian/M365 licence required)
- SR-C02 PM selects which artifacts are visible to client (granular toggle per artifact)
- SR-C03 Client Viewer role: read-only; cannot search internal KB; sees only shared artifacts
- SR-C04 Client dashboard: programme milestones, shared KPIs, AI-generated status summary
- SR-C05 Client workspace audit log: who viewed what, when
- SR-C06 Client workspace archival on engagement close (exportable ZIP)

---

## 10. Non-Functional Requirements

- NFR-01 SSO: Microsoft Entra / Okta / Atlassian Access
- NFR-02 RBAC: Admin · PM Lead · PM · Client Viewer
- NFR-03 Data residency: tenant data stays within selected region (EU / US / APAC)
- NFR-04 GDPR / SOC2 Type II compliant
- NFR-05 Uptime SLA: 99.5%
- NFR-06 Mobile-responsive web UI
- NFR-07 KB re-index: auto every 15 minutes via Rovo + M365 Graph webhooks
- NFR-08 Rovo / M365 Copilot licences required at org level — pm-os does not bundle them

---

## 11. Out of Scope (v1)

- Write-back to Jira / Confluence / SharePoint
- Native mobile app
- White-label for clients
- Revenue/billing module for client workspaces
- Real-time sync (< 15-minute latency)
