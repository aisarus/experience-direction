#!/usr/bin/env python3
"""Report which experience-direction gates are passed in a project.

Usage: check_gates.py [PROJECT_DIR]

Stage files are looked up in PROJECT_DIR/design/ first, then PROJECT_DIR/.
DIRECTION.md and LINES.md are looked up in PROJECT_DIR/.

For each stage file it checks the required sections (the output format in
the stage reference) and the IDs the invariants rely on. It cannot judge the
quality of a decision; it catches missing sections, empty refusals and
broken references, and tells you where to resume.

Exit code: 0 when the direction is complete, 1 otherwise, 2 on bad usage.
"""
import re
import sys
from pathlib import Path

# file -> (stage label, reference, required sections, required ID patterns)
STAGES = [
    ("scenario.md", "1. Scenario", "references/0-name.md, then references/1-scenario.md",
     ["Material", "Visitors", "Takeaway", "Concepts", "Punch", "Course", "Not included", "Rejected"],
     [r"\bM1\b", r"\bV1\b", r"\bK0\b", r"\bMAIN\b"]),
    ("storyboard.md", "2. Direction", "references/2-direction.md",
     ["Point of view", "Inputs", "Shown and hidden", "Shots", "Pace", "Without motion", "Rejected"],
     [r"\bS1\b", r"\bK\d+\b"]),
    ("space.md", "3. Space", "references/3-space.md",
     ["Type", "Edges", "Levels", "Placement law", "Distances", "Where the visitor stands", "Diagram", "Rejected"],
     [r"\bZ1\b", r"\bS\d+\b"]),
    ("look.md", "4. Look", "references/4-look.md",
     ["Sources", "Light", "Palette", "Type", "Material", "Impression", "Per zone", "Rejected"],
     [r"\bD1\b", r"#[0-9A-Fa-f]{6}\b", r"\bZ\d+\b"]),
]
BRIEF = ("brief.md", "Light brief", "SKILL.md, section Two modes",
         ["Material", "Visitors", "Concept", "Punch", "Course", "Shots", "Space", "Look", "Three minutes", "Not included"],
         [r"\bM1\b", r"\bV1\b", r"\bK0\b", r"#[0-9A-Fa-f]{6}\b"])
DIRECTION = ("DIRECTION.md", "5. Handoff", "references/5-handoff.md",
             ["Who and why", "Concept", "Punch", "Course", "Shots", "Inputs", "Space", "Look",
              "Not included", "Real material", "Departures", "Acceptance"],
             [r"\bA1\b", r"\bV1\b"])
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _-]{2,}\]")
TEXT_SUFFIXES = {".html", ".htm", ".md", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro"}


def find(root: Path, name: str):
    for d in (root / "design", root):
        p = d / name
        if p.is_file():
            return p
    return None


def sections(text: str) -> dict:
    """Map each '## Heading' to the text under it."""
    out, current = {}, None
    for line in text.splitlines():
        m = re.match(r"##\s+(.+?)\s*$", line)
        if m and not line.startswith("###"):
            current = m.group(1).strip()
            out[current] = ""
        elif current is not None:
            out[current] += line + "\n"
    return out


def check(path: Path, required, ids):
    """Return a list of problems with a stage file (empty = passes)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    problems = []
    first = text.lstrip().splitlines()[:1]
    if not first or not first[0].startswith("# "):
        problems.append("no '# <name>' header on the first line")
    found = sections(text)
    for want in required:
        match = next((k for k in found if k.lower().startswith(want.lower())), None)
        if match is None:
            problems.append(f"missing section '## {want}'")
        elif want in ("Rejected", "Not included") and len(found[match].strip()) < 10:
            problems.append(f"section '## {want}' is empty (invariant I8)")
    for pat in ids:
        if not re.search(pat, text):
            problems.append(f"no {pat.strip(chr(92) + 'b')} found")
    return problems


def report(label, name, problems):
    mark = "x" if not problems else " "
    print(f"  [{mark}] {label:<13} {name}")
    for p in problems:
        print(f"        - {p}")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 2

    print(f"project: {root}")
    resume = None
    brief = find(root, "brief.md")
    stages = [BRIEF] if brief else STAGES
    print("mode:    " + ("light (brief.md)" if brief else "full"))

    for name, label, ref, required, ids in stages:
        path = find(root, name)
        problems = check(path, required, ids) if path else ["missing"]
        report(label, name, problems)
        if problems and resume is None:
            resume = (label, name, ref)

    if resume is None:
        name, label, ref, required, ids = DIRECTION
        path = root / name
        problems = check(path, required, ids) if path.is_file() else ["missing"]
        report(label, name, problems)
        if problems:
            resume = (label, name, ref)

    lines = root / "LINES.md"
    print(f"  [{'x' if lines.is_file() else ' '}] {'LINES.md':<13} punch and 3 s / 30 s / 3 min at handoff; line after the build")

    placeholders = set()
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in TEXT_SUFFIXES and "node_modules" not in p.parts:
            placeholders.update(PLACEHOLDER.findall(p.read_text(encoding="utf-8", errors="replace")))
    if placeholders:
        print("placeholders present: " + ", ".join(sorted(placeholders)))

    if resume:
        label, name, ref = resume
        print(f"\nresume at: {label} — write or fix {name} (read {ref})")
        return 1
    print("\ndirection complete — DIRECTION.md is ready for the builder")
    return 0


if __name__ == "__main__":
    sys.exit(main())
