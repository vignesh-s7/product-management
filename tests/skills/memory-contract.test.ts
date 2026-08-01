import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { describe, it } from 'node:test';

const SKILLS_ROOT = 'skills';

async function listTopLevelSkills() {
  const entries = await readdir(SKILLS_ROOT, { withFileTypes: true });
  const skillPaths = [];
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const skillPath = path.join(SKILLS_ROOT, entry.name, 'SKILL.md');
    try {
      await readFile(skillPath, 'utf8');
      skillPaths.push(skillPath);
    } catch {
      // skip directories without SKILL.md at top level
    }
  }
  return skillPaths.sort();
}

function referencesMemory(source) {
  return source.includes('memory.md') || source.includes('.agent/memory');
}

describe('skill memory contract', () => {
  it('every skills/*/SKILL.md references local memory', async () => {
    const skillPaths = await listTopLevelSkills();
    assert(skillPaths.length > 0, 'expected at least one skill under skills/*/SKILL.md');

    const missing = [];
    for (const skillPath of skillPaths) {
      const source = await readFile(skillPath, 'utf8');
      if (!referencesMemory(source)) {
        missing.push(skillPath);
      }
    }

    assert.equal(
      missing.length,
      0,
      `skills missing memory.md or .agent/memory reference: ${missing.join(', ')}`
    );
  });

  it('productowner-skill mentions y-score-readiness', async () => {
    const source = await readFile(path.join(SKILLS_ROOT, 'productowner-skill', 'SKILL.md'), 'utf8');
    assert(
      source.includes('y-score-readiness'),
      'productowner-skill must delegate to y-score-readiness'
    );
  });
});
