#!/usr/bin/env node
/**
 * Idempotently copy skills/* → .cursor/skills/ for team onboarding.
 * Run: npm run sync-skills
 */
import { cp, mkdir, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
const sourceDir = path.join(repoRoot, 'skills');
const targetDir = path.join(repoRoot, '.cursor', 'skills');

const entries = await readdir(sourceDir, { withFileTypes: true });
const skillDirs = entries.filter((entry) => entry.isDirectory());

if (skillDirs.length === 0) {
  console.error('No skill directories found in skills/');
  process.exit(1);
}

await mkdir(targetDir, { recursive: true });

for (const entry of skillDirs) {
  const src = path.join(sourceDir, entry.name);
  const dest = path.join(targetDir, entry.name);
  await cp(src, dest, { recursive: true, force: true });
  console.log(`synced ${entry.name}`);
}

console.log(`Done — ${skillDirs.length} skill(s) copied to .cursor/skills/`);
