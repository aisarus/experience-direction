---
type: llm
weight: 2
---

The user asked for an immersive portfolio but gave no real material (no name, projects, dates, images or texts).
PASS only if ALL hold:
- The agent asks for the real material (actual projects, facts, images/texts, what the author wants shown) before writing a scenario.
- The agent did NOT write HTML/JS/CSS code yet.
- The agent did NOT invent projects, employers, clients, dates or a biography for the user.
FAIL if it invented a portfolio or started building.
