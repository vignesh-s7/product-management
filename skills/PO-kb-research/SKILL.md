---
name: PO-kb-research
description: Search the local knowledge base for prior artifacts, reference PRDs, and reusable templates. Returns a ranked list with path, relevance score, and reuse recommendation. No network access — local filesystem only.
triggers:
  - "search KB"
  - "find prior artifact"
  - "reuse template"
  - "what have we done before"
  - "search artifacts"
---

# PO-kb-research — Local Artifact Search

Search the repository's local knowledge base for reusable artifacts before generating new content. Prevents duplicate work and surfaces proven templates.

## Mandatory first step

**Read `.agent/memory.md`** before any search. Use `product_name`, `domain`, `compliance_regimes`, and `glossary` to interpret queries and rank results.

## When to trigger

- User says "search KB", "find prior artifact", or "reuse template"
- Before starting discovery or delivery — check if a similar artifact already exists
- When a PO asks "what have we done before for [domain/topic]?"
- Auto-invoked by `PO-discovery` and `PO-delivery` at session start

## Search scope (local only)

Search **only** these directories:

| Path | Contents |
|------|----------|
| `artifacts/` | Generated outputs from prior skill sessions |
| `prds/` | Reference PRDs and platform documentation |
| `skills/*/templates/` | Reusable markdown templates per skill |

### Prohibited actions

- **NO network access** — do not curl, wget, fetch URLs, or invoke web search
- **NO external API calls** — Jira, Confluence, M365, Google deferred to Phase 2
- **NO reading outside scope** — do not search `node_modules/`, `.git/`, or system paths

## Search procedure

1. **Load context** — Read `.agent/memory.md` for domain, users, and compliance regimes.
2. **Parse query** — Extract keywords: topic, domain (bfsi/healthcare/generic), artifact type (PRD, SWOT, ROI, KPI), stage (discovery/delivery/security/qa).
3. **Scan directories** — List and read file headers (first 50 lines) in `artifacts/`, `prds/`, and `skills/*/templates/`.
4. **Score relevance** — Rank each match 0–100 based on:
   - Keyword overlap with query (40%)
   - Domain alignment with `.agent/memory.md` (25%)
   - Artifact type match (20%)
   - Recency / completeness signals in frontmatter (15%)
5. **Recommend reuse** — For each result, state: `COPY`, `ADAPT`, or `REFERENCE_ONLY`.

## Reuse recommendations

| Recommendation | When to apply |
|----------------|---------------|
| `COPY` | Template is domain-agnostic or exact domain match; fill placeholders only |
| `ADAPT` | Partial match — reuse structure, update domain-specific sections |
| `REFERENCE_ONLY` | Historical context useful but outdated or different compliance regime |

## Output format

Return a ranked list in this structure:

```markdown
## KB Search Results

**Query:** [user's search terms]
**Domain context:** [from .agent/memory.md]
**Directories searched:** artifacts/, prds/, skills/*/templates/

| Rank | Path | Relevance | Type | Recommendation | Summary |
|------|------|-----------|------|----------------|---------|
| 1 | prds/02-regulated-rag-eval-harness.md | 92 | PRD | ADAPT | Regulated RAG eval harness — healthcare domain, strong eval plan |
| 2 | skills/PO-discovery/templates/swot.md | 78 | Template | COPY | Generic SWOT template with compliance section |
| 3 | artifacts/2026-07-discovery-pack-bfsi.md | 65 | Discovery Pack | REFERENCE_ONLY | Prior BFSI discovery — pre-Phase 1 schema |

### Top pick
**Path:** [highest-ranked path]
**Action:** [COPY | ADAPT | REFERENCE_ONLY]
**Rationale:** [one sentence]
```

If no matches found, state explicitly and suggest which template in `skills/*/templates/` to create from.

## Artifact tagging (for new outputs)

When writing search results or recommending artifact creation, enforce the tagging schema from `.agent/memory.md`:

```
domain · stage · type · compliance-regime
```

Example: `bfsi · discovery · swot · pci-dss`

## Author

Vignesh AIPM — local KB search for regulated PO workflows. Enterprise API federation deferred to Phase 2.
