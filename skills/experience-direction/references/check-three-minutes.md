# Check: three minutes

What the visitor gets at the third second, the thirtieth, and the third minute. Run at handoff (stage 5, step 2).

## Why

A poster gives everything in a second and then goes silent. A place keeps giving. The whole difference between a good page and a thing people return to lies in the third minute: in Bruno Simon's portfolio, around the tenth minute you find bowling pins nobody mentioned — and that is why people remember it for years.

## Inputs

- The course from `scenario.md`, the shots and *shown and hidden* from `storyboard.md`, the levels from `space.md`.

## Procedure

### Step 1. Write the three lines

Each line contains a concrete object or event and points to where it happens (`K`, `S`, `Z`).

    3 s     the whole line, "Mira Kovač — sound", four named stops with years       ← K0, S1
            (V1 already knows whose this is and what is here — I2)
    30 s    stopping at Low Tide: the lamp, the sea rising (the punch)              ← K3, S5
    3 min   keeping still *between* two stops plays the Tram 17 recording of that   ← new shot, Z1–Z2
            stretch of the line (M1)

"More detail", "deeper immersion", "unfolds gradually" don't count: those are promises, not discoveries.

### Step 2. Test the third minute

It must pass all four:

1. **New.** Something that wasn't there at thirty seconds — not "the same, but denser". Turning up a parameter is not a discovery.
2. **Unlabelled.** No arrows, no hints, no "try hovering". A labelled discovery stops being one.
3. **Not required.** Whoever left at thirty seconds must not feel cheated or miss anything they needed.
4. **Real.** Made of approved material, like everything else (I3). A discovery that needs an invented fact is not allowed.

These do not count as a third minute: settings, theme toggles, sliders; another section further down; text that could have been read at the third second; a counter going up.

### Step 3. Make sure it exists upstream

If the third-minute discovery is new at this point, it is not yet in the storyboard, so the builder will never make it. Add it where it belongs (I9): a course step in `scenario.md` (marked optional), a shot in `storyboard.md`, its place in `space.md`, and — if it changes the look — its `D` in `look.md`. Then re-run `check_gates.py`.

### Step 4. If there is nothing for the third line

The work is not ready. The cure is not polish but one new thing inside. Look first at the material that went to *Not included*, and at the "never opens, but felt" list in the storyboard: the discovery is often something already there, one step further.

## Output

- The `3 s`, `30 s`, `3 min` lines in `LINES.md` and in `DIRECTION.md → ## Course`.
- The third-minute discovery as a shot in `storyboard.md`, and as an acceptance check in `DIRECTION.md`.

## Exit criteria

- [ ] Three lines, each with an object or event and its `K` / `S` / `Z`
- [ ] The 3-second line contains `V1`'s basics (I2)
- [ ] The third minute is new, unlabelled, not required, and made of real material (I3)
- [ ] The discovery exists upstream in the stage files, not only here (I9)
