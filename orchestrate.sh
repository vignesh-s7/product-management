#!/usr/bin/env bash
# pm-os orchestrator — thin shim that routes a PRD through upstream agent crews.
# Heavy lifting: MetaGPT (arch/code), OpenHands (autonomous coding), Promptfoo (eval).
set -euo pipefail

PRD="${1:-}"
[ -z "$PRD" ] && { echo "Usage: $0 <prd.md>"; exit 1; }
[ -f "$PRD" ] || { echo "PRD not found: $PRD"; exit 1; }

NAME=$(basename "$PRD" .md | sed 's/^[0-9]*-//')
OUT="outputs/$NAME"
mkdir -p "$OUT"

echo "▶ pm-os: $NAME"
echo "  PRD: $PRD"
echo "  Out: $OUT"

# ── Stage 1: PM gate — Y-Score readiness check ──────────────────────────────
echo "[1/6] PM gate — Y-Score readiness check"
# TODO: invoke .claude/skills/y-score-readiness/ via Claude
cp "$PRD" "$OUT/PRD.md"

# ── Stage 2: Architect — MetaGPT ────────────────────────────────────────────
echo "[2/6] Architect — MetaGPT (arch + db schema)"
# Requires: pip install metagpt
# metagpt "$(cat $PRD)" --project-path "$OUT"
echo "  (stub — wire MetaGPT here)"

# ── Stage 3: Designer — UI scaffold ─────────────────────────────────────────
echo "[3/6] Designer — UI scaffold"
mkdir -p "$OUT/ui"
echo "  (stub — wire v0 / Onlook here)"

# ── Stage 4: Engineer — OpenHands autonomous build ──────────────────────────
echo "[4/6] Engineer — OpenHands"
# Requires: docker run -e LLM_API_KEY=$ANTHROPIC_API_KEY ghcr.io/all-hands-ai/openhands ...
echo "  (stub — wire OpenHands here)"

# ── Stage 5: QA — Promptfoo + Playwright ────────────────────────────────────
echo "[5/6] QA — Promptfoo evals"
mkdir -p "$OUT/evals"
echo "  (stub — wire Promptfoo here)"

# ── Stage 6: DevOps — Cloudflare Pages ──────────────────────────────────────
echo "[6/6] DevOps — Cloudflare Pages deploy"
if [ -n "${CLOUDFLARE_API_TOKEN:-}" ]; then
  echo "  (stub — wrangler pages deploy $OUT/ui)"
else
  echo "  Skipped: CLOUDFLARE_API_TOKEN not set"
fi

echo "✓ Done: $OUT"
