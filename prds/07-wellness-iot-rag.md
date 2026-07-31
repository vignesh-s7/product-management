# PRD 07 — Wellness IoT RAG

**Domain:** Healthcare · IoT
**Author:** Vignesh AIPM
**Status:** MVP

## Problem
Consumer wearables emit raw biometric data (HbA1c, BP, HR, steps, sleep) but apps deliver generic advice. Users want personalized, evidence-grounded recommendations and alerts on clinically meaningful thresholds.

## Target user
Health-app PMs, digital-therapeutic teams, wearable platform integrators.

## Solution
A reference architecture: Android Health Connect / CloudVendor Fit / Apple Health → ingestion pipeline → time-series store → RAG over clinical guideline corpus (ADA, JNC-8, WHO) → personalized AI recommendations + threshold alerts.

### Flow
1. Ingest from Health Connect / CloudVendor Fit / Apple Health
2. Normalize to FHIR Observation resources
3. Detect clinically significant deltas (HbA1c > 7%, BP > 140/90, etc.)
4. RAG-grounded recommendation citing guideline source
5. Alert delivery (push / SMS / EHR)

## Success metrics
- Recommendation source citation: 100%
- Alert precision ≥ 90% (synthetic golden set)
- Setup-to-first-recommendation: < 60s

## Deliverables
- `architecture.md` — Mermaid flow
- `ingest/` — sample Health Connect / Fit / HealthKit ingestion stubs
- `guidelines/` — open clinical guideline corpus (ADA, JNC-8 abstracts only — public)
- `rag/` — LlamaIndex config
- `alerts/` — threshold definitions JSON
- `compliance/hipaa-checklist.md`
- `README.md`

## Out of scope
- Diagnostic claims (recommendation only)
- Real EHR write-back
