# Check: the line

Run after the piece is built, before starting the next one. A new piece continues a named line, refutes it, or opens a new one.

## Why

> From the author's practice: a project folder held eighty-seven pieces. Not one referred to any other. Eighty-seven first steps and not a single second one.

A master differs from a generator not in the quality of a single thing, but in that the things know about each other. A heap of a hundred pieces is worth less than six pieces where you can see how a technique grew.

## The rule

Every new piece does one of three things — and says out loud which:

    CONTINUES    takes a named technique from a previous piece and carries it further
                 "88 continues 73: there the deformation ran across a plane,
                  here it runs through a volume"

    REFUTES      takes a technique and shows that it doesn't work.
                 That is also kinship, and often more honest than continuation
                 "89 refutes 88: in a volume the deformation reads as noise,
                  the technique is dead"

    OPENS        declares a new line. Allowed no more than once per five pieces,
                 and the previous line is closed in words:
                 "the deformation line is finished, because ..."
                 The first piece in a project always opens; there is nothing to close.

## What does NOT count as kinship

- A shared library. The same `components.js` is plumbing, not a line
- A shared palette or shared style lock
- The word "kinetic" in both names
- "Both pieces are about light"

Kinship is a specific technique, named in words, and a visible difference in what was done with it.

## Where it is recorded

`LINES.md` at the project root, in the `line` field of the piece's block (format in SKILL.md). Refer to pieces by name, or by number if the project numbers them:

    ## 88
    line       continues 73 — deformation moved from the plane to the volume
    ## 89
    line       refutes 88 — in a volume the deformation reads as noise, technique dead
    ## 90
    line       opens — "sound drives the picture". Deformation closed

Three lines like these are already a history. Eighty-seven folders without them are a heap.

## Gate

- [ ] The piece is named a continuation, a refutation or an opening
- [ ] For the first two, a specific previous piece is named
- [ ] Kinship is not reduced to a shared library, palette or topic
- [ ] The line is appended to `LINES.md`
- [ ] "Opens" no more than once per five pieces, with the previous line closed (the first piece is exempt)
