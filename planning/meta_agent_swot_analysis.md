# Architecture & SWOT: PO Meta Agent Across Repositories

To make your `productowner-skill` workflows function as a **Reusable Skill Meta Agent** across multiple repositories, we need an architecture that provides generic workflow instructions (the "Meta Agent") while reading repository-specific context (the "Memory").

Here is an analysis of how to achieve this at the initiation stage, weighing Plugins, MCP, and Repo-level Skills.

## 1. Architectural Options for the Meta Agent

### A. The Plugin Approach (Recommended for Initiation)
* **How it works:** The `productowner-skill` repo is installed into the user's agent environment (e.g., `~/.gemini/config/plugins/productowner-skill`). 
* **Memory Handling:** The skills are loaded globally. When the user opens a specific repository (e.g., `repo-A`), the agent uses the global PO skills but executes them against the local memory files (like `repo-A/.agent/memory.md`).
* **Why it's best for now:** It allows "write once, run anywhere" without copying files into every single repository.

### B. The MCP (Model Context Protocol) Approach
* **How it works:** You build an MCP server that exposes specific product management tools (e.g., a tool to "Generate PRD" or a tool to connect to Jira).
* **Memory Handling:** The server manages state and can pull data from external systems.
* **Why it's not ideal for initiation:** It is overengineered for text-based workflows. MCP is best when you need to execute code or connect to external APIs (like pulling live data from Confluence), which violates our "Zero Network/Stateless" security rule.

### C. The Git Submodule / `.agent/skills` Approach
* **How it works:** Each repository includes your `productowner-skill` skills as a Git submodule inside its own `.agent/skills/` folder.
* **Why it's not ideal:** Hard to maintain. If you update a skill, every repository owner has to manually pull the submodule update.

---

## 2. SWOT Analysis: Global Plugin Architecture

**STRENGTHS (What gives us an edge)**
* **Absolute Portability:** Once installed as a plugin, the agent can instantly generate PO artifacts in any new or existing repository.
* **Zero Configuration for End-Users:** The user doesn't need to copy templates into their repo; the agent already knows the workflows globally.
* **Strict Security:** Because it’s a plugin of markdown skills, it operates under the host agent’s strict security sandbox (stateless, local only).

**WEAKNESSES (What we need to watch out for)**
* **Context Overload:** Global skills take up token space. If the agent loads too many complex PO instructions at once, it might slow down or lose focus.
* **Repo Context Blindness:** The global skill doesn't inherently know about a specific repo's business logic unless the repo has good local documentation (Memory).

**OPPORTUNITIES (How we can scale)**
* **"Cross-Pollination" of Memory:** The meta agent can read the standard memory file in *any* repo (e.g., `CLAUDE.md` or `.agent/context.md`) and automatically adapt its standard PRD template to that specific repository's domain.
* **Open Source Trust:** Distributing this as a verified Plugin allows the community to audit the `SKILL.md` files, proving there are no executables or data leaks.

**THREATS (External risks)**
* **EDR/Security Flags:** If we introduce any `.sh` scripts into the plugin, enterprise endpoint detection will flag it. (Mitigated by our strict Markdown-only rule).
* **Inconsistent Agent Support:** Different AI IDEs (Cursor, Windsurf, Antigravity) handle global skills differently, meaning the installation process might vary slightly per tool.

---

## 3. The Initiation Plan (How to Start Today)

To achieve this cleanly without overengineering:

1. **Format as a Plugin:** Package the `productowner-skill` repo so it can be dropped into an agent's plugin directory.
2. **Define the Interface:** Establish a standard for "Local Memory." For example, the `PO-discovery` skill will explicitly say: *"First, read `.agent/memory.md` in the current repository to understand the context, then generate the SWOT."*
3. **Draft the Base Skills:** Create `skills/PO-discovery/SKILL.md` and `skills/PO-delivery/SKILL.md` as plain text files containing the pure logic. 

**Verdict:** Avoid MCP for now. MCP introduces network layers and executable server code, which directly contradicts the "absolute trust" and "no overengineering" security requirements. A **Markdown Plugin** is the safest, most effective way to start.
