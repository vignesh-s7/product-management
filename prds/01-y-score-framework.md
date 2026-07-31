# PRD 01 — Y-Score Framework

**Domain:** PO tooling · framework
**Author:** Vignesh AIPM
**Status:** MVP

## Problem
PMs ship AI features without a shared rubric for "is this ready to launch?" Subjective gut-checks lead to premature launches in regulated domains (BFSI, healthcare) where rollback is expensive or impossible.

## Target user
Product Owners and product owners shipping AI/GenAI features in regulated industries.

## Solution
A 7-dimension scoring rubric — the **Y-Score** — that scores a pilot/MVP against launch-readiness criteria. Each dimension is weighted; total ≥ 70% gates launch.

### The 7 dimensions
1. **Problem clarity** — one-sentence problem statement, measurable
2. **Target user** — named persona + JTBD
3. **Success metric** — leading + lagging, with baselines
4. **Constraints** — latency / cost / compliance budget defined
5. **Compliance posture** — HIPAA / PCI / GDPR / EU-AI-Act checklist done
6. **Eval plan** — golden set + regression suite + LLM-as-judge calibrated
7. **Rollback plan** — kill switch + comms + data-recovery path

## Success metrics
- 50+ teams adopt the rubric in 6 months
- Median time-to-launch-decision drops 40%
- Zero post-launch rollbacks among adopting teams

## Deliverables
- `README.md` — what / why / how
- `scoring-rubric.md` — full rubric with anchors
- `template.json` — machine-readable schema
- `examples/` — 3 worked examples (BFSI loan approval, healthcare wellness, KYC)

## Out of scope
- Web app / dashboard (v1 is markdown + spreadsheet)
- Automated scoring from PRD (that's `prd-to-sdlc` skill)
