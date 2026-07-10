# FRD — pm-os Platform (v0.4)

**Author:** Vignesh AIPM
**Status:** Draft v0.4
**Linked SRS:** docs/product/SRS.md

---

## Standard Tier

### F1: Unified Search & KB Reuse

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F1.1 | As a PM, I want to search Jira, Confluence, SharePoint, and Yammer in one place | Single search bar queries Rovo (Jira+Confluence) + M365 Graph (SharePoint+Yammer) in parallel; results in < 3s |
| F1.2 | As a PM, I want to filter results by source, artifact type, domain, and date | Multi-select filters; results update without full reload |
| F1.3 | As a PM, I want to open any KB artifact at its source URL | "Open" button opens URL in new tab |
| F1.4 | As a PM, I want to clone an artifact into our org KB so my team can reuse it | "Clone to KB" action; PM adds domain + stage + type tags before saving |
| F1.5 | As a PM, I want to search the Shared Library for anonymised templates from other engagements | Shared Library tab; filter by domain + artifact type |
| F1.6 | As a PM Lead, I want to see which artifacts my team has reused this quarter | Team KB dashboard: reuse count, top artifacts, contributing PMs |

### F2: Standard Reporting (PowerBI)

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F2.1 | As a PM, I want to see release and KPI reports without leaving the platform | PowerBI embeds in-page via Embed API; load < 5s |
| F2.2 | As a PM Lead, I want a team-level view of release health across all active products | Aggregated PowerBI report: all active products, milestone status, velocity |
| F2.3 | As a PM, I want to filter reports by date, PM, product area, and domain | Filter panel; report refreshes on selection |
| F2.4 | As a PM, I want to export a report snapshot for stakeholders | Export to PDF and PNG |
| F2.5 | As a client stakeholder, I want to see a programme status dashboard without needing internal tool access | Client Workspace dashboard: shared KPIs, milestone tracker, AI summary |

---

## AI Tier

### F3: AI Chat over KB

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F3.1 | As a PM, I want to ask questions about our Jira and Confluence content in natural language | Rovo Chat handles Atlassian-grounded questions; response < 8s |
| F3.2 | As a PM, I want AI to synthesise across Jira, Confluence, SharePoint, and Yammer | Claude API synthesises cross-tool results; cites each source with URL |
| F3.3 | As a PM, I want every AI answer to show the source artifact and URL | Each response: source name, type, URL, confidence level |
| F3.4 | As a PM, I want the AI to suggest relevant prior org artifacts while I chat | Sidebar: "Related artifacts from your KB" surfaced per conversation turn |
| F3.5 | As a PM, I want to copy or export AI responses into Confluence | Copy button; "Save to Confluence" creates a draft page via Confluence AI |

### F4: AI Artifact Generation

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F4.1 | As a PM, I want AI to generate a SWOT grounded in our org's prior SWOTs for the same domain | SWOT draft in < 30s; cites 2+ prior org SWOTs as references |
| F4.2 | As a PM, I want AI to draft a PRD section using our org's standard template | PRD draft follows org template; pre-fills domain, compliance regime, stakeholders |
| F4.3 | As a PM, I want Jira AI to break my PRD epics into user stories automatically | Jira AI integration: PM selects epic → Jira AI generates stories; PM reviews before save |
| F4.4 | As a PM, I want AI to clone the closest prior ROI model for my product domain and pre-fill it | Clone from Shared Library or org KB; AI pre-fills market size, assumptions from discovery pack |

### F5: AI PowerBI Interpretation

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F5.1 | As a PM, I want to paste a PowerBI screenshot and get a plain-English summary | Drag-drop or paste → PowerBI Copilot + Claude narrative + bullet findings < 8s |
| F5.2 | As a PM, I want to upload PowerBI CSV export and ask questions about it | CSV upload → Claude parses + answers natural language questions |
| F5.3 | As a PM Lead, I want to ask "how is my team tracking against release targets?" and get an AI answer | Direct PowerBI Copilot API query → natural language answer with data citations |
| F5.4 | As a PM, I want to export AI report interpretation for my stakeholder update | Export: markdown or PDF |

### F6: Deep Research

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F6.1 | As a PM, I want to trigger research on a topic and get a structured report | /research command → Summary, Findings, Gaps, Next Steps |
| F6.2 | As a PM, I want research to combine our internal KB and public web sources | Cites internal (Rovo + M365) + web URLs |
| F6.3 | As a PM, I want to choose research depth based on urgency | Quick (30s) / Standard (2min) / Deep (5min) |
| F6.4 | As a PM, I want to export research as a Confluence page draft | "Save to Confluence" creates draft via Confluence AI |

---

## Client Workspace

### F7: Client Collaboration

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F7.1 | As a PM, I want to create a Client Workspace and invite the client without requiring Atlassian licences | PM creates workspace; client gets invite link with Client Viewer access |
| F7.2 | As a PM, I want to control exactly which artifacts the client can see | Per-artifact visibility toggle; default = hidden |
| F7.3 | As a client stakeholder, I want to see a programme dashboard with milestones and KPIs | Client-facing dashboard: milestone timeline, shared KPIs, AI status summary |
| F7.4 | As a PM, I want to archive a client workspace when the engagement closes | "Archive" action: exports ZIP of all shared artifacts + audit log |
| F7.5 | As an admin, I want to see an audit log of client workspace activity | Audit log: who viewed what artifact, when |

---

## Admin

| ID | Feature | Description |
|----|---------|-------------|
| A1 | Integration Config | Connect Rovo (Jira+Confluence) + M365 (SharePoint+Yammer) + PowerBI per Workspace |
| A2 | Tier Management | Assign Standard or AI tier to users or groups |
| A3 | Shared Library Curation | Approve org artifacts for anonymisation + promotion to Shared Library |
| A4 | Re-index | Manual trigger; auto every 15 min via Rovo + M365 Graph webhooks |
| A5 | Usage Analytics | Search queries, top reused artifacts, AI volume, client workspace activity |
| A6 | Cost Monitor | Claude API token usage + cost per team per month |
