# PRD 04 — FHIR + Kafka + APIM Pattern

**Domain:** Healthcare interop
**Author:** Vignesh AIPM
**Status:** MVP

## Problem
Healthcare AI needs FHIR data in real time, but most integration guides stop at REST polling. Streaming FHIR via Kafka with Azure APIM as the consumer gateway is rare in public docs despite being a common enterprise pattern.

## Target user
Healthcare architects, integration PMs, AI teams building on FHIR.

## Solution
A reference pattern: FHIR R4 resources → Kafka topics (one per resource type) → Azure APIM consumer endpoints → downstream AI / analytics consumers. HIPAA-aware (encryption, audit, consent propagation).

## Success metrics
- p95 FHIR-event-to-consumer latency ≤ 2s
- 100% audit-log coverage on PHI access
- Zero PHI in topic names / partition keys

## Deliverables
- `architecture.md` — Mermaid diagram + sequence
- `topics.md` — topic naming, partition strategy, retention
- `apim-policies/` — sample APIM policy XML (rate limit, auth, audit)
- `consumers/python-sample/` — minimal Kafka consumer skeleton
- `compliance/hipaa-checklist.md`
- `README.md`

## Out of scope
- Production Kafka deployment
- FHIR server choice
