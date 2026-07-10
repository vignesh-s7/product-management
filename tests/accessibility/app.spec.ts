import { expect, test } from '@playwright/test';

test('workspace exposes keyboard and state semantics', async ({ page }) => {
  await page.goto('/app/index.html');
  await expect(page.locator('.demo-data')).toContainText('DEMO DATA');
  await expect(page.locator('.skip-link')).toHaveAttribute('href', '#workspace-content');
  await expect(page.locator('nav a[aria-current="page"]')).toContainText('Dashboard');
  const autoMode = page.getByRole('switch', { name: 'Toggle automatic demo activity' });
  await expect(autoMode).toHaveAttribute('aria-checked', 'false');
  await autoMode.click();
  await expect(autoMode).toHaveAttribute('aria-checked', 'true');
  await page.locator('nav a[data-section="kanban"]').click();
  await expect(page.getByRole('button', { name: /Move right:/ }).first()).toBeVisible();
  await page.locator('nav a[data-section="client"]').click();
  await expect(page.getByRole('switch', { name: /Share / }).first()).toBeVisible();
});
