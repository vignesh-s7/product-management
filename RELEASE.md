# Release process

This repository ships a **skills library** (markdown-only personas and gates). Releases are tagged on `main` with semantic version tags (`v*`). Client agents consume skills locally; there is no vendor runtime.

## Creating a release

1. Merge all changes to `main` with passing CI (`npm run check`, `npm test`).
2. Update `CHANGELOG.md` and bump `package.json` version if applicable.
3. Create and push an annotated tag:
   ```bash
   git tag -a v0.6.0 -m "v0.6.0 — signed skills manifest"
   git push origin v0.6.0
   ```
4. The **Release checksums** workflow (`.github/workflows/release-checksums.yml`) runs automatically on tag push. It generates `checksums/SKILLS.sha256` and uploads it as a workflow artifact.
5. Attach the artifact (or the manifest file) to the GitHub Release notes for consumers.

## What is checksummed

The manifest covers every file under:

- `skills/`
- `.cursor/skills/`
- `schemas/`

Paths are relative to the repository root. The manifest is regenerated on each tagged release — do not hand-edit it.

## Generating checksums locally

```bash
npm run checksums
```

Output: `checksums/SKILLS.sha256` (one line per file: `<sha256>  <relative-path>`).

## Verifying checksums (consumers)

After downloading or cloning a release tag:

```bash
# 1. Obtain the manifest from the release artifact or checksums/SKILLS.sha256 in the tag.
# 2. From the repository root, verify every listed file:
sha256sum -c checksums/SKILLS.sha256
```

On macOS (no `sha256sum` by default):

```bash
shasum -a 256 -c checksums/SKILLS.sha256
```

Expected result: every line reports `OK`. Any mismatch indicates tampering or an incomplete checkout — do not use the skills until resolved.

### Spot-check a single file

```bash
sha256sum skills/productowner-skill/SKILL.md
# Compare the hash to the matching line in checksums/SKILLS.sha256
```

## Security notes

- Checksums provide **integrity**, not authenticity. For supply-chain assurance, verify the tag signature or compare against the manifest attached to the official GitHub Release.
- Skills are declarative markdown only; checksums do not cover `node_modules/` or dev tooling under `scripts/`.
- Never run install scripts from unvetted packages when mirroring this repo into a regulated environment — see `cybersec-skill` Dependency Risk Assessor (ultra mode).
