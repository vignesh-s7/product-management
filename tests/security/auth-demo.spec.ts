import { expect, test } from '@playwright/test';

test('auth page is an honest public demo entry', async ({ page }) => {
  await page.goto('/auth.html');
  await expect(page.getByRole('heading', { name: 'Portfolio Demo' })).toBeVisible();
  await expect(page.getByText('Demo data only')).toBeVisible();
  await expect(page.locator('input[type="password"]')).toHaveCount(0);
  await expect(page.getByRole('button', { name: /sign in/i })).toHaveCount(0);
  await page.getByRole('link', { name: 'Enter Demo' }).click();
  await expect(page).toHaveURL(/\/app\/index\.html$/);
  expect(await page.evaluate(() => localStorage.getItem('pm_os_session'))).toBeNull();
});
