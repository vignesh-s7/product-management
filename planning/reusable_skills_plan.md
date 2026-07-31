# Plan: Reusable AI Agent Skills for Product Management

This plan outlines the architecture and steps required to transform the `productowner-skill` repository from a standalone demonstration project into a modular, plug-and-play **Reusable Skills Repository**. Any other repository or agent will be able to import these skills to execute standard PO workflows.

## 1. Goal
Transition the repository to the Antigravity `skills/` architecture so that other AI agents can natively invoke workflows like PRD generation, ROI modeling, and backlog prioritization simply by importing the skill.

## 2. Directory Restructuring

We will create a root `skills/` directory and break down the previous "Four Engines" into independent, executable skills:

```text
productowner-skill/
├── skills/
│   ├── PO-discovery/
│   │   ├── SKILL.md             # Market sizing, SWOT, ROI models
│   │   └── templates/           # Reusable markdown templates
│   ├── PO-delivery/
│   │   ├── SKILL.md             # Backlog prioritization (RICE), KPI planning
│   │   └── scripts/             # Helper scripts for metrics
│   ├── PO-kb-research/
│   │   └── SKILL.md             # Unified KB search instruction set
│   └── PO-code-pipeline/
│       ├── SKILL.md             # PRD to SDLC execution instructions
│       └── orchestrate.sh       # Existing orchestration script, generalized
```

## 3. Generalizing Existing Logic

Currently, much of the logic is tightly coupled to specific reference PRDs or the GitHub Pages demo. We will abstract this:
- **Remove Hardcoding:** Update scripts like `orchestrate.sh` to accept environment variables or arguments for paths, rather than expecting a fixed `prds/` directory structure.
- **Skill Instructions (`SKILL.md`):** Each skill will include strict YAML frontmatter (name, description, triggers) and explicit instructions on *when* and *how* an agent should use the skill, plus what tools it requires (e.g., `view_file`, `run_command`).
- **Template Library:** The existing `prds/` reference materials will be relocated to `templates/` to act as generic templates that agents can copy and fill out.

## 4. Execution Steps

1. **Create Skill Folders:** Initialize the new `skills/` directory structure.
2. **Migrate Documentation:** Extract the workflow logic from `README.md` and `AI_USE_CASES.md` and inject it directly into the respective `SKILL.md` files as agent instructions.
3. **Refactor Code:** Generalize `orchestrate.sh` and update `package.json` to act as standard scripts rather than repo-specific tasks.
4. **Clean Up Legacy Files:** Remove the hardcoded GitHub Pages demo files (`docs/`) if they are no longer relevant, or move them to an `examples/` directory to serve as reference output.

## 5. Result
Once complete, you will be able to navigate to any other codebase, point your agent to this repository's skills, and say: *"Generate a PRD for this repo using the PO-discovery skill."* The agent will automatically load the PO workflow instructions and execute the task.
