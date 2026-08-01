import { createHash } from 'node:crypto';
import { mkdir, readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const OUTPUT_DIR = path.join(ROOT, 'checksums');
const OUTPUT_FILE = path.join(OUTPUT_DIR, 'SKILLS.sha256');
const SCAN_ROOTS = ['skills', '.cursor/skills', 'schemas'];

async function walkFiles(dir) {
  const results = [];
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return results;
  }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...await walkFiles(full));
    } else if (entry.isFile()) {
      results.push(full);
    }
  }
  return results;
}

async function sha256File(filePath) {
  const data = await readFile(filePath);
  return createHash('sha256').update(data).digest('hex');
}

const files = [];
for (const root of SCAN_ROOTS) {
  const absRoot = path.join(ROOT, root);
  const walked = await walkFiles(absRoot);
  files.push(...walked);
}

files.sort((a, b) => a.localeCompare(b));

await mkdir(OUTPUT_DIR, { recursive: true });

const lines = [];
for (const file of files) {
  const hash = await sha256File(file);
  const relative = path.relative(ROOT, file).split(path.sep).join('/');
  lines.push(`${hash}  ${relative}`);
}

const content = `${lines.join('\n')}\n`;
await writeFile(OUTPUT_FILE, content, 'utf8');

console.log(`Wrote ${lines.length} checksums to ${path.relative(ROOT, OUTPUT_FILE)}`);
