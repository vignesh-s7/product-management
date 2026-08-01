# Security Policy

## Reporting a Vulnerability

Please open an issue tagged `security` or email vigneshaipm@gmail.com. Response target: 48 hours.

## Supported Versions

Latest tagged release only.

## Scope

This is a public-safe **skills library** and case-study repo. It contains no production credentials, PII, or client data.

---

## Data Handling

| Policy | Detail |
|---|---|
| **Zero data retention** | This repo does not collect, store, or process user data. There is no backend, database, or telemetry endpoint. |
| **No profiling** | We do not build user profiles, track usage patterns, or fingerprint clients. |
| **No telemetry** | No analytics beacons, crash reporters, or usage pings are embedded in skills or docs. |

All execution happens on the **client side** — in the developer's IDE, terminal, or CI runner. Nothing is sent to us.

---

## Execution Model

### What runs

- **`SKILL.md` instructions only** — declarative markdown that a client-side AI agent reads and follows locally.
- **Static docs** — HTML/markdown served via GitHub Pages for demonstration purposes (demo data only).

### What does NOT run

- **No vendor runtime** — we do not host agents, orchestrators, or model endpoints.
- **No backend** — there is no API server, webhook receiver, or job queue owned by this project.
- **No OAuth to us** — skills do not initiate authentication flows against our infrastructure.
- **No API keys to us** — skills never request, store, or transmit credentials to this project.

Client-side agents use **their user's own** API keys, cloud accounts, and tooling.

---

## No Executables in Skills

The `skills/` and `.cursor/skills/` directories contain **markdown only**:

- No `.sh`, `.py`, `.exe`, or other executable files.
- No `curl`/`wget` download instructions that pull and run remote code.
- No references to `orchestrate.sh` or shell-based orchestration.

CI enforces this via `scripts/check-source.mjs`.

---

## PII / PHI Policy

- **Synthetic data only** — all examples, PRDs, and demo content use fictional personas and placeholder data.
- **No real PII or PHI** — do not commit patient records, financial account data, government IDs, or live credentials.
- **Regulated workloads stay local** — if a skill guides healthcare or BFSI work, the user must run it in their own compliant environment with their own data controls.

---

## GDPR / HIPAA Posture (Skills Library)

Because this project is a **static skills library with no runtime**:

| Regulation | Posture |
|---|---|
| **GDPR** | No personal data is processed by us. Users who load skills into their own agents remain the data controller for any data they process locally. |
| **HIPAA** | We are not a Business Associate — there is no hosted service that touches PHI. Skills that reference healthcare patterns are instructional only; HIPAA compliance is the user's responsibility in their deployment. |
| **EU AI Act** | Skills may include readiness-check guidance (e.g. Y-Score rubric) but do not deploy AI systems on behalf of users. |

---

## CI / GitHub Actions

The `prd-pipeline.yml` workflow performs **read-only, declarative validation**:

- Confirms PRD paths exist and match naming conventions.
- Checks PRD markdown for minimum sections (Problem, Target user).
- Does **not** execute repo shell scripts, upload artifacts, or reference secrets.

Permissions are scoped to `contents: read`. Actions are pinned by commit SHA.

---

## What Users Should Do

1. Review any `SKILL.md` before loading it into an agent — treat it like any third-party prompt.
2. Run agents in an environment you control; never paste real PII/PHI into demo skills.
3. Rotate your own API keys if a skill suggests patterns that touch external services.
4. Report suspicious content via the vulnerability channel above.
