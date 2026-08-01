# productowner-skill — Skills Library for Client-Side AI Agents

**Author:** Vignesh AIPM · Senior PO · AI / BFSI / Healthcare

---

## What we are

**productowner-skill** is a **skills library** — markdown `SKILL.md` plugins that teach your local AI agent how to run Product Owner workflows in regulated domains (BFSI, healthcare, generic).

We provide **skills only**. Your client-side AI agent (Cursor, Claude Code, Antigravity, Codex CLI, etc.) reads those skills, runs the persona swarm gates locally, and builds a complete POC/MVP in **your** repository.

---

## Two end users

| End user | Role | How they interact |
|----------|------|-------------------|
| **Humans** | POs, PO leads, designers, engineers, InfoSec | Set intent, review gate outputs, approve POC/MVP deliverables |
| **Client-side AI agents** | Cursor Agent, Claude Code, Antigravity, etc. | Read `skills/` + `.agent/memory.md`, run discovery → delivery → gates, write artifacts |

Humans speak to **their own IDE agent**. There is no account with us, no API to call, and no runtime link between your environment and this repository.

```
Human (PO) ──intent──► Client AI Agent (local)
                              │
                              ├── reads skills/ (copied into your repo)
                              ├── reads .agent/memory.md (your repo)
                              ├── runs persona swarm gates (local)
                              └── writes artifacts/ + POC/MVP (your repo)

productowner-skill repo ──provides skills only──► copied once, no runtime connection
```

---

## What your client agent does

With our persona skills installed, your local agent can execute an end-to-end POC/MVP workflow:

1. **Discovery** — SWOT, TAM/SAM/SOM, competitor matrix, compliance risk map, GTM brief
2. **Delivery** — PRD with Gherkin AC, RICE backlog, KPI plan, rollout phases
3. **Persona swarm gates** — cybersec → UX → QA → Y-Score (local verdict JSON)
4. **Artifact release** — markdown outputs under `artifacts/` in your repo

See [examples/golden-run/](examples/golden-run/) for a synthetic walkthrough of human intent → agent outputs → gate JSONs.

---

## What we do not do

| We never | Why |
|----------|-----|
| Run a backend or SaaS | Skills are markdown; your agent is the runtime |
| OAuth, login, or accounts | No vendor relationship at execution time |
| Execute on our infrastructure | All codegen and doc generation runs on your machine |
| Receive prompts, data, or telemetry | No data flows through us — ever |
| Require API keys to productowner-skill | Use your agent's existing model and credentials |

---

## Quick install

| Doc | Purpose |
|-----|---------|
| [QUICKSTART.md](QUICKSTART.md) | Three steps: open repo → create memory → trigger PO |
| [docs/INSTALL.md](docs/INSTALL.md) | Full install guide (Cursor, Claude Code, Antigravity) |
| [docs/CLIENT-AGENT.md](docs/CLIENT-AGENT.md) | Vendor boundary — what the client agent does vs what we provide |

```bash
git clone https://github.com/vvs-PO/productowner-skill.git
mkdir -p .cursor/skills .agent artifacts
cp -r productowner-skill/skills/* .cursor/skills/
cp productowner-skill/.agent/memory.md .agent/memory.md   # then edit for your product
```

---

## Skills list

| Skill | Triggers | Gate role |
|-------|----------|-----------|
| `productowner-skill` | "Act as Product Owner", "Write a PRD", "Groom the backlog", "Run PO workflow", "Discovery to delivery" | Orchestrator |
| `PO-discovery` | "run discovery", "SWOT", "market sizing", "competitor analysis", "discovery pack", "GTM brief" | Discovery pack |
| `PO-delivery` | "prioritize backlog", "RICE score", "KPI plan", "delivery pack", "rollout plan", "write delivery artifacts" | Delivery pack |
| `PO-kb-research` | "search KB", "find prior artifact", "reuse template", "what have we done before", "search artifacts" | Local KB search |
| `PO-code-pipeline` | "run the pipeline", "PRD to SDLC", "full SDLC from PRD", "execute code pipeline", "discovery to release" | Pipeline router |
| `cybersec-skill` | "Threat model this", "Act as AppSec", "security review", "check for PII" | **BLOCK** on PII/PHI / critical OWASP |
| `ux-pro-skill` | "Review this UI", "Act as UX Pro", "accessibility review", "a11y check" | **BLOCK** on critical a11y; WARN on style drift |
| `qa-tester-skill` | "write tests", "Act as QA", "edge cases", "test matrix" | **WARN** only — never blocks pipeline |
| `y-score-readiness` | "is this ready to launch?", "readiness check", "score this PRD", `/y-score <prd.md>` | **BLOCK** if score &lt; 70 |
| `prd-to-sdlc` | PRD → architecture + code skeleton + eval harness | SDLC bundle (Phase 5) |

Skills live in `skills/` and `.claude/skills/`. Copy into `.cursor/skills/` or `.claude/skills/` in your target repo.

---

## Persona swarm gate model

Every artifact passes through the gate chain **on the client agent** before release:

```
write artifact
  → cybersec-skill      (BLOCK on PII/PHI or critical OWASP)
  → ux-pro-skill        (BLOCK on critical a11y; WARN on token/style drift)
  → qa-tester-skill     (WARN on missing edge cases or untestable AC)
  → y-score-readiness   (BLOCK if score < 70 for launch-bound artifacts)
  → release to artifacts/
```

- **BLOCK** — do not write or commit until resolved
- **WARN** — write with `> ⚠️ finding:` callout; flag for human review
- **pass** — proceed to next gate

Example gate outputs: [examples/golden-run/gates/](examples/golden-run/gates/)

---

## Portfolio demo (illustration only)

The static site at [vvs-PO.github.io/productowner-skill](https://vvs-PO.github.io/productowner-skill/) and everything under [`docs/`](docs/) is an **illustrative portfolio demo** — sample data, simulated UI, no authentication, no live integrations.

It shows what PO workflows *look like*; it is **not** the product runtime. The product is the skills library you copy into your repo.

> Do not enter confidential information in the demo. See [LIMITATIONS.md](LIMITATIONS.md).

| Page | URL |
|------|-----|
| Landing | [vvs-PO.github.io/productowner-skill](https://vvs-PO.github.io/productowner-skill) |
| PO Onboarding | [vvs-PO.github.io/productowner-skill/onboarding](https://vvs-PO.github.io/productowner-skill/onboarding/) |
| CuCP Slide Deck | [vvs-PO.github.io/productowner-skill/cucp/presentation.html](https://vvs-PO.github.io/productowner-skill/cucp/presentation.html) |

---

## Enterprise integrations (Phase 2)

Phase 2 adds optional enterprise KB orchestration — Atlassian Rovo, Microsoft 365 Copilot, Google Workspace AI — as **client-configured integrations**, not vendor-hosted services. Skills remain markdown-only; your agent and credentials connect to your org tools locally.

See [ROADMAP.md](ROADMAP.md) and `planning/phase1_brainstorm_5_personas.md` for phased delivery.

---

## Repository structure

```
productowner-skill/
├── skills/                    # Persona skills (copy to your agent config)
├── .agent/memory.md           # Memory schema — copy and customise per repo
├── examples/golden-run/       # Synthetic human → agent → artifacts walkthrough
├── docs/                      # Portfolio demo (GitHub Pages) + INSTALL.md
├── prds/                      # Reference PRDs
└── ROADMAP.md                 # Phased delivery plan
```

---

*Built by [Vignesh AIPM](https://github.com/vvs-PO) · Senior PO · AI / BFSI / Healthcare*

## Ownership

- Organization: `vvs-PO`
- Owner: Vignesh AIPM
