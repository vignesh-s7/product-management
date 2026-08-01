# AI Use Cases (2026) — productowner-skill Library

This repository is a **skills library only**. Client-side AI agents (Claude Code, Cursor, Copilot, etc.) read `SKILL.md` instructions locally and execute them in the developer's environment. There is no vendor runtime, no hosted orchestrator, and no connection back to this repo at execution time.

## How agents use the library

1. **Clone or browse** — pull skills from `skills/` or `.cursor/skills/`.
2. **Load a skill** — the agent reads declarative markdown (`SKILL.md`) as its playbook.
3. **Execute locally** — the agent runs tools, edits files, and calls models using the user's own API keys and infrastructure.
4. **Optional Phase 5 tooling** — on the **client side**, teams may wire MetaGPT, OpenHands, Promptfoo, or other tools into their own pipelines. These are optional integrations the user owns; this repo does not execute them.

## Per-PRD recommended pairings

| PRD type | Best crew (client-side) | Eval focus |
|---|---|---|
| Framework / spec (PRD 1, 6) | Just Claude Code | link-check, schema validation |
| Eval tooling (PRD 2) | MetaGPT + Promptfoo | F1 / precision/recall on golden set |
| Multi-agent (PRD 3) | CrewAI / LangGraph + MetaGPT | provenance + guardrail tests |
| Healthcare interop (PRD 4, 7) | LangGraph + FHIR MCP | data fidelity + p95 latency |
| Privacy / local LLM (PRD 5) | Ollama + LangChain | egress audit + setup time |
| DevTools (PRD 8) | Aider + OpenHands | benchmark fidelity |

## Multi-model strategy

- **Claude Opus 4.7** — primary generation (architecture, code)
- **Gemini 2.x** — long-context critic + dashboard summariser
- **Grok** — second-opinion judge (catches Claude overconfidence)
- **Ollama + Llama 3** — private fallback for PHI / regulated data

## Cost envelope per PRD run (client-side estimates)

| Stage | Tokens | Cost @ 2026 rates |
|---|---|---|
| PO Gate (Y-Score) | 2k / 500 | $0.01 |
| Architect | 8k / 3k | $0.06 |
| Engineer (OpenHands loop) | 30k / 10k | $0.25 |
| QA (Promptfoo) | 5k / 1k | $0.03 |
| **Total per PRD** | ~45k / 14.5k | **~$0.35** |

8 PRDs in the demo gallery → **< $3 total** to regenerate the entire portfolio (when run on the client's own model accounts).

## Limitations

- Skills are **instructions only** — no shell orchestration, no remote execution, no artifact upload from this repo.
- MetaGPT / OpenHands integration is **Phase 5 optional** and must be configured by the user on their machine or CI.
- Cloudflare deploy (if used) requires the user's own token in their GitHub Secrets — not ours.
