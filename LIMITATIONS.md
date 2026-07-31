# Demo Limitations and Production Boundary

productowner-skill is a static, front-end portfolio demonstration. It uses sample data and does not authenticate users, call AI providers, connect enterprise tools, or persist data outside the current browser.

## What the demo does

| Capability | Demo behavior |
|---|---|
| Onboarding | Configures a sample workspace in memory |
| Kanban and client workspace | Stores validated demo state in browser `localStorage` |
| AI chat and discovery | Returns fixed sample responses; no model is called |
| AgileBoard, WikiBoard, EnterpriseCloud 365, CloudVendor Workspace | Shows proposed integration UX only |
| Reports | Renders sample metrics only |
| Authentication | None; "Enter Demo" opens a public static experience |

Do not enter confidential, customer, credential, or production information.

## Credential policy

Provider credentials must never be stored in browser code, browser storage, repository files, or public GitHub Actions logs. A production implementation must keep credentials in a managed server-side secret store and expose only narrowly scoped backend endpoints.

## Production requirements

1. Add a backend authorization boundary and a supported identity provider.
2. Enforce tenant isolation and role checks server-side.
3. Replace sample integrations with audited OAuth applications and scoped tokens.
4. Store durable product data in an access-controlled database.
5. Add provider timeouts, retries, cost limits, evidence metadata, and human approval gates.
6. Run security, accessibility, migration, and end-to-end release checks before deployment.

See `AI_USE_CASES.md` and `ROADMAP.md` for planned architecture. Planned features are not live capabilities.
