# Golden Run — Human Intent → Client Agent → Outputs

Synthetic example of the dual end-user flow: a human PO sets intent; a **client-side AI agent** (Cursor, Claude Code, etc.) reads skills + memory and produces artifacts and gate verdicts **locally** in the client's repo.

No data is sent to productowner-skill. We provide skills only.

---

## Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. HUMAN — sets intent in IDE                                   │
│    "Act as Product Owner — run discovery for a fintech POC"     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│ 2. CLIENT AGENT — reads locally                                   │
│    • skills/productowner-skill, PO-discovery, PO-delivery, …    │
│    • .agent/memory.md (see .agent/memory.example.md)            │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│ 3. DISCOVERY — PO-discovery                                     │
│    → artifacts/discovery/sample-swot.md (synthetic)             │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│ 4. DELIVERY — PO-delivery                                       │
│    → artifacts/delivery/sample-prd-excerpt.md (Gherkin AC)       │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│ 5. PERSONA SWARM GATES (local verdict JSON)                     │
│    cybersec → ux-pro → qa-tester → y-score-readiness            │
│    → gates/*.json (examples in this folder)                       │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│ 6. HUMAN — reviews gates, approves POC/MVP in their repo        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Files in this example

| Path | Description |
|------|-------------|
| `.agent/memory.example.md` | Minimal memory for a fintech POC |
| `artifacts/discovery/sample-swot.md` | Synthetic discovery output |
| `artifacts/delivery/sample-prd-excerpt.md` | Synthetic PRD excerpt with Gherkin AC |
| `gates/cybersec-pass.json` | Security gate — pass |
| `gates/ux-warn.json` | UX gate — warn (style drift) |
| `gates/qa-warn.json` | QA gate — warn (coverage gap) |
| `gates/y-score.json` | Y-Score readiness — go (score ≥ 70) |

---

## How to reproduce

1. Copy skills per [docs/INSTALL.md](../../docs/INSTALL.md).
2. Copy `.agent/memory.example.md` to your repo as `.agent/memory.md` and edit.
3. In your IDE agent, trigger: **"Act as Product Owner — run discovery for [your problem]"**.
4. Run delivery and gates per [skills/productowner-skill/SKILL.md](../../skills/productowner-skill/SKILL.md).

All outputs are synthetic. Replace with validated research before external distribution.
