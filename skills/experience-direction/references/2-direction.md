# Stage 2. Direction

How the course from the scenario is *seen*: from where, at what pace, what is shown and what is hidden, where the eye goes in each moment.

The scenario says **what happens**. Direction says **how it is seen**. The same course can be told ten ways, and they produce ten different pieces. Choosing the way is the work.

## Inputs

- `scenario.md`: the main visitor `V1` and their 3-second line, the chosen concept, the punch `P`, the course `K0…Kend` with the moment marked.

## Procedure

### Step 1. Choose the point of view → `## Point of view`

Where the visitor looks from, and who they are in this world. Choose one.

    from above      a map reader: everything is surveyable, nothing is frightening
    first person    inside: sees only what is in front of them
    from the side   a spectator: the scene is separate from them
    from inside     they are the mechanism itself

Write the choice, the reason (which `V` and which part of the concept it serves), and whether it ever changes. A change of point of view is a strong move, but it must be a shot of its own — an event the visitor notices — never carelessness (I5).

    POV    from the side, then first person at a stop
    why    V1 must survey all four works at once (from the side = the whole line visible);
           listening is intimate (first person = at a stop, the line recedes, the piece fills the frame)
    change S4: arriving at a stop — the camera lowers onto the platform. Marked as an event.

### Step 2. Map the inputs → `## Inputs`

List every input the piece uses and its **one** meaning (I7). For each pointer input, name its touch and keyboard equivalents now — not at build time.

    scroll / swipe       ride the line: forward and back between stops
    tap / click a stop   ride straight to that stop
    stillness (1.5 s+)   at a stop: the piece's sound grows; anywhere else: nothing
    keys ← →             previous / next stop;   Enter = stay (same as stillness)
    Esc                  leave the stop, back to the whole line

If an input means two things in two places, either split it or make the switch a shot.

### Step 3. Decide what is hidden → `## Shown and hidden`

Three lists. Showing everything means showing nothing, and hiding the basics means losing `V1` (I2).

    visible at once          the line, her name, four stops with names and years, the contact stop
    opens through action     each piece's sound (stillness at a stop), the Quiet Rooms photos (stay longer)
    never opens, but felt    the stops between the four — the line continues past the edges of the screen

The third list gives depth: a world without edges reads as a set. The first list must contain everything in `V1`'s 3-second line.

### Step 4. Write the shot list → `## Shots`

A shot is one state of the frame between two actions. For each shot write six fields. Every shot points to the course step it tells (I4).

    S1  ← K0          (the first shot — this is also the share card)
        frame    the whole line across the screen from the side; four stops; name at the terminus
        eye      her name — the only lit text; the stops are quieter
        pace     still; 1 s of silence, then a far tram bell
        leave    scroll / swipe / → / tap a stop
        next     S2

    S3  ← K2          the ride
        frame    the line slides; the next stop grows from the right
        eye      the next stop's name
        pace     fast, 1.2 s; tram sound from M1
        leave    arrives on its own (the ride is the answer to the scroll, not autoplay)
        next     S4

    S5  ← K3          THE MOMENT (P)
        frame    at Low Tide, first person; a band of sea along the bottom
        eye      the sea band
        pace     slow — nothing happens for 1.5 s; then the sea rises as long as the visitor stays still
        leave    any movement: the sea falls back, the line returns
        next     S3 (ride) or S6

Rules for the shot list:

- **One place holds the eye per shot.** If there are two, there are zero (I5).
- **The first shot shows the concept**, not a logo or a heading, and contains `V1`'s 3-second line (I2).
- **Every shot ends on an action** of the visitor, except autoplay of at most three seconds before the first action (I6).
- **A pause before an appearance beats a more complex appearance.** Write the pause into the pace field.
- The moment (`P`) is one shot, marked.

### Step 5. Draw the pace → `## Pace`

One line per shot: slow, fast or pause, and why. Pace is not animation length; it is *how much the visitor manages to understand per unit of motion*.

    S1 still → S2 pause → S3 fast → S4 slow → S5 the longest stillness in the piece → S6 fast

If the pace line is flat — everything medium — nothing will be remembered.

### Step 6. Write the other versions → `## Without motion, on a phone`

For each shot, what replaces motion and the pointer:

- **Reduced motion:** a calm, fully lit version, not a broken one. The ride becomes a cut; the sea rises as a still image with sound on request.
- **Phone:** the line becomes vertical; stillness works the same (the finger rests); every tap target is at least 44 px.
- **Keyboard:** the input map from step 2; focus is visible on the current stop.

### Step 7. Record the rejected → `## Rejected`

The points of view, shots and hiding choices you considered and dropped, with the reason (I8).

    first person from the start — V1 could not see the four works at once (I2)
    autoplaying the ride between all stops as an intro — a visitor who waits leaves (I6)

## Output: `storyboard.md`

    # <name>
    ## Point of view      the POV, why, and the one change if any
    ## Inputs             every input, one meaning, touch and keyboard equivalents
    ## Shown and hidden   visible at once / opens through action / never opens
    ## Shots              S1…Sn, six fields each, each pointing to a K; the moment marked
    ## Pace               one line per shot
    ## Without motion, on a phone
    ## Rejected

## Exit criteria

- [ ] One point of view; any change is its own shot (I5)
- [ ] Every input has one meaning and a touch and keyboard equivalent (I7)
- [ ] *Visible at once* contains everything in `V1`'s 3-second line (I2)
- [ ] `S1` shows the concept and the 3-second line; it would work as a share card
- [ ] Every shot has one eye point and points to a `K`; every `K` has at least one shot (I4, I5)
- [ ] Every shot ends on an action, except autoplay ≤ 3 s before the first action (I6)
- [ ] The moment is one marked shot, and the pace line is not flat
- [ ] Reduced-motion, phone and keyboard versions are written
- [ ] *Rejected* is not empty (I8)

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| Everything appears on a timer | Autoplay instead of reveals | Give every reveal an action; cut autoplay to ≤ 3 s |
| Two things move in the first shot | Two eye points = zero | Keep one; the other waits for its own shot |
| Scroll moves the world here and scrolls text there | Input means two things | Split the inputs or make the switch a shot |
| A loading screen "for atmosphere" | Making people wait for beauty | A loading screen is a debt, not a genre — cut it or make it the first shot |
| The phone version is "the same but smaller" | Pointer mechanics with no touch equivalent | Rewrite step 6 per shot |

## Next

Stage 3, space: the structure of the world these shots happen in, and the law that places things in it.
