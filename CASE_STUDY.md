# Case study — productowner-skill

*A Senior PO's Persona Swarm: turn a PRD into a full SDLC by orchestrating Claude Skills + MetaGPT + Promptfoo. Public MVP shipped 2026-06 as v1.0.*

## Problem

Every regulated-AI product I've PO'd in the last 3 years started the same way: PRD written in WikiBoard, architecture on a whiteboard, evals discovered 6 weeks in when the model fails an edge case. The SDLC steps exist, but they don't ladder to each other. Every handoff loses fidelity.

Question: can a single-PO Persona Swarm reduce the PRD-to-eval-ready distance from weeks to hours, without hallucinating requirements?

## Approach

Three composed layers, each doing one thing:

1. **Claude Skills** (`prd-to-sdlc`, `y-score-readiness`) — canonical prompts that transform a PRD into structured artifacts (FRD, SRS, ADRs, initial eval cases). Not free-form generation. Structured output only.
2. **MetaGPT** — takes structured artifacts and produces architecture diagrams + starter code scaffolds. Runs as a multi-role agent (PO, architect, engineer, QA).
3. **Promptfoo** — auto-generates an initial eval suite from the PRD's acceptance criteria. Every requirement becomes a case; every non-goal becomes a negative case.

Output: a release-ready SDLC package — FRD, SRS, architecture diagram, scaffold code, eval suite that can run in CI on day one.

## Trade-offs

| Choice | Alternative | Why we picked this |
|---|---|---|
| Claude Skills (canonical prompts) | Fine-tuned model | Skills are portable, versionable, auditable. Fine-tuning locks you in. |
| MetaGPT multi-role | Single-prompt orchestration | Multi-role produces better structured outputs; single-prompt drifts. |
| Promptfoo | Custom eval runner | Adoption > custom. Contributors already know the format. |
| Runs locally (no server) | SaaS deployment | Data control. Regulated-AI PMs cannot ship PRDs through a third-party service. |

## Outcome (illustrative, from pilot use)

- PRD → eval-ready package: **~90 minutes**, from previous 3-6 weeks
- FRD/SRS produced automatically with structured traceability to PRD acceptance criteria
- 30-50 initial eval cases per PRD, based on stated requirements + non-goals
- Public MVP shipped as v1.0 in 3 weeks (weekly cadence, small PRs)

## Postmortem

What didn't work:

1. **First attempt used free-form Claude prompts** — outputs were prose, not parseable. Restructured as Skills with explicit output schemas. Fixed.
2. **MetaGPT hallucinated architecture components** not implied by the PRD. Added a "grounding pass": MetaGPT must cite the PRD line that motivated each architectural choice.
3. **Auto-generated eval suite over-tested acceptance criteria, under-tested negative cases.** Added explicit non-goal → adversarial-case mapping.

What's next in v2.0:

- Wire `productowner-skill` output directly to `agentic-compliance-evals` for eval schema compatibility
- Add ADR generation from PRD assumptions
- Publish 3rd Claude Skill: `postmortem-from-eval-failure`

## What this proves

An AI PO can codify their own workflow as public tooling. The tool is not the value — *the ability to expose how you PO* is the value. This case study, the tool, and the outcome are the artifact.

---

- 🌐 [Live app](https://vvs-PO.github.io/productowner-skill/)
- 📖 [Repo](https://github.com/vvs-PO/productowner-skill)
- 🧠 [prd-to-sdlc skill](./.claude/skills/prd-to-sdlc/SKILL.md)
- ⚡ [y-score-readiness skill](./.claude/skills/y-score-readiness/SKILL.md)
- 📅 Feedback / collaboration: [book 15 min](https://cal.com/Vignesh/15min)
