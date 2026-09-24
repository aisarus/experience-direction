# Invariants

Rules that hold at every stage, in every file, from the first line of `scenario.md` to the last line of `DIRECTION.md`. A stage's exit criteria are these invariants applied to that stage's file. If a later stage breaks one, the direction is broken, even if every stage looked fine on its own.

Each invariant says what must hold, how to check it, and what breaking it looks like.

## I1. One main visitor

There is exactly one main visitor, named in `scenario.md` as `V1`. Every later decision can say which visitor it serves, and when `V1` and another visitor conflict, `V1` wins unless the file says why not.

- **Check:** for any decision, ask "for whom?". The answer is `V1`, another named `V`, or "all". "The user" and "people" are not answers.
- **Broken looks like:** a concept chosen because it is striking, with nobody in particular in mind.

## I2. The basics by the third second

`V1` knows whose work this is and what is here by the third second, without doing anything. The concept decides *how* this is shown, never *whether*.

- **Check:** the `0 s` and `3 s` lines of the course, the first shot of the storyboard, and acceptance check 1 in `DIRECTION.md` all name the same two things: whose, and what is here.
- **Broken looks like:** a mood, a puzzle or a single instruction ("stand still", "scroll to begin") on the first screen, with the name and the work behind it.

## I3. Only real material

Every fact, name, date, number, quote and image that will reach the page is an item in the material inventory (`M1…Mn` in `scenario.md`) and is approved for publication. Anything missing is a `[PLACEHOLDER]`, and every placeholder is listed in `DIRECTION.md`.

- **Check:** pick any fact in any later file and find its `M` number. If you cannot, it was invented.
- **Broken looks like:** a plausible detail that sounds true ("roasted on site", "award-winning", "since 2012").

## I4. Traceability

Every decision in a stage file points to what it comes from upstream, by ID: a shot to a course step (`K3`), a zone of the space to a shot, a light to a zone. Nothing appears downstream from nowhere, and nothing upstream disappears silently: an upstream item is either used or moved to *not included* with a reason.

- **Check:** every ID in `scenario.md` appears somewhere downstream or in `X` (not included). Every heading in `storyboard.md`, `space.md`, `look.md` cites at least one ID.
- **Broken looks like:** a beautiful look idea that serves no shot; a project in the material that simply never shows up.

## I5. One of each

There is one concept, one punch, one space type, one placement law, one point of view, one place where the accent colour is spent, and one place that holds the eye in each shot. Any second one either replaces the first (and the file is edited) or goes to the next piece (`LINES.md`).

- **Check:** count them in each file.
- **Broken looks like:** "and also…" — a second trick added because the first felt thin.

## I6. Earned reveals

Everything that opens, opens because the visitor did something, and the file names that action. Autoplay is allowed for three seconds at most, and only before the first action.

- **Check:** every reveal in the course and storyboard has the form "action → answer".
- **Broken looks like:** sections fading in on a timer; a discovery that appears on its own.

## I7. Constant input

The same input means the same thing everywhere. If scrolling moves the world in one place, it moves the world everywhere. If the meaning of an input changes, that change is an event in the storyboard, announced to the visitor.

- **Check:** list every input (scroll, drag, click, hover, stillness, keys, tilt) and its single meaning in `storyboard.md`.
- **Broken looks like:** scroll moves the camera in the hero and scrolls text below it.

## I8. Written refusals

Every stage records what it considered and rejected, and why. A scenario keeps its two rejected concepts; a space keeps the rejected space type; a look keeps the rejected palette. Refusals are how the next person understands the choice and does not undo it.

- **Check:** each stage file has a *Rejected* section that is not empty.
- **Broken looks like:** a single option presented as if it were the only one possible.

## I9. Fix upstream, not downstream

When a later stage finds that an earlier decision does not work, the earlier file is edited and everything downstream of it is re-checked. The later file never quietly overrides the earlier one.

- **Check:** no stage file contradicts an earlier one. `check_gates.py` passes after every edit.
- **Broken looks like:** `look.md` says "warm daylight" while `storyboard.md` still describes a night scene.

## I10. Checkable words

Every decision is written so that someone could look at the built page and say whether it was carried out. Taste words ("atmospheric", "premium", "elegant", "immersive", "dynamic") are not decisions.

- **Check:** for each line in `DIRECTION.md`, ask "how would I see this on the page?". If there is no answer, rewrite the line.
- **Broken looks like:** "the site should feel calm and premium".

## IDs used across files

    M1…Mn   material items                         scenario.md
    V1…Vn   visitors (V1 is the main one)           scenario.md
    C1…C3   concepts (one chosen)                   scenario.md
    P       the punch                               scenario.md
    K0…Kn   course steps                            scenario.md
    X1…Xn   not included                            every file
    S1…Sn   shots                                   storyboard.md
    Z1…Zn   zones / objects in the space            space.md
    D1…Dn   look decisions (light, colour, type…)   look.md
    A1…An   acceptance checks                       DIRECTION.md
