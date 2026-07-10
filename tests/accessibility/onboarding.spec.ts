import { expect, test } from '@playwright/test';

test('onboarding selections use native buttons and announced summary', async ({ page }) => {
  await page.goto('/onboarding/index.html');
  await expect(page.locator('.demo-data')).toContainText('DEMO DATA');
  const domain = page.getByRole('button', { name: 'BFSI' });
  await expect(domain).toHaveAttribute('aria-pressed', 'false');
  await domain.click();
  await expect(domain).toHaveAttribute('aria-pressed', 'true');
  await page.evaluate(() => (window as any).goTo(3));
  await expect(page.locator('#tier-std')).toHaveAttribute('aria-pressed', 'true');
  await expect(page.locator('#summary-box')).toHaveAttribute('aria-live', 'polite');
});
