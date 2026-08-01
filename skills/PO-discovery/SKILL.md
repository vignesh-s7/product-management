---
name: PO-discovery
description: Generate a discovery pack — TAM/SAM/SOM, SWOT, competitor matrix, compliance risk map, and GTM brief — from repo memory context. Regulated-domain aware (BFSI/healthcare). Synthetic data only. Writes to artifacts/discovery/.
triggers:
  - "run discovery"
  - "SWOT"
  - "market sizing"
  - "competitor analysis"
  - "discovery pack"
  - "GTM brief"
---

# PO-discovery — Market & Strategy Discovery Pack

## Step 0 — Read Local Memory
Read `.agent/memory.md` in the current repository before generating anything.
Extract: `domain`, `product`, `users`, `constraints`, `compliance`, `integrations`, `glossary`.
If memory is missing, prompt the user to complete the schema — do not invent client-specific facts.

## Inputs
| Field | Required | Source |
|-------|----------|--------|
| Repo context | ✅ | `.agent/memory.md` |
| Prior artifacts | optional | `artifacts/` (local search only) |
| User focus | optional | e.g. "BFSI compliance angle", "EU market" |

## Outputs (write to `artifacts/discovery/`)
| File | Template | Description |
|------|----------|-------------|
| `swot.md` | `templates/swot.md` | Strengths, weaknesses, opportunities, threats |
| `market-sizing.md` | `templates/market-sizing.md` | TAM / SAM / SOM with assumptions |
| `competitor-matrix.md` | `templates/competitor-matrix.md` | Feature + positioning comparison |
| `compliance-risk-map.md` | *(inline)* | Domain-specific regulatory risks + mitigations |
| `gtm-brief.md` | *(inline)* | Segments, channels, pricing hypothesis, launch risks |

### Artifact frontmatter (required on every file)
```yaml
---
domain: {{domain}}
stage: discovery
type: {{swot|market-sizing|competitor-matrix|compliance-risk-map|gtm-brief}}
compliance-regime: {{hipaa|pci-dss|gdpr|eu-ai-act|generic}}
generated: {{ISO-date}}
synthetic-data: true
---
```

## Workflow
1. Read `.agent/memory.md` → note domain and compliance regime.
2. Copy templates from `skills/PO-discovery/templates/` → fill `{{placeholders}}`.
3. Generate `compliance-risk-map.md` and `gtm-brief.md` using memory context.
4. Run gate flow (delegate, do not skip):
   - `cybersec-skill` — BLOCK on PII/PHI
   - `ux-pro-skill` — BLOCK on critical a11y in any tables/diagrams; WARN on readability
   - `qa-tester-skill` — WARN if assumptions are untestable or sources missing
5. Write final pack to `artifacts/discovery/`.

## Regulated Domain Rules
| Domain | Compliance map must include |
|--------|----------------------------|
| `bfsi` | PCI-DSS, FATF/AML, fair-lending, EU-AI-Act high-risk, data residency |
| `healthcare` | HIPAA, FHIR consent, FDA SaMD class (if applicable), PHI handling |
| `eu` | GDPR DPIA, EU-AI-Act risk tier, cross-border transfer |
| `generic` | SOC 2 baseline, privacy review, vendor risk |

## Data Rules
- **Synthetic data only** — use mock company names (e.g. "Acme Health", "Demo Bank"), round-number market estimates with explicit assumption tags.
- Never include real client names, employee data, or proprietary financials from memory unless user explicitly provides synthetic equivalents.
- Cite assumption sources as `[ASSUMPTION]` or `[PUBLIC-SOURCE: description]` — no live web fetch in skill execution.

## Gate Verdict
Return a summary:
```
Discovery pack: artifacts/discovery/
Files: swot.md, market-sizing.md, competitor-matrix.md, compliance-risk-map.md, gtm-brief.md
Gates: cybersec {{PASS|BLOCK}} · ux {{PASS|WARN|BLOCK}} · qa {{PASS|WARN}}
```
