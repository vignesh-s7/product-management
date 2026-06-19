# PRD 05 — Local Private LLM Stack

**Domain:** Regulated AI · Privacy
**Author:** Vignesh Vignesh S
**Status:** MVP

## Problem
Regulated buyers (banks, hospitals, government) cannot send PHI / PII / NPI to cloud LLMs but still want LangChain / LlamaIndex / RAG. Setting up a fully local, PII-encrypted stack requires assembling 6+ tools.

## Target user
Regulated-industry AI PMs, security architects, on-prem AI teams.

## Solution
A docker-compose stack: Ollama (local model) + encrypted vector store + LangChain / LlamaIndex + audit log + sample BFSI and healthcare use cases. PII never leaves the host.

### Stack
- **Model runtime:** Ollama (Llama / Qwen / Mistral)
- **Vector store:** Qdrant with at-rest AES-256
- **Orchestration:** LangChain + LlamaIndex
- **Audit:** structured log per query (no PII captured)
- **Network:** egress-deny default

## Success metrics
- 5-minute setup (`docker-compose up`)
- Zero network egress on default config (verified by iptables test)
- 1k+ GitHub stars (HN / r/LocalLLaMA viral potential)

## Deliverables
- `docker-compose.yml` + `.env.example`
- `samples/bfsi-kyc/` — local KYC doc Q&A
- `samples/healthcare-discharge/` — local discharge summary Q&A
- `audit/` — sample audit log + dashboard
- `security/threat-model.md`
- `README.md`

## Out of scope
- Production multi-tenant deployment
- Model fine-tuning
