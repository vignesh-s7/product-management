---
name: pptx-official
description: Automates the creation of professional widescreen (16:9) PowerPoint presentation slide decks using a clean corporate light theme and native tables.
---

# pptx-official Skill

This skill enables the agent to programmatically generate executive-ready widescreen PowerPoint slide decks using the `python-pptx` library.

## Design Systems

When using this skill to generate slide decks, follow these guidelines:
- **Aspect Ratio**: Always set width to `13.333` inches and height to `7.5` inches (16:9 widescreen format).
- **Color Palette**:
  - Background: Off-white/Light gray (`#F8FAFC`)
  - Primary text: Dark slate (`#172B4D` - Jira Text)
  - Secondary/Muted text: Gray (`#5E6C84` - Jira Muted)
  - Primary Accent: Blue (`#0052CC` - Jira Blue)
  - Secondary Accent/AI Features: Green (`#10A37F` - ChatGPT Green)
  - Highlights/Alerts: Red (`#FF5630`), Green (`#36B37E`), Gold (`#FFAB00`)
- **Typography**: Use standard fonts like `Segoe UI` or `Arial` for professional corporate layout rendering.
- **Card-based layouts**: Group related text in cards (rounded rectangles) with a clean white background, a thin `#DFE1E6` border, and soft padding.
- **Structured Tables**: Use native PowerPoint table shapes for comparative data or metrics. Format cells with custom font sizes, text alignments, and background fills (e.g. gold-highlighting for critical rows).
