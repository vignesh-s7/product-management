# Sprint Memory — Trustworthy Plugin Foundation (Top 1%)

> **Read before any agent run.** Captures current sprint context, decisions, execution plan, and pre-run state.
> **Last updated:** 2026-08-01
> **Sprint name:** P0 Trust + First-Access
> **Branch:** `cursor/phase1-brainstorm-5-personas-fcfe`
> **PR:** #2

---

## Sprint goal

Fix trust contradictions and deliver **first-access experience** so a user who clones this repo gets top 1% outcomes — launch-ready PO artifacts — with **zero backend, zero OAuth, zero execution files** in the plugin path.

**Tagline:** *Outcomes users want. Skills that deliver. Zero scripts. Zero telemetry.*

---

## Strategic position (6-persona consensus)

| We compete on | We do NOT compete on |
|---------------|----------------------|
| Regulated PO outcomes | GitHub stars / autonomous codegen |
| Persona swarm gates (PO → cybersec → UX → QA) | Docker / Python orchestration |
| Markdown-only plugin (`SKILL.md`) | MCP servers in core plugin |
| InfoSec approves in 1 review | Feature parity with OpenHands/MetaGPT |

**Competitors:** OpenHands (~80k), MetaGPT (~70k), GPT-Engineer (~55k), ChatDev (~25k), SuperAGI (~18k), generic Cursor skills (often with `scripts/`).

**Our moat:** Only solution combining regulated PO depth + persona gates + zero-execution plugin.

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
6. **Plugin ≠ demo site** — document both entry paths clearly

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
