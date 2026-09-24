# Stage 5. Handoff

Compile the direction into one document a builder can carry out without this conversation: `DIRECTION.md`, in the project root.

## Gate

**Requires `scenario.md`, `storyboard.md`, `space.md`, `look.md`** (or `brief.md` in light mode). Run the **punch** and **three minutes** checks first; their sentences go into the document.

## Why a separate document

The stage files are the director's notebook: alternatives, refusals, arguments. The builder needs the decisions. A builder who gets four files and a conversation takes the parts that are easy to build and drops the rest — usually the pause, the hidden thing and the refusal. One page of decisions, each one checkable, survives the handoff.

## Template

Write it in this order. Every line is a decision, not a mood. Where a line cannot be checked by looking at the built page, rewrite it until it can.

    # <name>

    ## Who and why
    main visitor     <who, and what they must get>
    by 3 s they know <whose this is and what is here — hard rule 2>
    others           <who else, and what must not obstruct them>

    ## Concept
    <one sentence>. What it means for:
      navigation   <...>
      headings     <...>
      cursor/touch <...>
      transitions  <...>

    ## Punch
    <one sentence with an event>

    ## Course
    0 s     <what is visible before any action — this is the share card>
    3 s     <...>
    30 s    <what opened once they started>
    3 min   <the unlabelled discovery>
    end     <what they leave with>

    ## Space
    type <...>, edges <...>, placement law <...>
    <the diagram from space.md>

    ## Look
    light      <where from, how many sources, what is in shadow>
    palette    <4–6 hex values, each with a role; where the accent is spent>
    type       <display / text / utility faces; scripts they must cover>
    material   <what the world is made of, and how it behaves>
    sources    <named non-web sources and the principle taken from each>

    ## Not included
    <what we know and deliberately do not show, and why>

    ## Real material
    <every fact, text and image the builder may use — and nothing else>
    placeholders: <[LIKE_THIS], each with what is missing>

    ## Acceptance — the build is not done until
    <the checks below, filled in for this piece>

## Acceptance checks for the builder

Copy these into the document and make each one specific to this piece:

1. **Small window.** Opened at about 500×400, within three seconds the main visitor sees what the "0 s" and "3 s" lines promise — including whose this is and what is here.
2. **Phone.** At 390 wide, the same is true, and every mechanic that lives on the cursor has its touch equivalent (name it).
3. **The punch happens.** Describe the exact action and the visible result the builder must reproduce.
4. **The third minute exists** and is labelled nowhere.
5. **Reduced motion** is a calm, fully lit version, not a broken one. **Keyboard** focus is visible and the order makes sense.
6. **Text is readable** everywhere — no canvas over a heading.
7. **Only the real material** appears; every placeholder is still marked.
8. **The name** is in `<title>` and on the page.

Add one line for the builder about where effort goes: *an hour of work must change something visible in a before/after screenshot; invisible tuning waits unless the page errors, drops below 30 fps, fails to render, or misses one of the checks above.*

And one line against the usual shortcut: *primitive shapes standing in for a real subject (a building made of rectangles, a cup made of circles) read as a child's drawing — use the real images from the material, a proper illustration, or an abstract treatment that does not pretend to depict the thing.*

## After the build

If the page was built in this session, run the acceptance checks against it with your own eyes (a screenshot at ~500×400 and at 390 wide). If you cannot render it, say "not visually verified" and give the user the checks to do themselves. Then run the **line** check.

## Don't

**Don't hand off the notebook.** Four files and "see above" is not a handoff.

**Don't leave taste words.** "Atmospheric", "premium", "elegant" cannot be checked. "One warm light from the upper left; everything below the fold in shadow until scrolled" can.

**Don't let the builder's defaults win silently.** If the builder has its own style rules (frontend-design does), the direction document names where this piece deliberately departs from them and why.
