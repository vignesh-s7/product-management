# Backlog Memory — 6-Persona Master Task List

> **Persistent backlog** for Trustworthy Plugin Foundation → Top 1% in regulated PO plugin space.
> **Last updated:** 2026-08-01 (revised — dual end-user model: humans + client-side AI agents)
> **Sprint filter:** P0 = current sprint (see `.agent/sprint-memory.md`)

---

## Backlog status legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Done |
| 🔲 | To do |
| ⏭️ | Deferred to later phase |
| 🟡 | Stretch / P2 |

---

## Product model (backlog scope)

**We provide skills. Client-side AI agents execute everything. No runtime connection to us.**

| End user | Role |
|----------|------|
| **Human users** | POs, leads, designers, engineers, InfoSec — set intent, review gates, approve POC/MVP |
| **Client-side AI agents** | Cursor, Claude Code, Antigravity — read skills + memory, run persona swarm, write artifacts, build POC/MVP locally |

**Vendor boundary:** Copy skills once → client agent runs forever in client's repo. No OAuth, no API, no telemetry, no data to us.

---

## P0 — Trust contradictions + first access (CURRENT SPRINT)

| ID | Task | Persona | Status | Notes |
|----|------|---------|--------|-------|
| B-001 | Fix `prd-pipeline.yml` — remove `orchestrate.sh`, use declarative Y-Score only | Engineering | 🔲 | Trust killer |
| B-002 | Remove `orchestrate.sh` refs from `AI_USE_CASES.md` | Security | 🔲 | |
| B-003 | Create `TRUST.md` — file inventory, what executes vs not | Architect | 🔲 | |
| B-004 | Expand `SECURITY.md` — zero retention, no profiling, no network, no exec | Security | 🔲 | |
| B-005 | Mirror `skills/*` → `.cursor/skills/` in repo | Architect | 🔲 | Instant plugin access |
| B-006 | Rewrite README — plugin-first, outcomes-first | PO + Business | 🔲 | |
| B-007 | Fix `docs/INSTALL.md` repo URLs | Business | 🔲 | |
| B-008 | CI: fail if `.sh` added under `skills/` or `.cursor/skills/` | Engineering | 🔲 | Extend check-source.mjs |
| B-049 | Document dual end-user model (humans + client agents) in README + TRUST.md | PO + Architect | 🔲 | Core positioning |
| B-050 | Create `docs/CLIENT-AGENT.md` — vendor boundary, what agent does, what we never do | Architect | 🔲 | |
| B-051 | Update B-006 README scope — skills-for-agents, not "use our platform" | PO + Business | 🔲 | Replaces generic plugin-first |

---

## P1 — Top 1% outcomes + proof

| ID | Task | Persona | Status | Notes |
|----|------|---------|--------|-------|
| B-009 | `examples/golden-run/` — human intent → client agent → POC/MVP + gate JSONs | PO | 🔲 | Proves dual-user flow |
| B-010 | JSON schemas for gate outputs (cybersec, ux, qa, y-score) | Engineering | 🔲 | |
| B-011 | `QUICKSTART.md` — 3 steps: open repo → memory → trigger PO | Architect | 🔲 | |
| B-012 | Trust badge on `docs/index.html` | UX | 🔲 | |
| B-013 | Landing "Skills for your agent" + "Portfolio demo" — two paths, no confusion | UX | 🔲 | Was "Plugin vs Demo" |
| B-014 | Update `CASE_STUDY.md` — zero-exec plugin narrative | Business | 🔲 | |
| B-015 | InfoSec one-pager — "approved in 1 review" | Business | 🔲 | |
| B-016 | Auto-invoke Y-Score on every PRD write in productowner-skill | PO | 🔲 | |
| B-017 | `disable-model-invocation: true` on cybersec-skill | Security | 🔲 | |
| B-018 | CI badge "zero-execution verified" in README | Security | 🔲 | |
| B-019 | BFSI walkthrough example session | PO | 🔲 | |
| B-020 | Healthcare walkthrough example session | PO | 🔲 | |
| B-021 | IDE compatibility matrix in INSTALL | Architect | 🔲 | Cursor / Claude / Antigravity |

---

## P2 — Polish + distribution

| ID | Task | Persona | Status | Notes |
|----|------|---------|--------|-------|
| B-022 | Signed GitHub releases + SHA256 checksums | Security | 🟡 | |
| B-023 | Submit to skills directories (agentskills.io, top-agent-skills) | Business | 🟡 | |
| B-024 | Story Slicing (Epic → Stories) in PO-delivery | PO | 🟡 | |
| B-025 | DoR Gate — analytics tracking enforcement | PO | 🟡 | |
| B-026 | GitHub Actions Y-Score validation on PRD PRs | Engineering | 🟡 | |
| B-027 | Eval harness — "did skill read memory?" assertions | Engineering | 🟡 | |
| B-028 | Micro-interactions on onboarding wizard | UX | 🟡 | |
| B-029 | `docs/quickstart` CTA page | UX | 🟡 | |
| B-030 | `paths` frontmatter on skills for monorepo scoping | Architect | 🟡 | |
| B-031 | Symlink/copy helper in INSTALL for team onboarding | Architect | 🟡 | |
| B-032 | Design tokens enforced on all `docs/` pages | UX | 🟡 | |
| B-033 | Consistent focus-visible across all demo pages | UX | 🟡 | |
| B-034 | GitHub topics + repo description aligned to plugin niche | Business | 🟡 | |
| B-035 | Dependency Risk Assessor (cybersec ultra) — doc only | Security | 🟡 | |

---

## P3 — Deferred (Phase 2+)

| ID | Task | Phase | Persona |
|----|------|-------|---------|
| B-036 | Atlassian Rovo KB search | Phase 2 | PO |
| B-037 | Microsoft 365 Graph search | Phase 2 | PO |
| B-038 | Google Workspace API search | Phase 2 | PO |
| B-039 | Unified federated search UI | Phase 2 | Architect |
| B-040 | PowerBI / Looker embed | Phase 2 | PO |
| B-041 | Optional read-only MCP as separate package | Phase 2 | Architect |
| B-042 | AI chat tier (Rovo + Claude + Gemini) | Phase 3 | PO |
| B-043 | Client Workspace tenant isolation | Phase 4 | Business |
| B-044 | MetaGPT / OpenHands / Promptfoo live pipeline | Phase 5 | Engineering |
| B-045 | Billing + white-label SaaS | Phase 6 | Business |
| B-046 | Zero-Trust AuthZ reviewer (cybersec) | Phase 2 | Security |
| B-047 | Native mobile app | Phase 6 | UX |
| B-048 | API for third-party integrations | Phase 6 | Architect |

---

## Completed (Phase 1 core — do not rebuild)

| ID | Task | Completed |
|----|------|-----------|
| B-DONE-01 | `.agent/memory.md` local memory standard | 2026-08-01 |
| B-DONE-02 | `skills/productowner-skill/SKILL.md` upgraded | 2026-08-01 |
| B-DONE-03 | `skills/PO-discovery/SKILL.md` | 2026-08-01 |
| B-DONE-04 | `skills/PO-delivery/SKILL.md` | 2026-08-01 |
| B-DONE-05 | `skills/PO-kb-research/SKILL.md` | 2026-08-01 |
| B-DONE-06 | `skills/PO-code-pipeline/SKILL.md` | 2026-08-01 |
| B-DONE-07 | `skills/cybersec-skill/SKILL.md` | 2026-08-01 |
| B-DONE-08 | `skills/qa-tester-skill/SKILL.md` | 2026-08-01 |
| B-DONE-09 | `skills/ux-pro-skill/SKILL.md` | 2026-08-01 |
| B-DONE-10 | 6 templates under `skills/*/templates/` | 2026-08-01 |
| B-DONE-11 | `docs/INSTALL.md` | 2026-08-01 |
| B-DONE-12 | CI skill validation in `check-source.mjs` | 2026-08-01 |
| B-DONE-13 | Portfolio UX pass on onboarding + landing (partial) | 2026-08-01 |
| B-DONE-14 | `planning/phase1_brainstorm_5_personas.md` | 2026-08-01 |
| B-DONE-15 | ROADMAP Phase 1 revised | 2026-08-01 |
| B-DONE-16 | Playwright 7/7 tests passing | 2026-08-01 |

---

## Per-persona task ownership (full backlog)

### Persona 1 — Technical Architect
B-003, B-005, B-011, B-021, B-030, B-031, B-039, B-041, B-048

### Persona 2 — Product Owner
B-006, B-009, B-016, B-019, B-020, B-024, B-025, B-036–B-038, B-040, B-042

### Persona 3 — Business Strategist
B-006, B-007, B-014, B-015, B-023, B-034, B-043, B-045

### Persona 4 — Cybersecurity
B-002, B-004, B-017, B-018, B-022, B-035, B-046

### Persona 5 — Engineering Lead
B-001, B-008, B-010, B-026, B-027, B-044

### Persona 6 — UX/UI Designer
B-012, B-013, B-028, B-029, B-032, B-033, B-047

---

## User outcomes mapped to backlog (dual end-user model)

| Outcome | Who benefits | Backlog IDs |
|---------|--------------|-------------|
| "My agent built a full POC/MVP from skills alone" | Human + Client agent | B-009, B-049, B-050, B-051 |
| "Installed skills in 5 min, no account with vendor" | Human + Admin | B-005, B-007, B-011, B-021 |
| "InfoSec approved — no data leaves our perimeter" | Human + InfoSec | B-003, B-004, B-015, B-017, B-018, B-050 |
| "Agent produced discovery pack in one session" | Client agent | B-009, B-019, B-020 |
| "PRD with gates ready for engineering" | Human PO | B-016, B-009, B-010 |
| "Agent never called vendor APIs" | Client agent | B-001–B-004, B-008, B-050 |
| "Accessible demo explains skills model" | Human | B-012, B-013, B-032, B-033 |

---

## Agent run checklist (read before starting)

1. Read `.agent/memory.md` — repo context
2. Read `.agent/sprint-memory.md` — current sprint scope
3. Read `.agent/backlog-memory.md` — task IDs and status
4. Pick session (A/B/C/D) and task IDs only — no scope creep
5. Run `npm run check` + `npx playwright test` before commit
6. Update backlog status (🔲 → ✅) in this file after each task
7. Update sprint-memory exit criteria when P0 complete

---

**Author:** Vignesh AIPM · persistent backlog for agent continuity
