# PRD 08 — Doc to Markdown Pipeline

**Domain:** DevTools · LLM context
**Author:** Vignesh AIPM
**Status:** MVP

## Problem
LLM context windows demand clean Markdown, but most enterprise content lives as PDFs, emails (EML / PST / MSG), Office files, scanned docs, and DocRepo. Existing converters lose structure (tables, sections, footnotes) or hallucinate content.

## Target user
AI PMs and engineers building RAG, agent context, or knowledge-base ingestion.

## Solution
A pipeline (CLI + library) that converts files / mail / PDFs into structured Markdown with preserved headings, tables, footnotes, and source-line citations. Optional Claude Skill / MCP server wrapper.

### Supported inputs
- PDF (born-digital + scanned via OCR)
- Email (EML, PST, MSG)
- Office (DOCX, XLSX, PPTX)
- HTML, RTF

### Output guarantees
- Stable heading hierarchy (no orphaned `###`)
- Tables as Markdown or HTML fallback if irregular
- Footnotes preserved
- Page / line citations for traceability

## Success metrics
- 95%+ structural fidelity on a 100-doc benchmark
- < 5s per page (no OCR), < 30s per page (OCR)
- MCP server adopted by 100+ Claude Code / Cursor users

## Deliverables
- `cli/` — Python CLI (`doc2md`)
- `mcp-server/` — MCP server wrapper
- `.claude/skills/doc-to-md/` — Claude Skill
- `benchmark/` — 100 sample docs + scoring harness
- `README.md`

## Out of scope
- Web crawling
- Real-time streaming conversion
