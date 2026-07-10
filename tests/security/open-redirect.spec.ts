import { expect, test } from '@playwright/test';

test('external redirect query cannot change demo destination', async ({ page }) => {
  await page.goto('/auth.html?return_to=https://example.com/phishing');
  const entry = page.getByRole('link', { name: 'Enter Demo' });
  await expect(entry).toHaveAttribute('href', 'app/index.html');
  await entry.click();
  await expect(page).toHaveURL('http://127.0.0.1:4173/app/index.html');
});
