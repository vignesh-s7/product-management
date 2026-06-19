# PRD 03 — Multi-Agent Credit Risk Reference

**Domain:** BFSI · Agentic AI
**Author:** Vignesh Vignesh S
**Status:** MVP

## Problem
Banks want agentic credit-risk scoring but lack a reference architecture that satisfies risk, compliance, and ops simultaneously. Most public examples are toy notebooks.

## Target user
BFSI architects, AI PMs, risk officers evaluating agentic systems for credit decisioning.

## Solution
A reference architecture (no client data, no production code) for a multi-agent credit-risk orchestration: deep-RAG retrieval, multi-step reasoning, guardrails, anti-hallucination patterns, dual-backend (AWS Bedrock + Azure OpenAI) for resilience.

### Agents
- **Ingestion agent** — pulls bureau, bank, KYC, statement data
- **Feature agent** — derives risk features
- **Reasoning agent** — deep-RAG over policy corpus, multi-hop
- **Guardrail agent** — checks FATF / BSA / fair-lending constraints
- **Decision agent** — score + rationale + audit trail

## Success metrics
- Decision rationale traceable to source policy clause (100%)
- Hallucination rate < 0.1% on synthetic golden set
- p95 decision time ≤ 4s

## Deliverables
- `architecture/` — Mermaid C4 diagrams (system, container, component)
- `agents/` — agent role specs (markdown)
- `guardrails/` — anti-hallucination + compliance prompts
- `evals/` — Promptfoo config + golden set (synthetic)
- `README.md`

## Out of scope
- Production deployment code
- Real bureau / bank integrations
