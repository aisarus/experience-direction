# Stage 5. Handoff

Compile the direction into one document a builder can carry out without this conversation: `DIRECTION.md`, in the project root. Then give it to the builder.

## Why a separate document

The stage files are the director's notebook: alternatives, refusals, arguments. The builder needs the decisions. A builder who gets four files and a conversation takes the parts that are easy to build and drops the rest — usually the pause, the hidden thing and the refusal. One document of decisions, each one checkable, survives the handoff.

## Inputs

- `scenario.md`, `storyboard.md`, `space.md`, `look.md` (or `design/brief.md` in light mode).
- The builder, if known: the `frontend-design` skill, another tool, or a person. Their defaults matter in step 5.

## Procedure

### Step 1. Run the trace audit

Before writing anything, check the invariants across all four files at once. This is the step that catches what every single stage missed.

1. **Material (I3).** List every fact, name, number and image mentioned in any stage file. Each has an `M` number and is approved; otherwise remove it or make it a `[PLACEHOLDER]`.
2. **Traceability (I4).** Every `M` used is in a `K`; every `K` has an `S`; every `S` happens in a `Z`; every `Z` has its `D`. Every unused item is in a *Not included* list.
3. **One of each (I5).** One concept, one punch, one space type, one placement law, one point of view, one accent place, one eye point per shot.
4. **Basics (I2).** `V1`'s 3-second line, the course `K0–K1`, the first shot `S1` and the level-1 look all show whose and what.
5. **Contradictions (I9).** Read the four files in order and look for any later decision that contradicts an earlier one. Fix the earlier file, then re-check downstream.

If the audit changes a stage file, re-run `check_gates.py`.

### Step 2. Run the two checks

- **Punch** (`check-punch.md`): the sentence, the subtraction test, one punch.
- **Three minutes** (`check-three-minutes.md`): 3 s, 30 s and 3 min, each with an object or an event.

Write both into `LINES.md` (format in `SKILL.md`). If either fails, go back to the stage that owns it (usually stage 1 or 2), not forward.

### Step 3. Compile the decisions

Fill the template below from the stage files. **Copy decisions, not arguments**: rejected options and reasons stay in the notebook. Keep the IDs, so the builder and a reviewer can trace any line back.

### Step 4. Write the acceptance checks

Turn the invariants and the key decisions into checks that can be done **on the built page**, by looking and using it. Each check names what to do and what must be seen. Make them specific to this piece.

    A1  small window    open at ~500×400; within 3 s, without input: the whole line, "Mira Kovač — sound",
                        four stop names with years (I2)
    A2  phone           at 390 wide: the line is vertical; resting a finger on a stop grows its sound (S5)
    A3  the punch       at Low Tide, keep still 1.5 s: the lamp (#F2C14E) lights and the sea rises;
                        any movement makes it fall back (P)
    A4  third minute    keep still *between* two stops, not at one: the Tram 17 recording of that stretch
                        of the line plays (M1); nothing on the page hints at it
    A5  inputs          scroll, tap, ← →, Enter, Esc do exactly what the input map says, everywhere (I7)
    A6  reduced motion  the ride is a cut, the page is fully readable and lit; no motion is required to reach anything
    A7  keyboard        focus is visible on the current stop; Tab order follows the line
    A8  readable        no canvas or image covers any text at any size
    A9  material        every fact on the page is in the Real material list; every placeholder is still marked (I3)
    A10 name            "Mira Kovač — sound" in <title> and on the page
    A11 accent          #F2C14E appears only at the moment (I5)

Every check must be answerable by "yes" or "no" by someone who has never read the stage files (I10).

### Step 5. Name the departures from the builder's defaults

If the builder has its own style rules — `frontend-design` does, and so does any designer — write down where this piece deliberately departs from them, and why. Otherwise the builder's taste wins silently.

    frontend-design warns against hairline rules and dense print-like layouts;
    here the line is a print diagram on purpose (D1) — keep it flat, thin and printed.

### Step 6. List the placeholders

Every `[PLACEHOLDER]` that will reach the page, with what is missing and who can supply it.

    [EMAIL]              contact address — from Mira
    [QUIET ROOMS PHOTOS] six photos, one per room — from Mira (M7 supplied later)

### Step 7. Hand off

- If the user wants it built in this session: invoke the `frontend-design` skill (if available) with `DIRECTION.md` as the brief, or build following it yourself. **`DIRECTION.md` wins over any default taste.**
- Otherwise: stop and give the user `DIRECTION.md`. It is written to be pasted into any tool or sent to any person.

End your reply with: the concept in one sentence, the punch, what `V1` sees in the first three seconds, and every open placeholder.

## Output: `DIRECTION.md`

Exactly these sections. Every line is a decision, not a mood.

    # <name>

    ## Who and why
    main visitor      V1 — who, what they must get
    by 3 s they know  whose this is and what is here
    others            V2… — and what must not obstruct them

    ## Concept
    one sentence. What it means for navigation / headings / cursor and touch / transitions

    ## Punch
    P — one sentence with an event

    ## Course
    K0 (0 s — the share card), K1 (3 s), … the moment …, Kend — sees / understands / does

    ## Shots
    S1…Sn — frame, eye, pace, leave, next; the moment marked

    ## Inputs
    every input, one meaning; touch and keyboard equivalents

    ## Space
    type, edges, levels, placement law, distances — and the diagram with zones Z1…Zn

    ## Look
    D1…Dn — sources and their principles, light, palette (hex + role), type, material, per zone

    ## Not included
    what we know and deliberately do not show

    ## Real material
    M1…Mn that may be used — and nothing else
    placeholders: [LIKE_THIS] — what is missing, from whom

    ## Departures from the builder's defaults

    ## Acceptance — the build is not done until
    A1…An

    ## Notes for the builder
    - An hour of work must change something visible in a before/after screenshot. Invisible tuning waits
      unless the page errors, drops below 30 fps, fails to render, or fails an acceptance check.
    - Primitive shapes standing in for a real subject (a building of rectangles, a cup of circles) read as
      a child's drawing. Use the real images, a proper illustration, or an abstract treatment that does
      not pretend to depict the thing.
    - A file handed over must open on its own: inline what it needs, or hand over the folder.

## Exit criteria

- [ ] The trace audit passed; any stage file it changed passes `check_gates.py` (I3, I4, I5, I9)
- [ ] Punch and three-minutes lines are in `LINES.md`
- [ ] Every template section is filled; IDs are kept
- [ ] Acceptance checks cover I2 (small window, phone), P, the third minute, inputs, reduced motion, keyboard, readability, material, the name, the accent
- [ ] Every acceptance check is yes/no for someone who has not read the stage files (I10)
- [ ] Departures from the builder's defaults are named
- [ ] Every placeholder is listed with its source
- [ ] No taste words anywhere in the document (I10)

## After the build

If the page was built in this session, run the acceptance checks against it with your own eyes: a screenshot at ~500×400 and at 390 wide, then use it. If you cannot render it, say **"not visually verified"** and give the user the checks to do themselves. Then run the **line** check (`check-line.md`).

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| "See scenario.md for details" | The notebook was handed off, not the decisions | Copy the decisions into the template |
| "It should feel calm and premium" | Taste words | Rewrite as light, colour, pace decisions (I10) |
| An acceptance check nobody can fail | Too vague ("looks good on mobile") | Name the action and what must be seen |
| The builder's style overrode the look | Defaults won silently | Step 5 |
| A fact on the page that is in no stage file | Invented during the build | A9; remove it or make it a placeholder |
