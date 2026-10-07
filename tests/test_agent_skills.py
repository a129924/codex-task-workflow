"""TC-AGENT-SKILLS-001: execute installed tracker CLI in disposable fixtures.

Prompt skills require separate real-agent evidence; these tests do not certify
skill discovery, independent review, dispatch or worktree authorization policy.
"""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest


class AgentSkillsTestCase(unittest.TestCase):
    """Exercise observable CLI behavior without modifying any repository."""

    entry = Path(__file__).resolve().parents[1] / ".agents/skills/plan-step-tracker/scripts/step_tracker.py"
    operations = ("read_all", "read_not_run", "read_success", "check_all_succeeded", "check_impl_steps_succeeded")

    def run_cli(self, operation, content):
        with tempfile.TemporaryDirectory(prefix="TC-AGENT-SKILLS-001-", dir="/private/tmp") as fixture:
            if content is not None:
                destination = Path(fixture) / "plan/fixture/fixture.step.md"
                destination.parent.mkdir(parents=True)
                destination.write_text(content, encoding="utf-8")
            environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            return subprocess.run([sys.executable, str(self.entry), operation, "fixture"], cwd=fixture, env=environment, text=True, capture_output=True, check=False)

    def test_installed_entry_and_success(self):
        self.assertGreaterEqual(sys.version_info, (3, 11))
        self.assertTrue(self.entry.is_file())
        content = "## Implementation Steps\n- [X] 1. Implement fixture\n## Lifecycle\n- [X] Independent review\n"
        for operation in self.operations:
            with self.subTest(operation=operation):
                result = self.run_cli(operation, content)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                if operation == "read_not_run":
                    self.assertEqual(result.stdout, "")
                elif operation.startswith("read_"):
                    self.assertEqual(result.stdout.splitlines(), ["[X] 1. Implement fixture", "[X] Independent review"])
                else:
                    self.assertIn("SUCCESS", result.stdout)

    def test_read_filtering_and_distinct_gates(self):
        content = "## Implementation Steps\n- [X] Implemented\n## Lifecycle\n- [ ] Review pending\n"
        expected = {
            "read_all": (0, "[X] Implemented\n[ ] Review pending\n"),
            "read_not_run": (0, "[ ] Review pending\n"),
            "read_success": (0, "[X] Implemented\n"),
        }
        for operation, (code, output) in expected.items():
            with self.subTest(operation=operation):
                result = self.run_cli(operation, content)
                self.assertEqual(result.returncode, code)
                self.assertEqual(result.stdout, output)
        for operation, code in (("check_impl_steps_succeeded", 0), ("check_all_succeeded", 1)):
            with self.subTest(operation=operation):
                result = self.run_cli(operation, content)
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertIn("SUCCESS" if code == 0 else "BLOCKED", result.stdout)

    def test_lowercase_is_pending_with_warning(self):
        content = "## Implementation Steps\n- [x] Needs proof\n"
        for operation in self.operations:
            with self.subTest(operation=operation):
                result = self.run_cli(operation, content)
                self.assertEqual(result.returncode, 1 if operation.startswith("check_") else 0)
                self.assertIn("lowercase [x]", result.stderr)
                if operation == "read_success":
                    self.assertEqual(result.stdout, "")
                if operation in ("read_all", "read_not_run"):
                    self.assertEqual(result.stdout, "[x] Needs proof\n")

    def test_missing_empty_duplicate_implementation_section(self):
        fixtures = {
            "missing": "## Other\n- [X] A\n",
            "empty": "## Implementation Steps\n## Other\n- [X] A\n",
            "duplicate": "## Implementation Steps\n- [X] A\n## Implementation Steps\n- [X] B\n",
        }
        for fixture, content in fixtures.items():
            for operation in self.operations:
                with self.subTest(fixture=fixture, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, 1 if operation == "check_impl_steps_succeeded" else 0)
                    if operation == "check_impl_steps_succeeded":
                        self.assertIn("Error:", result.stderr)
                    elif operation.startswith("read_"):
                        expected = "" if operation == "read_not_run" else "[X] A\n" + ("[X] B\n" if fixture == "duplicate" else "")
                        self.assertEqual(result.stdout, expected)

    def test_missing_file_and_fenced_evidence(self):
        for operation in self.operations:
            with self.subTest(operation=operation, fixture="missing-file"):
                result = self.run_cli(operation, None)
                self.assertEqual(result.returncode, 1)
                self.assertIn("File not found", result.stderr)
        fenced = "## Implementation Steps\n```markdown\n- [X] Example only\n```\n"
        for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
            with self.subTest(operation=operation, fixture="fenced-only"):
                result = self.run_cli(operation, fenced)
                self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
