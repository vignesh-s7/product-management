# SRS — PM Knowledge Base Platform

**Author:** Vignesh Vignesh S
**Status:** Draft v0.1
**Linked PRD:** prds/00-pm-os-platform.md

---

## 1. System Overview

Two-tier web platform for PMs to discover, reuse, and generate PM artifacts
from connected enterprise knowledge sources.

| Tier | Core Capability |
|------|----------------|
| Standard | Federated KB search · PowerBI standard reports · URL reuse |
| AI | LLM chat over KB · PowerBI AI interpretation · Deep research |

---

## 2. Integrations

| Source | Protocol | Access | Data Retrieved |
|--------|----------|--------|---------------|
| Jira | OAuth2 / REST API | Read-only | Epics, issues, comments, attachments |
| Confluence | OAuth2 / REST API | Read-only | Pages, spaces, labels, attachments |
| SharePoint | Microsoft Graph API | Read-only | Documents, sites, lists |
| Yammer / Viva Engage | Microsoft Graph API | Read-only | Posts, groups, announcements |
| PowerBI | Embed API + REST API | Read + Embed | Reports, datasets, dashboards |

---

## 3. Search Requirements (Standard Tier)

- SR-01 Federated search across all 4 sources in a single query
- SR-02 Results: title, source icon, URL, artifact type tag, last updated
- SR-03 Filters: source system, artifact type, domain, date range
- SR-04 "Reuse" action: open URL in new tab or copy shareable link
- SR-05 Search latency < 3 seconds (p95)
- SR-06 Ranking: TF-IDF + recency weighting

---

## 4. Reporting Requirements (Standard Tier)

- SR-07 Embedded PowerBI reports (read-only)
- SR-08 Pre-built templates: Release Velocity · KPI Dashboard · CuCP Status · PM Time Allocation
- SR-09 Filters: date range, PM name, product area, domain
- SR-10 Export: PDF, PNG

---

## 5. AI Chat Requirements (AI Tier)

- AI-01 Chat UI grounded in KB search results (RAG)
- AI-02 Every response cites: source name, artifact type, URL, confidence level
- AI-03 Multi-turn context within session; resets on new session
- AI-04 Suggested prompts on load (domain-relevant)
- AI-05 Response latency < 8 seconds (p95)
- AI-06 LLM: Claude Sonnet 4.6 primary, Gemini fallback

---

## 6. AI PowerBI Interpretation (AI Tier)

- AI-07 Screenshot paste/upload → AI narrative summary within 8 seconds
- AI-08 CSV upload → AI parses and answers natural language questions
- AI-09 Direct dataset query: AI queries PowerBI REST API, returns natural language answer
- AI-10 Output exportable as markdown or PDF

---

## 7. Deep Research (AI Tier)

- AI-11 /research command → structured report: Summary · Findings · Gaps · Next Steps
- AI-12 Sources: internal KB artifacts (URL) + web sources (URL)
- AI-13 Depth selector: Quick (30s) · Standard (2min) · Deep (5min)
- AI-14 Export: markdown, PDF, Confluence page draft

---

## 8. Non-Functional Requirements

- NFR-01 SSO: Microsoft Entra / Okta
- NFR-02 RBAC: Standard Tier · AI Tier · Admin
- NFR-03 Data stays within tenant — no external LLM training on user data
- NFR-04 GDPR / SOC2 compliant
- NFR-05 Uptime SLA: 99.5%
- NFR-06 Mobile-responsive web UI
- NFR-07 KB re-index: auto every 15 minutes, manual trigger available

---

## 9. Out of Scope (v1)

- Write-back to any connected source
- Native mobile app
- Real-time sync (< 15-minute latency)
- Multi-tenant
