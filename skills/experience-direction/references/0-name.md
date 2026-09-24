# Stage 0. Name

The name of the piece. It comes first because a name that won't come is the earliest sign that there is no subject yet, and that is cheaper to find now than after four stage files.

## Inputs

- The brief and the material inventory (or at least the list of what the material is about).
- The names of other pieces in the same project, if any (`LINES.md`, other folders).

## The rule

**A name names the subject.** Not a mood, not a material, not an epithet.

## Procedure

### Step 1. Say what you are making, in plain words

Complete the sentence "I made ___" in the plainest words possible, as if telling a friend. Do not try to be clever yet.

    I made a map of Mira Kovač's sound work, laid out as a tram line

This sentence is the *working subject*. If you cannot write it, stop: the problem is the idea, not the name. Go to stage 1, write the concepts, and come back.

### Step 2. Write three candidate names

Derive them from the working subject. At least one should use a real word from the material (a place, a title, an object).

    N1  "Mira Kovač — sound"
    N2  "Line 17"
    N3  "Resonance"

### Step 3. Run the three tests on each

**Substitution.** Say "I made ___" with the name. If the listener would ask "made what?", the name is empty.

    "I made Resonance"          → made what?   FAIL
    "I made Line 17"            → a line, of something — borderline; passes with the subtitle on the page
    "I made Mira Kovač — sound" → clear        PASS

**Portability.** Hold the name up against any other piece in the project, and against any other person's portfolio. If it fits, it is a genre label, not a name.

> From the author's practice: one title, "ETHER 60 — Kinetic Architecture of Luminous Volume", sat on three different pieces at once. The files were different — checksums confirmed it. Three pieces, one name. The name was about the genre, not the work.

**Translation.** If the name is in a different language from the work, say why. `Kinetic Apex`, `Voidframe`, `Nexus`, `Aether`, `Prism`, `Flux`, `Lumen` are T-shirt slogans. A foreign-language name is allowed only when it names the subject more precisely than your own language does, and you can say how.

### Step 4. Reject the forbidden constructions

- Noun + noun with no subject: Voidframe, Lightform, Datascape
- Two or three abstract nouns in a row: "Architecture of Luminous Depth"
- "Digital" plus something lofty: "digital sanctuary", "digital poem"
- A serial number instead of a name: ETHER 80, piece-87
- A double name where the second half explains the first: "Kinetic Apex — a digital sanctuary". One name; explanations live in the description.

A person's own name plus their field ("Mira Kovač — sound") is not a double name: it is the plainest possible subject, and for a portfolio it is often right.

### Step 5. Choose and record

Pick the survivor that is most specific to this subject. Write it as the first line of `scenario.md`, and the rejected candidates with the test that rejected each in `scenario.md → ## Rejected`.

    # Mira Kovač — sound

## Output

- The `# <name>` header of `scenario.md`.
- Rejected names in `scenario.md → ## Rejected`.

## Exit criteria

- [ ] "I made ___" with the name needs no follow-up question
- [ ] The name fits no other piece in the project and no other person's work
- [ ] No other piece in the project carries this name
- [ ] No forbidden construction
- [ ] Rejected candidates are recorded with their test (I8)

The name is checked again by the builder, not now: it must be in `<title>` and on the page itself. That check goes into `DIRECTION.md` as an acceptance check.

## Typical failures

| What you see | What went wrong | Fix |
|---|---|---|
| Every candidate is an abstract noun | There is no subject yet | Write the "I made ___" sentence in plain words first |
| The name is beautiful but you can't say what it names | Mood instead of subject | Substitution test; keep the plain sentence as the subtitle |
| The name is in English "because it sounds better" | Translation test failed | Say what it names more precisely than your language, or drop it |

## Next

Stage 1, scenario. If the name did not come, start stage 1 with the working subject and return here after step 4 of the scenario.
