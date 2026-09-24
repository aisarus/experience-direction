# Stage 1. Scenario

What happens to the person who arrives, step by step, and what they leave with.

The scenario is the only stage that decides *what*. Every later stage decides *how*, so every later stage points back here. A weak scenario cannot be rescued by direction, space or look; it can only be decorated.

## Inputs

- The user's brief, in their words.
- The real material (Gate B): facts, texts, images, links, dates.
- The name from stage 0, or a working subject if the name has not come yet.

If any of these is missing, stop and ask. Do not start the procedure with invented material to "show what it could look like".

## Procedure

Work through the steps in order. Each step writes a section of `scenario.md`. Do not skip a step because the answer seems obvious — obvious answers are exactly the ones that turn out wrong two stages later.

### Step 1. Inventory the material → `## Material`

List every item of material as a numbered line. One item is one fact, one text, one image or one link.

    M1   2019 "Tram 17": field recordings, every stop of Zagreb tram 17, 38-min album   approved
    M2   2021 "Low Tide": game sound design, ~40k players on Steam                       approved
    M3   Low Tide mechanic: the sea gets louder the longer you stand still              approved
    M7   photos of Quiet Rooms                                                          approved, not supplied yet
    M9   the author's burnout in 2023                                                   PERSONAL, not approved

For each item mark: **approved**, **not approved**, or **PERSONAL** (health, money, relationships, other people's names, breakdowns — hard rule 9). Ask for a yes on every PERSONAL item before step 4. No answer means no.

Read everything; publish only the approved items. The inventory is the only source of facts for every later file (invariant I3).

### Step 2. Name the visitors → `## Visitors`

Name two or three real kinds of visitor. For each, write four fields:

    V1  audio director at a game studio (MAIN)
        arrives from   a link in a freelancer shortlist
        time budget    20–40 seconds on the first visit
        question       "has she done the kind of sound we need, and can I hear it fast?"
        success        hears one piece of game audio and finds how to reach her

    V2  festival curator
        arrives from   an application or a colleague's recommendation
        time budget    a few minutes, deliberately
        question       "is her installation work serious, and what would she bring?"
        success        understands Quiet Rooms and sees the list of shows

Mark exactly one as MAIN (invariant I1). The main visitor is the one whose failure would make the site pointless — usually the one who can hire, fund, publish or return.

Then write the main visitor's **3-second line**: what `V1` must know by the third second without doing anything (invariant I2). Almost always: *whose work this is* and *what is here*.

    V1 by 3 s    Mira Kovač, sound designer — games, installations, film; four works, each playable

### Step 3. Write the takeaway → `## Takeaway`

One sentence `V1` will say about the site a day later, in their own words, to a colleague. Write it in their voice, not yours.

    "The sound designer whose portfolio is a tram line — you stop at a project and it plays."

If you cannot write it, you do not have a scenario yet, only a list of sections. Go back to the material and look for what is specific to this person.

### Step 4. Generate three concepts → `## Concepts`

Write **three** candidate concepts, each one sentence. The first is always the dullest, because it comes from what you already know how to do; the third usually comes from the material itself.

Find concepts in the material, not in the genre. Good places to look:

- a mechanic the author already invented (M3: stillness makes the sea louder);
- a structure in the work (M1: a line with stops);
- the author's actual medium (sound, not visuals, for a sound designer);
- a physical place or object the work is about.

For each candidate, fill the consequence table. A concept that cannot fill it is a trick.

    C2  "Her work is a tram line: each project is a stop; you ride between stops,
         and at a stop, the longer you stay, the more of the piece plays."
        navigation     riding the line: next/previous stop, or tap any stop on the map
        headings       stop names on the line: "Tram 17", "Low Tide", "Quiet Rooms", "Salt"
        cursor/touch   stillness at a stop = the sound grows (from M3)
        transitions    the ride: a short passage of recorded tram sound between stops (from M1)
        V1 at 3 s      the whole line is visible with her name at the terminus and four named stops

Then reject candidates by these tests, in this order. Write down which test rejected each one:

1. **Trick test** — the table is mostly empty: it is an effect, not a concept.
2. **Obstruction test** — `V1 at 3 s` does not show whose and what (invariant I2).
3. **Portability test** — swap in another person's material: if the concept still fits, it is a genre, not this person.
4. **One-screen test** — the idea runs out after the first screen, and a feed of sections follows.
5. **Topic test** — it names what the site is about, not what happens ("a site about sound").

Of the survivors, pick the one with **more consequences**, not the one that is easier to build.

Run the **punch check** (`check-punch.md`) on the chosen concept now and write the punch as `P`.

### Step 5. Write the course → `## Course`

The course is a sequence of events, not sections. A section is a place; an event is *what the visitor saw, understood and did next*. Write each step on three lines:

    K0  0 s     sees     the whole tram line across the screen; "Mira Kovač — sound" at the terminus;
                         four stops with names and years
                understands  whose, and that there are four works
                does     nothing yet
    K1  3 s     sees     the nearest stop gently lit, a short line: "stop anywhere to listen"
                understands  that stopping is the way in
                does     taps or scrolls to "Low Tide"
    K2  …       sees     the ride — 2 seconds of tram sound, the line sliding
    K3  moment  at Low Tide, holds still: the sea rises, the first sound of her work (P happens here)
    Kend        leaves with  one piece heard, the contact at the last stop, the takeaway sentence

Rules for the course:

- `K0` and `K1` together satisfy the 3-second line from step 2.
- Every reveal names the visitor's action that earns it (invariant I6).
- Mark exactly one step as **the moment** — the step everything exists for. The punch happens there.
- Every `M` that is used appears in at least one `K`. Note the IDs in the step.

### Step 6. Write what is not included → `## Not included`

List every approved material item that is not in the course, with a reason. Add anything else you considered and dropped.

    X1  M9 (burnout) — personal, not approved
    X2  a "clients" logo wall — nothing in the material; would be invented
    X3  a full CV — V1 does not need it in 40 seconds; one link at the last stop

A scenario is above all a refusal. If this list is empty, you have not chosen anything.

### Step 7. Record the rejected concepts → `## Rejected`

Keep the two rejected concepts from step 4 with the test that rejected each (invariant I8). This is how stage 2 and the builder know not to drift back to them.

## Output: `scenario.md`

Exactly these sections, in this order:

    # <name>                       (stage 0; a working subject if the name has not come yet)
    ## Material                    M1…Mn with approval status
    ## Visitors                    V1 (MAIN) … Vn, four fields each; V1's 3-second line
    ## Takeaway                    one sentence in V1's voice
    ## Concepts                    C1–C3 with consequence tables; the chosen one marked
    ## Punch                       P, one sentence with an event
    ## Course                      K0…Kend, saw / understood / did; the moment marked
    ## Not included                X1…Xn with reasons
    ## Rejected                    the two concepts not chosen, and the test that rejected each

## Exit criteria

Stage 2 does not start until every box is true.

- [ ] Every fact in the file has an `M` number, and every `M` used is approved (I3)
- [ ] Every PERSONAL item has an explicit yes, or is in *Not included* (hard rule 9)
- [ ] Exactly one visitor is MAIN, and their 3-second line names whose and what (I1, I2)
- [ ] The takeaway is one sentence in the visitor's voice, with something specific to this person
- [ ] Three concepts were written; the chosen one fills all five rows of its table
- [ ] The chosen concept passes all five rejection tests; each rejected one names its test (I8)
- [ ] The punch passes `check-punch.md`
- [ ] `K0`–`K1` deliver the 3-second line; exactly one step is the moment; every reveal names its action (I2, I6)
- [ ] Every approved `M` appears in a `K` or an `X` (I4)

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| The concept would fit any portfolio | It came from the genre, not the material | Go back to step 4 and look for a mechanic or structure the author already made |
| The first screen is a mood with no name | The concept obstructs `V1` | Rewrite `K0` so the concept *shows* whose and what, in its own language |
| The course reads "hero → about → projects → contact" | Sections, not events | Rewrite each step as sees / understands / does |
| Every material item is in the course | Nothing was refused | Cut until *Not included* hurts a little |
| The takeaway is "a beautiful, immersive site" | An evaluation, not an event | Write what the visitor would *describe* — an object or an event |

> From the author's practice: a portfolio for a sound designer opened on a black field with one line of light and the words "stand still". No name, no list of work — the projects surfaced only if you held still. The concept was the strongest of its batch, and it lost a blind comparison to a plain page that simply showed the projects, each with its own small mechanic. The audio director it was written for would have closed the tab before holding still. The same stillness mechanic, moved *inside* a visible map of the work (C2 above), keeps the idea and loses the wall.

## Next

Stage 2, direction: how this course is seen — point of view, pace, what is hidden, where the eye goes.
