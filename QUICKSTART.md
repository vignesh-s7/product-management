# Quickstart — 3 Steps to Your First PO Session

**We provide skills only.** Your local AI agent does everything — discovery, PRD writing, gate checks, and POC/MVP artifacts. No vendor runtime, no API keys, no account with us.

**Repository:** [github.com/vignesh-s7/product-management](https://github.com/vignesh-s7/product-management)

---

## Step 1 — Clone the repo

Skills are **already mirrored** in `.cursor/skills/` on clone. No manual copy step required for Cursor users.

```bash
git clone https://github.com/vignesh-s7/product-management.git
cd product-management
```

**What you get:**

| Skill | Purpose |
|-------|---------|
| `productowner-skill` | Core PO orchestration |
| `PO-discovery` | SWOT, TAM/SAM/SOM, competitor analysis |
| `PO-delivery` | RICE backlog, KPI plan, rollout |
| `PO-kb-research` | Local artifact search |
| `PO-code-pipeline` | Declarative SDLC pipeline |
| `cybersec-skill` | PII blocker + OWASP auditor |
| `ux-pro-skill` | Accessibility + design tokens |
| `qa-tester-skill` | Edge-case matrix generator |
| `y-score-readiness` | 7-dimension launch gate |
| `prd-to-sdlc` | PRD → full SDLC artifact set |

For Claude Code, skills also live under `.claude/skills/`. See [docs/INSTALL.md](docs/INSTALL.md) for other agents.

---

## Step 2 — Copy and edit `.agent/memory.md` for your product

Every skill reads `.agent/memory.md` first. Customize it for **your** product — not this demo repo.

```bash
mkdir -p .agent artifacts
cp .agent/memory.md /path/to/your-repo/.agent/memory.md   # or edit in place if this is your repo
```

Edit the YAML sections: `product_name`, `domain`, `target_users`, `compliance_regimes`, `constraints`, and `glossary`.

```bash
touch artifacts/.gitkeep
```

---

## Step 3 — Tell your agent to run discovery

Open your IDE agent (Cursor, Claude Code, or Antigravity) and say:

> **Act as Product Owner — run discovery for [your problem statement]**

Your agent will:

1. Read `.agent/memory.md` for your product context
2. Load skills from `.cursor/skills/` (or `.claude/skills/`)
3. Run the persona swarm (discovery → delivery → gates)
4. Write outputs to `artifacts/` in **your** repo

**That's it.** We never see your prompts, data, or outputs.

---

## What happens next

| You say | Agent does |
|---------|------------|
| "Write a PRD with Gherkin acceptance criteria" | `PO-delivery` → `cybersec-skill` gate |
| "Score this PRD against Y-Score readiness" | `y-score-readiness` gate |
| "Run the pipeline from this PRD" | `PO-code-pipeline` → full SDLC pack |

All execution stays on your machine. See [docs/CLIENT-AGENT.md](docs/CLIENT-AGENT.md) for the full client-agent model.

---

## Verify trust (optional)

```bash
npm run check
```

See [TRUST.md](TRUST.md) for the full security posture.

---

## Walkthroughs

| Walkthrough | Domain |
|-------------|--------|
| [BFSI credit-risk POC](examples/walkthroughs/bfsi-poc-session.md) | PCI-DSS, fair lending (synthetic) |
| [Healthcare FHIR wellness POC](examples/walkthroughs/healthcare-poc-session.md) | HIPAA, synthetic PHI rules |
| [Golden-run reference](examples/golden-run/) | Gate JSON examples + sample artifacts |

---

**Remember:** YOUR agent does everything. We provide skills only.
