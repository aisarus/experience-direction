# Stage 4. Look (concept art)

What it looks like: light, colour, material, type, atmosphere. Sources come from outside the web.

## Gate

**Requires `space.md`. Until `look.md` is written, the handoff does not begin.**

The file contains: the palette as exact values, typefaces by role, the rule of light, the material, and — mandatory — **sources that are not websites**.

## Sources: not from the web

The most common defeat looks like this: you look at twenty sites and make the twenty-first. You cannot leave a genre by looking only at the genre.

> From the author's practice: the reference set was five pieces — Lusion, Locomotive, Obys, Bruno Simon, CrewAI. **All five were web pages.** The ceiling turned out exactly where it had to be: the results were websites. Good ones, recognisable as "another site with an effect".

Look where there is not a single button:

    painting                   composition without motion or interaction
    theatre                    the light goes out on everything but one thing
    film                       editing, shot length, what to show and what not to
    architecture               how a space leads a person without explaining anything
    light                      what a shadow does, what a single source does
    print                      typography a hundred years old, stronger than animation
    scientific illustration    how to show the complex without decorating it

**Transfer the principle, not the form.** Theatrical light is not "a dark background". It is "exactly one lit place in the frame, and it moves with the attention".

Name the source in the file. A named source forces you to hold the principle rather than decorate.

## What gets decided

### Light

Before colour. Light is: where from, how many sources, what is in shadow.

One source is almost always stronger than three. Shadow is not the absence of light but a tool: it hides what must not compete for the eye.

### Palette

4–6 values, each named and given a role. Not "blue and orange" — exact numbers and purpose.

**Neutrals are chosen, not taken by default.** Pure grey reads as unconsidered; grey leaning slightly toward the accent reads as chosen.

**The accent is spent in one place.** If the bright colour is everywhere, it is nowhere. A good move: one colour that appears exactly once in the whole piece, at the moment the piece exists for.

### Type

Two or three roles: a display face with character, a text face, a utility face. The display face is not the one everything else is set in.

Check that the face actually covers every script you need (Cyrillic, Hebrew, Arabic, etc.). Many beautiful Latin faces don't, and you find out on screen, not in the spec.

### Material

What the world is made of: paper, glass, metal, smoke, ink, film. Material gives rules of behaviour — paper creases, glass glints, smoke has no edge.

Without a material, the piece looks "made in a browser", because it really was made in a browser.

## Impression, not machinery

A rule for this stage and the next, and it was measured.

> From the author's practice: five modules in a row, each more complex than the last.
>
>     vertex-shader deformation         simplest technique   → loved
>     particle field                    medium
>     GPU flock, 16,384 springs,
>     state in two textures,
>     all physics on the GPU            most complex         → failed
>
> The first and simplest was loved. The one with the most engineering failed: the first screen was almost black, the effect was buried.

**The complexity went into machinery, not impression.** And that is the tempting strategy: adding technique is cheaper than achieving impression, and by formal signs the two are indistinguishable.

The sign you have gone wrong: **you want to print a number in the interface.** "16,384 particles", "60 fps". The number impresses the author, not the viewer.

Where the complexity should go instead: **contrast**, **timing** and **composition**. One bright point on a dark field is stronger than a glowing field. A pause before an appearance is stronger than a complex appearance.

## Don't

**Don't build a moodboard from websites** — it gives you the genre average, and the genre average is exactly what irritates people.

**Don't take the fashionable defaults.** Cream background with a serif and a terracotta accent, a purple-blue gradient, Inter as the "safe choice", emoji instead of icons, everything rounded — it looks generated because it is.

**Don't decide colour before light.** A palette without light is a list of numbers.

**Don't read "one light" as "dark background".** Theatre, a single source and "the light goes out on everything but one thing" are principles, not a black page. Daylight, paper under a lamp, snow glare, an overexposed photograph are single-source light too. A near-black field with one warm accent is itself a genre default — take it only when the subject is literally dark (night, a cave, a closed room), and say why in `look.md`. If the last pieces in `LINES.md` were dark, this one must justify it twice.

## Next

Stage 5, handoff — compile everything into `DIRECTION.md` for the builder.
