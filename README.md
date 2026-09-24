# Experience Direction

> **Status: in testing.** Not released yet — see [TESTING.md](TESTING.md) once it lands.

**Direction before design.** A Claude Code skill that acts as the director of an immersive web experience — not the designer, not the developer. Before anyone picks a font or writes a line of code, it decides what happens to the person who arrives, and hands one checkable document to whoever builds.

AI-built "immersive" sites fail the same way: one clever effect with an ordinary page around it. The model isn't bad at drawing; it jumps from brief to code, and nobody ever invents the idea. Film solved this long ago: script before shooting, direction before set building — and the director never paints the set.

```
brief + real material
   │
   ▼
0 name ─▶ 1 scenario ─▶ 2 direction ─▶ 3 space ─▶ 4 look ─▶ 5 handoff
          scenario.md   storyboard.md   space.md   look.md   DIRECTION.md
                                                                 │
                                         frontend-design · another tool · a human designer
```

| Stage | Answers |
|---|---|
| **Scenario** | Who arrives and why, what they take away, the concept, what is left out |
| **Direction** | Point of view, pace, what stays hidden, where the eye goes, the first shot |
| **Space** | The type of space, its edges, and the one law that decides where things stand |
| **Look** | Light before colour; palette, type, material — and sources that are *not websites* |
| **Handoff** | `DIRECTION.md`: every decision on one page, plus acceptance checks the builder must pass |

Three checks run along the way:

- **Punch** — one sentence with an *event* ("the floor remembered where I walked"). Remove it and the work must fall apart.
- **Three minutes** — what the person finds at 3 s, 30 s and 3 min. The third-minute discovery is labelled nowhere.
- **Line** — every new piece continues, refutes or opens a named line of work (`LINES.md`).

## What it will not do

- **Build.** The output is a document. Build it with Anthropic's [`frontend-design`](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) skill, with any other tool, or give it to a person.
- **Direct a routine page.** Café or shop landings, product pages, dashboards, forms, docs — they need to be clear and fast, not a "world". It says so in one line and steps aside.
- **Invent facts.** No material → it asks and waits. Missing facts become marked placeholders like `[ADDRESS]`, listed in the handoff.
- **Hide the basics for the sake of a concept.** By the third second the main visitor knows whose this is and what is here. The concept changes *how* that is shown, never *whether*.

## Install

```
/plugin marketplace add aisarus/experience-direction
/plugin install experience-direction@experience-direction
```

Then ask for something immersive — *"I want an interactive portfolio, here are my projects…"* — or call it directly with `/experience-direction:experience-direction`.

**Two modes.** Full mode writes one file per stage into `design/`. Light mode (single-screen pieces, quick experiments, or "go fast") writes a single `design/brief.md` that still answers every question.

## Where the rules come from

Every rule grew out of a measured failure, and the case travels inside the skill next to the rule it caused: the 16,384-particle GPU flock that lost to the simplest vertex shader; fifteen pages nobody ever looked at; eighty-seven pieces, none of which referred to another — and a portfolio whose concept was the strongest of its batch and still lost a blind test, because the visitor had to solve it before they could read it.

## Testing

See [`TESTING.md`](TESTING.md) for what was tested, how, and what failed. `evals/` holds a [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) suite that runs each case with and without the plugin:

```
claude plugin eval . --trust-plugin --allow-tools Write Edit
```

## License

MIT
