# Stage 3. Space (art direction)

The third and central stage. The structure of the space and how objects are placed in it: scale, neighbours, distances, the edges of the world.

## Gate

**Requires `storyboard.md`. Until `space.md` is written, stage 4 does not begin.**

The file must contain: the type of space, its edges, the levels of scale, the placement rule, and a diagram — in text or symbols. The diagram is mandatory: a space that cannot be drawn has not been invented yet.

## What this stage decides

**The structure of the space and how objects are placed in it.**

Not decoration, not colour, not type — that is stage 4. Here you decide what stands where and why exactly there. A mistake here is not fixed by colour or animation: if the space is meaningless, a beautiful space will be beautifully meaningless.

## 1. Type of space

Pick one and hold it. Mixing types reads as the absence of a concept.

    strip        everything in one line, forward and back. Honest and dull.
    room         one place, objects around you, you go nowhere
    map          everything visible at once; you move across the surveyable
    corridor     you walk forward, don't look back, the order is fixed
    descent      depth instead of length: the further, the lower and quieter
    world        space larger than the screen; it has an edge and emptiness
    mechanism    you don't walk, you operate it, and it answers

An application, rather than a page, usually needs a **world** or a **mechanism** — otherwise there is nowhere to put the scale.

## 2. Edges

What happens at the edge? "Nothing" is a bad answer.

    wall         you can't go further, and it's visible in advance
    return       the edge wraps back; the world is closed
    void         you can walk into nothing, and it means something
    horizon      the edge is unreachable but always visible

**A world without an edge reads as a set.** The edge is what makes the space real, even if the person never reaches it.

## 3. Levels of scale

How many times the person can "zoom in", and what changes at each level.

    example:   galaxy → system → planet → surface → object

At each level answer: **what is visible, what has disappeared, what has appeared.** A level that is just "the same, but bigger" is not needed — remove it.

Rule: **every level has its own thing to do.** If the only thing to do on a level is to fall deeper, it is not a level; it is a transition animation.

## 4. Placement rule

The most important and most skipped. **By what law do objects stand where they stand?**

    by time        older further, newer closer
    by kinship     similar things together, foreign things apart
    by weight      large things hold the centre, small ones the periphery
    by history     the order in which it happened to the author
    by meaning     what the person must meet first stands at the entrance

The law must be **one**, and it must read without a caption. If placement is random, the person feels it, even without being able to name it.

Test: take two objects and ask "why is this one here and that one there". If the answer is "that's how it landed", there is no law.

## 5. Distance as meaning

In a space, distance is a statement. Far means "unimportant" or "hard to reach". Near means "connected".

- **The emptiness between objects is also an object.** It sets rhythm and scale.
- **Equal intervals kill hierarchy.** If everything is equally spaced, nothing is the main thing.
- **A cluster reads as one thing.** Want to show obsession? Put twenty objects right next to each other; it will say more than any caption.

## 6. Where the person stands

At every moment: are they inside or outside? Do they move, or does the world move? Do they see themselves?

**The answer must be the same at every level** — or its change must be an event the person notices and understands.

## Diagram

Draw it. Even in symbols in a text file:

    ┌─ PROMPT ──────┐        ┌─ LANGUAGE ┐
    │ ●●●●●●        │        │  ● ●      │
    │ ●●●●●●●●●●●●  │        │ ● ● ●     │
    └───────────────┘        └───────────┘
              ╲                  ╱
               ┌─ AGENTS ──────┐
               │   ◉  ● ●      │      ◉ — the heaviest
               └───────────────┘

If the diagram won't draw, the space has not been invented, and code will not save it.

## Don't

**Don't reach for a grid by default.** A grid is the law "everyone is equal". Use it only when that is the law you chose — and say so in the placement rule.

**Don't make the space bigger than the content.** An empty world reads as unfinished, not spacious. Emptiness must be a decision, not a leftover.

**Don't hide the structure behind the camera.** If the person can't build a map in their head, they can't come back — and so they won't explore.

## Next

Stage 4, look — what it looks like: light, colour, material, type.
