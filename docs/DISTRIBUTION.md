# Skills Directory Submission Guide

How to list **productowner-skill** on public skill directories and improve discoverability on GitHub. Skills are Markdown-only — no executables, no telemetry, no hosted runtime.

---

## Where to submit

| Directory | URL | Notes |
|-----------|-----|-------|
| **Agent Skills** | [agentskills.io](https://agentskills.io) | Primary open registry for `SKILL.md` packages |
| **Top Agent Skills** | [top-agent-skills](https://github.com/topics/top-agent-skills) (GitHub topic + community lists) | Curated lists; tag repo and open a PR to featured collections when available |
| **GitHub Topics** | Repository **Settings → Topics** | Free discoverability; see [GitHub metadata](#github-metadata) below |

---

## Submission checklist

Before submitting to any directory:

- [ ] Each skill has a valid `SKILL.md` with `name`, `description`, and trigger guidance
- [ ] Skills live under `skills/` and are mirrored in `.cursor/skills/` (and `.claude/skills/` where applicable)
- [ ] `QUICKSTART.md` and `docs/INSTALL.md` are up to date
- [ ] `TRUST.md` states Markdown-only, no executables, no telemetry
- [ ] Gate schemas under [`schemas/gates/`](../schemas/gates/) match skill outputs
- [ ] Golden examples under [`examples/golden-run/gates/`](../examples/golden-run/gates/) validate against schemas
- [ ] `LICENSE` and `SECURITY.md` are present
- [ ] Repo description and topics set (see below)
- [ ] Demo pages link to skills path, not a hosted SaaS login

---

## Skill metadata to include

When filling a directory form or `SKILL.md` front matter, include:

| Field | Example / guidance |
|-------|---------------------|
| **Name** | `productowner-skill`, `PO-discovery`, `y-score-readiness` |
| **Description** | One sentence: what the skill does and for whom (POs, regulated domains) |
| **Category** | Product management, discovery, delivery, security gate, compliance |
| **Runtime** | Client-side agent only (Cursor, Claude Code, Antigravity) |
| **Inputs** | `.agent/memory.md`, local repo artifacts |
| **Outputs** | PRDs, backlogs, gate JSON (see schemas), POC/MVP code in `artifacts/` |
| **Compliance** | BFSI, healthcare, EU AI Act — when skill supports regulated workflows |
| **License** | Match repo `LICENSE` |
| **Repository URL** | Canonical GitHub URL |
| **Install path** | `skills/<name>/` → copy to `.cursor/skills/<name>/` |
| **Gate schemas** | Link to [`schemas/gates/`](../schemas/gates/README.md) for `cybersec`, `ux`, `qa`, `y-score` verdicts |

### Gate schema reference

Structured gate outputs must conform to JSON Schema in [`schemas/gates/`](../schemas/gates/):

- `cybersec-gate.schema.json` — `pass` · `block` · `warn`
- `ux-gate.schema.json` — `pass` · `warn` · `block`
- `qa-gate.schema.json` — `pass` · `warn`
- `y-score-gate.schema.json` — `go` · `no-go` with score 0–100

Golden examples: [`examples/golden-run/gates/`](../examples/golden-run/gates/).

---

## agentskills.io submission

1. Fork or prepare the repo with skills under `skills/*/SKILL.md`.
2. Ensure each `SKILL.md` has a clear **When to use** section and **no** shell execution instructions unless documented as user-run.
3. Open a listing PR or use the site’s submit flow (follow current [agentskills.io](https://agentskills.io) docs).
4. Point the listing install command at:

   ```bash
   git clone <repo-url>
   cp -r skills/* .cursor/skills/
   ```

5. Link to `docs/quickstart.html` or `QUICKSTART.md` as the getting-started URL.

---

## GitHub metadata

### Recommended topics

Add these in **Repository → Settings → Topics** (or via `gh repo edit --add-topic`):

- `agent-skills`
- `product-management`
- `cursor-skills`
- `claude-skills`
- `po-tools`
- `regulated-ai`

Optional: `markdown-skills`, `y-score`, `prd`, `discovery`, `bfsi`, `healthcare`.

### Recommended repository description

Copy-paste for the GitHub **Description** field:

```text
Markdown-only PO persona skills for client-side AI agents (Cursor, Claude Code). Discovery, PRD delivery, cybersec/UX/QA gates, Y-Score readiness — no SaaS, no telemetry. Regulated-AI friendly.
```

### About section (website + topics)

- **Website:** link to `docs/quickstart.html` on GitHub Pages or raw `QUICKSTART.md`
- **Topics:** apply the list above
- **README badge:** optional link to agentskills.io once listed

---

## After listing

- Add the directory badge or “Listed on …” line to `README.md` (one line; avoid duplicate marketing blocks).
- Keep `CHANGELOG.md` updated when skills or gate schemas change.
- Re-run `npm run check` before tagging a release intended for directory crawlers.
