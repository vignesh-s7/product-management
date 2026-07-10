import { expect, test } from '@playwright/test';
import { readFile } from 'node:fs/promises';

test('PRD workflow separates untrusted validation from trusted execution', async () => {
  const workflow = await readFile('.github/workflows/prd-pipeline.yml', 'utf8');
  expect(workflow).toContain("if: github.event_name == 'pull_request'");
  expect(workflow).toContain("github.ref == 'refs/heads/main'");
  expect(workflow).toContain('^prds/[A-Za-z0-9._-]+\\.md$');
  expect(workflow).toContain('permissions:\n  contents: read');
  expect(workflow).not.toContain('secrets.');
  expect(workflow).not.toContain('pull_request_target');
  expect(workflow).toMatch(/actions\/checkout@[a-f0-9]{40}/);
  expect(workflow).toMatch(/actions\/upload-artifact@[a-f0-9]{40}/);
  expect(workflow).not.toMatch(/uses:\s+[^\s]+@v\d/);
});
