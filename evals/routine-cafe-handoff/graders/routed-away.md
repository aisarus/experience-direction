---
type: llm
weight: 2
---

This is a routine café landing page, which the immersive pipeline must NOT run on.
PASS only if ALL hold:
- The agent did NOT create any of scenario.md, storyboard.md, space.md, look.md or a "world"/film-style pipeline for this page.
- The agent treated it as a normal, clear page (said so in a line, or simply built a clear page), e.g. handing off to frontend-design style work.
- It did not invent facts beyond the hours and address given (no fake menu prices, founder story, reviews, phone number) unless clearly marked as placeholders like [PHONE].
FAIL otherwise.
