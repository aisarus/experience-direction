#!/usr/bin/env python3
"""Report which experience-direction gates are passed in a project.

Usage: check_gates.py [PROJECT_DIR]

Stage files are looked up in PROJECT_DIR/design/ first, then PROJECT_DIR/.
Prints the mode, each gate's state and the stage to resume at.
Exit code: 0 when every gate for building is passed, 1 otherwise.
"""
import re
import sys
from pathlib import Path

FULL = [
    ("1. Scenario", "scenario.md", "references/0-name.md, then references/1-scenario.md"),
    ("2. Direction", "storyboard.md", "references/2-direction.md"),
    ("3. Space", "space.md", "references/3-space.md"),
    ("4. Look", "look.md", "references/4-look.md"),
]
# Words that must appear in a stage file for it to count as written, not stubbed.
REQUIRED = {
    "scenario.md": ["concept", "not"],
    "space.md": ["placement", "edge"],
    "look.md": ["light", "#"],
}
MIN_CHARS = 200
PLACEHOLDER = re.compile(r"\[[A-Z][A-Z0-9 _-]{2,}\]")


def find(root: Path, name: str):
    for d in (root / "design", root):
        p = d / name
        if p.is_file():
            return p
    return None


def written(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < MIN_CHARS:
        return False, f"only {len(text.strip())} characters"
    missing = [w for w in REQUIRED.get(path.name, []) if w not in text.lower()]
    if missing:
        return False, "does not mention " + ", ".join(repr(w) for w in missing)
    return True, ""


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 2

    brief = find(root, "brief.md")
    print(f"project: {root}")
    resume = None

    if brief:
        print("mode:    light (brief.md)")
        ok, why = written(brief)
        print(f"  [{'x' if ok else ' '}] brief.md" + ("" if ok else f"  — {why}"))
        if not ok:
            resume = ("Light brief", "design/brief.md", "SKILL.md, section Two modes")
    else:
        print("mode:    full")
        for stage, name, ref in FULL:
            path = find(root, name)
            ok, why = written(path) if path else (False, "missing")
            print(f"  [{'x' if ok else ' '}] {stage:<13} {name}" + ("" if ok else f"  — {why}"))
            if not ok and resume is None:
                resume = (stage, name, ref)
        scenario = find(root, "scenario.md")
        if scenario:
            first = scenario.read_text(encoding="utf-8", errors="replace").lstrip().splitlines()[:1]
            if not first or not first[0].startswith("#"):
                print("  [ ] 0. Name        scenario.md has no '# <name>' header")
                resume = resume or ("0. Name", "scenario.md", "references/0-name.md")

    if resume is None:
        handoff = root / "DIRECTION.md"
        ok = handoff.is_file() and "acceptance" in handoff.read_text(encoding="utf-8", errors="replace").lower()
        print(f"  [{'x' if ok else ' '}] 5. Handoff    DIRECTION.md" + ("" if ok else "  — missing, or has no acceptance checks"))
        if not ok:
            resume = ("5. Handoff", "DIRECTION.md", "references/5-handoff.md")

    lines = root / "LINES.md"
    print(f"  [{'x' if lines.is_file() else ' '}] LINES.md      (punch, 3 s / 30 s / 3 min — written at handoff; line — after the build)")

    placeholders = set()
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in {".html", ".md", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte"} \
                and "node_modules" not in p.parts and p.name not in {"LINES.md"}:
            placeholders.update(PLACEHOLDER.findall(p.read_text(encoding="utf-8", errors="replace")))
    if placeholders:
        print("placeholders still present: " + ", ".join(sorted(placeholders)))

    if resume:
        stage, name, ref = resume
        print(f"\nresume at: {stage} — write {name} (read {ref})")
        return 1
    print("\ndirection complete — DIRECTION.md is ready for the builder")
    return 0


if __name__ == "__main__":
    sys.exit(main())
