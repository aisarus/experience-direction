# Stage 4. Look (concept art)

What the space looks like: light, colour, material, type — and where they come from. Sources come from outside the web.

This stage decides the look, not the craft. Exact tokens, type scale and layout are the builder's job; here you decide what they must express and where the builder may not use their defaults.

## Inputs

- `space.md`: type, edges, levels, zones `Z1…Zn`, the diagram.
- `storyboard.md`: the shots, their eye points, the moment.
- `scenario.md`: the material — especially the author's own medium, places and objects.

## Procedure

### Step 1. Find sources outside the web → `## Sources`

Before any colour. You cannot leave a genre by looking only at the genre.

> From the author's practice: the reference set was five pieces — Lusion, Locomotive, Obys, Bruno Simon, CrewAI. **All five were web pages.** The ceiling turned out exactly where it had to be: the results were websites. Good ones, recognisable as "another site with an effect".

Look where there is not a single button:

    painting                   composition without motion or interaction
    theatre                    the light goes out on everything but one thing
    film                       editing, shot length, what to show and what not to
    architecture               how a space leads a person without explaining anything
    light                      what a shadow does, what a single source does
    print                      typography a hundred years old, stronger than animation
    scientific illustration    how to show the complex without decorating it

Start from the material: the author's own world usually has its sources in it (a sound designer → the printed tram timetable, the waveform, the spectrogram). Name two or three sources, and for each write **the principle** you take, not the form.

    D1  Zagreb ZET tram route diagram (print)      principle: a line and dots carry the whole map; stops are named, nothing else is drawn
    D2  spectrogram (scientific illustration)      principle: sound shown as density, not as a wave; quiet = empty paper
    D3  the platform at dusk (light)               principle: one lamp over the stop you are at; the rest of the line is in daylight

A source is not a mood picture. "Theatrical light" is not "a dark background"; it is "exactly one lit place in the frame, and it moves with attention".

### Step 2. Decide the light → `## Light`

Before colour. A palette without light is a list of numbers. Write: where the light comes from, how many sources, what is in shadow, and how the light changes between shots.

    D4  light   daylight, flat and even over the whole line (level 1): nothing hidden, V1 sees everything
                at a stop (level 2) the day dims around one lamp over the platform — the only directional light
                shadow hides the other stops while you listen, and returns them when you leave

One source is almost always stronger than three. Shadow is a tool: it hides what must not compete for the eye.

**"One light" does not mean "dark background".** Daylight, paper under a lamp, snow glare, an overexposed photograph are single-source light too. A near-black field with one warm accent is itself a genre default — take it only when the subject is literally dark (night, a cave, a closed room), and say why. If the last pieces in `LINES.md` were dark, this one must justify it twice.

### Step 3. Build the palette → `## Palette`

4–6 exact values, each with a name and a role. The roles come from the light and the shots, not from taste.

    D5  paper     #EEF0EA   the daylight field — the line’s world (level 1)
    D6  ink       #1F2A2E   the line, the stop names, the text
    D7  signal    #D8452B   the tram route colour — the line itself, and nothing else
    D8  lamp      #F2C14E   spent ONCE: the lamp over the platform at the moment (S5)
    D9  shade     #8F988F   dimmed stops while you listen — neutral leaning toward ink, not grey

Rules:

- **Neutrals are chosen, not taken by default.** Pure grey reads as unconsidered; grey leaning toward the accent reads as chosen.
- **The accent is spent in one place** (I5). A strong move: one colour that appears exactly once, at the moment the piece exists for.
- Check the palette against the builder's usual defaults and name them if you are close (cream + serif + terracotta; near-black + acid green; purple-blue gradient). Close is allowed only with a reason from the material.

### Step 4. Assign the type → `## Type`

Two or three roles: a display face with character, a text face, a utility face. The display face is not the one everything else is set in.

    D10 display   a condensed grotesque in the family of transit signage — stop names, her name
    D11 text      a quiet humanist sans — the one-line descriptions
    D12 utility   the display face at small size — years, "stop anywhere to listen"

Check that each face covers every script the material needs (Latin with diacritics for "Kovač", Cyrillic, Hebrew, Arabic…). Many beautiful Latin faces don't, and you find out on screen.

### Step 5. Name the material → `## Material`

What the world is made of: paper, glass, metal, smoke, ink, film. Material gives rules of behaviour — paper creases, glass glints, smoke has no edge. Without a material, the piece looks "made in a browser", because it was.

    D13 material   printed timetable paper: matte, slightly toothy; ink sits on it, never glows
                   behaviour: nothing is glossy; the only light that glows is the lamp (D8)

### Step 6. Say where the complexity goes → `## Impression, not machinery`

One paragraph: what the visitor will *see* the effort in — contrast, timing, composition — and what you deliberately will not engineer.

> From the author's practice: five modules in a row, each more complex than the last. The simplest — vertex-shader deformation — was loved. The most complex — a GPU flock, 16,384 springs, state in two textures — failed: the first screen was almost black, the effect was buried.

The sign you have gone wrong: you want to print a number in the interface ("16,384 particles", "60 fps"). The number impresses the author, not the viewer.

    the effort goes into the timing of the lamp (S5) and the 1.2-second ride (S3);
    no 3D, no particles, no shaders — the line is flat print and stays flat

### Step 7. Map the look to the space → `## Per zone`

Every zone and every key shot gets its light, colours and type by ID (I4), so the builder can check each place separately.

    Z1–Z4 at level 1   D4 daylight, D5 paper, D6 ink, D7 signal; names in D10
    Z2 at S5         D4 dims, D8 lamp over the platform, D9 shade on the rest
    Z5 terminus      D6 ink on D5 paper; the contact in D10, same size as her name

### Step 8. Record the rejected → `## Rejected`

    night tram with neon (near-black + one accent) — a genre default; nothing in the material is dark
    waveform as decoration — shows sound as a wave, which everyone does; D2 shows it as density

## Output: `look.md`

    # <name>
    ## Sources                      D1…, two or three non-web sources, the principle from each
    ## Light                        where from, how many, what is in shadow, how it changes
    ## Palette                      4–6 hex values with names and roles; where the accent is spent
    ## Type                         display / text / utility; scripts covered
    ## Material                     what the world is made of, and how it behaves
    ## Impression, not machinery    where the effort goes, what is not engineered
    ## Per zone                     each zone and key shot → D IDs
    ## Rejected

## Exit criteria

- [ ] At least two sources, none of them a website, each with a principle (not a form)
- [ ] Light is decided before colour, with one main source and a named shadow
- [ ] 4–6 colours, each with a role; the accent is spent in one named place (I5)
- [ ] A dark field is justified by the subject, or not used
- [ ] Type roles cover every script in the material
- [ ] A material with behaviour rules
- [ ] Every zone and the moment have their look by ID (I4)
- [ ] No taste words in any decision (I10)
- [ ] *Rejected* is not empty (I8)

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| The moodboard is all websites | The genre average | Replace with painting, print, film, architecture, science |
| Near-black with one warm accent, again | "One light" read as "dark" | Step 2: find the single source in daylight or on paper |
| The accent colour is on every button | Spent everywhere = spent nowhere | Give it one place, at the moment |
| "Premium, calm, elegant" | Taste words | Rewrite as light, colour and material decisions |
| A beautiful Latin face; the name has diacritics | Script not checked | Step 4 check |

## Next

Stage 5, handoff: compile everything into `DIRECTION.md` for the builder.
