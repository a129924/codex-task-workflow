"""TC-AGENT-SKILLS-001: execute installed tracker CLI in disposable fixtures.

Prompt skills require separate real-agent evidence; these tests do not certify
skill discovery, independent review, dispatch or worktree authorization policy.
"""
from pathlib import Path
import os
import importlib.util
import subprocess
import sys
import tempfile
import unittest


class AgentSkillsTestCase(unittest.TestCase):
    """Exercise observable CLI behavior without modifying any repository."""

    entry = Path(__file__).resolve().parents[1] / ".agents/skills/plan-step-tracker/scripts/step_tracker.py"
    operations = ("read_all", "read_not_run", "read_success", "check_all_succeeded", "check_impl_steps_succeeded")

    def run_cli(self, operation, content):
        with tempfile.TemporaryDirectory(prefix="TC-AGENT-SKILLS-001-") as fixture:
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

    def test_unsafe_topics_never_read_outside_fixture(self):
        with tempfile.TemporaryDirectory(prefix="tracker-outside-") as outside:
            sentinel = Path(outside) / "sentinel.step.md"
            original = "## Implementation Steps\n- [X] OUTSIDE_SENTINEL\n"
            sentinel.write_text(original, encoding="utf-8")
            topics = (str(sentinel.with_suffix("")), "a/b", "a\\b", ".", "..", "")
            for topic in topics:
                for operation in self.operations:
                    with self.subTest(topic=topic, operation=operation):
                        with tempfile.TemporaryDirectory(prefix="tracker-topic-") as fixture:
                            result = subprocess.run([sys.executable, str(self.entry), operation, topic], cwd=fixture, text=True, capture_output=True, check=False)
                        self.assertEqual(result.returncode, 1)
                        self.assertIn("Error:", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
                        self.assertNotIn("OUTSIDE_SENTINEL", result.stdout + result.stderr)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), original)

    def test_symlink_escape_is_rejected_by_every_operation(self):
        with tempfile.TemporaryDirectory(prefix="tracker-links-") as fixture, tempfile.TemporaryDirectory(prefix="tracker-outside-") as outside:
            root = Path(fixture)
            sentinel = Path(outside) / "escape.step.md"
            original = "## Implementation Steps\n- [X] OUTSIDE_SENTINEL\n"
            sentinel.write_text(original, encoding="utf-8")
            for variant in ("topic-directory", "step-file", "plan-root"):
                plan = root / "plan"
                if variant == "plan-root":
                    plan.symlink_to(outside, target_is_directory=True)
                else:
                    plan.mkdir()
                    topic = plan / "escape"
                    if variant == "topic-directory":
                        topic.symlink_to(outside, target_is_directory=True)
                    else:
                        topic.mkdir()
                        (topic / "escape.step.md").symlink_to(sentinel)
                for operation in self.operations:
                    with self.subTest(variant=variant, operation=operation):
                        result = subprocess.run([sys.executable, str(self.entry), operation, "escape"], cwd=root, text=True, capture_output=True, check=False)
                        self.assertEqual(result.returncode, 1)
                        self.assertIn("resolves outside", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
                        self.assertNotIn("OUTSIDE_SENTINEL", result.stdout + result.stderr)
                if plan.is_symlink():
                    plan.unlink()
                else:
                    if topic.is_symlink():
                        topic.unlink()
                    else:
                        (topic / "escape.step.md").unlink()
                        topic.rmdir()
                    plan.rmdir()
            self.assertEqual(sentinel.read_text(encoding="utf-8"), original)

    def test_read_failures_return_errors_without_traceback(self):
        for variant in ("directory", "invalid-utf8"):
            with tempfile.TemporaryDirectory(prefix="tracker-read-error-") as fixture:
                target = Path(fixture) / "plan/fixture/fixture.step.md"
                target.parent.mkdir(parents=True)
                if variant == "directory":
                    target.mkdir()
                else:
                    target.write_bytes(bytes([255]))
                for operation in self.operations:
                    with self.subTest(variant=variant, operation=operation):
                        result = subprocess.run([sys.executable, str(self.entry), operation, "fixture"], cwd=fixture, text=True, capture_output=True, check=False)
                        self.assertEqual(result.returncode, 1)
                        self.assertIn("Error:", result.stderr)
                        self.assertNotIn("Traceback", result.stderr)
                        self.assertEqual(result.stdout, "")

    def test_fences_require_matching_whitespace_only_closure(self):
        fences = (("```", "```not-a-closing-fence", "```"), ("~~~", "~~~not-a-closing-fence", "~~~"), ("````", "```", "````"), ("~~~~", "~~~", "~~~~"), ("```", "~~~", "```"), ("~~~", "```", "~~~"))
        for opening, false_close, real_close in fences:
            content = "## Implementation Steps\n- [X] Done\n" + opening + "markdown\n" + false_close + "\n- [X] Example only\n" + real_close + "  \n- [ ] Pending\n"
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(opening=opening, false_close=false_close, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("[ ] Pending", result.stdout)
                    self.assertNotIn("Example only", result.stdout)

    def test_nested_tasks_fail_closed_but_code_examples_are_ignored(self):
        for indentation in ("  ", "    ", "\t"):
            for marker in ("[ ]", "[X]"):
                content = "## Implementation Steps\n- [X] Parent\n" + indentation + "- " + marker + " Child\n"
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(indentation=indentation, marker=marker, operation=operation):
                        result = self.run_cli(operation, content)
                        self.assertEqual(result.returncode, 1)
                        self.assertIn("Malformed or unsupported", result.stderr)
        for continuation in ("  - Notes", "  Description"):
            content = "## Implementation Steps\n- [X] Parent\n" + continuation + "\n    - [ ] Child\n"
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(continuation=continuation, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("Malformed or unsupported", result.stderr)
        code = "## Implementation Steps\n- [X] Implemented\n\nAn indented code example follows:\n\n    - [ ] Example only\n"
        for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
            with self.subTest(operation=operation, fixture="indented-code"):
                result = self.run_cli(operation, code)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("SUCCESS", result.stdout)

    def test_implementation_heading_boundaries(self):
        for heading in ("# Lifecycle", "## Lifecycle"):
            content = "## Implementation Steps\n- [X] Implemented\n" + heading + "\n- [ ] Review pending\n"
            for operation, expected in (("check_impl_steps_succeeded", 0), ("check_all_succeeded", 1)):
                with self.subTest(heading=heading, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)
        for content in ("## Implementation Steps\n- [X] Implemented\n### More implementation\n- [ ] Pending\n", "## Implementation Steps\n- [X] Implemented\n```markdown\n# Example heading\n```\n- [ ] Pending\n"):
            with self.subTest(content=content):
                result = self.run_cli("check_impl_steps_succeeded", content)
                self.assertEqual(result.returncode, 1)
                self.assertIn("[ ] Pending", result.stdout)

    def test_public_parsers_share_path_and_section_boundaries(self):
        spec = importlib.util.spec_from_file_location("installed_tracker_regression", self.entry)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory(prefix="tracker-parser-") as fixture:
                plan = Path(fixture) / "plan"
                target = plan / "fixture/fixture.step.md"
                target.parent.mkdir(parents=True)
                target.write_text("## Implementation Steps\n- [X] Implemented\n# Lifecycle\n- [ ] Review pending\n", encoding="utf-8")
                self.assertEqual([step.text for step in module.parse_impl_steps("fixture", plan)], ["Implemented"])
                self.assertEqual([step.text for step in module.parse_steps("fixture", plan)], ["Implemented", "Review pending"])
                for parser in (module.parse_steps, module.parse_impl_steps):
                    with self.subTest(parser=parser.__name__):
                        with self.assertRaises(ValueError):
                            parser("../escape", plan)
        finally:
            del sys.modules[spec.name]


if __name__ == "__main__":
    unittest.main()
