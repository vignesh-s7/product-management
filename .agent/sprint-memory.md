# Sprint Memory — Trustworthy Plugin Foundation (Top 1%)

> **Read before any agent run.** Captures current sprint context, decisions, execution plan, and pre-run state.
> **Last updated:** 2026-08-01 (revised — dual end-user model)
> **Sprint status:** P0 COMPLETE (2026-08-01)
> **Branch:** `cursor/phase1-brainstorm-5-personas-fcfe`
> **PR:** #2

---

## Product model (revised — read before any agent run)

**We are a skills library. Client-side AI agents do everything. No runtime connection to us.**

| | Us (vendor) | Client |
|--|-------------|--------|
| **Provides** | `SKILL.md` plugins, templates, memory schema, install docs | Their repo, their IDE agent, their model |
| **Executes** | Nothing at runtime | Full POC/MVP — discovery → PRD → gates → artifacts |
| **Connects to us** | Never at runtime | Copy skills once; no API, no OAuth, no account |
| **End users** | N/A — we don't have users at runtime | **Humans (POs)** + **Client AI agents** |

```
Human (PO) ──intent──► Client AI Agent (Cursor / Claude / Antigravity)
                              │
                              ├── reads skills/ (copied from our repo)
                              ├── reads .agent/memory.md (client repo)
                              ├── persona swarm gates (local)
                              └── POC/MVP artifacts in client repo

Our repo ──skills only──► copied once ──X── no runtime link
```

**Outcome we enable:** Complete product POC/MVP built entirely by the client's AI agent using our skills — not through us, not directly with us.

---

## Sprint goal

Fix trust contradictions and deliver **first-access experience** so a human + their **client-side AI agent** can clone skills and produce a complete POC/MVP — with **zero backend, zero OAuth, zero execution files, zero runtime connection to us**.

**Tagline:** *Outcomes users want. Skills that deliver. Zero scripts. Zero telemetry.*

---

## Strategic position (6-persona consensus)

| We compete on | We do NOT compete on |
|---------------|----------------------|
| Skills for client agents to build POC/MVP locally | Hosted platforms / SaaS PO tools |
| Regulated PO outcomes via persona gates | GitHub stars / autonomous codegen |
| Markdown-only plugin (`SKILL.md`) — agent is runtime | Docker / Python orchestration on our side |
| InfoSec approves in 1 review (no vendor data flow) | MCP servers / APIs that call us |
| Dual end-user: humans + client AI agents | "Users log into our product" |

**Competitors:** OpenHands (~80k), MetaGPT (~70k), GPT-Engineer (~55k), ChatDev (~25k), SuperAGI (~18k), generic Cursor skills (often with `scripts/`).

**Our moat:** Only skills library where client AI agents build regulated POC/MVP end-to-end locally — no vendor runtime, no data egress to us.

---

## Phase 1 completion status (before this sprint)

| Deliverable | Status |
|-------------|--------|
| `.agent/memory.md` | ✅ Done |
| All 8 persona skills (`skills/`) | ✅ Done |
| 6 templates (`skills/*/templates/`) | ✅ Done |
| `docs/INSTALL.md` | ✅ Done |
| CI skill validation (`check-source.mjs`) | ✅ Done |
| Portfolio UX pass (onboarding + landing partial) | ✅ Done |
| Playwright tests | ✅ 7/7 pass |
| Trust badge on landing | 🔲 Pending |
| README plugin-first rewrite | 🔲 Pending |
| `TRUST.md` | 🔲 Pending |
| Trust contradictions fixed | 🔲 Pending |

---

## Revised P0 tasks (includes dual end-user docs)

| # | Task | Owner | Status |
|---|------|-------|--------|
| 1–8 | *(unchanged — trust + first access)* | — | 🔲 |
| 9 | Document dual end-user model in README + TRUST.md | PO + Architect | 🔲 |
| 10 | Add `docs/CLIENT-AGENT.md` — what client agent does, vendor boundary | Architect | 🔲 |
| 11 | Golden-run: human intent → client agent → full POC/MVP path | PO | 🔲 |

---

## Current sprint — P0 tasks (must complete before P1)

| # | Task | Owner persona | Status |
|---|------|---------------|--------|
| 1 | Fix `prd-pipeline.yml` — remove `orchestrate.sh` | Engineering | 🔲 |
| 2 | Remove `orchestrate.sh` refs from `AI_USE_CASES.md` | Security | 🔲 |
| 3 | Create `TRUST.md` — file inventory, zero-exec proof | Architect | 🔲 |
| 4 | Expand `SECURITY.md` — full trust handshake | Security | 🔲 |
| 5 | Mirror `skills/*` → `.cursor/skills/` | Architect | 🔲 |
| 6 | Rewrite README — plugin-first, outcomes-first | PO + Business | 🔲 |
| 7 | Fix `INSTALL.md` repo URLs | Business | 🔲 |
| 8 | CI: fail on `.sh` in `skills/` or `.cursor/skills/` | Engineering | 🔲 |

**Sprint exit criteria:**
- [ ] No `orchestrate.sh` references in active code/docs/workflows
- [ ] `TRUST.md` + expanded `SECURITY.md` exist
- [ ] Skills usable immediately from `.cursor/skills/` on clone
- [ ] README leads with plugin, not enterprise APIs
- [ ] `npm run check` passes
- [ ] Playwright 7/7 pass

---

## Agent execution plan (pre-run — do NOT start until backlog saved)

### Session A — Security + Engineering
**Agent scope:** Tasks #1, #2, #4, #8, #10 (partial)
- Fix `prd-pipeline.yml` → declarative Y-Score validation only
- Clean `AI_USE_CASES.md` stale refs
- Expand `SECURITY.md`
- Extend `check-source.mjs` for workflow `.sh` scan in plugin paths

### Session B — Architect + Business
**Agent scope:** Tasks #3, #5, #7, #11, #20
- Create `TRUST.md`
- Mirror skills to `.cursor/skills/`
- Fix INSTALL URLs
- Add `QUICKSTART.md`
- IDE compatibility matrix

### Session C — PO + UX
**Agent scope:** Tasks #6, #9, #12, #13, #16, #19
- Rewrite README plugin-first
- `examples/golden-run/` with gate JSONs
- Trust badge + Plugin vs Demo on landing
- Y-Score auto-invoke note in productowner-skill
- BFSI/healthcare walkthrough stubs

### Session D — Business + Security (after P0)
**Agent scope:** Tasks #14, #15, #17, #18, #21
- CASE_STUDY update
- InfoSec one-pager
- cybersec `disable-model-invocation`
- CI badge in README
- Signed releases (P1)

**Run order:** A + B + C in parallel → verify → D

---

## Persona swarm gate (unchanged)

```
User request
  → productowner-skill (read .agent/memory.md first)
  → cybersec-skill (BLOCK on PII/OWASP)
  → ux-pro-skill (BLOCK critical a11y; WARN style)
  → qa-tester-skill (WARN edge-case gaps)
  → y-score-readiness (BLOCK if < 70 for launch)
  → release to artifacts/
```

---

## Key decisions (do not reverse without 6-persona re-brainstorm)

1. **No executables** in `skills/` or `.cursor/skills/` — ever
2. **No OAuth/backend** in Phase 1 plugin path
3. **Enterprise KB APIs** deferred to Phase 2
4. **Codegen loops** (MetaGPT/OpenHands) deferred to Phase 5 — separate repo if ever
5. **Scope by user outcomes**, not feature count
6. **Plugin ≠ demo site** — demo is illustration; real work = client agent + skills
7. **Dual end users** — humans set intent; client-side AI agents execute everything
8. **No runtime vendor relationship** — skills copied once; never phone home
9. **POC/MVP is the outcome** — not "using our platform" but "agent built it locally"

---

## Known trust contradictions (fix in this sprint)

| File | Issue |
|------|-------|
| `.github/workflows/prd-pipeline.yml` | Calls missing `./orchestrate.sh` |
| `AI_USE_CASES.md` | References `orchestrate.sh` stubs |
| `README.md` | Stale — no skills, no install, enterprise-first |
| `SECURITY.md` | Too thin for InfoSec sign-off |
| `docs/INSTALL.md` | Wrong repo URL (`vvs-PO` vs actual) |
| Skills in `skills/` only | User must manually copy to `.cursor/skills/` |

---

## References

- Brainstorm: `planning/phase1_brainstorm_5_personas.md`
- Backlog: `.agent/backlog-memory.md`
- Repo context: `.agent/memory.md`
- Roadmap: `ROADMAP.md`
- Install: `docs/INSTALL.md`

---

**Author:** Vignesh AIPM · saved before P0 agent run
