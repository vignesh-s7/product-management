# PIF — Session Handoff (2026-08-13)

Written at repo root, not inside `portable-mvp/` or `five-file-structure/`, so neither bundle's file-count invariant breaks.

## State

- No code changed this session. Read-only investigation only.
- Working folder: `portable-mvp/` (13-file local baseline). Sibling `five-file-structure/` is a separate 5-file transfer bundle, untouched.
- Ownership: Claude owns `index.html`. Codex owns `layer_a.py`, `test_layer_a.py`, `layer_a_config.json`, docs.
- Preview server: port 8081, mtime hot-reload on `index.html`.

## Scope decision (settled)

`PIF_MASTER_SPEC.md` v1.0, 98 sections, **frozen**. No new scope.

`portable-mvp/` is the generic distillation of ~30-50 prior prototype repos with domain specifics stripped. Size is deliberate, not bloat.

PIF's job: replace the humans who write the PRD / BRD / architecture / UI / story `.md` files that already feed the working agent pipeline. Nothing more.

**Export is the payoff.** It must emit the exact `.md` files that pipeline already consumes: detailed PRD, research in PA-skill format, user story + AC. Exact contents NDA-blocked — needs targeted questions, not guesses.

## Verified against spec (do NOT "fix")

- `index.html` 13 screens == spec §17.
- `appState` shape == spec §40.
- `askPIFAI()` mocked == spec §42 prescribes it. Not a defect. I wrongly called it one; retracted.

## Open items

1. **Simplified UI plan — requested, not delivered.** Constraint given: must-have = spec §17 (Overview + 01 Problem … 14 Export), §16 main nav, §34 three-pane layout, as written. Everything I proposed (5 archetypes, Proof/Control/Grounding regroup, platform/product split, storage tiers, harness/instantiation) → **Phase 2**. Minimal rework.
2. **Screen 07 "AI-Native Business Primitives"** — group the 8 primitive cards properly; move non-essential content into an "others" section. Target node: `<main id="main-workspace">`.
3. **Spec conflict, undecided.** §43/§62/§66 require FastAPI + PostgreSQL + server-side AI provider (NVIDIA/Gemini). Repo is stdlib-only, SQLite, no network. Until resolved, `askPIFAI` stays mocked forever and §94's success hypothesis cannot be tested.
4. **Repo not under git.** Two agents editing one tree, no rollback. Highest bug-cost risk. Recommend git init before further edits.
5. **Codex B1 specced, not handed over:** five thin routes over already-validated engines that currently have no HTTP route —
   | Engine | Line in `layer_a.py` | Gate |
   |---|---|---|
   | `inspect_agent` | 5087 | 1 |
   | `run_evaluation_suite` | 5362 | 9 |
   | `evaluate` | 5207 | 11 |
   | `diagnose` | 5418 | 12 |
   | `compare_agent_reports` | 5296 | 14 |

   Proposed routes: `/api/agent/inspect|evaluate|fit|gaps|compare`. Add to allowlist at 7257-7258, elif chain from ~7302. Note `/api/compare` is already taken by Part B's `compare_e` (6696) — do not collide.

   B2-B5 (platform state, templates, inheritance-delta, honest readiness) **on hold** — overengineering.

## Working agreements

- No new subsystems beyond frozen spec. Check spec before calling code a defect.
- Fewer tool calls, lower complexity, bug-averse.
- Never open external Chrome/Playwright for UI review. No saved screenshots. Embedded editor browser only.
- Personal/career background shared by user is PII — not stored anywhere.

## Resume commands

```bash
cd /Users/subramanianvittobh/Layer-A-Product-Task/portable-mvp
python3 layer_a.py validate
python3 -W error::ResourceWarning -m unittest -v
python3 layer_a.py serve
```
