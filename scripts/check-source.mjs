import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

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

for (const path of ['.github/workflows/prd-pipeline.yml', '.github/workflows/ci.yml', '.github/workflows/pages.yml']) {
  const source = await readFile(path, 'utf8');
  assert(!/^\s*uses:\s+[^\s]+@v\d+/m.test(source), `${path} must pin actions by commit SHA`);
}

console.log('Source policy checks passed.');
