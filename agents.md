# Layer A + Part B — Five-File Transfer Bundle

Authoritative contract for this folder. Designed for copying into any approved local or Git workspace, then splitting later with agents. Parent `portable-mvp/` remains untouched reference baseline.

## Cursor resume memory — 2026-08-13

Read this complete file before editing. Continue only in `/Users/subramanianvittobh/Layer-A-Product-Task/five-file-structure`. This folder is active transfer bundle; sibling `portable-mvp/` is retained thirteen-file baseline and was not changed by five-file/UI work.

Current checkpoint:

- Bundle contains exactly five source files: `AGENTS.md`, `layer_a.py`, `layer_a_config.json`, `index.html`, and `test_layer_a.py`. Do not add files before transfer.
- Latest executable evidence: `python3 layer_a.py validate` → `PASS`, `5/5`; `python3 -W error::ResourceWarning -m unittest -v` → `60/60 OK`; JavaScript syntax and Python compile checks pass.
- Part A remains honestly `INCOMPLETE`: 18 gates `VALIDATED`; Gate 18 `EXTERNAL_SIGN_OFF`. Part B remains 8/8 `VALIDATED_POC`. Plugin remains `UNSIGNED`.
- UI was reshaped in `index.html` using Anthropic `frontend-design` guidance plus clean-room structural ideas from Figma Sidebar Navigation Starter Kit and Dmitry Sergushkin's sidebar-navigation case study. No external component source, package, CDN, font, icon, image, or executable code was imported.
- Active UI direction: evidence-first product workspace; light neutral canvas; ink text; blue actions; green evidence state; flat cards; restrained density; serif display headings; system sans body; monospace utility labels.
- Sidebar direction: 248px expanded rail, 60px collapsed rail, grouped `Understand` / `Decide` / `Advanced` items, visible active state, completion marks, mobile drawer, quiet background, local/mock status in footer.
- Fixed defects: stale legacy route normalized to `pb_portfolio`; legacy AI panel hidden; duplicate top-bar Readiness/Copilot actions removed; desktop collapse grid fixed; collapsed labels hidden; desktop sidebar close button fixed; mobile backdrop stacking fixed (`#sidebar-backdrop` below `#left-sidebar`) so transparent overlay no longer steals sidebar clicks.
- Normal navigation exposes Part B experiences plus Plugin and Compare. Large legacy PIF Engine rendering code still exists dormant/unreachable inside `index.html`; remove only through behavior-preserving refactor with tests.
- User reports UI had many issues. Latest sidebar click defect is fixed in code, but visual acceptance is not claimed. Continue with user-observed issues one at a time and verify in Cursor/VS Code embedded preview.
- Never open external Chrome/Playwright for UI review. Never create or save screenshots/images. User reviews through embedded editor browser only.
- Before serving, confirm port 8080 is serving this folder, not sibling baseline. Expected page title: `PIF — Evidence Workspace`; visible brand: `PIF Evidence`.

Resume commands:

```bash
cd /Users/subramanianvittobh/Layer-A-Product-Task/five-file-structure
python3 layer_a.py validate
python3 -W error::ResourceWarning -m unittest -v
python3 layer_a.py serve
```

Design references (reference only; do not download or execute):

- `https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md`
- `https://www.figma.com/community/file/1090687088484431239/sidebar-navigation-starter-kit`
- `https://www.dmitrysergushkin.com/blog/case-study-research-sidebar-navigation`

## Goal

Preserve runnable local deterministic POC in exactly five source files:

1. `AGENTS.md` — transfer contract, usage, security, limitations.
2. `layer_a.py` — runtime, APIs, validators, embedded-resource export.
3. `layer_a_config.json` — all contracts/config plus embedded plugin, MCP, and Product Discovery skill resources.
4. `index.html` — dependency-free same-origin frontend.
5. `test_layer_a.py` — executable evidence.

Generated local state, caches, Git metadata, and later unpacked resources are not part of five-file transfer bundle.

## Commands

```bash
python3 layer_a.py validate
python3 -W error::ResourceWarning -m unittest -v
python3 -m py_compile layer_a.py test_layer_a.py
python3 layer_a.py serve
```

Review URL: `http://127.0.0.1:8080/`.

## Expand after transfer

Embedded plugin resources stay inspectable as JSON/text inside `layer_a_config.json`. Export into separate folder without overwrite:

```bash
python3 layer_a.py unpack --unpack-dir ./expanded-resources
```

Writes only:

- `plugin.json`
- `mcp.json`
- `skills/product-discovery/SKILL.md`

Command refuses existing targets and refuses writing into five-file bundle. Agents may later split documentation, configuration, runtime modules, frontend assets, tests, Docker files, or CI files inside destination Git repository after explicit scope approval.

## Current truth

- Python standard library only.
- Localhost-only server and same-origin `/api/*` frontend calls.
- Deterministic mocked/redacted research and model behavior; no real LLM or live research.
- First-party SQLite state under generated `.layer-a-state/`.
- Part A: 18 validated gates; Gate 18 remains `EXTERNAL_SIGN_OFF`; overall `INCOMPLETE`.
- Part B: 8/8 experiences `VALIDATED_POC`.
- Embedded Agent Plugin remains `UNSIGNED`; exact local approval still required.
- Five physical transfer files plus three embedded/exportable plugin artifacts.

## Security boundary

- No network, downloads, installs, remote Git/API operations, browser automation, credentials, or private enterprise data.
- Never execute pasted, downloaded, or unknown code.
- Never store secrets, tokens, passwords, private keys, customer data, account numbers, or card numbers.
- External providers, adapters, live research, remote MCP/A2A, authentication, hosting, and cloud persistence remain disabled.
- SQLite is local POC persistence, not encrypted enterprise storage.
- Signatures, popularity, publisher identity, and local tests do not prove safety or production readiness.
- Remote action, dependency install, destructive action, credential use, or production connection needs explicit action-specific approval.

## Frontend contract

- Keep `index.html` separate for direct UI editing.
- Vanilla HTML/CSS/JavaScript only; no CDN, npm, framework, remote font, image, icon, analytics, or absolute runtime URL.
- Requests stay relative same-origin `/api/*`.
- Treat API/user text as untrusted. Prefer `textContent`; escape fixed-template interpolation.
- Preserve keyboard focus, semantic labels, request/error/empty/blocked states, reduced motion, and 320/768/1024/1440 layouts.
- Product-user view hides manifests, MCP, task packets, trust internals, and storage JSON unless advanced/admin detail is deliberately opened.
- No browser automation or saved screenshots/images for review. User views UI through VS Code Simple Browser.

## Ownership and migration

- Five-file folder is independent alternative, not replacement for parent baseline.
- Never edit parent `portable-mvp/` while working here unless user explicitly asks.
- Preserve behavior before structural splitting. Use expand → migrate → verify → contract.
- Do not delete embedded resources until exported equivalents validate and callers use new paths.
- No additional permanent file in this folder without explicit scope change.

## Validation gate

Change is complete only when:

- `python3 layer_a.py validate` reports `PASS`, expected/actual `5`;
- full unit suite passes;
- Python compile passes;
- frontend remote-dependency scan returns no matches;
- unpack test proves three resources export without overwrite;
- parent five authoritative source hashes remain unchanged.

## Honest limitations

No production SSO/RBAC, secret store, encrypted database, remote models, live market/news/legal research, hostile-code containment, distributed workers, cloud hosting, remote plugin installation, verified signatures, enterprise approval, or deployment certification.
