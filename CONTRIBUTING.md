# Contributing to the Persona Swarm

First off, thank you for considering contributing to this repository! It's people like you that make the open-source AI community secure and powerful.

## 🛡️ The Golden Rule: Zero-Trust Markdown Only
This project is built for strict Enterprise IT compliance (Big 4, BFSI, Healthcare). Because of this, **we do not accept any executable scripts (`.sh`, `.bat`, `.py`) or API calls** in pull requests.

If you are contributing a new Persona Skill, it **MUST** be written entirely as a Declarative Markdown (`SKILL.md`) file. 

## How to Contribute
1. **Fork the repo** and create your branch from `main`.
2. **If you've added a skill**, ensure it relies solely on the host agent for execution.
3. **If you've changed documentation**, ensure it aligns with our Responsible AI and Data Sovereignty ethos.
4. **Issue that pull request!**

## Code Review Process
All submissions will be reviewed by the core maintainers. We specifically look for:
- **No PII Risks:** Prompts must encourage synthetic data.
- **No Network Calls:** Agents must be instructed to run locally.
- **Clarity:** The Markdown instructions for the agent must be deterministic and clear.
