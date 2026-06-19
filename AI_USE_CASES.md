# AI Use Cases (2026) — pm-os Console

The Console itself is the meta-AI use case. It composes:
- **MetaGPT** (47K★) — Architect / Engineer / QA roles
- **OpenHands** (40K★) — autonomous coding loops
- **Aider** — surgical edits
- **Promptfoo** — mandatory eval gate
- **Onlook / v0** — UI scaffolding
- **Wrangler / Cloudflare Pages** — free public deploys

## Per-PRD recommended pairings
| PRD type | Best crew | Eval focus |
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

## Cost envelope per PRD run
| Stage | Tokens | Cost @ 2026 rates |
|---|---|---|
| PM Gate (Y-Score) | 2k / 500 | $0.01 |
| Architect | 8k / 3k | $0.06 |
| Engineer (OpenHands loop) | 30k / 10k | $0.25 |
| QA (Promptfoo) | 5k / 1k | $0.03 |
| **Total per PRD** | ~45k / 14.5k | **~$0.35** |

8 PRDs in the demo gallery → **< $3 total** to regenerate the entire portfolio.

## Limitations
The Console is a prototype: real MetaGPT / OpenHands wiring lives in `orchestrate.sh` (currently stubs — see issues). Cloudflare deploy needs a token in GitHub Secrets.
