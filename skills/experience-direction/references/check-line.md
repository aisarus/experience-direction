# Check: the line

How this piece relates to the previous ones. Run after the piece is built, before starting the next one — and at stage 1 if `LINES.md` already has entries, so the new concept knows what it continues.

## Why

> From the author's practice: a project folder held eighty-seven pieces. Not one referred to any other. Eighty-seven first steps and not a single second one.

A master differs from a generator not in the quality of a single thing, but in that the things know about each other. A heap of a hundred pieces is worth less than six pieces where you can see how a technique grew.

## Inputs

- `LINES.md` (may be empty or missing for the first piece).
- This piece's punch and its main technique — the one thing the piece does that another piece could take further.

## Procedure

### Step 1. Name this piece's technique

One phrase: the specific thing this piece does, in words a builder would recognise. Not the topic, not the palette.

    technique   stillness as input: the longer you don't move, the more plays

### Step 2. Find its relatives

Read `LINES.md`. For each earlier piece, ask whether this piece uses, extends or contradicts the same technique. Kinship is a specific technique, named in words, with a visible difference in what was done with it.

These do **not** count as kinship:

- a shared library — the same `components.js` is plumbing, not a line;
- a shared palette or style lock;
- the same word in both names;
- a shared topic ("both are about light").

### Step 3. Declare one of three

    CONTINUES   takes a named technique from a previous piece and carries it further
                "88 continues 73: there the deformation ran across a plane; here it runs through a volume"

    REFUTES     takes a technique and shows it doesn't work — kinship too, often more honest
                "89 refutes 88: in a volume the deformation reads as noise; the technique is dead"

    OPENS       declares a new line. At most once per five pieces, and the previous line is
                closed in words: "the deformation line is finished, because …"
                The first piece in a project always opens; there is nothing to close.

For CONTINUES and REFUTES, name the specific earlier piece and the visible difference.

### Step 4. Record it

Append the `line` field to this piece's block in `LINES.md` (format in `SKILL.md`). Refer to pieces by name, or by number if the project numbers them.

    ## Mira Kovač — sound
    punch   "I stopped at a stop and the sea came up"
    3 s     the whole line, her name, four named stops
    30 s    the lamp and the rising sea at Low Tide
    3 min   stillness between stops plays the Tram 17 recording
    line    opens — "stillness as input". First piece in this project.

Three lines like these are already a history. Eighty-seven folders without them are a heap.

### Step 5. Hand the second punch forward

If the punch check (step 4) moved a second punch out of this piece, write it under the line as the seed of the next piece. That is a ready-made continuation.

## Exit criteria

- [ ] This piece's technique is named in one phrase
- [ ] The piece is declared a continuation, a refutation or an opening
- [ ] For the first two, a specific earlier piece and the visible difference are named
- [ ] Kinship is not a shared library, palette, name or topic
- [ ] "Opens" at most once per five pieces, with the previous line closed (the first piece is exempt)
- [ ] The block is in `LINES.md`
