# Stage 3. Space (art direction)

The structure of the world the shots happen in, and the law by which things stand where they stand: type of space, edges, levels of scale, distances, where the visitor is.

Not decoration, not colour, not type — that is stage 4. A mistake here is not fixed by colour or animation: a meaningless space made beautiful is beautifully meaningless.

## Inputs

- `storyboard.md`: point of view, shots `S1…Sn`, *shown and hidden*.
- `scenario.md`: the material items that become objects in the space.

## Procedure

### Step 1. Choose the type of space → `## Type`

Choose one and hold it. Mixing types reads as the absence of a concept (I5).

    strip       everything in one line, forward and back. Honest, and dull unless the material is a line
    room        one place, objects around you, you go nowhere
    map         everything visible at once; you move across the surveyable
    corridor    you walk forward, don't look back, the order is fixed
    descent     depth instead of length: the further, the lower and quieter
    world       larger than the screen; it has an edge and emptiness
    mechanism   you don't walk; you operate it, and it answers

Write the type and which shots and which part of the concept it serves.

    type   strip — the material is literally a line (M1, tram 17), and the concept rides it.
           The usual dullness of a strip is answered by the stops: each one opens downward (step 3).

An application rather than a page usually needs a **world** or a **mechanism**, otherwise there is nowhere to put the scale.

### Step 2. Decide the edges → `## Edges`

What happens at each edge. "Nothing" is not an answer: a world without an edge reads as a set.

    wall      you can't go further, and it's visible in advance
    return    the edge wraps back; the world is closed
    void      you can walk into nothing, and it means something
    horizon   the edge is unreachable but always visible

    left edge    horizon — the line continues before 2019 into fog: the stops before her work (never opens, felt)
    right edge   wall — the terminus: her name and the contact. The line ends where you can reach her.

### Step 3. Define the levels of scale → `## Levels`

How many times the visitor can "zoom in", and what changes at each level. For every level write: what is visible, what has disappeared, what has appeared, and **what there is to do** there.

    1  the line      visible: four stops, years, the name     to do: choose a stop
    2  a stop        disappeared: the other stops              to do: stay still and listen
                     appeared: the piece's own frame
    3  a room        only at Quiet Rooms (six rooms, M5)        to do: step between rooms
                     appeared: one room's sound and photo

A level whose only activity is falling deeper is not a level but a transition animation — remove it.

### Step 4. State the placement law → `## Placement law`

The most important and most skipped decision: **by what law do objects stand where they stand?** Choose one.

    by time       older further, newer closer
    by kinship    similar things together, foreign things apart
    by weight     large things hold the centre, small ones the periphery
    by history    in the order in which it happened to the author
    by meaning    what the visitor must meet first stands at the entrance

    law    by time: stops in the order of the years, 2019 → 2024, left to right, toward the terminus

The law must read without a caption. Test it: take any two objects and ask "why is this one here and that one there?". If the answer is "that's how it landed", there is no law.

### Step 5. Use distance → `## Distances`

In a space, distance is a statement: far is "unimportant" or "hard to reach", near is "connected".

    gaps between stops are proportional to the years between works:
      Tram 17 ──2 yr── Low Tide ─1 yr─ Quiet Rooms ──2 yr── Salt ─── terminus

- **The emptiness between objects is an object.** It sets rhythm and scale.
- **Equal intervals kill hierarchy.** If everything is equally spaced, nothing is the main thing.
- **A cluster reads as one thing.** Twenty objects side by side say "obsession" better than a caption.

### Step 6. Place the visitor → `## Where the visitor stands`

At each level: inside or outside? Do they move, or does the world move? Do they see themselves? The answer is the same at every level, or its change is a marked shot (I7).

    1  outside, beside the line; the line moves past them
    2  on the platform (the POV change in S4); the world is still, only sound moves
    3  inside a room; the same as 2

### Step 7. Draw the diagram → `## Diagram`

Mandatory. A space that cannot be drawn has not been invented yet, and code will not save it. Mark the zones `Z1…Zn`, and point each to the shots that happen there (I4).

    fog ····●───────────●─────●───────────●──────── ▣ Mira Kovač — sound
         (horizon)  Z1 Tram 17  Z2 Low Tide  Z3 Quiet   Z4 Salt     Z5 terminus: contact
                   2019        2021  Rooms 2022        2024      (wall)
                                │         ┌─┬─┬─┐
                                ▼         │ │ │ │  level 3: six rooms (Z3a–Z3f)
                            sea band      └─┴─┴─┘
    Z1–Z4 ← S2–S6    Z5 ← S7

### Step 8. Record the rejected → `## Rejected`

    map (all four works as islands) — no placement law the visitor could read; lost the tram, the author's own structure
    equal spacing between stops — killed the reading of time

## Output: `space.md`

    # <name>
    ## Type                   one type, and why
    ## Edges                  each edge and what happens there
    ## Levels                 1…n: visible / disappeared / appeared / to do
    ## Placement law          one law, and the two-object test
    ## Distances              what the gaps say
    ## Where the visitor stands
    ## Diagram                with zones Z1…Zn pointing to shots
    ## Rejected

## Exit criteria

- [ ] One type of space (I5)
- [ ] Every edge has an answer that is not "nothing"
- [ ] Every level has its own thing to do
- [ ] One placement law that passes the two-object test without a caption (I5)
- [ ] Intervals are not all equal, or equality is the stated law
- [ ] The visitor's position is the same at every level, or its change is a marked shot (I7)
- [ ] A diagram exists; every zone points to shots and every shot happens in a zone (I4)
- [ ] *Rejected* is not empty (I8)

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| Objects on a grid | "Everyone is equal" by default | A grid is a law; use it only when equality is the point, and say so |
| An empty world with a few objects | The space is bigger than the content | Shrink it; emptiness must be a decision, not a leftover |
| The visitor gets lost and doesn't come back | The structure is hidden behind the camera | Make the whole visible at least once (usually S1) |
| "The same, but bigger" at the next level | A transition pretending to be a level | Remove the level, or give it its own thing to do |

## Next

Stage 4, look: light, colour, material and type for this space.
