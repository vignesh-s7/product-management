# FRD — PM Knowledge Base Platform

**Author:** Vignesh Vignesh S
**Status:** Draft v0.1
**Linked SRS:** docs/product/SRS.md

---

## Standard Tier

### F1: Search & Discovery

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F1.1 | As a PM, I want to search Jira, Confluence, SharePoint, and Yammer in one place | Results from all 4 sources in a single ranked list, < 3 seconds |
| F1.2 | As a PM, I want to filter by source system | Checkboxes for each source; results update without full reload |
| F1.3 | As a PM, I want to filter by artifact type (PRD, SRS, Sprint, Research, Decision) | Type tag on each result; multi-select filter |
| F1.4 | As a PM, I want to filter by domain (BFSI, Healthcare, SaaS) | Domain tag on each result; multi-select filter |
| F1.5 | As a PM, I want to open or copy the URL of any KB artifact to reuse it | "Open" opens URL in new tab; "Copy link" copies to clipboard |
| F1.6 | As a PM, I want to see who last updated an artifact and when | Last modified date + author shown on each result card |

### F2: Standard Reporting (PowerBI)

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F2.1 | As a PM, I want to see release and KPI reports without leaving the platform | PowerBI report renders in-page; load < 5 seconds |
| F2.2 | As a PM, I want to filter reports by date, PM, and product area | Filter panel; report refreshes on selection |
| F2.3 | As a PM, I want to export a report snapshot for stakeholders | Export to PDF and PNG on each report |
| F2.4 | As a PM, I want ready-made report templates so I don't build dashboards from scratch | 4 templates available: Release Velocity, KPI Dashboard, CuCP Status, PM Time |

---

## AI Tier

### F3: AI Chat over KB

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F3.1 | As a PM, I want to ask questions in natural language and get answers from our KB | Chat UI with input, response area, conversation history |
| F3.2 | As a PM, I want every AI answer to show the source artifact and URL | Each response: source name, type, URL, confidence level |
| F3.3 | As a PM, I want prompt suggestions so I know what to ask | 4–6 suggested prompts on load, relevant to user's domain |
| F3.4 | As a PM, I want the AI to remember context within a session | AI references prior turns; resets on new session |
| F3.5 | As a PM, I want to copy or export AI responses | Copy button per response; export as markdown |

### F4: AI PowerBI Interpretation

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F4.1 | As a PM, I want to paste a PowerBI screenshot and get an AI summary | Drag-drop or paste → narrative summary + bullet findings < 8 seconds |
| F4.2 | As a PM, I want to upload exported PowerBI data and ask questions | CSV upload → AI answers natural language questions about the data |
| F4.3 | As a PM, I want to query a connected PowerBI dataset in natural language | AI queries REST API → natural language answer with data citations |
| F4.4 | As a PM, I want to export AI interpretations for my review docs | Export: markdown or PDF |

### F5: Deep Research

| ID | User Story | Acceptance Criteria |
|----|-----------|-------------------|
| F5.1 | As a PM, I want to trigger deep research on a topic and get a structured report | /research command → Summary, Findings, Gaps, Next Steps |
| F5.2 | As a PM, I want research to combine internal KB and public sources | Cites internal KB artifacts + web URLs |
| F5.3 | As a PM, I want to choose research depth based on urgency | Quick (30s) / Standard (2min) / Deep (5min) selector |
| F5.4 | As a PM, I want to export research output as a shareable doc | Export: markdown, PDF, or Confluence page draft |

---

## Admin

| ID | Feature | Description |
|----|---------|-------------|
| A1 | Integration Config | Connect Jira, Confluence, SharePoint, Yammer via OAuth2 / Graph API |
| A2 | Tier Management | Assign Standard or AI tier to users or groups |
| A3 | PowerBI Config | Link PowerBI workspace; select reports to embed |
| A4 | Re-index | Manual trigger; auto every 15 minutes |
| A5 | Usage Analytics | Search queries, top reused artifacts, AI chat volume, report views |
