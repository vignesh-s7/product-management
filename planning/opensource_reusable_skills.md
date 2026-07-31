# Top Reusable Open-Source Skills (50K+ Stars)

To avoid reinventing the wheel, we wrap industry-leading, top-ranked open-source repositories inside our **Declarative Markdown Plugin** structure. 

By wrapping them, we enforce our **Zero-Trust, Local-Execution, No-Telemetry** rules, ensuring these powerful tools pass all enterprise cybersecurity criteria.

---

## 1. Data Analytics & Business Intelligence (BI)
**The Challenge:** Vibe coding data dashboards usually means sending raw, proprietary CSV/SQL data to an external LLM, violating data protection policies.
**The Secure Wrapping Solution:**
* **Apache Superset (65,000+ stars):** We map this to the `data-analyst-skill`. Superset runs in a local Docker container. The agent generates the dashboard configuration files (JSON/YAML) locally without ever seeing or transmitting the raw data rows.
* **Metabase (50,000+ stars):** Mapped to the `bi-architect-skill`. The agent writes raw SQL queries that execute strictly within the local Metabase container, providing instant visualization without data exfiltration.

## 2. System Architecture & Diagrams
**The Challenge:** Generating visual diagrams usually requires proprietary SAAS tools (like Lucidchart) that lock in your architecture data.
**The Secure Wrapping Solution:**
* **Mermaid.js (89,000+ stars):** We map this to the `system-architect-skill`. Mermaid renders diagrams purely from text. Our agent writes the text markdown, and Mermaid renders it locally, ensuring your proprietary architecture maps stay entirely offline.
* **Excalidraw (85,000+ stars):** Mapped to the `ux-pro-skill`. The agent can generate local JSON files that represent Excalidraw whiteboard files, allowing for offline, programmatic UI wireframing.

## 3. AI Solutions & Integrations
**The Challenge:** Building AI features into an app usually means hardcoding OpenAI API keys, leading to major supply chain vulnerabilities.
**The Secure Wrapping Solution:**
* **Ollama (177,000+ stars):** We map this to the `ai-integration-skill`. Ollama allows you to run massive LLMs locally. Our agent will wire up your application to use a local Ollama instance during development. This guarantees that your testing and integration data never leaves your laptop.
* **Hugging Face Transformers (130,000+ stars):** Mapped to the `ml-engineer-skill`. The agent will write Python code to download open-weight models directly to the user's secure perimeter, entirely bypassing third-party API dependencies.

---

## 4. Automation & Vibe Coding (Original Stack)
* **OpenHands (~80,000+ stars):** Mapped to the `builder-skill`. Wrapped securely to only execute inside isolated Docker containers.
* **AutoGPT (~185,000+ stars):** Mapped to the `researcher-skill`. Stripped of local execution rights, limited purely to autonomous web crawling for documentation.
* **LangChain (~95,000+ stars):** Mapped to the `productowner-skill`. Used strictly for its output parsers to guarantee perfectly formatted Gherkin Acceptance Criteria.
* **Playwright (~60,000+ stars):** Mapped to the `qa-tester-skill`. Runs 100% locally and headless for UI testing without telemetry.

---

### The "Trust Wrapping" Strategy
None of these tools are run "raw." We create a `SKILL.md` for each one (e.g., `skills/superset-bi/SKILL.md`) that explicitly tells the host agent:
1. **"Use this open-source tool's syntax."**
2. **"Do NOT send analytics."**
3. **"Do NOT execute without user approval."**

This allows us to leverage millions of hours of open-source engineering while maintaining absolute cybersecurity trust.
