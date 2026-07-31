# RICE Prioritization: Persona Skills Roadmap

To determine the execution order for our new Persona Skills (`productowner`, `ux-pro`, `cybersec`, `qa-tester`), we have scored the features using the **RICE Framework**. 

* **Reach:** How many workflows/users this affects (1 = low, 10 = massive)
* **Impact:** How much value/security it adds (1 = low, 5 = massive)
* **Confidence:** Our certainty in executing it via LLM markdown (0% - 100%)
* **Effort:** Time/complexity to build the `SKILL.md` (1 = low, 5 = high)
* **Score:** `(Reach × Impact × Confidence) / Effort`

---

## High Priority (Build Immediately)

| Persona Skill | Feature | Reach | Impact | Confidence | Effort | RICE Score | Rationale |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **`cybersec`** | **Data Minimization (PII/PHI Blocker)** | 10 | 5 | 100% | 1 | **50.0** | Absolute trust requirement. Easy to implement via strict boundary prompts. |
| **`productowner`** | **Gherkin Acceptance Criteria (Given/When/Then)** | 9 | 4 | 95% | 1 | **34.2** | Core to the PO skill. LLMs excel at formatting raw text into BDD structure. |
| **`qa-tester`** | **Boundary & Edge-Case Generator** | 8 | 4 | 90% | 1 | **28.8** | Instantly saves developers time by catching nulls, limits, and edge cases before coding. |
| **`cybersec`** | **OWASP Top 10 Auditor (SQLi/XSS checks)** | 7 | 5 | 80% | 1 | **28.0** | High security value; can be achieved purely by instructing the agent to scan PRs against OWASP rules. |

---

## Medium Priority (Build Next)

| Persona Skill | Feature | Reach | Impact | Confidence | Effort | RICE Score | Rationale |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **`productowner`** | **Story Slicing (Epic → Stories)** | 8 | 3 | 80% | 1 | **19.2** | Great for backlog grooming, though requires good context memory to be accurate. |
| **`ux-pro`** | **Accessibility (a11y) Enforcer** | 6 | 4 | 85% | 2 | **10.2** | Crucial for enterprise compliance (WCAG). Requires the agent to read UI code deeply. |
| **`ux-pro`** | **Design System Adherence** | 7 | 3 | 75% | 2 | **7.8** | Good for consistency, but requires the skill to first learn the specific repo's design tokens. |
| **`cybersec`** | **Zero-Trust Reviewer (AuthZ Checks)** | 5 | 5 | 60% | 2 | **7.5** | High impact, but LLMs sometimes miss complex custom authentication flows. |

---

## Low Priority (Build Later / Evaluate)

| Persona Skill | Feature | Reach | Impact | Confidence | Effort | RICE Score | Rationale |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **`productowner`** | **DoR Gate (Analytics Tracking Enforcement)** | 5 | 3 | 80% | 3 | **4.0** | Useful, but requires strict rules tailored to how each company handles analytics. |
| **`qa-tester`** | **E2E Playwright Architect** | 4 | 4 | 60% | 3 | **3.2** | E2E tests are notoriously brittle; generating them purely via LLM without running them is complex. |
| **`ux-pro`** | **Micro-Interaction Mapping** | 4 | 2 | 70% | 2 | **2.8** | Nice to have, but purely aesthetic and subjective. |

---

### Execution Plan
Based on the RICE scores, we will start by building the **Data Minimization (PII blocker)** and the **Gherkin AC Generator**. These have the highest ROI—they establish immediate security trust and core PO functionality with very low effort (since they rely entirely on declarative markdown prompts).
