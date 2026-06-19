---
name: prd-to-sdlc
description: Convert a one-page PRD into a full SDLC artifact set — architecture, DB schema, code skeleton, eval harness, and deploy config — by routing through MetaGPT / OpenHands / Promptfoo with PM-grade guardrails baked in (Y-Score readiness, regulated-AI checks, anti-hallucination patterns).
---

# prd-to-sdlc

A reusable Claude Skill that takes a PRD and produces a deployable SDLC bundle.

## When to trigger
- User says "turn this PRD into a project"
- User says "scaffold the repo for [PRD path]"
- User invokes `/prd-to-sdlc <prd.md>`
- A new file lands in `prds/` on the `pm-os` repo

## Inputs
| Field | Required | Notes |
|---|---|---|
| `prd_path` | ✅ | Markdown PRD with at minimum: problem, users, success metrics, constraints |
| `domain` | optional | `bfsi` / `healthcare` / `devtools` / `generic` — toggles compliance guardrails |
| `deploy` | optional | `cloudflare-pages` (default), `none` |

## Stages

### 1. PM gate — Y-Score readiness
Score the PRD against 7 dimensions: problem clarity, target user, success metric, constraints, compliance, eval plan, rollback. Block if score < 70%. *See `.claude/skills/y-score-readiness/`.*

### 2. Architect
Invoke MetaGPT with PRD → emit `architecture.md` (Mermaid C4) + `db/schema.sql` + `api/openapi.yaml`.

### 3. Designer
Invoke v0 / Onlook with the user-facing flows from PRD → emit `ui/` (React + Tailwind).

### 4. Engineer
Invoke OpenHands with the spec bundle → emit `code/` (working app), runs tests until green.

### 5. QA
Generate Promptfoo `evals/promptfooconfig.yaml` from PRD success metrics. Generate Playwright smoke tests from UI flows.

### 6. DevOps
Emit `wrangler.toml` + `.github/workflows/deploy.yml`. If `CLOUDFLARE_API_TOKEN` set, deploy.

## Outputs
```
outputs/<slug>/
├── PRD.md
├── architecture.md
├── db/schema.sql
├── api/openapi.yaml
├── ui/
├── code/
├── evals/
├── wrangler.toml
└── README.md            # auto-generated, attribution to pm-os + upstream
```

## Guardrails (always on)
- **Anti-hallucination**: every architecture claim cites the PRD line that justifies it.
- **Compliance-aware**: if `domain ∈ {bfsi, healthcare}`, inject HIPAA/PCI/GDPR/EU-AI-Act checklists into Architect prompt.
- **Eval-first**: refuse to mark SDLC complete without passing Promptfoo eval gate.
- **No client PII**: scan all outputs against a PII regex pack before commit.

## Upstream credits
MetaGPT · OpenHands · Promptfoo · Onlook · Wrangler. See `CREDITS.md`.
