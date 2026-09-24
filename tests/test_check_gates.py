"""Tests for skills/experience-direction/scripts/check_gates.py. Run: python3 -m unittest discover tests"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/experience-direction/scripts/check_gates.py"

FULL = {
    "scenario.md": "# Mira Kovač — sound\n## Material\nM1 Tram 17 approved\n## Visitors\nV1 audio director (MAIN)\n"
                   "## Takeaway\nthe tram line portfolio\n## Concepts\nC1 C2 C3\n## Punch\nP the sea came up\n"
                   "## Course\nK0 the line\n## Not included\nX1 burnout, personal\n## Rejected\nC1 map, no placement law\n",
    "storyboard.md": "# Mira Kovač — sound\n## Point of view\nside\n## Inputs\nscroll\n## Shown and hidden\nline\n"
                     "## Shots\nS1 <- K0\n## Pace\nS1 still\n## Without motion, on a phone\ncut\n## Rejected\nfirst person, hides the four works\n",
    "space.md": "# Mira Kovač — sound\n## Type\nstrip\n## Edges\nhorizon\n## Levels\n1 line\n## Placement law\nby time\n"
                "## Distances\nyears\n## Where the visitor stands\nbeside\n## Diagram\nZ1 <- S1\n## Rejected\nmap, no readable law\n",
    "look.md": "# Mira Kovač — sound\n## Sources\nD1 timetable\n## Light\ndaylight\n## Palette\n#EEF0EA paper\n## Type\ngrotesque\n"
               "## Material\npaper\n## Impression, not machinery\ntiming\n## Per zone\nZ1 D1\n## Rejected\nnight neon, genre default\n",
}
DIRECTION = ("# Mira Kovač — sound\n## Who and why\nV1\n## Concept\nline\n## Punch\nP\n## Course\nK0\n## Shots\nS1\n## Inputs\nscroll\n"
             "## Space\nstrip\n## Look\nD1\n## Not included\nX1 burnout\n## Real material\nM1 [EMAIL]\n"
             "## Departures from the builder's defaults\nprint lines\n## Acceptance — the build is not done until\nA1 small window\n")


def run(files):
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "design").mkdir()
        for name, text in files.items():
            target = root / name if name in ("DIRECTION.md", "LINES.md") else root / "design" / name
            target.write_text(text, encoding="utf-8")
        p = subprocess.run([sys.executable, str(SCRIPT), d], capture_output=True, text=True)
        return p.returncode, p.stdout


class CheckGates(unittest.TestCase):
    def test_empty_project_resumes_at_scenario(self):
        code, out = run({})
        self.assertEqual(code, 1)
        self.assertIn("resume at: 1. Scenario", out)

    def test_missing_section_is_reported(self):
        files = dict(FULL)
        files["scenario.md"] = files["scenario.md"].replace("## Takeaway\nthe tram line portfolio\n", "")
        code, out = run(files)
        self.assertEqual(code, 1)
        self.assertIn("missing section '## Takeaway'", out)
        self.assertIn("resume at: 1. Scenario", out)

    def test_empty_rejected_breaks_I8(self):
        files = dict(FULL)
        files["space.md"] = files["space.md"].replace("## Rejected\nmap, no readable law\n", "## Rejected\n\n")
        code, out = run(files)
        self.assertIn("'## Rejected' is empty", out)
        self.assertIn("resume at: 3. Space", out)

    def test_stages_done_resumes_at_handoff(self):
        code, out = run(FULL)
        self.assertEqual(code, 1)
        self.assertIn("resume at: 5. Handoff", out)

    def test_complete_direction_passes_and_lists_placeholders(self):
        code, out = run({**FULL, "DIRECTION.md": DIRECTION})
        self.assertEqual(code, 0, out)
        self.assertIn("direction complete", out)
        self.assertIn("[EMAIL]", out)

    def test_light_mode_uses_brief(self):
        brief = ("# Kilo\n## Material\nM1\n## Visitors\nV1 MAIN\n## Concept\nx\n## Punch\nP\n## Course\nK0\n## Shots\nS1\n"
                 "## Space\nstrip\n## Look\n#112233\n## Three minutes\n3 s\n## Not included\nX1 benchmarks, none given\n")
        code, out = run({"brief.md": brief})
        self.assertIn("mode:    light", out)
        self.assertIn("resume at: 5. Handoff", out)


if __name__ == "__main__":
    unittest.main()
