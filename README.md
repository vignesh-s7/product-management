# Product Owner Persona Swarm & Skill Plugins

**Author:** Vignesh AIPM · Senior PO · AI / BFSI / Healthcare

## About

**productowner-skill** is a highly secure, declarative **Persona Skill Plugin Suite** designed for local AI agents (like Antigravity). Instead of opaque, high-risk Python execution environments, this repository provides a swarm of specialized, Markdown-based persona plugins (`productowner`, `ux-pro`, `cybersec`, `qa-tester`) that orchestrate the Software Development Lifecycle (SDLC).

It is built on a **Zero-Trust, Local Execution** model that is guaranteed to pass InfoSec compliance (GDPR, HIPAA, No Telemetry).

**Interactive portfolio demo:** https://vignesh-s7.github.io/product-management/

---

## What is the Persona Skill Suite?

It is a collection of "Caveman-style" global skills. You install them into your AI agent's brain, and they fundamentally change how your agent behaves, thinks, and enforces rules during the software development lifecycle.

The Swarm includes:
1. **`productowner-skill`:** The Core Orchestrator. Writes PRDs and FSDs, enforces strict Gherkin (Given/When/Then) Acceptance Criteria, and ensures Non-Functional Requirements (NFRs) are defined.
2. **`ux-pro-skill`:** Reads the FSD and generates production-ready, glassmorphism UI/UX (HTML/CSS/SVG) conforming to strict WCAG 2.1 AA accessibility standards.
3. **`cybersec-skill`:** (Coming Phase 2) The Gatekeeper. Audits PRs against OWASP Top 10 and prevents PII leaks.
4. **`qa-tester-skill`:** (Coming Phase 2) Generates edge cases and headless Playwright tests.

---

## ⚡ Quick Start: How to Install & Use the Plugin Mode

Because this is a **Global Plugin** (like the `caveman` skill), you do not need to copy complex scripts into every repository you work on. 

### Step 1: Installation
Copy the skill folders from this repository directly into your local agent's global skills directory.
For Antigravity, the path is typically `~/.gemini/antigravity-cli/skills/`:

```bash
# Example for Windows / Antigravity users
Copy-Item -Path "skills\productowner-skill" -Destination "C:\Users\YourUser\.gemini\antigravity-cli\skills\" -Recurse
Copy-Item -Path "skills\ux-pro-skill" -Destination "C:\Users\YourUser\.gemini\antigravity-cli\skills\" -Recurse
```

### Step 2: Usage in Any Repository
Open your terminal in **any** of your existing projects. Launch your AI agent, and use the trigger phrases defined in the skills:

* **To start the PO Workflow:**
  > *"Act as Product Owner and generate a PRD for a new secure login portal."*

* **To generate UI from the PRD:**
  > *"Act as UX Pro and design the UI wireframes for this feature."*

### Step 3: Handling Drift & Feedback (`/learn`)
* **Definition Drift:** If requirements change mid-flight, do not let the AI rewrite the code. Tell the `productowner-skill` to update the PRD/FSD markdown first. The markdown is the ultimate source of truth.
* **Continuous Improvement:** Use the `/learn` slash command to permanently update a skill. For example: *"Always include database indexing requirements in the NFRs."* -> `/learn`. The skill will update its local rules forever.

---

## Security & Trust (Why this beats MetaGPT/OpenHands)

Existing multi-agent frameworks (MetaGPT, OpenHands, AutoGPT) are built as heavyweight Python applications that require unconstrained terminal execution and external API calls. Cybersecurity teams heavily restrict them.

**Our Competitive Advantage:**
* **Declarative Markdown:** The skills are just `.md` text files. They cannot execute malicious background code.
* **Stateless:** The agent retains no persistent telemetry or profiling data across sessions.
* **Trust Wrapping:** We integrate powerful open-source tools (Superset, Ollama, Playwright) by wrapping them in strict Markdown instructions that force them to run locally and safely.

See `planning/` directory for our complete Cybersecurity Trust Plan and Competitor Analysis.

---

## Repository Structure

```
productowner-skill/
├── skills/                        # The Core Plugins
│   ├── productowner-skill/        # PO Orchestration Skill
│   └── ux-pro-skill/              # UI/UX Generation Skill
├── planning/                      # Phase 1 Execution & Strategy Docs
│   ├── PHASE_1_EXECUTION_PLAN.md
│   ├── cybersecurity_trust_plan.md
│   ├── opensource_reusable_skills.md
│   ├── vibe_coding_gap_analysis.md
│   └── top_5_competitors.md
├── docs/                          # Interactive GitHub Pages Demo
│   ├── index.html                 # UI landing page
│   └── ECP/                      # Declarative Presentation Blueprints
└── prds/                          # Reference PRDs (Archived)
```

---

*Built by [Vignesh AIPM](https://github.com/vignesh-s7) · Senior PO · AI / BFSI / Healthcare*
