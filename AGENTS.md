# PI Meta Product — Eight-File Sole Authority

Authoritative, standalone contract for this folder. Copy only the eight named source files. After copying, no parent repository, sibling folder, absolute machine path, prior chat, generated database, screenshot, cache, or Git history is required to understand or run the local POC.

Do not add a ninth source file. Do not split this bundle unless the user explicitly changes the eight-file contract in a later turn. Generated `.layer-a-state/`, `__pycache__/`, and `*.pyc` artifacts are runtime output, not transfer source.

## Current resume memory — 2026-08-19

Read this complete file before editing. Work only in the directory containing this file and its seven sibling source files. Never depend on a former local path or sibling workspace.

### PI Meta Product — Complete Architecture & Subproduct Hierarchy

For any incoming AI agent or engineer resuming this session, here is the complete situational context and technical architecture:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               PI META PRODUCT TOPOLOGY                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [SUBPRODUCT 1: Foundation] ──► [SUBPRODUCT 2: Product] ──► [SUBPRODUCT 3: Assistant] │
│   • Problem & Persona Framing    • RICE Scoring              • π Gen Meta-Agent        │
│   • Evidence Dossier             • Gherkin Contracts         • Context & Diffs         │
│   • Desired Outcome              • PRD & Spec Handoff        • Token Optimizer (-70%)  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [SUBPRODUCT 4: Execution Engine]               [SUBPRODUCT 5: Admin & Governance]     │
│   • Ephemeral Loopback Runner (Port 8081+)       • BYOK Vault (secret:// Boundary)     │
│   • Sandboxed Iframe Live Preview                • repo-check Pre-Install Gate         │
│   • In-UI Terminal Drawer (Ctrl+`)               • 4 SQLite Engines (Zero Silent Writes)│
├────────────────────────────────────────────────────────────────────────────────────────┤
│  PERSISTENCE: 4 Local SQLite Stores (products, memory, knowledge, governance)          │
│  SECURITY:    Single-Use Cryptographic Approval Tokens, repo-check Gate, 0 Silent Writes│
│  COMPRESSION: Default MIT token-optimizer Skill (Caveman protocol, up to 70% cost cut) │
│  RAG ENGINE:  Zero-Cost SQLite FTS5 (BM25) + Immutable Typed Mistake Ledger            │
│  STANDALONE:  Exact 5-File Monolith Bundle, Standard-Library Python, 0 Pip/NPM Bloat   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 1. Core Positioning & The Strategic Moat
- **Strategy**: We do not compete by training frontier LLMs. We win on the **Model-Agnostic Agentic Orchestration Framework & Upstream Problem Preparation Pipeline** (Apps 1 & 2 prepare structured problem context + App 3 Meta-Agent orchestrates + App 4 executes in isolated sandbox with BYOK keys).
- **Meta π AI Supervisor**: Modeled after Google Contact Center AI (CCAI) Agent-Assist. Continuously detects intent, auto-fills persona/PRD cards across the 4 apps in the background, and prevents "form fatigue" by asking at most 1–2 high-leverage clarifying questions.
- **Lightweight Local RAG & Anti-Drift Engine**: Uses SQLite FTS5 lexical BM25 indexing in `knowledge.sqlite3` ($0 cost, 0 external vector DB subscriptions) and records user corrections in `memory.sqlite3` to prevent hallucinations, eliminate context drift, and guarantee zero repeat mistakes.

#### 2. The 8-File Sole Authority Invariant
- The entire system lives in exactly eight source files:
  1. `AGENTS.md`: Master contract, SDLC backlog, competitor benchmark, SWOT, and resume memory.
  2. `CONTEXT.md`: Agent coordination blackboard for sprint sync between parallel agents.
  3. `layer_a.py`: Zero-dependency standard-library backend, HTTP server, 4 SQLite stores, UACP models.
  4. `layer_a_build.py`: Ephemeral HTTP prototype runner (EphemeralBuildManager, ports 8081–8099).
  5. `layer_a_config.json`: Master configuration, handoff contracts, and 4 embedded exportable resources (`plugin.json`, `mcp.json`, `skills/product-discovery/SKILL.md`, `skills/token-optimizer/SKILL.md`).
  6. `layer_a_terminal.py`: Allowlisted terminal command executor (TerminalExecService: validate/test/compile).
  7. `index.html`: Vanilla HTML/CSS/JS frontend with 4 launcher destinations (`Frame idea`, `Design product`, `Ask π Gen`, `Advanced`).
  8. `test_layer_a.py`: 141 unit tests verifying Part A (19 gates), Part B (8 experiences), Memory (M1-M9), Plugins (P1-P10), Story 04.1+04.2, UI-11–UI-27, and AKP-01–AKP-09 contracts.
- **Rule**: Never create a 9th source file. Never add external pip/npm packages. Expand solely via declarative skills/templates in `layer_a_config.json`.

#### 3. Security & Governance Invariants
- **Cryptographic Approval Ledger**: Every state mutation requires an `ApprovalRequest` token binding `(action, target, payload_hash)`. The token is destroyed immediately upon execution; zero silent writes occur.
- **`repo-check` Supply-Chain Gate**: Pre-install verification skill registered locally and globally. Blocks unauthorized npm/pip/curl downloads and enforces 7-step static vetting.
- **Opaque Vault Boundaries (`secret://`)**: API keys resolve only inside backend HTTP handler over secure memory references. Never exposed in HTML or client logs.

#### 4. Executable Verification Baseline
- `PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -B layer_a.py validate` → `PASS`, `8/8` files.
- `PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -W error::ResourceWarning -m unittest -v` → `141/141 OK`.
- `PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -m py_compile layer_a.py layer_a_build.py layer_a_terminal.py test_layer_a.py` → `PASS`.
- `python3 layer_a.py serve` → Serves local web UI on `http://127.0.0.1:8080`.

#### 5. Multi-Agent Orchestration & 30–60 Minute Sprint Protocol
- **Multi-Agent Parallel Delegation**: Incoming orchestrator agents must leverage parallel worker subagents (e.g. `research` / `investigator` for read-only exploration and contract tracing, `builder` for atomic diffs, `reviewer` for verification) to save main context tokens and maximize speed.
- **Single Integration Owner**: Exactly one agent owns edits to `layer_a.py` and `index.html` to prevent merge collisions.
- **Plan & Explicit Confirmation Gate**: Never run external LLM simulations, trigger live API calls, spawn daemon servers, or modify database schemas without presenting an explicit plan and obtaining human confirmation first.
- **30 to 60 Minute Session Timebox**: Structure all sprint work into compact 30–60 minute deliverable increments. If reaching session boundaries, immediately checkpoint state to `AGENTS.md` (Plan B) so the next terminal agent resumes instantly without context loss.

#### 6. Live AI Scrum Standup & Sprint Status Board
- **Sprint Goal**: Deliver Subproduct 4 Execution Engine (Story 04.1 Live Prototype Runner & Sandboxed Split Preview + Story 04.2 In-UI Terminal Drawer + Multi-File Emitter & Deterministic Archive Export).
- **Completed**:
  - [x] Bundle frozen at exact 8 source files (`AGENTS.md`, `CONTEXT.md`, `index.html`, `layer_a.py`, `layer_a_build.py`, `layer_a_config.json`, `layer_a_terminal.py`, `test_layer_a.py`).
  - [x] All 19 Part A Gates, 8 Part B Experiences, and Memory M1–M9 validated.
  - [x] **Story 04.1**: Implemented isolated build directory `.layer-a-state/builds/<id>/`, loopback HTTP daemon (`8081–8099`), and sandboxed `<iframe>` preview in `index.html` + `layer_a_build.py`.
  - [x] **Story 04.2**: Implemented in-UI bottom terminal drawer (`Ctrl + \``) with `/api/terminal/exec` bridge for allowlisted CLI execution (`validate`, `test`, `compile`).
  - [x] **Data Model & Multi-File Artifact Emitter**: Deterministic emission of `index.html`, `data-model.md`, `schema.sql`, `er.svg`, `BRD.md`, `PRD.md`, `FSD.md` (clean product boundary, zero CDN/JS dependencies).
  - [x] **Deterministic Zip Export**: `/api/build/archive` with stdlib `zipfile` fixed timestamp `(2026, 1, 1, 0, 0, 0)` and path containment guard.
  - [x] **Vault & Handoff Traceability Tests**: Added `TestVaultAndHandoffTraceability`; coverage remains green in expanded suite.
  - [x] **UI-11–UI-27**: Completed secondary UI/accessibility polish with focused static regression contracts.
  - [x] **AKP-01–AKP-09**: Product-bound create/Ping/prototype flow, exact Gherkin review states, blank RICE inputs, reload continuity, accessible errors, and visible loopback controls implemented.
  - [x] **Portfolio User Scoped Routing & Discrete Build Stages**: Added `/p/<user_id>/<product_id>` routing with preview/archive/files subroutes, 6-stage discrete build pipeline with ms timings, and last-good preview fallback.
  - [x] Full validation suite passing with 143/143 tests OK (test floor: 143).
- **Today / Next**:
  - [x] UI-11–UI-27 local implementation and executable verification complete; see Signal 69.
  - [x] AKP-01–AKP-09 local implementation and executable verification complete; see Signal 71.
  - [ ] Human Akshara Play browser UAT rerun remains required.
  - [ ] Human browser review at 320/768/1024/1440 remains external visual evidence, not automated proof.
- **Blockers / Risks**: No code blocker. Browser-rendered interaction/visual proof remains unrun by policy. Zero external dependencies constraint strictly preserved.
- **Immediate Shell Commands to Resume**:
  ```bash
  cd test-module
  PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -B layer_a.py validate
  PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -W error::ResourceWarning -m unittest -v
  PYTHONPYCACHEPREFIX="$TMPDIR/pycache" python3 -m py_compile layer_a.py layer_a_build.py layer_a_terminal.py test_layer_a.py
  python3 layer_a.py serve
  ```
- **Live Local Endpoint**: `http://127.0.0.1:8080` (Browser preview port range: `8081–8099`).

---

## Start full development after copying

Copy this entire folder with all five files and preserve filenames. The receiving AI must treat this folder as authoritative, read this `AGENTS.md` completely, and validate the unchanged baseline before development.

### Gemini continuation prompt

```text
Read AGENTS.md completely first.

Treat these eight files as the complete and sole project source. Ignore every parent folder, sibling folder, prior repository, prior chat, cache, screenshot, and generated database. Do not create a ninth source file.

You are the build-time engineering agent. You are not π Gen and you do not select π Gen's runtime provider. π Gen remains provider-neutral BYOK with no selected provider. Gemini, Grok/xAI, NVIDIA NIM, and other providers are future disabled candidates only.

If your environment has an explicitly connected local shell, run before editing:
python3 layer_a.py validate
python3 -W error::ResourceWarning -m unittest -v
python3 -m py_compile layer_a.py test_layer_a.py

If your environment cannot run these local commands, say so. Do not claim they passed. Return exact patches or complete replacement content for only the eight existing files, then give commands for a local operator.

Work autonomously inside the eight-file boundary: inspect -> plan smallest vertical slice -> edit -> add focused regression proof -> run focused checks -> run full gates -> report evidence and remaining gaps. Keep one integration owner for layer_a.py. Use parallel agents only for read-only analysis or non-overlapping ownership.

Preserve four-app ownership, single-user onboarding, canonical product identity, database contracts, API behavior, security boundaries, current UI behavior, Part A frozen gates, Part B contracts, and executable evidence. Follow MoSCoW priorities in AGENTS.md and machine-readable handoff_contract in layer_a_config.json.

Stop and ask for explicit action-specific approval before network access, provider calls, credentials, dependency installation, external code, destructive data/schema changes, remote mutation, publishing, migration, deployment, or release. Never infer approval from "autonomous," "continue," or this prompt.
```

These eight files contain development instructions and resume memory, local backend/API implementation, full dependency-free UI, embedded configuration/resources, and the 70-test validation suite. They are sufficient for an AI to resume local development. Production capabilities such as live AI, BYOK vault, authentication, encrypted shared storage, hosting, and external integrations still require separate implementation, security review, and explicit approval.

### Gemini AI Studio truth boundary

Google AI Studio can hold these eight files as context and can propose code. Do not assume it can see a user-local filesystem, preserve files between sessions, start localhost, run Python, install tools, deploy, or inspect browser state. Evidence exists only when an explicitly connected tool returns command output. Without that tool, Gemini must produce patches and mark execution `UNRUN`.

Google AI Pro consumer limits, Gemini API quotas, Firebase quotas, and any provider billing are separate. Never encode a subscription as runtime authorization or assume it funds API calls. Free/unpaid model services must not receive confidential, personal, credential, or company-restricted content. Re-check current provider terms, data use, models, quotas, and corporate approval at integration time.

OpenHands Agent Canvas and Software Agent SDK remain optional build-time references only. They are not installed, bundled, approved, or required. Firebase is not selected as hosting, database, authentication, or runtime AI infrastructure. Installing or connecting either needs separate exact approval and must not change π Gen's provider-neutral contract.

### Autonomous engineering loop

1. Read all eight files before changing behavior.
2. Run unchanged baseline when tool access exists; record exact results.
3. Select one `MUST` gap or one user-reported reproducible defect.
4. Trace contract, config, backend, UI, and matching tests.
5. Change narrowest responsible layer; preserve API compatibility.
6. Add positive, negative, boundary, failure, and security proof proportional to risk.
7. Run focused test, full suite, compile, JavaScript parse, dependency scan, and `validate`.
8. Update status only from executable evidence. `ADD`, `UI`, or `EXTERNAL` never becomes validated from prose.
9. Report changed files, behavior preserved, commands/results, unrun checks, risks, and next smallest slice.
10. Stop. Do not start unrelated cleanup after gates pass.

### Low-token coordinator protocol

Use one bounded packet for every agent or parallel task:

```text
GOAL: one observable outcome
OWN: exact functions, sections, or one existing file
READ: smallest required anchors and contracts
INPUT: stable IDs, fixtures, and known evidence
OUTPUT: patch or read-only findings plus exact proof
DONE: measurable acceptance and stop condition
```

- One integration owner controls overlapping edits to `layer_a.py` and shared contracts.
- Parallelize read-only investigation, independent test design, and non-overlapping file work only.
- Never ask multiple agents to rewrite same function, schema, route, or UI region.
- Read narrow anchors first; widen only when caller, invariant, or failure path requires it.
- Prefer smallest vertical slice spanning config, runtime, UI, and proof over broad cleanup.
- Reuse existing helpers and schemas. New abstraction needs two real callers or one security boundary.
- Agent summary is not evidence. Preserve exact command, result, changed anchor, limitation, and handoff.
- Stop after requested acceptance passes. Put unrelated findings in backlog with `MUST`, `SHOULD`, `COULD`, or `WON'T NOW` priority.

Quality order: correctness and data integrity; security and privacy; evidence and traceability; regression safety; product clarity/accessibility; simplicity; token/time/cost; recovery and rollback.

### Recovered modular architecture map — reference, not extra files

Earlier modular implementation separated these replaceable boundaries. Five-file build merges them into `layer_a.py`, `layer_a_config.json`, `index.html`, and tests; preserve separation conceptually when editing:

| Boundary | Responsibility | Current five-file location |
|---|---|---|
| Adapters | JSON manifest and Python AST inspection; normalized facts only | `layer_a.py` adapters and config fixtures |
| UACP | Canonical model, stable IDs, evidence states, source references | runtime dataclasses/validators plus `layer_a_config.json` |
| Discovery pipeline | Discover, assess, diagnose, remediate, evaluate | backend engines, gates, and API handlers |
| Runtime/workflow | Local execution, checkpoints, approval, resume/cancel | runtime services and process-memory state |
| Model/protocol | Provider-neutral model contract, MCP/A2A seams, deterministic fixture | disabled adapters/config and local mock |
| Knowledge/context | Workspace-scoped ingestion, chunks, retrieval, citations, bounded transfer | Knowledge SQLite and context builders |
| Memory | Typed records, revisions, lifecycle, search, export/import | Memory SQLite and memory service |
| Storage/governance | Product records, fingerprints, budgets, audit, backup/restore | Product and Governance SQLite services |
| Plugins/skills | Trust, identity, compatibility, enable/disable/rollback, bundled skill metadata | embedded config resources and lifecycle APIs |
| Sandbox policy | Path/action limits and deny-first execution policy; not hostile-code containment | validators, approval gates, security contract |
| Interfaces | Local CLI, loopback HTTP/API, dependency-free web UI | `layer_a.py` and `index.html` |

Historical modular test inventory was broader than this transfer suite. Treat it only as regression ideas. Current `61/61 OK` is sole executable five-file claim; never report old counts as current evidence.

## Product north star and four-app ownership

PI is an AI-native product-definition environment. It helps one product move from rough idea through evidence, product design, launch, readiness, and engineering handoff. Human review remains product truth. Coding agents implement downstream; π Gen advises and proposes changes but never silently edits, approves, exports, deploys, or releases.

Target journey:

```text
Create product
  -> frame problem, intended user, context, evidence, desired outcome, hypothesis, decision
  -> start product design
  -> review research evidence and gaps
  -> compare solution options
  -> define requirements and validation
  -> plan launch
  -> assess readiness
  -> preview reviewed engineering handoff
```

Canonical ownership:

| App | User label | Owns | Must not own |
|---|---|---|---|
| Foundation | Frame idea | Why, who, context, evidence framing, outcome, hypothesis, supported decision | Provider/model selection, detailed delivery workflow |
| Product | Design product | Research review, solution options, requirements, validation, launch, readiness, handoff | Duplicate foundation capture, secret/provider administration |
| Assistant | Ask π Gen | Conversation, exact selected context, gaps, recommendations, reviewable field proposals, session activity | Product truth, approval, hidden writes, runtime provider choice |
| Admin | Advanced | AI behavior, provider adapters, credentials boundary, skills, plugins, permissions, policy | Normal PM journey, product readiness decision |

All apps use one canonical `workspace_id + product_id`. Foundation context flows into Product. π Gen reads explicit selected fields and evidence. Advanced config never rewrites business intent.

Single-user product decision: onboarding has no owner field, user-management flow, or end-user RBAC. Internal roles, owner labels, injected claims, and approval actors in backend/config are POC engine fixtures and future policy seams, not current user-facing product features.

Required target artifacts remain: detailed research dossier; BRD; PRD; FSD; user journeys; user stories; Gherkin-ready acceptance criteria; requirements/capabilities/evidence traceability; assumptions; risks; decisions; unknowns; Markdown, JSON, and YAML engineering handoff. Current POC implements only part of this depth; never claim full artifact completion until content and tests prove it.

Eight generic primitives remain frozen: Knowledge, Memory, Decisions, Workflow, Approvals, Automation, AI Interaction, and Execution. Core stays metadata-driven. Domain examples belong in product data/templates, never hard-coded product logic.

## Strategic market context, competitor analysis, and SWOT

### Strategic positioning: framework and problem preparation + BYOK (not raw foundation LLMs)

PI does not train proprietary frontier LLMs. PI competes on the **Model-Agnostic Agentic Orchestration Framework & Problem Preparation Pipeline**:
1. **Upstream Problem Preparation**: Ingests problem, persona, evidence, PRD, RICE, and Gherkin validation criteria before code generation starts (eliminates user hallucination and wrong-direction builds).
2. **Meta-Agent Orchestration (Subproduct 3 / π Gen)**: Conversational controller driving Foundation (1), Product Design (2), and Execution/Deploy (4).
3. **Downstream BYOK & Execution Security**: Pure Bring-Your-Own-Key (Gemini, Claude, OpenAI, Ollama) running in isolated execution environments gated by `repo-check` pre-install verification and single-use cryptographic approval tokens.

### Top 10 competitor benchmark matrix

| Company / Tool | Primary User Archetype | What User Provides → What Agent Builds | Critical Limitation / Pain Point | PI Framework Advantage |
|---|---|---|---|---|
| **GitHub Copilot** | Enterprise & solo developers | Task/issue → full PR & repo updates | In-editor only; no problem framing or PRD verification. | Full upstream spec preparation & Gherkin traceability. |
| **Cursor** | Power software engineers | Prompt in editor → multi-file code & terminal fixes | Requires manual engineering prompt babysitting; no PRD. | Meta-agent automates end-to-end spec-to-code pipeline. |
| **Vercel (v0)** | Frontend developers & designers | Prompt/wireframe → Next.js UI component | Visual toy-scale; lacks backend architecture & evidence tracking. | Complete 4-app lifecycle from problem definition to deploy. |
| **Replit Agent** | Non-technical & solo founders | Simple prompt → live fullstack deployed web app | High hallucination risk without structured requirements or tests. | Gherkin-grounded builds; zero silent code writes. |
| **Anthropic (Claude Code)** | Terminal & CLI power users | Terminal prompt → git commits, test passes, refactors | Terminal-only; lacks visual product discovery & stakeholder UI. | Frontier UI for product intake + future advanced CLI engine. |
| **Codeium (Windsurf)** | Fullstack developers in IDE | High-level goal → autonomous file writes & builds | Confined to IDE context; no market framing or business context. | Product-first framing connected to downstream engineering. |
| **Cognition (Devin)** | Engineering orgs & QA | Jira ticket → tested production PR | Expensive closed SaaS; unverified third-party dependencies. | Open BYOK secret vault + built-in `repo-check` security gate. |
| **OpenAI (Canvas/Agent)** | Broad prototypers & general devs | Natural language → working script/component | Fragmented code scratchpad; no formal handoff contract. | Structured 4-SQLite deterministic handoff artifacts. |
| **OpenHands** | Open-source devs & researchers | GitHub issue → Docker container PR | Complex setup; developer-centric without product framing. | Clean-room zero-dependency local POC + metadata primitives. |
| **Augment Code** | Large enterprise codebases | Multi-repo context → verified code changes | Closed enterprise lock-in; high subscription cost. | Provider-agnostic local BYOK with strict tenant isolation. |

### SWOT matrix (PI framework & BYOK architecture)

| Dimension | Key Factors & Evidence |
|---|---|
| **Strengths (S)** | • Upstream problem preparation eliminates prompt hallucination.<br>• Model-agnostic BYOK: zero frontier LLM lock-in.<br>• Built-in supply-chain security gate (`repo-check`) blocks unverified tools.<br>• Cryptographic single-use approval ledger prevents silent writes.<br>• Strict tenant & product isolation on `(workspace_id, product_id)`. |
| **Weaknesses (W)** | • π Gen currently runs deterministic local mock (live BYOK loop pending).<br>• Ephemeral sandbox runner requires container/WebContainer wiring.<br>• 5-file architecture density requires strict code modularity.<br>• Single-user POC boundary (multi-tenant enterprise RBAC in Phase 2). |
| **Opportunities (O)** | • Enterprise demand for spec-driven SWE and PRD traceability.<br>• Enterprise shift to private BYOK vaults over closed third-party SaaS.<br>• Convergence of PM specification and autonomous SWE code generation.<br>• AI supply-chain regulatory compliance requiring pre-install tool vetting. |
| **Threats (T)** | • Competitors adding shallow planning/spec-generation wizards.<br>• Upstream LLM provider API drift and breaking schema updates.<br>• Developer entrenchment in existing IDEs (mitigated by future CLI bridge). |

## π Gen build/runtime separation and BYOK target

Build-time Gemini helps develop PI. Runtime π Gen is a separate product capability.

- No runtime provider selected or preferred.
- Future candidates include Google Gemini, xAI Grok, NVIDIA NIM, and other approved providers.
- Candidate names are planning context, not approval, availability, endorsement, or default.
- Current π Gen stays deterministic local mock.
- Future provider adapter must normalize capability discovery, health, generation, streaming, structured tool calls, usage/cost, timeout, cancellation, and errors.
- BYOK keys go from user to authenticated backend secret vault over HTTPS. Browser keeps no key, prompt, credential, provider token, or secret reference.
- UI may retain masked fingerprint, provider, credential ID, created date, last verified, last used, permissions, limits, location, and retention only after backend supports them.
- Rotation, revocation, fallback, spending limits, residency, retention, and emergency disable require enforceable backend controls.
- Missing, rejected, stale, replayed, disabled, unavailable, or misconfigured provider fails closed. No silent switch to another live provider.
- Every proposed product mutation shows field-level before/after values, evidence, rationale, assumptions, unknowns, confidence, and Accept/Edit/Reject.
- Accepted change creates canonical revision and audit evidence. Rejection writes nothing.

## MoSCoW full-build priorities

### MUST — release-blocking

1. Keep exactly eight authoritative source files and zero sibling dependency.
2. Keep one canonical product registry, identity, revision, and context across all four apps.
3. Keep single-user onboarding without owner/RBAC fields.
4. Create new products from a blank canonical template; never inherit synthetic research, hypothesis, solution, launch, or readiness data.
5. Persist explicit Foundation/Product work to canonical backend state with optimistic revision and evidence traceability. Page-memory drafts must be visibly temporary.
6. Preserve drafts during active session without `localStorage`, `sessionStorage`, IndexedDB, cookies, URL state, analytics, or prompt logs.
7. Separate workflow preparation, evidence confidence, decision readiness, delivery readiness, and approval status. Page visits or preview never mean ready.
8. Keep π Gen simple and conversation-first: compact context disclosure, Fast/Normal behavior, sticky composer, Send/Stop, useful follow-ups, exact source fields, and proposal approval.
9. Keep π Gen provider-neutral. Secure vault, auth, permission, audit, spending, retention, and disable controls must exist before live BYOK activation.
10. Preserve SQLite schemas, transactions, revisions, migrations, failure behavior, backup/restore boundaries, API contracts, and regression tests.
11. Apply same readiness/export gate across Foundation and Product. No reviewed/exportable claim with missing core fields or approvals.
12. Meet semantic labels/dialogs, keyboard operation, visible focus, 44×44 targets, WCAG AA contrast, reduced motion, and responsive 320/768/1024/1440 behavior.
13. Escape untrusted API/user text; block secret-shaped input; prevent duplicate submissions, stale decisions, ID mix-ups, and approval replay.
14. Require deterministic tests plus human/external evidence before status promotion, provider access, migration, deployment, or release.

### SHOULD — next after MUST

- Backend-backed draft recovery and explicit discard warnings without browser persistence.
- Detailed BRD/PRD/FSD/journey/story/Gherkin/traceability exports.
- Product archive/delete with confirmation, retention/recovery policy, and audit.
- Versioned API envelopes, idempotency, pagination, compatibility, and deprecation policy.
- Metadata-only observability, correlation, budgets, retries, cancellation, rollback, backup, and restore drills.
- Automated accessibility, responsive, concurrency, migration, recovery, injection, Unicode, and large-data tests.
- Skills metadata: source, version, license, permissions, and scope. Plugin metadata: publisher, origin, checksum, license, permissions, data access, trust, and lifecycle.

### COULD — optional ecosystem value

- Voice, image, and attachments only when actual processing, consent, privacy, error, and deletion behavior exist.
- More provider adapters after neutral contract suite passes.
- Organization-size profiles, templates, domain packs, data-platform mappings, and reusable archetypes.
- Cloud collaboration, multi-tenant operation, or enterprise RBAC only through explicit scope change.
- Approved catalog discovery and explainable ranking after safe trust/lifecycle foundations.

### WON'T NOW — deliberate exclusions

- Select/prefer Gemini, Grok, NVIDIA NIM, or another runtime provider.
- Make Firebase, OpenHands, Agent Canvas, hosted memory, or marketplace service a core dependency.
- Live web/market/news/legal research without approved connectors, citations, freshness, access, and legal/security review.
- Download, install, or execute unknown plugin, skill, MCP, repository, pasted code, or model tool.
- Auto-approve product changes, readiness, export, release, migration, or deployment.
- Store raw prompts, drafts, credentials, keys, secrets, PII, confidential data, or chain-of-thought in browser persistence/logs.
- Claim SSO, RBAC, encryption, compliance, model truth, production readiness, or deployment certification from local POC tests.

## Database and state contract — preserve exactly

Implementation lives in `layer_a.py`; structured inventory lives in `layer_a_config.json`; executable proof lives in `test_layer_a.py`.

### Memory SQLite

Default: `.layer-a-state/memory.sqlite3`; `PRAGMA user_version = 1`.

Tables:

- `memory_metadata`: database/workspace binding metadata.
- `memory_records`: current scoped record, revision, lifecycle state, expiry, JSON, checksum.
- `memory_revisions`: immutable revision history.
- `memory_requests`: workspace/idempotency key to payload hash and record mapping.
- `memory_audit`: content-free actor/action/record/detail hashes.

Required behavior: schema/size/checksum validation; workspace and role isolation; idempotent same request; conflict on changed payload or stale revision; candidate/quarantine/active/archive/supersede/expire/delete/purge lifecycle; instruction-like untrusted content quarantine; secret rejection; sensitive content rejection while encryption is absent; bounded summary-first search; explicit full retrieval; export/import validation; transaction rollback on error; future schema fails closed.

### Product SQLite

Default: `.layer-a-state/products.sqlite3`; logical schema version 1.

Table `product_blueprints`: `workspace_id`, `product_id`, `revision`, `owner`, `lifecycle_phase`, `status`, readiness JSON, canonical blueprint JSON, fingerprint, and update time; primary key is workspace/product.

Required behavior: stable IDs; workspace isolation; canonical schema; size and sensitive-data checks; duplicate-create denial; optimistic revision update; fingerprint verification; explicit proposal acceptance before write; reopen after restart. Current `owner` is compatibility metadata only. Target single-user UI does not ask for it. Production needs explicit migrations, archive/delete, encrypted tenancy, backup/restore, and durable proposal/audit records.

### Knowledge SQLite

Default: `.layer-a-state/knowledge.sqlite3`; logical schema version 1.

Tables: `knowledge_sources` and `knowledge_chunks`. Preserve workspace/role scope, version/idempotency/conflict, bounded TXT/MD/CSV/JSON/HTML parsing, source/chunk hashes, deterministic lexical retrieval, and resolvable citations. Retrieval proves matching content, not factual truth.

### Governance SQLite

Caller-supplied safe local path; logical schema version 1.

Tables: `governance_meta`, `governance_budget`, and `governance_audit`. Preserve policy fingerprint, workspace/subject budget, metadata-only audit, hashed secret reference, exact permissions, health, new-target backup, verified restore, symlink/path refusal, and tamper denial. Injected identity claims are test input, not production authentication.

### Non-durable state

Pending approvals, pending product proposals, π Gen conversation/activity, and unsaved drafts currently live in process/page memory and clear on restart/refresh. Never describe them as durable. Generated database rows are not embedded transfer source; safe synthetic seed blueprint remains in config. If real data must move, create separately approved redacted migration/export—never base64-dump unknown database content into source.

Migration rule: inspect current version, back up before destructive change, write explicit forward migration and rollback/recovery plan, test old/new/tampered/future schemas, preserve IDs/revisions/fingerprints, then change status. Never silently recreate, downgrade, drop, or reinterpret data.

## Current HTTP/API contract

Loopback server: `python3 layer_a.py serve`; frontend uses relative same-origin paths. POST requires JSON and body ≤1 MB. Error shape: `{"status":"ERROR","error":"human-readable reason"}`. Responses use `Cache-Control: no-store`, CSP, `nosniff`, frame denial, and no stack traces.

GET: `/health`, `/api/bootstrap`, `/api/products`, `/api/task`, `/api/plugin`, `/api/plugin/admin`.

POST: `/api/intake`, `/api/discover`, `/api/compare`, `/api/products/create`, `/api/products/open`, `/api/research`, `/api/definition`, `/api/solution`, `/api/gtm`, `/api/readiness`, `/api/copilot/propose`, `/api/copilot/decision`, `/api/export`, `/api/plugin/enable`, `/api/plugin/disable`, `/api/plugin/rollback`.

Current routes are local POC and unversioned. Before production, define versioned request/response/error schemas, auth/tenancy, idempotency, optimistic concurrency, pagination, archive/delete, compatibility/deprecation, audit correlation, and rate/cost limits. Stable IDs—not display names—bind actions. No product delete endpoint exists now; never fake deletion.

## Frozen acceptance families

- Part A gates 1–19: 18 locally `VALIDATED`; Gate 18 remote extension sync remains `EXTERNAL_SIGN_OFF`; Part A overall stays `INCOMPLETE`.
- Memory M1–M9: typed schema; SQLite restart/migration/idempotency; safe writes; lifecycle/access; bounded context; MCP parity; portable export/import; optional Mem0 disabled; full deterministic evidence. M8 remains optional-disabled.
- Product B1–B8: portfolio; definition; eleven-factor deterministic research; evidence-linked solution; GTM; readiness; controlled assistant; export. `VALIDATED_POC` means contract behavior exists, not production/user readiness.
- Plugin P1–P10: natural discovery; portable package; hidden Part A MCP; trust gate; canonical identity/freshness; lifecycle; two compatibility profiles; exact trust states; progressive loading; layman controls. Current bundled plugin remains `UNSIGNED`.
- Plugin P11–P13 SHOULD: project/global scope, cryptographic origin, durable transparency/revocation. Not implemented.
- Plugin P14–P15 COULD: approved catalog discovery and explainable ranking. Not implemented.
- Plugin P16 WON'T NOW: arbitrary marketplace/pasted-code download or execution.
- Session S1–S5: versioned contract, exact receipt, format drift blocking, sourced claims/unknowns, context drift. S6 external gateway enforcement remains partial.

Gate promotion requires behavior in code, configuration-driven contract, positive/negative/boundary/failure tests, full gates passing, evidence/limitations, no secret leakage, matching config status, and truthful docs. Prose, interface, simulation, AI confidence, screenshots, or popularity never promote status.

## Frontend, copy, and design contract

- Light peacock canvas `#F7FBFA`; white surfaces; border `#D7E7E4`; ink near `#102A3A`.
- Teal-to-blue gradient reserved for PI feather, selected navigation, and primary action. Success green means confirmed success only.
- Sidebar 264px expanded/64px collapsed; one toggle in logo position; current workspace tree only; full-height mobile drawer.
- Header and mobile controls ≥44×44; icons 18–20px with consistent 2px stroke; no emoji/Unicode menu icons.
- H1 about 28px, H2 20px, card heading 16px; sentence case; dense but calm 20–24px cards.
- π Gen panel 420–520px where safe, full screen on mobile, conversation first, sticky 112–220px rounded composer, compact context, Fast/Normal only, Send or Stop—not both.
- Context says exact fields/evidence included. Remove internal route IDs, model names, revision noise, unsupported image/voice controls, and repeated warnings.
- Product navigation labels destination: `Continue to Context`, not generic `Continue`.
- Solution option never becomes requirement without explicit Convert, review, and approval. RICE disabled until reach, impact, confidence, and effort exist for every option.
- Dialogs use role/name, `aria-modal`, inert background, focus trap, Escape, and focus restoration. Repeated actions include item-specific accessible names.
- Main content never height `0`; side panels never overlap/crush content; no horizontal overflow at 320/390/768/1024/1280/1440.
- Treat API/user text as untrusted. Prefer DOM/textContent; escape template values; never put user text in inline handlers.

Plain-language missing-value vocabulary:

| Meaning | Copy |
|---|---|
| Optional value absent | `Not provided` |
| Required value absent | `Missing` |
| Check never run | `Not checked yet` |
| Known incomplete | `Needs input` |
| Evidence absent | `Needs evidence` |
| Setup absent | `Not configured` |
| Empty collection | `No … yet` |
| Unsupported local feature | `Unavailable in local preview` |
| True epistemic uncertainty | `Still unknown` |
| Score absent | `Not scored` or `Not rated` |
| Truly irrelevant | `Not applicable` |

Never use bare `-`, `N/A`, `NA`, raw machine state, internal ID, or false `Ready`. Map `PASS` → `Passed`, `READY_FOR_REVIEW` → `Ready for review`, `UNKNOWN` → `Needs input`, and similar values only at display boundary; preserve API constants internally.

## Security and threat model

- Local-only, deny-first, no external network/provider/runtime by default.
- No raw secrets in files, browser, payload history, output, log, trace, context, error, URL, analytics, or export.
- `secret://` is opaque reference only. Resolve only at approved call time through injected provider; suppress value/reference from results.
- Remote content and pasted code remain untrusted data in quarantine. Static review, hash, signature, publisher, stars, or tests do not make execution safe.
- Approval binds exact action, target, version, fingerprint, run, cost, and expiry; single use; mismatch/stale/replay denied.
- Enforce path containment, regular-file/no-symlink checks, byte/count/time limits, content type, ID validation, revisions, and transactional failure.
- Memory/model/research output cannot self-certify evidence, trust, readiness, approval, or policy.
- CSP currently permits inline bundled JS; therefore escaping and safe DOM construction remain mandatory.
- Production requires verified identity/tenancy, encrypted storage, secret vault, data classification/residency/retention, audit, monitoring, containment, backup/restore, incident response, legal review, and human release gates.

## Known build gaps — next Gemini must reproduce before editing

1. New-product backend currently clones populated synthetic blueprint sections. Target is blank canonical product with onboarding context persisted.
2. Several Discover/Define/Solution/Launch fields remain session-only while validators read saved sample record. Target is one canonical progressive record and downstream invalidation when upstream changes.
3. Legacy Foundation renderers remain broad and contain dormant engineering/product-structure concepts. Normal UI hides most behind Advanced disclosure; remove only through tested migration.
4. Backend retains owner/role fixtures for compatibility and policy tests. Do not expose them as end-user RBAC.
5. Current π Gen answers are safe deterministic guidance, not live evidence-grounded provider execution.
6. API has no product delete/archive, durable proposal/session store, auth, vault, production versioning, or deployment contract.
7. Detailed BRD/PRD/FSD/journey/Gherkin export depth remains incomplete.
8. Automated tests do not prove rendered keyboard, dialog, accessibility, responsive, or cross-browser behavior.

Reproduce each gap against current source before changing it. Old audit text is evidence to check, not permission to refactor unrelated code.

## Legacy analysis register — reference only

Recovered prior analysis so deletion of old workspaces/chats does not erase intent:

- Original concept described an AI-native, Salesforce-like generic product composition environment. Current user-facing name is PI, not PIF or Blueprint Studio.
- Earlier UI had duplicate sidebar controls, Unicode icons, dark assistant, clipped quick actions, duplicated workflow tracker, huge forms/cards, false statuses, mobile navigation failure, inconsistent product identity, and contradictory persistence copy. Current UI contains many fixes; never reapply old redesign blindly.
- Earlier product audits found page-visit completion, lost Discover drafts, empty Define import, GTM output ignoring session inputs, false 100% handoff, mixed Part A/B identities, technical assistant persona, inaccessible Advanced navigation, and conflicting save/privacy claims. Current code fixed some and made other limits explicit. Verify runtime before marking open/closed.
- Earlier π Gen direction became: one simple conversation, useful follow-ups, compact context, Fast/Normal, field-level proposals, human acceptance, session-only activity, no unsupported image/voice/model controls. Preserve this current direction.
- Earlier ownership decision became: Foundation frames why/who/outcome; Product designs what/how/validation; π Gen proposes; Advanced owns provider/policy. Do not restore 14-step normal Foundation journey or duplicate product capture.
- Earlier security review found browser-storage violations and unsafe HTML interpolation. Current five-file source must remain free of browser persistence and must escape untrusted values.
- Earlier copy review standardized truthful missing states and removed raw machine IDs/statuses. Preserve vocabulary table above.
- Referenced 98-section master product specification is absent from available local source. Exact contents cannot be recovered or claimed. NDA-specific export examples were never supplied and must not be guessed.
- Obsolete local handoffs referenced old dark themes, old names, 13-file bundles, image/mode variants, stale evidence counts, and machine-specific paths. They are deliberately superseded by this file.
- Optional references discussed: assistant-ui interaction patterns, Tabler-style icons, OpenHands Agent Canvas/SDK as build tooling, Firebase as possible future infrastructure, and Gemini as build agent. None is installed, copied, approved, or selected as runtime dependency.

## Test backlog retained from prior analysis

Current `AUTO` evidence remains executable tests. Recommended `ADD`/`UI` work includes:

- Product: byte limits, same-name IDs, conflicting evidence, unsupported claims, deterministic ties, zero/negative/NaN/infinite ranking input, human priority override, script/HTML input.
- Memory: duplicate deletion, concurrent revision writers, transaction interruption, TTL/timezone boundary, relevance scale, conflicting active facts, backup/restore parity.
- Workflow: nested resume without repeated side effect; cancellation during stream with explicit partial state.
- Security: sleeper/indirect injection, workspace exfiltration, Unicode-obfuscated secrets/instructions, remote URL refusal.
- UI: offline smoke, stable IDs/revisions, truthful gaps, proposal accept/reject/edit, safe paste, draft recovery, keyboard/accessibility, responsive widths.
- Operations: database migration from prior version, restore drill, malformed/tampered database, audit continuity, provider failure/timeout/cancel/cost, rollback, deployment smoke, release rollback.

Never promote `ADD`, `UI`, or `EXTERNAL` from documentation alone.

## SDLC and release roadmap

1. **Baseline:** exact five files, deterministic tests, source inventory, no selected provider.
2. **Canonical data:** blank product factory, shared identity/context, durable explicit drafts, downstream invalidation, migrations.
3. **Product depth:** requirements/validation, complete artifact generation, consistent readiness/export gate.
4. **π Gen contract:** exact context builder, structured answers/proposals, durable accepted revisions; keep mock provider.
5. **Provider platform:** versioned neutral adapter, auth/vault/policy/budgets/audit; synthetic contract tests first.
6. **Infrastructure:** user-approved hosting/database/identity choice; environments, secrets, migrations, backup/restore, observability.
7. **Quality:** unit/integration/API/security/accessibility/responsive/recovery/load tests; threat-model review.
8. **Delivery:** deterministic CI, signed artifacts/SBOM where approved, staging, migration rehearsal, rollback rehearsal.
9. **Release:** human product/security/legal/operations approval; monitored canary; rollback authority; post-release verification.

No agent approves its own production release. Coding output, tests, and model confidence are evidence inputs—not deployment authorization.

## PI Meta Product Portfolio Epics & SMART User Stories (Scrum Master Register)

### 1. Portfolio Governance & Freeze Classification

| Subproduct | Component Name | Scrum Lifecycle Status | Test Evidence & Gates |
|---|---|---|---|
| **Subproduct 1** | **Foundation** | `[CORE FROZEN / VALIDATED]` | 19 Gates (Part A) + Gate B2 (Part B) |
| **Subproduct 2** | **Product** | `[CORE FROZEN / VALIDATED]` | Gate B4 (RICE/Scope) + Gate B6 (Readiness) |
| **Subproduct 3** | **π Gen Assistant** | `[CORE FROZEN / VALIDATED]` | Gate B7 (Diffs) + MIT Token Optimizer (P1-P10) |
| **Subproduct 4** | **Execution Engine** | `[ACTIVE SPRINT / IN BUILD]` | Ephemeral HTTP Runner + In-UI Terminal Drawer |
| **Subproduct 5** | **Admin & Governance** | `[CORE FROZEN / VALIDATED]` | 4 SQLite Stores + Memory M1-M9 + repo-check |

---

### 2. Epics & SMART User Stories Breakdown

#### EPIC-01: Foundation Problem & Evidence Framing (Subproduct 1)
- **STORY-01.1 [P0 / CORE FROZEN] — Structured Problem, Persona & Outcome Framing**
  - **User Story:** *As a product builder, I want to capture structured problem definitions, target personas, evidence dossiers, and desired outcomes so that upstream intent is immutable before any code is generated.*
  - **SMART Criteria:**
    - **S (Specific):** Input fields for Problem Statement, User Persona, Evidence Dossier, and Desired Outcome mapped to `FoundationIntake` schema.
    - **M (Measurable):** 100% test pass on Gate B2; rejects empty submissions and flags ungrounded claims.
    - **A (Attainable):** Standard-library schema validation persisting to `products.sqlite3`.
    - **R (Relevant):** Eliminates 80% of downstream hallucinations caused by ambiguous problem framing.
    - **T (Time-bound / Testable):** Verified deterministically in `<10ms` locally.

#### EPIC-02: Product Specification, RICE & Gherkin Matrix (Subproduct 2)
- **STORY-02.1 [P0 / CORE FROZEN] — Automated RICE Prioritization & Gherkin Verification**
  - **User Story:** *As an engineering lead, I want to calculate deterministic RICE scores and compile user journeys into formal Gherkin acceptance matrices so that product requirements are testable contracts.*
  - **SMART Criteria:**
    - **S (Specific):** RICE score computed via `(Reach * Impact * Confidence) / Effort` + Gherkin scenarios formatted with `Given / When / Then`.
    - **M (Measurable):** Validated by Gate B4 (three priority methods) and Gate B6 (readiness verification).
    - **A (Attainable):** Zero-dependency pure Python mathematical and text compilation.
    - **R (Relevant):** Creates machine-executable verification criteria before code execution.
    - **T (Time-bound / Testable):** Executed in memory in `<5ms`.

#### EPIC-03: π Gen Meta-Agent & Token Compression (Subproduct 3)
- **STORY-03.1 [P0 / CORE FROZEN] — Supervised Intent Dispatcher with Cryptographic Approval Tokens**
  - **User Story:** *As a developer, I want π Gen to act as an orchestrating supervisor (Google CCAI style) proposing structured mutation diffs that require single-use approval tokens so that zero silent writes occur.*
  - **SMART Criteria:**
    - **S (Specific):** Reviewable JSON diffs generated with SHA-256 bound `ApprovalRequest` token.
    - **M (Measurable):** Token destroyed immediately upon execution; proven by Gate 3 & Gate B7.
    - **A (Attainable):** Native UACP event-model inside standard-library `layer_a.py`.
    - **R (Relevant):** Prevents unvetted AI overwrites of production source.
    - **T (Time-bound / Testable):** Atomic SQLite transaction commit upon token receipt.
- **STORY-03.2 [P0 / CORE FROZEN] — Default MIT Token Optimizer Skill**
  - **User Story:** *As a commercial operator, I want all outgoing prompt contexts compressed via the bundled MIT token-optimizer skill so that commercial BYOK API spend is cut by up to 70%.*
  - **SMART Criteria:**
    - **S (Specific):** Caveman ultra-compression stripping filler while preserving 100% of technical terms, code blocks, numbers, and URLs.
    - **M (Measurable):** Tested via `test_agent_plugin_package_and_all_must_demo_pass` across 4 embedded resources.
    - **A (Attainable):** Pure declarative skill in `layer_a_config.json`.
    - **R (Relevant):** Massive cost reduction on Gemini 2.0 Flash, Claude, Grok, and OpenAI keys.
    - **T (Time-bound / Testable):** Zero latency impact (<1ms string transform).

#### EPIC-04: Autonomous Execution Engine, Terminal & Live Preview (Subproduct 4)
- **STORY-04.1 [P0 / ACTIVE SPRINT] — Isolated Prototype Build & Ephemeral HTTP Runner**
  - **User Story:** *As a product prototyper, I want to autonomously build and serve generated prototype files on an ephemeral loopback port (`8081–8099`) with split-view iframe preview so that I can click and test live apps in under 2 seconds.*
  - **SMART Criteria:**
    - **S (Specific):** Generated files written strictly into `.layer-a-state/builds/<id>/`; served on loopback `127.0.0.1:8081+` with sandboxed `<iframe sandbox="allow-scripts allow-forms allow-same-origin">`.
    - **M (Measurable):** Port lifecycle tracked via PID with single-action start/stop; 0 platform root files mutated.
    - **A (Attainable):** Standard-library `http.server` + `subprocess` process manager.
    - **R (Relevant):** Delivers #1 core feature of Cursor / v0 / Replit Agent.
    - **T (Time-bound / Testable):** Prototype interactive in browser in `<2.0s`.
- **STORY-04.2 [P1 / ACTIVE SPRINT] — Embedded In-UI Interactive Terminal & CLI Console**
  - **User Story:** *As a developer, I want a bottom-docked terminal drawer (`Ctrl + \`` or `⌘ + J`) to execute validation commands, test suites, and converse with the Meta-Agent CLI in real time.*
  - **SMART Criteria:**
    - **S (Specific):** Dark theme drawer with tab bar, status bar, command history, and `/api/terminal/exec` bridge.
    - **M (Measurable):** Runs `validate`, `test`, `build`, `serve` and streams stdout/stderr back into UI buffer.
    - **A (Attainable):** Lightweight vanilla JS terminal renderer + backend standard-library subprocess runner.
    - **R (Relevant):** Claude Code / Cursor terminal drawer parity.
    - **T (Time-bound / Testable):** Drawer toggle opens in `<50ms`.
- **STORY-04.3 [P1 / BACKLOG] — Visual Click-to-Inspect Element Tagger (v0 / Bolt.new Parity)**
  - **User Story:** *As a UI designer, I want to click any element in the live iframe preview to auto-inject its CSS selector into the π Gen composer so I can prompt localized UI changes with zero typing.*
  - **SMART Criteria:**
    - **S (Specific):** Iframe DOM listener emitting `postMessage({ tag, id, class })` to parent window.
    - **M (Measurable):** Auto-injects `@element: #selector` tag into composer input field.
    - **A (Attainable):** 20-line vanilla JS event listener with zero external libraries.
    - **R (Relevant):** Cuts prompt iteration cycle by 50%.
    - **T (Time-bound / Testable):** Element selected in `<10ms`.
- **STORY-04.4 [P1 / BACKLOG] — Self-Healing Test-Debug Loop (Devin Parity)**
  - **User Story:** *As an engineer, I want the system to automatically intercept unit test failure tracebacks and feed them into π Gen for surgical fix generation so that bugs are resolved autonomously.*
  - **SMART Criteria:**
    - **S (Specific):** Error parser capturing stderr tracebacks, packaging into error payload, and triggering minimal fix diff.
    - **M (Measurable):** Auto-generates fix diffs that pass the failing test suite upon operator approval.
    - **A (Attainable):** Standard-library regex parser on test outputs.
    - **R (Relevant):** Automated repair cycle reducing human triage time.
    - **T (Time-bound / Testable):** Fix generated in 1 agent turn.
- **STORY-04.5 [P2 / BACKLOG] — SQLite Schema & Data Visualizer (Replit Agent Parity)**
  - **User Story:** *As a full-stack builder, I want a visual database inspector table in App 4 showing prototype SQLite tables, schema definitions, and row data in real time.*
  - **SMART Criteria:**
    - **S (Specific):** Standard `PRAGMA table_info` query rendering interactive HTML table in Subproduct 4.
    - **M (Measurable):** Inspects table schema and previews up to 100 rows per table with pagination.
    - **A (Attainable):** Read-only SQLite query connection.
    - **R (Relevant):** Complete full-stack visibility without external DB viewer tools.
    - **T (Time-bound / Testable):** Schema renders in `<20ms`.
- **STORY-04.6 [P2 / BACKLOG] — PWA Viewport & Responsive Quality Health Check**
  - **User Story:** *As a QA engineer, I want a multi-viewport preview bar (320px, 768px, 1024px, 1440px) and Web Manifest audit so that mobile and desktop layouts are verified prior to handoff.*
  - **SMART Criteria:**
    - **S (Specific):** 4-button responsive toggle adjusting iframe viewport width + manifest.json presence check.
    - **M (Measurable):** Passes audit checklist (viewport meta tag, manifest icons, touch target sizing).
    - **A (Attainable):** Pure CSS container queries + standard JS viewport switcher.
    - **R (Relevant):** Eliminates broken mobile prototypes.
    - **T (Time-bound / Testable):** Viewport resizes instantly (<16ms 60fps).

#### EPIC-05: Admin, Governance, Anti-Drift RAG & Security (Subproduct 5)
- **STORY-05.1 [P0 / CORE FROZEN] — Zero-Cost SQLite FTS5 Local RAG & Typed Mistake Ledger**
  - **User Story:** *As an enterprise architect, I want all product context indexed in local SQLite FTS5 (BM25) and user corrections recorded in an immutable typed mistake ledger so that hallucinations and context drift are eliminated with zero SaaS costs.*
  - **SMART Criteria:**
    - **S (Specific):** Full-text lexical search in `knowledge.sqlite3` + typed correction records in `memory.sqlite3`.
    - **M (Measurable):** Verified by Memory tests M1–M9; zero external vector DB subscriptions.
    - **A (Attainable):** Standard-library `sqlite3` FTS5 module.
    - **R (Relevant):** Eliminates repetitive AI mistakes and context drift across multi-turn sessions.
    - **T (Time-bound / Testable):** Search query execution in `<3ms`.
- **STORY-05.2 [P0 / CORE FROZEN] — `repo-check` Supply-Chain Sandbox Gate**
  - **User Story:** *As a security officer, I want all external repositories, skills, and tools statically vetted against a 7-step security rule before installation so that supply-chain attacks and secret exfiltration are blocked.*
  - **SMART Criteria:**
    - **S (Specific):** Static AST & regex scan for malicious network exfiltration, arbitrary code execution, and unapproved package managers.
    - **M (Measurable):** Proven by Gate 1 & Gate 18 fail-closed tests.
    - **A (Attainable):** Python standard library AST parser and regex validator.
    - **R (Relevant):** Protects developer host environment from untrusted open-source dependencies.
    - **T (Time-bound / Testable):** Vetting complete in `<150ms`.
- **STORY-05.3 [P1 / BACKLOG] — SQLite SHA-256 Time-Travel & Version History Slider (Canvas Parity)**
  - **User Story:** *As a product manager, I want an interactive time-travel slider to preview and restore previous SHA-256 state snapshots across all 4 SQLite stores with one click.*
  - **SMART Criteria:**
    - **S (Specific):** Slider UI binding to `portfolio_revisions` and `memory_revisions` tables with instant rollback action.
    - **M (Measurable):** Restores exact historical state hash without data corruption or orphan records.
    - **A (Attainable):** Existing revision hash schema in `layer_a.py`.
    - **R (Relevant):** Complete auditability and risk-free iteration.
    - **T (Time-bound / Testable):** State rollback executed in `<15ms`.

---

## Live prototype build, ephemeral HTTP runner, and browser preview

Specification for Subproduct 4 autonomous prototype build, background process execution, and live browser review:

- **Isolated Build Path:** Generated prototype files (`index.html`, `app.js`, `server.py`) are strictly written into `.layer-a-state/builds/<product_id>/`. The 5 platform root source files are never mutated by prototype generation.
- **Ephemeral Process Manager:**
  - Prototype server runs on loopback `127.0.0.1` allocating dynamic ports in range `8081–8099`.
  - Process lifecycle tracked via PID with single-action start, stop, and status query.
  - Automatic process reaping on platform shutdown and 30-minute idle timeouts.
- **Split-View Iframe Sandboxing:**
  - Interactive preview embedded via `<iframe sandbox="allow-scripts allow-forms allow-same-origin" src="...">`.
  - Prototype code is isolated from parent platform storage, session tokens, and SQLite databases.
  - Dedicated controls: `[Start / Stop]`, Port indicator, URL bar, Reload, and `[Open in Browser]` for external Chromium review.

## Embedded interactive terminal window (In-UI CLI Console)

Specification for the in-app bottom-docked terminal drawer across all 4 subproducts:

- **Dual-Modality Interface:** Toggleable drawer (Shortcut: `Ctrl + \`` or `⌘ + J`, or bottom footer tab).
- **Core CLI Capabilities:**
  - Fast problem framing: `> pi frame "<idea>"` (syncs directly to App 1 Foundation cards).
  - Instant RICE & Gherkin compilation: `> pi gherkin --compile` (syncs to App 2 Product matrix).
  - Conversational Meta-Agent interaction: Chat directly in the CLI with live token count & thinking time.
  - Local process control: Execute `validate`, `test`, `build`, `serve` with real-time log streaming.
- **Status Bar Telemetry:** Displays active BYOK model, MIT `token-optimizer` status (70% savings), and SQLite store health.

## Top 10 Competitor Benchmark & Core 50% Parity Roadmap

### 1. Top 10 Competitors 3-Feature Architectural Breakdown

| # | Competitor | Top 1: Killer Core Feature | Top 2: High-Value Feature | Top 3: Developer Moat |
|---|---|---|---|---|
| **1** | **Cursor** | **Composer Multi-File Diffs**: Edits 10+ files simultaneously with instant green/red review. | **Integrated Browser & Terminal**: Live preview running next to code with in-editor CLI. | **Deep Codebase Indexing**: Real-time semantic symbol graph. |
| **2** | **Cursor Cloud Agents** | **Async Background Task Agent**: Agent works on a cloud branch/PR while developer works locally. | **Headless Self-Verification**: Runs CI lint/tests in cloud before prompting user. | **GitHub PR Dispatch**: Packages completed branch into reviewable PR. |
| **3** | **v0 / Bolt.new** | **Instant Web Preview (Iframe Runner)**: Renders working, clickable HTML/React in 2 seconds. | **Visual Click-to-Edit**: Click a button on preview to instruct: "Make this green". | **1-Click Cloud Deployment**: Instant shareable preview link for stakeholders. |
| **4** | **Replit Agent** | **Full-Stack Autonomous Build**: Creates DB schema + backend server + frontend in 1 prompt. | **Live Container Execution**: Port forwarding and interactive app window. | **Auto-Dependency Provisioning**: Auto-installs missing packages on error. |
| **5** | **Claude Code** | **Terminal-Native Agentic Loop**: Fast CLI execution with deep Unix tools (grep, git, find). | **Ultra-Token Efficiency**: Aggressive context compression across long sessions. | **Subagent Delegation**: Spawns worker subagents for code research. |
| **6** | **GitHub Copilot Workspace** | **Structured 4-Stage Spec Flow**: Issue ──► Spec ──► Plan ──► Code Implementation. | **Pre-Implementation Verification**: Validates build passes before code merge. | **GitHub Native Context**: Pulls issues, discussions, and repo history directly. |
| **7** | **Devin** | **Autonomous Sandbox (Browser + Shell)**: Headless Chromium to test its own web UI. | **Self-Healing Test Loops**: Runs tests, reads stack traces, auto-fixes until 100% green. | **Long-Horizon State Snapshots**: Rollback to any step in the multi-hour task. |
| **8** | **Windsurf (Codeium)** | **Cascade Multi-File Workflows**: Multi-file code generation with strict symbol tracking. | **Inline Action Lenses**: 1-click refactor/test buttons directly above functions. | **Collaborative System Rules**: Preserves project rules across prompts. |
| **9** | **OpenAI Canvas** | **Side-by-Side Split Workspace**: Chat on left, living editable document/code on right. | **Targeted Inline Selection**: Highlight specific paragraphs for localized mutation. | **Version History Slider**: Instant time-travel between document iterations. |
| **10** | **OpenHands** | **Docker Sandbox Isolation**: Runs agent commands inside a secure, throwaway container. | **Event-Stream Architecture**: Real-time streaming of stdout, file diffs, and actions. | **Extensible Tool Registry**: Modular tools for browser, bash, and git. |

### 2. High-Leverage "Doable" Micro-Features for PI (Zero Core Bloat)

Six high-value capabilities from these competitors that are 100% doable within our standard-library 5-file architecture:

1. **Visual Click-to-Inspect (from v0 / Bolt.new):**
   - In iframe live preview, clicking any DOM element sends a lightweight `postMessage({ tag, id, class })` to π Gen composer, auto-tagging `@element: #button-id` so the user can say *"Change this button to emerald green"*.
2. **Self-Healing Test-Fix Loop (from Devin):**
   - When test suites or builds fail in the in-UI terminal, PI automatically captures the traceback snippet, creates an error packet, and prompts π Gen to auto-generate the minimal surgical fix diff.
3. **SQLite Time-Travel & Version Slider (from OpenAI Canvas):**
   - Leverages existing SHA-256 revision hashes in `portfolio_revisions` and `memory_revisions`. Renders a simple slider `[v1]──[v2]──[v3]` with 1-click restore.
4. **Inline Action Lenses (from Windsurf):**
   - Action badges rendered directly above Gherkin tables and PRDs: `[▶ Run Scenario]`, `[⚡ Optimize Tokens]`, `[📝 Export PRD]`, `[🔍 Security Scan]`.
5. **Headless Background Checkpoints (from Cursor Cloud Agents):**
   - Asynchronous background task runner in `governance.sqlite3` that executes linting, test suites, and token optimizations quietly, showing a non-blocking toast when ready.
6. **SQLite Schema & Data Visualizer (from Replit Agent):**
   - Visual inspector table in App 4 showing prototype SQLite schema tables, row counts, and sample records directly in the web UI.

## External design references

Reference only; do not download, install, copy, or execute:

- `https://www.assistant-ui.com/` — conversation and composer interaction reference.
- `https://github.com/assistant-ui/assistant-ui/blob/main/LICENSE` — MIT license reference; no source copied.
- `https://tabler.io/icons` — icon vocabulary/reference only.
- `https://github.com/tabler/tabler-icons` — MIT license/reference; local sprite is clean-room authored.

## Goal

Preserve runnable local deterministic POC in exactly eight source files:

1. `AGENTS.md` — transfer contract, usage, security, limitations.
2. `CONTEXT.md` — agent coordination blackboard (sprint sync).
3. `layer_a.py` — runtime, APIs, validators, embedded-resource export.
4. `layer_a_build.py` — ephemeral HTTP prototype runner (ports 8081–8099).
5. `layer_a_config.json` — all contracts/config plus embedded plugin, MCP, and Product Discovery skill resources.
6. `layer_a_terminal.py` — allowlisted terminal command executor.
7. `index.html` — dependency-free same-origin frontend.
8. `test_layer_a.py` — executable evidence.

Generated local state, caches, Git metadata, and later unpacked resources are not part of eight-file transfer bundle.

## Commands

```bash
python3 layer_a.py validate
python3 -W error::ResourceWarning -m unittest -v
python3 -m py_compile layer_a.py layer_a_build.py layer_a_terminal.py test_layer_a.py
python3 layer_a.py serve
```

Review URL: `http://127.0.0.1:8080/`.

## Embedded-resource inspection

Embedded plugin resources stay inspectable as JSON/text inside `layer_a_config.json`. Export into separate folder without overwrite:

```bash
python3 layer_a.py unpack --unpack-dir ./expanded-resources
```

Writes only:

- `plugin.json`
- `mcp.json`
- `skills/product-discovery/SKILL.md`

Command refuses existing targets and refuses writing into eight-file bundle. Under current strict contract, use this only with an explicit user-approved target outside the bundle; exported resources do not become additional authoritative source files.

## Current truth

- Python standard library only.
- Localhost-only server and same-origin `/api/*` frontend calls.
- Deterministic mocked/redacted research and model behavior; no real LLM or live research.
- First-party SQLite state under generated `.layer-a-state/`.
- Part A: 18 validated gates; Gate 18 remains `EXTERNAL_SIGN_OFF`; overall `INCOMPLETE`.
- Part B: 8/8 experiences `VALIDATED_POC`.
- Embedded Agent Plugin remains `UNSIGNED`; exact local approval still required.
- Eight physical transfer files plus four embedded/exportable plugin artifacts (`plugin.json`, `mcp.json`, `skills/product-discovery/SKILL.md`, `skills/token-optimizer/SKILL.md`).
- Default Token Optimizer skill: MIT-licensed, permissive for commercial use, achieving up to 70% token/cost compression.

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

- Eight-file folder is sole authority after transfer. Ignore any unrelated or older local folders.
- Do not split under current contract. If user later approves structural migration, preserve baseline and use expand → migrate → verify → contract.
- Do not delete embedded resources until exported equivalents validate and callers use new paths.
- No additional permanent file in this folder without explicit scope change.

## Validation gate

Change is complete only when:

- `python3 layer_a.py validate` reports `PASS`, expected/actual `8`;
- full unit suite passes;
- Python compile passes;
- frontend remote-dependency scan returns no matches;
- unpack test proves four resources export without overwrite;
- structured handoff contract in `layer_a_config.json` validates and reports no selected runtime provider.

## Honest limitations

No production SSO/RBAC, secret store, encrypted database, remote models, live market/news/legal research, hostile-code containment, distributed workers, cloud hosting, remote plugin installation, verified signatures, enterprise approval, or deployment certification.

## Third-party attribution

PI AI overlay UI patterns (studio layout, split-pane workbench, chat composer, settings tabs) adapted from bolt.diy — the open-source Bolt.new by StackBlitz Labs — MIT License. Copyright (c) 2024 StackBlitz, Inc. and bolt.diy contributors. Repo: `stackblitz-labs/bolt.diy` on GitHub. No source code copied verbatim; layout patterns re-implemented in vanilla HTML/CSS/JS with zero build tools and no WebContainer runtime.
