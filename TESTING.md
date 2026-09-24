# Testing

What was tested, how, and what failed. Failures stay in this file: they are why the skill looks the way it does.

## 1. Automated evals (`claude plugin eval`)

Each case runs **with** the plugin and **without** it (a baseline arm with the same model and tools). Graders are file checks plus an LLM judge (3 votes).

| Case | What must happen | With | Without |
|---|---|---|---|
| `portfolio-stages` | Real material → four stage files and a `DIRECTION.md` with visitor, concept, punch, shots, space, look, acceptance checks; nothing invented; no code | **2/2** | 0/2 |
| `missing-material-asks` | "Immersive portfolio" with no material → asks for it, writes no code, invents nothing | **3/3** | 2/3 |
| `product-page-routed` | A showcase page for a small tool, asked to be "memorable" → *not* directed; a clear page | **3/3** | 2/3 |
| `routine-cafe-handoff` | A café landing page → *not* directed | see below | |

The café case is being re-run after its grader was split into two questions: *did the skill stay out of the way* (the skill's job) and *did the builder invent facts* (the builder's job — it happens with and without the plugin, e.g. "roasted on site").

Run it yourself:

```
claude plugin eval . --trust-plugin --allow-tools Write Edit
```

### What the evals caught

| Round | Finding | Fix |
|---|---|---|
| 1 | The skill **never fired on its own** — not even for "an immersive portfolio, like Bruno Simon". The model asked its own questions instead | Description rewritten to be used *first*, before clarifying questions |
| 1 | Café pages gained invented facts ("roasted on site") | No-invention rule stated for handed-off pages too |
| 5 | Skill now fires where it should (5/5), but directed a **tool page** because the user wrote "memorable, not generic" — words the description used as triggers | Gate A decides by *what the thing is*, not by adjectives (0/3 → 3/3) |

## 2. Blind visual comparison

The same brief is built twice; a person compares the pages without knowing which is which, in a ~500×400 window, three seconds, then a minute or two of use.

### Round 1 — the old skill (director *and* builder)

| Brief | Winner | Result for the skill |
|---|---|---|
| Portfolio of a sound designer | the page **without** the skill | loss |
| Interactive story (Tunguska event) | both fine | tie |
| Showcase for a small editor | both weak | tie |

The ideas with the skill were clearly stronger — a concept and a punch instead of a list of sections — but the pages were not better. The losing portfolio opened on a black field with "stand still" and hid the name and the work behind the mechanic: the strongest concept of the batch, a wall for the visitor it was written for.

**What changed because of it:**

- The scope moved from *designing* to *directing*: the skill now stops at a direction document and hands it to a builder. Rendering craft is the builder's job.
- Invariant I2: by the third second the main visitor knows whose this is and what is here. The concept changes *how*, never *whether*.
- A rule against the dark default: all three pages with the skill came out near-black with one accent, which is itself a generic AI look.
- Every stage was rewritten as a procedure with exit criteria, and ten invariants were added.

### Round 2 — the new skill (director only; a separate session builds from `DIRECTION.md`)

Pending: blind review of three pairs (a new portfolio brief that is not the skill's worked example, the Tunguska story, the editor showcase).

## 3. Unit tests

`tests/test_check_gates.py` covers the gate checker: missing sections, empty refusals, resume points, light mode, placeholder listing.

```
python3 -m unittest discover tests
```

## Not yet tested

- Human review by people other than the author (planned: 2–3 people, blind).
- Other models than the default one.
- Real projects with real material, end to end.
