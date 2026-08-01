# Client-Side AI Agent Model

This document describes what your **local AI agent** does with our skills, what we **never** do, which agents are supported, and the path from problem statement to POC/MVP.

**Repository:** [github.com/vignesh-s7/product-management](https://github.com/vignesh-s7/product-management)

---

## What the client-side AI agent does

Your IDE agent is the **primary executor** of all PO workflow work. We provide Markdown instructions; the agent provides intelligence, codegen, and file I/O.

| Responsibility | How it works |
|----------------|--------------|
| **Read skills** | Loads `SKILL.md` from `.cursor/skills/` or `.claude/skills/` at conversation time |
| **Read memory** | Parses `.agent/memory.md` first — product name, domain, compliance, constraints |
| **Run gates** | Invokes persona swarm locally: `cybersec-skill` → `ux-pro-skill` → `qa-tester-skill` |
| **Search KB** | `PO-kb-research` scans `artifacts/`, `prds/`, and skill templates in your repo |
| **Write artifacts** | Produces PRDs, backlogs, test matrices, and SDLC packs to `artifacts/` |
| **Build POC/MVP** | Generates application code, configs, and deploy scaffolding in your repo |

```text
Human intent
    │
    ▼
Client AI Agent (local)
    ├── read .agent/memory.md
    ├── read .cursor/skills/*/SKILL.md
    ├── delegate: PO-discovery → PO-delivery → PO-code-pipeline
    ├── gate: cybersec → UX → QA → Y-Score
    └── write artifacts/ + POC/MVP code
```

Nothing in this flow calls vendor infrastructure. The agent uses **your** model, **your** credentials, and **your** filesystem.

---

## What we never do

| We never… | Why |
|-----------|-----|
| Run skills on our servers | Skills are Markdown — no runtime on vendor side |
| Receive prompts or artifacts | No API, no webhook, no telemetry endpoint |
| Collect session state or analytics | No phone-home, no usage tracking |
| Require API keys to us | Skills use your agent's existing model access |
| Execute code from `skills/` at install | Nothing in `skills/` runs on clone or `npm install` |
| Host your POC/MVP | Your agent builds locally; you own all outputs |

See [TRUST.md](../TRUST.md) for verification steps (`npm run check`).

---

## Supported agents

| Agent | Skills path | Status |
|-------|-------------|--------|
| **Cursor** | `.cursor/skills/` (pre-mirrored on clone) | Supported |
| **Claude Code** | `.claude/skills/` (pre-installed in repo) | Supported |
| **Antigravity** | Point skill loader at `skills/` or copy to agent config | Supported |

Any agent that reads `SKILL.md` with YAML frontmatter (`name`, `description`) can consume these skills. Consult your agent's documentation for the exact config path.

### Dual end users

| End user | Role |
|----------|------|
| **Humans** | Set intent, review gates, approve deliverables, install skills |
| **Client AI agents** | Execute skills, run gates, write artifacts, build POC/MVP |

Both operate in **your** environment. Humans speak to their agent; the agent never speaks to us.

---

## POC/MVP outcome path

From a single problem statement to a working proof-of-concept or minimum viable product — entirely on the client side.

```text
Phase 1 — Discovery
  "Act as Product Owner — run discovery for [problem]"
  → SWOT, market sizing, competitor matrix (artifacts/)

Phase 2 — Definition
  "Write a PRD with Gherkin acceptance criteria"
  → PRD + RICE backlog + KPI plan
  → cybersec-skill gate (PII / OWASP)

Phase 3 — Readiness
  "Score this PRD against Y-Score readiness"
  → 7-dimension go/no-go report

Phase 4 — SDLC pack
  "Run the pipeline from this PRD"
  → Architecture, DB schema, code skeleton, eval harness (prd-to-sdlc)
  → ux-pro-skill + qa-tester-skill gates

Phase 5 — POC/MVP build
  Agent generates application code in your repo
  → You run, test, and deploy on your infrastructure
```

| Outcome | Location | Owner |
|---------|----------|-------|
| Discovery pack | `artifacts/` | You |
| PRD + delivery pack | `artifacts/` or `prds/` | You |
| Gate reports | Inline in agent session + `artifacts/` | You |
| Application code | Your repo (agent-generated) | You |
| Deploy config | Your repo (agent-generated) | You |

We provide the **skills and templates**. Your agent provides the **execution**. You provide the **product intent and infrastructure**.

---

## Getting started

1. Clone [github.com/vignesh-s7/product-management](https://github.com/vignesh-s7/product-management)
2. Edit `.agent/memory.md` for your product — see [QUICKSTART.md](../QUICKSTART.md)
3. Tell your agent: **"Act as Product Owner — run discovery for [problem]"**

For full install options and troubleshooting, see [INSTALL.md](INSTALL.md).
