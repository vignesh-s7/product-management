# Gate output schemas

JSON Schema definitions for persona-swarm gate verdicts. Each gate skill emits a single JSON object matching its schema as the **final structured result** of a review.

## Schemas

| File | Skill | Verdict values |
|------|-------|----------------|
| [`cybersec-gate.schema.json`](cybersec-gate.schema.json) | `cybersec-skill` | `pass` · `block` · `warn` |
| [`ux-gate.schema.json`](ux-gate.schema.json) | `ux-pro-skill` | `pass` · `warn` · `block` |
| [`qa-gate.schema.json`](qa-gate.schema.json) | `qa-tester-skill` | `pass` · `warn` (never `block`) |
| [`y-score-gate.schema.json`](y-score-gate.schema.json) | `y-score-readiness` | `go` · `no-go` (with `score` 0–100) |

## Golden examples

Synthetic gate outputs live under [`examples/golden-run/gates/`](../../examples/golden-run/gates/):

| Example | Schema |
|---------|--------|
| `cybersec-pass.json` | `cybersec-gate.schema.json` |
| `ux-warn.json` | `ux-gate.schema.json` |
| `qa-warn.json` | `qa-gate.schema.json`¹ |
| `y-score.json` | `y-score-gate.schema.json` |

¹ `qa-warn.json` uses the legacy field name `coverage_gaps`; canonical name is `edge_case_gaps` (same object shape). Rename when updating examples.

## Usage

### Validate a gate output (Node.js)

```bash
npm install --save-dev ajv ajv-formats
node --input-type=module -e "
import Ajv from 'ajv';
import addFormats from 'ajv-formats';
import { readFileSync } from 'node:fs';

const ajv = new Ajv({ allErrors: true });
addFormats(ajv);

const schema = JSON.parse(readFileSync('schemas/gates/cybersec-gate.schema.json', 'utf8'));
const data = JSON.parse(readFileSync('examples/golden-run/gates/cybersec-pass.json', 'utf8'));

const validate = ajv.compile(schema);
if (!validate(data)) {
  console.error(validate.errors);
  process.exit(1);
}
console.log('valid');
"
```

### Agent workflow

1. Run the gate skill on the target artifact (see skill `SKILL.md` for triggers and intensity).
2. Parse the final JSON block from the skill response.
3. Optionally validate against the matching schema before writing to `artifacts/gates/<gate>-<timestamp>.json`.
4. Respect verdict semantics in the persona swarm chain (see root [`README.md`](../../README.md#persona-swarm-gate-model)).

### Field notes

- **cybersec** — `blockers` non-empty or PII/PHI detected ⇒ `verdict: "block"`. `checks` maps named sub-scans (`pii_phi_scan`, `owasp_review`, etc.) to `pass` | `warn` | `fail` | `skip`.
- **ux** — critical `wcag_failures` ⇒ `block`; style drift or low `flow_score` ⇒ `warn`.
- **qa** — `test_matrix_ref` points at the markdown/JSON test matrix; `edge_case_gaps` lists missing boundary or negative cases.
- **y-score** — `score` ≥ 70 with empty `blockers` ⇒ `verdict: "go"`; otherwise `no-go`.
