# PRD 02 — Regulated RAG Eval Harness

**Domain:** Eval · BFSI · Healthcare
**Author:** Vignesh AIPM
**Status:** MVP

## Problem
Teams ship RAG systems into loan/policy/claim approval workflows without rigorous eval. "It works in demo" is not enough when a wrong answer creates audit liability.

## Target user
AI PMs and ML engineers building decision-support RAG in regulated domains.

## Solution
A Python eval harness that wraps Promptfoo + LLM-as-judge with regulated-domain extensions: precision / recall / F1 on approval decisions, hallucination detection against source corpus, cost-per-decision tracking, latency SLOs.

## Success metrics (proven pattern)
- Move approval accuracy from MVP baseline → 99%+ via eval-driven RAG iteration (replicating the 75% → 99% lift from production work, sanitized).
- p95 latency ≤ 3s; cost ≤ $0.05 per decision.
- Zero hallucinated approvals on golden set.

## Deliverables
- `harness/` — Python package (eval runner, judges, scorers)
- `golden-sets/` — synthetic golden sets for loan / policy / claim approval
- `promptfooconfig.yaml` — Promptfoo config preset
- `reports/` — HTML eval reports with drift charts
- `README.md` — quickstart + methodology

## Out of scope
- Vector DB choice (BYO)
- Model fine-tuning
