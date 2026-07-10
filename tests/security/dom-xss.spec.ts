import { expect, test } from '@playwright/test';

const payload = '<img src=x onerror="window.__xss=true">';

test('stored Kanban and artifact text never executes as HTML', async ({ page }) => {
  await page.addInitScript((attack) => {
    localStorage.setItem('pm_os_kanban', JSON.stringify({
      backlog: [{ id: 'SAFE-1', title: attack, sp: 3, domain: 'bfsi', priority: 'med', assignee: 'VG' }],
      sprint: [], review: [], done: []
    }));
    localStorage.setItem('pm_os_artifacts', JSON.stringify([
      { id: 1, name: attack, meta: attack, on: true }
    ]));
  }, payload);
  await page.goto('/app/index.html');
  await page.locator('nav a[data-section="kanban"]').click();
  await expect(page.getByText(`SAFE-1: ${payload}`)).toBeVisible();
  await page.locator('nav a[data-section="client"]').click();
  await expect(page.locator('#artifact-list .artifact-name')).toHaveText(payload);
  expect(await page.evaluate(() => Boolean((window as any).__xss))).toBe(false);
  await expect(page.locator('img[src="x"]')).toHaveCount(0);
});

test('onboarding summary treats form values as text', async ({ page }) => {
  await page.goto('/onboarding/index.html');
  await page.locator('#pm-name').fill(payload);
  await page.locator('#pm-org').fill(payload);
  await page.evaluate(() => (window as any).goTo(6));
  await expect(page.locator('#summary-box')).toContainText(payload);
  expect(await page.evaluate(() => Boolean((window as any).__xss))).toBe(false);
  await expect(page.locator('img[src="x"]')).toHaveCount(0);
});
