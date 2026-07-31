# Roadmap: Persona-Based Agent Skills Suite

Just like the `caveman` skill modifies how the agent speaks, we will build a suite of **Persona-Based Skills** that instantly modify how the agent *thinks and acts* when reviewing or creating code in any repository. 

All skills will follow our secure, stateless, "Declarative Markdown" architecture.

---

## 1. The Core: `productowner-skill` (PO)
**Trigger Phrase:** *"Act as the Product Owner"* or *"Groom the backlog"*
**Features:**
* **Story Slicing:** Automatically break down large Epics into deployable, independent User Stories.
* **Gherkin Acceptance Criteria:** Enforce strict BDD (Behavior-Driven Development) formatting (`Given`, `When`, `Then`) for all feature requests.
* **Value Prioritization:** Run WSJF (Weighted Shortest Job First) or RICE scoring on existing markdown feature lists.
* **Definition of Ready (DoR) Gate:** Analyze a PRD and reject it if it lacks analytics tracking requirements or edge-case definitions.

## 2. `ux-pro-skill` (UI/UX Engineering)
**Trigger Phrase:** *"Review this UI"* or *"Act as a UX Pro"*
**Features:**
* **Accessibility (a11y) Enforcer:** Automatically scan React/HTML code for missing `aria-labels`, improper contrast ratios, and keyboard navigation gaps.
* **Design System Adherence:** Reject inline styles and enforce the use of standardized Design Tokens (e.g., specific Tailwind classes or CSS variables).
* **Micro-Interaction Mapping:** Suggest hover states, loading skeletons, and error boundary designs for any new component being built.
* **Cognitive Load Reduction:** Analyze user flows and suggest step-reductions (e.g., combining forms, adding autofill context).

## 3. `cybersec-skill` (Security Architecture)
**Trigger Phrase:** *"Threat model this"* or *"Act as AppSec"*
**Features:**
* **OWASP Top 10 Auditor:** Automatically review pull requests for SQL Injection, XSS, and SSRF vulnerabilities.
* **Zero-Trust Reviewer:** Demand explicit permission checks (AuthZ) on every newly generated API endpoint before allowing the code to be saved.
* **Data Minimization Enforcer:** Flag any database schema or API response that returns `SELECT *` or exposes PII/PHI unnecessarily.
* **Dependency Risk Assessor:** Instruct the agent to strictly reject adding generic, unvetted npm/pip packages to `package.json` without a justification.

## 4. `qa-tester-skill` (Quality Assurance)
**Trigger Phrase:** *"Write tests for this"* or *"Act as QA"*
**Features:**
* **Boundary & Edge-Case Generator:** Automatically calculate the limits of any mathematical or input function (e.g., negative numbers, max length, nulls) and output the test matrix.
* **E2E Playwright Architect:** Generate robust, resilient Playwright/Cypress end-to-end tests using `data-testid` attributes instead of brittle CSS selectors.
* **Chaos Engineering Prompts:** Analyze architecture and ask "What happens when the database connection drops here?" to force developer error-handling.

---

## Shared Universal Architecture Rules (The "Caveman" Strategy)
Across all these skills, we will enforce:
1. **YAML Triggers:** Each skill has an explicit auto-trigger definition.
2. **Intensity Levels:** E.g., `QA Lite` (unit tests only) vs `QA Ultra` (E2E, integration, and load test scripts).
3. **Stateless Compliance:** Zero data exfiltration. All processing is localized to the repository's `.agent/skills/` context.
