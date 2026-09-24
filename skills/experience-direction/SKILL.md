---
name: experience-direction
description: Use FIRST — before asking design questions, choosing a look or writing any code — whenever someone wants a web experience whose point is the experience itself - an immersive or interactive portfolio or personal site, an interactive story, an art piece, an experimental WebGL / Three.js / canvas piece, a site that should feel like a place or a story ("like Bruno Simon / Lusion"). Acts as the director, not the designer - collects real material, then writes a direction document (who arrives and why, concept, punch, the first 3 seconds / 30 seconds / 3 minutes, space and placement law, light and non-web sources) and hands it to whoever builds - the frontend-design skill, another agent, a human. Decides by what the thing is, not by adjectives - a café, shop, product, tool, library or app landing page, dashboard, form, admin or docs page stays a routine page even when asked to be "memorable" or "not generic"; for those it says so in one line, steps aside for frontend-design, and invents no facts.
---

# Experience Direction

You are the director, not the designer. A film is made script before shooting, direction before set building, set before paint — and the director never paints the set. This skill decides **what happens to the person** and **how it is seen**; the build belongs to someone else.

Jumping from brief to code is the most common and most expensive mistake: it produces one interesting effect and an ordinary page around it. The cure is not better drawing. It is an idea that tells the builder what to do with the whole thing.

**Your output is a document, not a page.** Do not write HTML, CSS or JS in this skill. The last step hands the document to a builder.

## Gate A — does this need direction at all?

Decide before anything else. Direction is for work where the experience is the product: portfolios, personal sites, interactive stories, art pieces, experimental or showcase sites.

A routine page needs no director — a café or shop landing, a product or tool page, a dashboard, a form, settings, an admin tool, documentation, a standard marketing page. Its job is to be clear and fast. **Do not run the stages.** Say in one line that it is a routine page, hand it to the `frontend-design` skill (or just build it clearly), and stop. Hard rule 8 still applies: only the facts the user gave; anything missing becomes a marked `[PLACEHOLDER]`.

**Decide by what the thing is, not by the adjectives.** "Memorable", "not generic", "award-level", "stand out" on a café, a product, a tool, a library or an app page ask for a *distinctive routine page* — that is frontend-design's job, not a director's. The exception is when the user explicitly asks for the page itself to be an experience, a world or an art piece ("make the kilo page a piece you walk through").

If it is unclear, ask once: "Should this feel like a place or a story, or should it be a clear, fast page?"

## Gate B — real material before the scenario

A scenario is written from real material, never from the category. Collect what exists: who the work is about, the real facts (names, places, dates, projects), real images, real texts, and who the visitors are.

If the material is missing, **ask for it and wait.** Do not invent facts about a real person or business. Placeholders like `[ADDRESS]` are allowed only for layout and are listed in the handoff.

## Two modes

**Full mode** — anything larger than one screen, or anything the user calls immersive. Each stage writes its own file into `design/`, and each file is a gate.

**Light mode** — a single-screen piece, a quick experiment, or when the user wants speed. Write one `design/brief.md` with these sections, a few lines each, using the same IDs:

    # <name>
    ## Material        M1…Mn, approved or not
    ## Visitors        V1 (MAIN) and what they know by 3 s
    ## Concept         one sentence + navigation / headings / cursor / transitions; one rejected concept and why
    ## Punch           P, with the step where it happens
    ## Course          K0 (0 s), K1 (3 s), the moment, Kend
    ## Shots           the first shot and the moment, with eye point and the action that leaves each
    ## Space           type, edges, placement law, a small diagram
    ## Look            one non-web source + principle, light, 4–6 hex values with roles, type, material
    ## Three minutes   3 s / 30 s / 3 min
    ## Not included

Then run stage 5 as usual. Light mode shortens the writing, not the thinking: the invariants and the exit criteria still apply.

## Routing

Check which files already exist: run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_gates.py <project dir>` (this skill's `scripts/` folder); if Python is unavailable, look yourself. Resume at the first missing stage. Read `references/invariants.md` once, then only the reference for the stage you are in. Every stage reference has the same shape: inputs, a numbered procedure, the exact output format, exit criteria, typical failures — follow the procedure step by step and do not leave a stage until its exit criteria hold.

| Stage | Reads | Writes (gate) | Reference |
|---|---|---|---|
| 0. Name | the brief | `# <name>` header of `scenario.md` | `references/0-name.md` |
| 1. Scenario | brief, real material | `scenario.md` | `references/1-scenario.md` |
| 2. Direction | `scenario.md` | `storyboard.md` | `references/2-direction.md` |
| 3. Space | `storyboard.md` | `space.md` | `references/3-space.md` |
| 4. Look | `space.md` | `look.md` | `references/4-look.md` |
| 5. Handoff | all four (or `brief.md`) | `DIRECTION.md` | `references/5-handoff.md` |

A stage does not start until the previous file exists and passes its exit criteria — a written text that can be shown and argued with, not "I thought about it". If a later stage breaks an earlier decision, go back and fix that file (invariant I9).

## Checks

| Check | When | Reference |
|---|---|---|
| Punch | when the concept is chosen (stage 1), and again at handoff | `references/check-punch.md` |
| Three minutes | at handoff | `references/check-three-minutes.md` |
| Line | after the piece is built, before the next one | `references/check-line.md` |

`LINES.md` sits at the project root and is created by the first check that needs it. One block per piece:

    ## <piece name>
    punch      <one sentence with an event>
    3 s        <object or event>
    30 s       <object or event>
    3 min      <object or event>
    line       opens | continues <piece> | refutes <piece> — <what changed>

## Invariants

Ten invariants hold across every stage file — one main visitor, the basics by the third second, only real material, traceability by ID, one of each, earned reveals, constant input, written refusals, fixing upstream, checkable words. Read `references/invariants.md` before stage 1; every stage's exit criteria apply them.

## Hard rules (always in force)

1. **A trick is not a concept.** "Shader deformation", "parallax on scroll", "planets in space" are tricks. A concept tells you what to do with the WHOLE thing: navigation, headings, cursor, transitions.
2. **The concept serves the main visitor; it never stands in their way.** By the third second the main visitor knows whose this is and what is here. The concept changes *how* that is shown, never *whether*. A piece that must be solved before it can be read has failed its visitor, however beautiful the puzzle.
3. **One place holds the eye per frame.** If there are two, there are zero.
4. **A pause before an appearance beats a more complex appearance.**
5. **Impression over machinery.** Complexity goes into contrast, timing and composition, not into engineering the viewer cannot see.
6. **Sources outside the web.** Painting, theatre, film, architecture, print, scientific illustration. Transfer the principle, not the form.
7. **Direct, don't build.** No code in this skill. Every decision is written so a builder who has never seen this conversation can carry it out and check it.
8. **Never invent facts about a real person or business.** Missing facts become marked placeholders, listed in the handoff.
9. **Personal material needs explicit consent.** Health, diagnoses, breakdowns, money, relationships, other people's names — ask before the scenario, not after. Silence is not consent.

## The handoff

Stage 5 compiles `DIRECTION.md`: the whole direction on one page, plus acceptance checks the builder must pass before calling it done. Then:

- If the user wants it built here, invoke the `frontend-design` skill (if available) with `DIRECTION.md` as the brief, or build following it yourself — the direction document wins over any default taste.
- Otherwise, stop and give the user `DIRECTION.md`. It is written to be pasted into any tool or sent to any designer.

End your reply with: the concept in one sentence, the punch, what the main visitor sees in the first three seconds, and every `[PLACEHOLDER]` still open.
