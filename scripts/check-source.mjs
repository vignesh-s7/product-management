import assert from 'node:assert/strict';
import { readFile, readdir, access } from 'node:fs/promises';
import path from 'node:path';

const pages = [
  'docs/auth.html',
  'docs/index.html',
  'docs/app/index.html',
  'docs/onboarding/index.html'
];

const sources = Object.fromEntries(
  await Promise.all(pages.map(async (path) => [path, await readFile(path, 'utf8')]))
);

for (const [path, source] of Object.entries(sources)) {
  assert(!source.includes('pm_os_session'), `${path} must not create identity sessions`);
  assert(!source.includes('return_to'), `${path} must not accept redirect destinations`);
  assert(source.includes('DEMO DATA') || path === 'docs/auth.html', `${path} must identify demo data`);
  for (const script of source.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)) {
    if (/\bsrc=/.test(script[1])) continue;
    try {
      new Function(script[2]);
    } catch (error) {
      throw new Error(`${path} contains invalid inline JavaScript: ${error.message}`);
    }
  }
}

assert(!sources['docs/auth.html'].includes('type="password"'), 'auth page must not accept passwords');
assert(!sources['docs/auth.html'].includes('startSSO'), 'auth page must not simulate SSO');
assert(sources['docs/auth.html'].includes('href="app/index.html"'), 'demo entry must use fixed internal destination');

const limitations = await readFile('LIMITATIONS.md', 'utf8');
assert(!/localStorage\.setItem\([^\n]*API_KEY/.test(limitations), 'browser API-key instructions are forbidden');

const workflow = await readFile('.github/workflows/prd-pipeline.yml', 'utf8');
assert(!workflow.includes('secrets.'), 'PRD workflow must not reference secrets');
assert(!workflow.includes('pull_request_target'), 'untrusted target workflow is forbidden');
assert(workflow.includes('permissions:\n  contents: read'), 'workflow permissions must be read-only');
assert(!workflow.includes('orchestrate.sh'), 'PRD workflow must not reference orchestrate.sh');

async function findShellScripts(dir) {
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
      results.push(...await findShellScripts(full));
    } else if (entry.name.endsWith('.sh')) {
      results.push(full);
    }
  }
  return results;
}

for (const skillsDir of ['skills', '.cursor/skills']) {
  const shellScripts = await findShellScripts(skillsDir);
  assert(shellScripts.length === 0, `${skillsDir}/ must not contain .sh files (found: ${shellScripts.join(', ')})`);
}

for (const path of ['.github/workflows/prd-pipeline.yml', '.github/workflows/ci.yml', '.github/workflows/pages.yml']) {
  const source = await readFile(path, 'utf8');
  assert(!/^\s*uses:\s+[^\s]+@v\d+/m.test(source), `${path} must pin actions by commit SHA`);
}

console.log('Source policy checks passed.');

// --- Skill validation (skills/**/SKILL.md) ---

async function findSkillFiles(dir) {
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
      results.push(...await findSkillFiles(full));
    } else if (entry.name === 'SKILL.md') {
      results.push(full);
    }
  }
  return results;
}

function stripBackticksAndCodeBlocks(source) {
  return source
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`[^`]*`/g, '');
}

function isProhibitionLine(line) {
  const lower = line.toLowerCase();
  return (
    /\b(no|not|never|forbid|banned|without|must not)\b/.test(lower) ||
    /\bdo not\b/.test(lower) ||
    /\bdon't\b/.test(lower)
  );
}

function assertNoBannedPatterns(skillPath, source) {
  const stripped = stripBackticksAndCodeBlocks(source);
  const lines = stripped.split('\n');
  for (const { pattern, label } of bannedChecks) {
    for (const line of lines) {
      if (isProhibitionLine(line)) continue;
      assert(!pattern.test(line), `${skillPath} must not contain banned pattern: ${label}`);
    }
  }
}

function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const yaml = match[1];
  const name = yaml.match(/^name:\s*(.+)$/m)?.[1]?.trim();
  const description = yaml.match(/^description:\s*(.+)$/m)?.[1]?.trim();
  return { name, description };
}

const SKILLS_ROOT = 'skills';
const skillFiles = await findSkillFiles(SKILLS_ROOT);
assert(skillFiles.length > 0, `${SKILLS_ROOT}/**/SKILL.md must include at least one skill`);

const bannedChecks = [
  { pattern: /\bcurl\b/i, label: 'curl' },
  { pattern: /\bwget\b/i, label: 'wget' },
  { pattern: /orchestrate\.sh/i, label: 'orchestrate.sh' },
  { pattern: /\bAPI_KEY\b/, label: 'API_KEY' },
  { pattern: /(?:^|\s)(?:bash|sh)\s+\S+\.sh\b/i, label: '.sh execution' },
  { pattern: /\.\/\S+\.sh\b/, label: '.sh execution' },
  { pattern: /type=["']password["']/, label: 'password input' },
];

for (const skillPath of skillFiles) {
  const source = await readFile(skillPath, 'utf8');
  const frontmatter = parseFrontmatter(source);
  assert(frontmatter, `${skillPath} must start with YAML frontmatter (---)`);
  assert(frontmatter.name, `${skillPath} frontmatter must include name`);
  assert(frontmatter.description, `${skillPath} frontmatter must include description`);

  assertNoBannedPatterns(skillPath, source);
}

const requiredNamedSkills = ['cybersec-skill', 'qa-tester-skill', 'ux-pro-skill'];
for (const skillName of requiredNamedSkills) {
  const skillPath = path.join(SKILLS_ROOT, skillName, 'SKILL.md');
  await access(skillPath);
}

const poSkillDirs = (await readdir(SKILLS_ROOT, { withFileTypes: true }))
  .filter((entry) => entry.isDirectory() && entry.name.startsWith('PO-'));
assert(poSkillDirs.length > 0, `${SKILLS_ROOT}/PO-* skills must exist`);
for (const entry of poSkillDirs) {
  const skillPath = path.join(SKILLS_ROOT, entry.name, 'SKILL.md');
  await access(skillPath);
}

console.log('Skill validation checks passed.');
