# Plugin Install Guide — 5 Minutes

Install the productowner-skill persona swarm in any repository. No Docker, no API keys, no backend infrastructure.

**Target time:** under 5 minutes on a clean machine with an IDE agent (Cursor, Claude Code, or Antigravity).

---

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| Git | Clone or fork `productowner-skill` |
| IDE with agent skills support | Cursor, Claude Code, or compatible agent |
| No API keys | Skills use your agent's existing model |
| No Docker | Declarative markdown only |

---

## IDE Compatibility Matrix

Skills ship pre-mirrored in `.cursor/skills/` on clone. Copy or symlink for other agents as needed.

| IDE/Agent | Skills path | Memory path | Trigger example | Notes |
|-----------|-------------|-------------|-----------------|-------|
| Cursor | `.cursor/skills/` | `.agent/memory.md` | "Act as Product Owner" | Auto-discovered |
| Claude Code | `.claude/skills/` | `.agent/memory.md` | Same | |
| Antigravity | `.cursor/skills/` or agent config | `.agent/memory.md` | Same | |
| Codex CLI | `.codex/skills/` | `.agent/memory.md` | `/skill-name` | |
| Gemini CLI | `.gemini/skills/` | `.agent/memory.md` | Varies | |

---

## Step 1 — Copy skills to agent config paths

Clone the repository (or copy the `skills/` directory from a release):

```bash
git clone https://github.com/vignesh-s7/product-management.git
cd product-management
```

### Cursor

Copy platform skills into your project's agent skills directory:

```bash
mkdir -p .cursor/skills
cp -r skills/* .cursor/skills/
cp -r .claude/skills/y-score-readiness .cursor/skills/
cp -r .claude/skills/prd-to-sdlc .cursor/skills/
```

Alternatively, symlink for live updates during development:

```bash
ln -s ../../skills/productowner-skill .cursor/skills/productowner-skill
```

Or use the sync helper (recommended for teams):

```bash
npm run sync-skills
```

This idempotently copies all `skills/*` directories into `.cursor/skills/`.

### Claude Code

Copy skills into the Claude skills directory:

```bash
mkdir -p .claude/skills
cp -r skills/* .claude/skills/
```

The `y-score-readiness` and `prd-to-sdlc` skills ship pre-installed under `.claude/skills/` in this repository.

### Antigravity / other agents

Point your agent's skill loader at the repository `skills/` directory. Consult your agent's documentation for the equivalent config path.

---

## Team onboarding

After cloning the repository, sync canonical skills from `skills/` into the Cursor agent path:

```bash
npm run sync-skills
```

This runs `scripts/sync-skills.mjs`, which copies every skill directory to `.cursor/skills/` (idempotent — safe to re-run after pulling updates).

**When to sync:**
- First clone or new team member setup
- After editing skills under `skills/` (source of truth)
- Before opening a PR that changes skill definitions

**Source of truth:** `skills/` — always edit there, then run `npm run sync-skills` to mirror to `.cursor/skills/`.

For Claude Code, copy manually or symlink as shown in Step 1 above.

---

## Step 2 — Create local memory from template

Every skill reads `.agent/memory.md` first. Create it in **your target repository** (not just the plugin source repo):

```bash
mkdir -p .agent artifacts
cp /path/to/product-management/.agent/memory.md .agent/memory.md
```

Edit the YAML sections for your product:

| Section | What to customise |
|---------|-------------------|
| `product_name` | Your product name, version, tagline |
| `domain` | `bfsi`, `healthcare`, or `generic` |
| `target_users` | Personas and jobs-to-be-done for your product |
| `compliance_regimes` | Applicable regulations (HIPAA, PCI-DSS, GDPR, etc.) |
| `constraints` | Technical, operational, and data constraints |
| `integrations` | Planned and current tool integrations |
| `design_tokens` | Colours, fonts, spacing for UX skill enforcement |
| `glossary` | Domain-specific terms your team uses |

Ensure the `artifacts/` directory exists for generated outputs:

```bash
touch artifacts/.gitkeep
```

---

## Step 3 — Verify installation

### 3a. List available skills

Ask your agent:

> List the productowner-skill plugins available in this repository.

Expected skills:

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

### 3b. Run a sample trigger

Test the memory contract and KB search:

> Search KB for prior PRD templates in this repository.

The agent should:
1. Read `.agent/memory.md`
2. Search `artifacts/`, `prds/`, and `skills/*/templates/`
3. Return a ranked list with reuse recommendations

Test the Y-Score gate:

> Score prds/00-pm-os-platform.md against Y-Score readiness.

### 3c. Confirm security posture

Verify no executables were introduced:

```bash
node scripts/check-source.mjs
```

Expected: pass with zero banned file types in `skills/`.

---

## Step 4 — First session workflow

Recommended first run in a new repository:

1. **Fill in** `.agent/memory.md` for your product.
2. **Search KB:** "find prior artifact for [your domain]"
3. **Run discovery:** "Act as Product Owner — run discovery for [problem statement]"
4. **Run delivery:** "Write a PRD with Gherkin acceptance criteria"
5. **Run pipeline:** "run the pipeline from this PRD"

All outputs land in `artifacts/` with the tagging schema: `domain · stage · type · compliance-regime`.

---

## Directory layout after install

```text
your-repo/
├── .agent/
│   └── memory.md              # Repo-specific context (required)
├── .cursor/skills/            # Cursor agent skills
│   ├── productowner-skill/
│   ├── PO-discovery/
│   ├── PO-delivery/
│   ├── PO-kb-research/
│   ├── PO-code-pipeline/
│   ├── cybersec-skill/
│   ├── ux-pro-skill/
│   ├── qa-tester-skill/
│   └── y-score-readiness/
├── artifacts/                 # Generated outputs
│   └── .gitkeep
├── prds/                      # Your PRDs (optional)
└── docs/                      # Your documentation (optional)
```

---

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Agent does not recognise skills | Confirm skills are in `.cursor/skills/` or `.claude/skills/` and restart the agent session |
| Skills generate generic output | Ensure `.agent/memory.md` exists and is populated for your product |
| "Skill not found" for sub-skills | Copy all skills from Step 1 — the pipeline delegates across multiple skills |
| Security gate blocks output | Review `cybersec-skill` findings; replace any real PII/PHI with synthetic data |
| KB search returns empty | Normal on a fresh repo — `prds/` and `artifacts/` populate over time |

---

## What is NOT required

- Docker or container runtime
- API keys (OpenAI, Anthropic, Atlassian, Microsoft, Google)
- OAuth or enterprise SSO
- Database or backend server
- Network access from skills (local filesystem only in Phase 1)

---

## Next steps

| Goal | Action |
|------|--------|
| Run full SDLC | Trigger `PO-code-pipeline` with a PRD |
| Portfolio demo | Deploy `docs/` to GitHub Pages (see `.github/workflows/pages.yml`) |
| Enterprise KB search | Deferred to Phase 2 — Atlassian Rovo, M365 Graph, Google Workspace API |
| Autonomous codegen | Deferred to Phase 5 — MetaGPT, OpenHands, Promptfoo |

---

**Author:** Vignesh AIPM · [product-management](https://github.com/vignesh-s7/product-management)
