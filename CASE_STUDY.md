# Case study — productowner-skill

*A Senior PO's operating system for regulated domains: teach your local AI agent how to PO, gate every artifact through a persona swarm, and build a POC/MVP in your repo — without shipping PRDs through a vendor runtime.*

**Author:** Vignesh AIPM · Senior PO · AI / BFSI / Healthcare

---

## Problem

Every regulated-AI product I've PO'd in the last 3 years started the same way: PRD written in Confluence, architecture on a whiteboard, evals discovered 6 weeks in when the model fails an edge case. The SDLC steps exist, but they don't ladder to each other. Every handoff loses fidelity.

Worse in BFSI and healthcare: InfoSec won't approve a third-party SaaS that receives prompts, artifacts, or telemetry. The PO workflow has to run **inside** the client's environment — with gates that block PII/PHI leakage before anything gets committed.

Question: can a single-PO operating system reduce the PRD-to-gated-artifact distance from weeks to hours, **without** a vendor runtime, **without** hallucinating requirements, and **without** sending data anywhere?

---

## Approach

**productowner-skill is a skills library, not a platform.** We ship markdown `SKILL.md` files. Your client-side AI agent (Cursor, Claude Code, Antigravity, etc.) is the runtime.

Two end users:

| End user | Role |
|----------|------|
| **Humans** | POs, PO leads, designers, engineers, InfoSec — set intent, review gate outputs, approve POC/MVP |
| **Client-side AI agents** | Read skills + `.agent/memory.md`, run discovery → delivery → gates, write artifacts and POC code locally |

```
Human (PO) ──intent──► Client AI Agent (local)
                              │
                              ├── reads skills/ (copied once into your repo)
                              ├── reads .agent/memory.md (your repo)
                              ├── runs persona swarm gates (local)
                              └── writes artifacts/ + POC/MVP (your repo)

productowner-skill repo ──provides skills only──► no runtime connection
```

### What ships today (Phase 1)

1. **Persona skills** — `productowner-skill` orchestrates; `PO-discovery` and `PO-delivery` produce structured packs; `PO-kb-research` searches local artifacts.
2. **Persona swarm gates** — run on the client agent before release:
   - `cybersec-skill` — **BLOCK** on PII/PHI or critical OWASP
   - `ux-pro-skill` — **BLOCK** on critical a11y; **WARN** on style drift
   - `qa-tester-skill` — **WARN** on missing edge cases (never blocks)
   - `y-score-readiness` — **BLOCK** if launch-readiness score &lt; 70
3. **Zero vendor execution** — nothing in `skills/` runs at install. No `orchestrate.sh`. No API to call. No telemetry. No data egress to us.

### What's Phase 5 (not shipped yet)

- `prd-to-sdlc` — full PRD → architecture + code skeleton + eval harness via MetaGPT / OpenHands / Promptfoo
- `orchestrate.sh` — staged pipeline trigger (`--stage discovery|delivery|release|all`)
- GitHub Actions full pipeline on PRD commit
- Hosted SaaS, multi-tenant billing (Phase 6)

The skills library is honest about this boundary. Phase 1 delivers gated discovery and delivery packs; your agent builds POC/MVP code from Gherkin AC — we don't run MetaGPT for you.

---

## Trade-offs

| Choice | Alternative | Why we picked this |
|---|---|---|
| Markdown skills (client agent runtime) | SaaS PO platform | Regulated PMs cannot ship PRDs through third-party services. Data stays local. |
| Persona swarm gates (BLOCK/WARN) | Single-prompt review | Multi-persona catches PII, a11y, and untestable AC before commit — not after demo day. |
| Declarative skill delegation | `orchestrate.sh` shell orchestration | Shell scripts are hard to audit in InfoSec review. Skills are plain markdown. |
| Synthetic data in all examples | Realistic demo fixtures | BFSI/healthcare reviewers need proof we never embed live PII/PHI. |
| Portfolio demo (`docs/`) separate from skills | Demo as product runtime | Illustrates what PO workflows *look like*; skills are the product. |

---

## Outcome (illustrative, from pilot use)

These numbers come from regulated-domain pilots where a human PO triggered their **local** agent with our skills installed. They are not vendor-hosted benchmarks.

| Metric | Before | With skills + local agent |
|--------|--------|---------------------------|
| PRD → gated delivery pack | 3–6 weeks | ~90 minutes (discovery + PRD + gates) |
| PII/PHI caught pre-commit | Ad hoc review | cybersec-skill BLOCK on every artifact |
| Initial eval cases from AC | Manual, late | Gherkin AC + qa-tester-skill WARN gaps surfaced in-session |
| InfoSec review cycles | 2–3 rounds | 1 round when paired with [INFOSEC-ONEPAGER.md](docs/INFOSEC-ONEPAGER.md) |

**What actually ships in the repo today:**

- Discovery pack (SWOT, TAM/SAM/SOM, competitor matrix, compliance map)
- Delivery pack (PRD with Gherkin AC, RICE backlog, KPI plan, rollout phases)
- Gate verdict JSONs (cybersec, UX, QA, Y-Score) — see [examples/golden-run/gates/](examples/golden-run/gates/)
- POC/MVP code generated by the **client agent** in the user's repo (not pre-built by us)

**What Phase 5 will add:** automated SDLC bundle (architecture diagram, DB schema, scaffold code, Promptfoo eval suite) via `prd-to-sdlc`.

---

## Postmortem

What didn't work:

1. **First narrative positioned this as a SaaS orchestration platform** — InfoSec reviewers asked where data flows. Rewrote the product model: skills only, client agent executes, zero egress. Fixed in README, TRUST.md, and this case study.
2. **Early docs referenced `orchestrate.sh` and MetaGPT as shipped** — they are Phase 5. Skills now declare "delegate declaratively; do not execute bash orchestration." Fixed.
3. **Free-form agent prompts produced prose, not parseable artifacts** — restructured as Skills with explicit output schemas, YAML frontmatter, and gate JSON contracts. Fixed.
4. **Auto-generated content over-tested happy paths** — qa-tester-skill now WARNs on missing negative cases; non-goals in PRD map to adversarial test suggestions.

What's next:

- Phase 2: optional enterprise KB integrations (Rovo, M365, Google) as **client-configured** — still no vendor runtime
- Phase 5: `prd-to-sdlc` + `orchestrate.sh` for full pipeline automation
- Publish walkthroughs for BFSI credit-risk and healthcare FHIR POC sessions ([examples/walkthroughs/](examples/walkthroughs/))

---

## What this proves

An AI PO can codify their own workflow as **auditable, installable skills** — not as a black-box SaaS. The tool is not the value. *The ability to expose how you PO, gate it for regulated domains, and let the client's agent execute locally* is the value.

InfoSec approves markdown instructions that never phone home. Humans set intent. Client agents build POC/MVPs. We ship the playbook.

---

- 🌐 [Portfolio demo](https://vvs-PO.github.io/productowner-skill/) (illustrative UI — not the runtime)
- 📖 [Repo](https://github.com/vvs-PO/productowner-skill)
- 🧠 [productowner-skill](./.cursor/skills/productowner-skill/SKILL.md)
- ⚡ [y-score-readiness](./.cursor/skills/y-score-readiness/SKILL.md)
- 🔒 [InfoSec one-pager](./docs/INFOSEC-ONEPAGER.md)
- 📅 Feedback / collaboration: [book 15 min](https://cal.com/Vignesh/15min)
