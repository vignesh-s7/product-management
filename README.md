# productowner-skill — AI-Native PO 

**Author:** Vignesh AIPM · Senior PO · AI / BFSI / ANY Domain
## About

**productowner-skill** is a Product Operating System that converts a Product Requirements Document into a full software development lifecycle. It orchestrates Claude Skills, MetaGPT, and Promptfoo so that a Product Owner, working alone, can move from a PRD to an eval-ready SDLC package in under two hours. Built by a Senior Product Owner for teams shipping AI features in regulated industries.

**Interactive portfolio demo:** https://vvs-PO.github.io/productowner-skill/

---

**Live:** [vvs-PO.github.io/productowner-skill](https://vvs-PO.github.io/productowner-skill)
**Status:** Static portfolio demo · sample data · no authentication or live integrations

> productowner-skill demonstrates product workflows and UI concepts. It does not authenticate users, call AI providers, connect enterprise systems, or process production data. See [LIMITATIONS.md](LIMITATIONS.md).

---

## What is productowner-skill?

productowner-skill is a full-lifecycle PO operating system that takes a product from first idea to post-launch review — generating every artifact a PO needs along the way.

It does not replace Jira, Confluence, SharePoint, or Google Workspace. It **orchestrates** them, adding a PO-specific workflow layer on top of Atlassian Rovo, Microsoft 365 Copilot, Google Workspace AI, and Claude.

---

## The Problem

Product Owners spend 60–80% of their working week on documentation and re-work:

- Market research, SWOT, competitor analysis, ROI models — produced from scratch every time
- Jira, Confluence, SharePoint, Yammer, Google Drive searched separately with no unified view
- AI exists in each tool (Rovo, M365 Copilot, Gemini) but is not connected into a PO workflow
- Nothing is reused across products, teams, or client engagements

---

## Two-Tier Product Model

| | Standard | AI ✨ |
|--|----------|-------|
| **Search** | Federated KB search: Jira + Confluence (Rovo) · SharePoint + Yammer + Teams (M365) · Google Drive + Docs (Google API) | Same + AI chat grounded in KB (Rovo Chat + Claude) |
| **Reporting** | Embedded PowerBI + Looker standard templates | PowerBI Copilot + Looker AI — natural language queries and screenshot interpretation |
| **Research** | Browse + reuse artifact URLs | Deep research: internal KB + web, structured report (Quick / Standard / Deep) |
| **Artifacts** | PO templates library — clone and edit | AI-generated drafts: SWOT, PRD, ROI model, KPI plan, release strategy |
| **Org** | Multi-PO org KB · Client workspace (read-only) | AI-summarised client status · cross-product pattern recognition |

---

## Four Engines

### 1. Discovery Engine
Input: problem statement + domain
Output: market sizing (TAM/SAM/SOM) · SWOT · competitor matrix · ROI model · compliance risk map · GTM brief

### 2. Delivery Engine
Input: PRD
Output: prioritised backlog (RICE/WSJF/MoSCoW) · KPI plan · Y-Score gate · beta strategy · phased rollout plan

### 3. KB Layer
- Indexed across: Jira, Confluence (Rovo) · SharePoint, Yammer, Teams (M365) · Google Drive, Docs (Google API)
- Every artifact tagged: domain · stage · product-type · compliance-regime
- Standard: search + reuse URLs · AI: Rovo Chat + Claude, cited responses
- Client workspace: PO creates, client views — no Atlassian/M365 licence required for client
- Shared Library: anonymised templates reusable across all client engagements

### 4. Code Pipeline (original productowner-skill)
Input: PRD → MetaGPT (architecture) → OpenHands (code) → Promptfoo (QA) → Cloudflare (deploy)

---

## Live Pages

| Page | URL |
|------|-----|
| Landing | [vvs-PO.github.io/productowner-skill](https://vvs-PO.github.io/productowner-skill) |
| PO Onboarding | [vvs-PO.github.io/productowner-skill/onboarding](https://vvs-PO.github.io/productowner-skill/onboarding/) |
| CuCP Slide Deck | [vvs-PO.github.io/productowner-skill/cucp/presentation.html](https://vvs-PO.github.io/productowner-skill/cucp/presentation.html) |
| Teams Tab | [vvs-PO.github.io/productowner-skill/onboarding/teams.html](https://vvs-PO.github.io/productowner-skill/onboarding/teams.html) |

---

## Repository Structure

```
productowner-skill/
├── prds/                          # Reference PRDs
│   ├── 00-productowner-skill-platform.md       # Master platform PRD (v0.4)
│   ├── 01-y-score-framework.md    # Launch readiness framework
│   ├── 02–08-*.md                 # Domain reference PRDs
│   └── 09-cucp-program-ops.md    # Coupa CuCP 90-day rollout
├── docs/                          # GitHub Pages (live site)
│   ├── index.html                 # Landing page
│   ├── onboarding/
│   │   ├── index.html             # 6-step PO onboarding wizard
│   │   ├── teams.html             # Microsoft Teams entry point
│   │   └── manifest.json          # Teams app manifest
│   ├── cucp/
│   │   └── presentation.html      # CuCP slide deck (6 slides)
│   └── product/
│       ├── SRS.md                 # System requirements (v0.4)
│       └── FRD.md                 # Functional requirements (v0.4)
├── ROADMAP.md                     # Phased delivery plan
└── .github/workflows/pages.yml   # Auto-deploy to GitHub Pages
```

---

## Integration Strategy

productowner-skill builds on existing enterprise AI — it does not reinvent it:

| Layer | Tool Used | productowner-skill Adds |
|-------|-----------|-----------|
| Jira + Confluence search + AI | Atlassian Rovo (Search + Chat) | PO templates, KB tagging, cross-product patterns |
| SharePoint + Yammer + Teams | Microsoft 365 Copilot / Graph API | Unified view alongside Atlassian |
| Google Drive + Docs + Chat | Google Workspace API + Gemini | Same unified view, Google-native orgs |
| PowerBI + Looker reports | PowerBI Embed + Copilot · Looker API | PO pre-built templates, AI narrative layer |
| AI chat + artifact generation | Rovo Chat + Claude Sonnet 4.6 | PO workflow context, cited KB responses |

---

## Constraints

- LLM cost < $0.50 per full discovery pack (Claude Sonnet 4.6 with prompt caching)
- All outputs are human-editable markdown — no lock-in
- AI outputs cite every source with URL (EU AI Act Art. 13 explainability)
- Standard tier: zero LLM cost — Rovo + M365 + Google search only
- Client data is fully isolated — separate tenants, never cross-contaminated
- Rovo / M365 Copilot / Google Workspace licences required at org level

---

## Explore the Demo

Open [vvs-PO.github.io/productowner-skill](https://vvs-PO.github.io/productowner-skill/) or the [sample onboarding flow](https://vvs-PO.github.io/productowner-skill/onboarding/). No account, API key, or external connection is required. Do not enter confidential information.

---

## Built With

[Atlassian Rovo](https://www.atlassian.com/software/rovo) · [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/copilot) · [Google Workspace AI](https://workspace.google.com/intl/en/features/ai/) · [Claude API (Anthropic)](https://www.anthropic.com) · [MetaGPT](https://github.com/geekan/MetaGPT) · [OpenHands](https://github.com/All-Hands-AI/OpenHands) · [Promptfoo](https://github.com/promptfoo/promptfoo) · [Cloudflare Workers](https://workers.cloudflare.com)

---

*Built by [Vignesh AIPM](https://github.com/vvs-PO) · Senior PO · AI / BFSI / Healthcare*

## Ownership

- Organization: `vvs-PO`
- Owner: Vignesh AIPM
