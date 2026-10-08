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

    def test_invalid_backtick_info_does_not_hide_pending(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        for opening in ("```bad`info", "````bad`info"):
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(opening=opening, operation=operation):
                    result = self.run_cli(operation, prefix + opening + "\n- [ ] Still pending\n```\n")
                    self.assertEqual(result.returncode, 1)
                    self.assertNotIn("SUCCESS", result.stdout)
        for opening, closing in (("```", "```"), ("```markdown", "```"), ("~~~bad`info", "~~~"), ("```html <!--", "```")):
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(valid_opening=opening, operation=operation):
                    result = self.run_cli(operation, prefix + opening + "\n- [ ] Example only\n" + closing + "\n")
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("SUCCESS", result.stdout)

    def test_whole_gate_plain_tasks_and_exact_base_metadata(self):
        prefix = "## Implementation Steps\n- [X] Implemented\n"
        for marker in ("-", "*", "+", "1.", "1)"):
            content = prefix + "## Lifecycle\n" + marker + " Review pending\n"
            for operation, expected in (("check_all_succeeded", 1), ("check_impl_steps_succeeded", 0)):
                with self.subTest(marker=marker, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)
            result = self.run_cli("read_all", content)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "[X] Implemented\n")
        metadata = (
            "- Selected profile: base-plan\n"
            "- Source plan: plan/fixture/fixture.plan.md\n"
            "- Shared lifecycle shell: .agents/skills/step-creator/templates/shared-lifecycle-shell.md\n"
            "- Managed worktree intent: topic=fixture; branch=chore/a129924/fixture; managed-path-intent=/disposable/fixture.worktrees/agent-fixture; primary-worktree=false\n"
            "- Progression truth inputs: plan/fixture/fixture.plan.md; plan/agent-handoff-workflow.md; plan/topic-plan-contract.md\n"
            "- Completion evidence inputs: controlled CLI markers only, not execution evidence\n"
            "- Marker semantics: [X] exact evidence; [ ] pending; [x] pending\n"
            "- Tracker semantics: whole covers all action rows; impl only Implementation Steps\n"
            "- Owner-only updates: only action owner; no overwrite\n"
        )
        # Frozen Base wire shape, with deliberately controlled action markers.
        base = (
            "---\ntopic: fixture\nstep_profile: base-plan\nsource_plan: plan/fixture/fixture.plan.md\ncreated: 2026-10-07\n---\n"
            "# fixture — Step Tracking\n"
            "## Workflow Stages\n| Current status | Allowed next transitions | Next actor |\n| --- | --- | --- |\n| approved | [] | Implementer |\n"
            "## Actionable Steps\n### Observer — Fixed Head\n"
            "- [X] **Actor:** Observer — **Action:** Dispatch authorized feature preparation\n"
            "- [X] **Actor:** Implementer — **Action:** Verify selected feature\n"
            "### Contextual Actions\n- [X] **Actor:** Implementer — **Action:** Execute bounded implementation\n"
            + prefix +
            "## Observer Actionable Steps — Fixed Tail\n"
            "- [X] **Actor:** Observer — **Action:** Dispatch assigned checks to Tester\n"
            "- [X] **Actor:** Tester — **Action:** Execute checks\n"
            "- [X] **Actor:** Observer — **Action:** Dispatch evidence to independent Reviewer\n"
            "- [X] **Actor:** Reviewer — **Action:** Return bounded verdict\n"
            "- [X] **Actor:** Observer — **Action:** Route or stop for human review\n"
            "## Handoff / Gate Notes\n" + metadata
        )
        for variant, content, whole in (
            ("base-control", base, 0),
            ("unknown-action", base + "- Review pending\n", 1),
            ("empty-known-value", base.replace("- Source plan: plan/fixture/fixture.plan.md", "- Source plan: "), 1),
            ("wrong-section", base.replace("## Handoff / Gate Notes", "## Other Notes"), 1),
            ("wrong-heading", base.replace("## Handoff / Gate Notes", "## Handoff / Gate Notes extra"), 1),
            ("checkbox-still-task", base + "- [ ] Pending note action\n", 1),
            ("malformed-known", base.replace("- Selected profile: base-plan", "* Selected profile: base-plan"), 1),
        ):
            for operation, expected in (("check_all_succeeded", whole), ("check_impl_steps_succeeded", 0)):
                with self.subTest(variant=variant, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if expected:
                        self.assertNotIn("SUCCESS", result.stdout)

    def test_comments_preserve_visible_tasks_and_real_boundaries(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        cases = {
            "comment-H1": prefix + "<!--\n# Old heading\n-->\n- [ ] Pending\n",
            "comment-H2": prefix + "<!--\n## Old heading\n-->\n- [ ] Pending\n",
            "inline-before-task": prefix + "<!-- old -->- [ ] Pending\n",
            "inline-after-task": prefix + "- [ ] Pending<!-- old -->\n",
            "multiline-outside": prefix + "<!-- old\nheading -->- [ ] Pending\n",
            "comment-only-checkbox": prefix + "<!--\n- [ ] Example only\n-->\n",
            "real-heading-after-comment": prefix + "<!-- old -->\n# Lifecycle\n- [ ] Pending\n",
            "fenced-comment-syntax": prefix + "```html\n<!--\n## Old heading\n```\n- [ ] Pending\n",
            "indented-comment-syntax": prefix + "An indented code example follows:\n    <!--\n    ## Old heading\n- [ ] Pending\n",
            "unclosed-comment": prefix + "<!--\n- [ ] Pending\n",
        }
        for name, content in cases.items():
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                expected = 0 if name == "comment-only-checkbox" or (name == "real-heading-after-comment" and operation == "check_impl_steps_succeeded") else 1
                with self.subTest(fixture=name, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if name == "unclosed-comment":
                        self.assertIn("Unclosed HTML comment", result.stderr)
                    if expected:
                        self.assertNotIn("SUCCESS", result.stdout)
        spec = importlib.util.spec_from_file_location("installed_tracker_comment_regression", self.entry)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory(prefix="tracker-comment-parser-") as fixture:
                plan = Path(fixture) / "plan"
                target = plan / "fixture/fixture.step.md"
                target.parent.mkdir(parents=True)
                for name in ("comment-H1", "comment-H2", "inline-before-task", "multiline-outside"):
                    target.write_text(cases[name], encoding="utf-8")
                    with self.subTest(public_parser=name):
                        self.assertEqual([step.text for step in module.parse_impl_steps("fixture", plan)], ["Done", "Pending"])
        finally:
            del sys.modules[spec.name]

    def test_raw_fence_info_is_not_promoted_by_comment_removal(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        invalid = prefix + "\x60\x60\x60lang<!--\x60-->rest\n- [ ] Still pending\n\x60\x60\x60\n"
        valid_prefix = prefix + "<!-- note -->\n\x60\x60\x60markdown\n- [ ] Example only\n\x60\x60\x60\n"
        invalid_prefix = prefix + "<!-- note -->\x60\x60\x60markdown\n- [ ] Still pending\n\x60\x60\x60\n"
        for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
            with self.subTest(operation=operation, fixture="raw-invalid"):
                result = self.run_cli(operation, invalid)
                self.assertEqual(result.returncode, 1)
                self.assertIn("[ ] Still pending", result.stdout)
                self.assertNotIn("SUCCESS", result.stdout)
            with self.subTest(operation=operation, fixture="comment-prefix-no-promotion"):
                result = self.run_cli(operation, invalid_prefix)
                self.assertEqual(result.returncode, 1)
                self.assertIn("[ ] Still pending", result.stdout)
            with self.subTest(operation=operation, fixture="valid-next-raw-line"):
                result = self.run_cli(operation, valid_prefix)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_quote_prefixed_checkboxes_fail_closed_but_quote_prose_does_not(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        for quote in ("> ", ">> ", "> > "):
            for marker in ("[ ]", "[X]", "[x]", "[?]", "[??]"):
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(quote=quote, marker=marker, operation=operation):
                        result = self.run_cli(operation, prefix + quote + "- " + marker + " Quoted task\n")
                        self.assertEqual(result.returncode, 1)
                        self.assertIn("Unsupported quoted", result.stderr)
                        self.assertNotIn("SUCCESS", result.stdout)
        controls = (
            "> Ordinary quoted prose\n> [documentation](https://example.invalid)\n",
            "\x60\x60\x60markdown\n> - [ ] Code example\n\x60\x60\x60\n",
            "<!--\n> - [ ] Comment example\n-->\n",
            "An indented code example follows:\n    > - [ ] Example only\n",
        )
        for content in controls:
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(control=content, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_nested_descriptions_are_prose_only_under_supported_parent(self):
        for indentation in ("  ", "    "):
            for marker, expected in (("[X]", 0), ("[ ]", 1), ("[x]", 1)):
                content = (
                    "## Implementation Steps\n- " + marker + " Update the bounded write set\n"
                    + indentation + "- src/example.py\n"
                    + indentation + "- tests/test_example.py\n"
                    + "- [X] Run the affected tests\n"
                )
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(indentation=indentation, marker=marker, operation=operation):
                        result = self.run_cli(operation, content)
                        self.assertEqual(result.returncode, expected, result.stderr)
                        self.assertNotIn("Malformed", result.stderr)
                        if marker == "[x]":
                            self.assertIn("lowercase [x]", result.stderr)
        orphan = "## Implementation Steps\n  - Unowned description\n- [X] Done\n"
        reset = "## Implementation Steps\n- [X] Done\nBoundary prose\n  - Unknown action\n"
        unknown_lifecycle = "## Implementation Steps\n- [X] Done\n## Lifecycle\n- Review pending\n"
        for name, content in (("orphan", orphan), ("reset", reset), ("unknown-lifecycle", unknown_lifecycle)):
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                expected = 0 if name == "unknown-lifecycle" and operation == "check_impl_steps_succeeded" else 1
                with self.subTest(fixture=name, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)


    def test_only_top_level_headings_control_implementation_scope(self):
        prefix = "## Implementation Steps\n- [X] Parent\n"
        fixtures = {
            "nested-H1": (prefix + "  # Details\n  - [ ] Pending child\n", 1, 1),
            "nested-H2": (prefix + "  ## Details\n  - [ ] Pending child\n", 1, 1),
            "nested-heading-ancestry": (prefix + "  ## Details\n  Description\n    - [ ] Pending child\n", 1, 1),
            "nested-only-opener": ("  ## Implementation Steps\n- [X] Done\n", 0, 1),
            "nested-opener-no-reset": (prefix + "  ## Implementation Steps\n- [ ] Still pending\n", 1, 1),
            "nested-metadata-no-section": (prefix + "  ## Handoff / Gate Notes\n- Selected profile: base-plan\n", 1, 1),
            "H3-stays-inside": (prefix + "### Details\n- [ ] Still pending\n", 1, 1),
            "actual-top-level-tail": (prefix + "## Lifecycle\n- [ ] Review pending\n", 1, 0),
            "actual-top-level-duplicate": (prefix + "## Implementation Steps\n- [X] Duplicate\n", 0, 1),
            "nested-opener-in-tail": (prefix + "# Lifecycle\n  ## Implementation Steps\n- [ ] Review pending\n", 1, 0),
        }
        for name, (content, whole, implementation) in fixtures.items():
            for operation, expected in (("check_all_succeeded", whole), ("check_impl_steps_succeeded", implementation)):
                with self.subTest(fixture=name, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if expected:
                        self.assertNotIn("SUCCESS", result.stdout)
        spec = importlib.util.spec_from_file_location("installed_tracker_heading_regression", self.entry)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory(prefix="tracker-heading-parser-") as fixture:
                plan = Path(fixture) / "plan"
                target = plan / "fixture/fixture.step.md"
                target.parent.mkdir(parents=True)
                for name, content, expected in (
                    ("nested-boundary", prefix + "  ## Details\n- [ ] Still pending\n", ["Parent", "Still pending"]),
                    ("nested-only", "  ## Implementation Steps\n- [X] Done\n", []),
                    ("actual-tail", fixtures["actual-top-level-tail"][0], ["Parent"]),
                ):
                    target.write_text(content, encoding="utf-8")
                    with self.subTest(public_parser=name):
                        self.assertEqual([step.text for step in module.parse_impl_steps("fixture", plan)], expected)
        finally:
            del sys.modules[spec.name]

    def test_explicit_quoted_fences_are_code_at_matching_container(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        for quote in ("> ", ">> ", "> > "):
            for token in ("`" * 3, "~" * 4):
                content = prefix + quote + token + "markdown\n" + quote + "- [ ] Example only\n" + quote + token + "  \n"
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(quote=quote, token=token, operation=operation):
                        result = self.run_cli(operation, content)
                        self.assertEqual(result.returncode, 0, result.stderr)
        content = prefix + "> <!-- old -->\n> " + "`" * 3 + "html<!--info-->\n> - [ ] Example only\n> " + "`" * 3 + "\n"
        for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
            result = self.run_cli(operation, content)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_quoted_fence_container_exit_preserves_pending_evidence(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        tick = "`" * 3
        cases = {
            "unquoted-exit": "> " + tick + "markdown\n> Example\n- [ ] Actual pending\n> " + tick + "\n",
            "lower-depth-exit": ">> " + tick + "markdown\n>> Example\n> - [ ] Actual pending\n>> " + tick + "\n",
            "wrong-type": "> " + tick + "markdown\n> ~~~\n> - [ ] Example only\n- [ ] Actual pending\n",
            "short-token": "> " + tick + "`markdown\n> " + tick + "\n> - [ ] Example only\n- [ ] Actual pending\n",
            "nonspace-suffix": "> " + tick + "markdown\n> " + tick + "not-a-close\n> - [ ] Example only\n- [ ] Actual pending\n",
            "higher-depth-not-close": "> " + tick + "markdown\n>> " + tick + "\n> - [ ] Example only\n- [ ] Actual pending\n",
            "raw-invalid-info": "> " + tick + "lang<!--`-->rest\n> - [ ] Actual pending\n> " + tick + "\n",
            "comment-prefix-not-opener": "> <!-- x -->" + tick + "lang\n> - [ ] Actual pending\n> " + tick + "\n",
            "multiple-fake-closures": ">> ````markdown\n>> Example\n> ````\n>> ~~~~\n>> ```\n>> ````not-a-close\n- [ ] Actual pending\n",
        }
        for name, content in cases.items():
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(fixture=name, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, 1, result.stderr)
                    self.assertNotIn("SUCCESS", result.stdout)


    def test_quoted_plain_and_ordered_lists_are_unsupported_tasks(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        for quote in ("> ", ">> ", "> > "):
            for action in ("- Review pending", "* Review pending", "+ Review pending", "1. Review pending", "2) Review pending", "- Source plan: plan/fixture/fixture.plan.md"):
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(quote=quote, action=action, operation=operation):
                        result = self.run_cli(operation, prefix + quote + action + "\n")
                        self.assertEqual(result.returncode, 1, result.stderr)
                        self.assertIn("Unsupported quoted", result.stderr)
                        self.assertNotIn("SUCCESS", result.stdout)
        tick = chr(96) * 3
        controls = (
            "> Ordinary quoted prose\n> [documentation](https://example.invalid)\n",
            "> " + tick + "markdown\n> - Review pending\n> 1. Review pending\n> " + tick + "\n",
            "<!--\n> - Review pending\n> 1. Review pending\n-->\n",
        )
        for content in controls:
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(control=content, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, 0, result.stderr)

    def test_inline_tick_comment_tokens_cannot_hide_real_pending(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        tick = chr(96)
        hidden = "The token " + tick + "<!--" + tick + " starts a comment\n- [ ] Pending\nThe token " + tick + "-->" + tick + " ends a comment\n"
        for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
            result = self.run_cli(operation, prefix + hidden)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("[ ] Pending", result.stdout)
            self.assertNotIn("SUCCESS", result.stdout)
        for width in (1, 2, 3):
            fence = tick * width
            complete = (
                "## Implementation Steps\n- [X] Describe " + fence + "<!--" + fence + " and " + fence + "-->" + fence + "\n"
                + "The tokens " + fence + "<!--" + fence + " and " + fence + "-->" + fence + " illustrate comments.\n"
            )
            for operation in self.operations:
                with self.subTest(width=width, operation=operation):
                    result = self.run_cli(operation, complete)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    if operation in ("read_all", "read_success"):
                        self.assertEqual(result.stdout, "[X] Describe " + fence + "<!--" + fence + " and " + fence + "-->" + fence + "\n")
        ambiguous = (
            "Unmatched " + tick + "<!--\n- [ ] Pending\n-->\n",
            "Unequal " + tick * 2 + "<!--" + tick + "\n- [ ] Pending\n-->\n",
            "Multiline " + tick + "<!--\n- [ ] Pending\n" + tick + "-->\n",
        )
        for content in ambiguous:
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(ambiguity=content, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("Ambiguous inline-code", result.stderr)
                    self.assertNotIn("SUCCESS", result.stdout)
        controls = (
            "<!-- Actual comment with " + tick + "ticks" + tick + "\n- [ ] Example only\n" + tick + "-->" + tick + "\n",
            "<!-- Actual comment -->- [ ] Pending after comment\n",
            "Literal unmatched " + tick + " without comment syntax\n- [ ] Pending\n",
            tick * 3 + "html\nUnmatched " + tick + "<!--\n- [ ] Example only\n" + tick * 3 + "\n",
            tick * 3 + "lang " + tick + "<!--" + tick + " rest\n- [ ] Pending after raw candidate\n",
        )
        for index, content in enumerate(controls):
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                expected = 0 if index in (0, 3) else 1
                with self.subTest(control=index, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if index == 4:
                        self.assertIn("[ ] Pending after raw candidate", result.stdout)

    def test_escaped_html_openers_use_contiguous_backslash_parity(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        slash = chr(92)
        for width in (1, 3, 5):
            content = prefix + "Literal " + slash * width + "<!-- token\n- [ ] Pending\nLiteral " + slash * width + "--> token\n"
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(odd=width, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, 1, result.stderr)
                    self.assertIn("[ ] Pending", result.stdout)
                    self.assertNotIn("SUCCESS", result.stdout)
        for width in (0, 2, 4):
            content = prefix + "Real " + slash * width + "<!-- comment\n- [ ] Example only\n-->\n"
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(even=width, operation=operation):
                    result = self.run_cli(operation, content)
                    self.assertEqual(result.returncode, 0, result.stderr)
        tick = chr(96)
        controls = (
            ("Literal " + slash + "<!-- then <!-- real\n- [ ] Example only\n-->\n", 0),
            ("<!-- actual\n- [ ] Example only\n" + slash + "-->\n- [ ] Pending after close\n", 1),
            ("<!-- actual\n- [ ] Example only\n" + tick + slash + "-->" + tick + "\n- [ ] Pending after close\n", 1),
            ("Inline " + tick + slash + "<!--" + tick + " token\n- [ ] Pending\n", 1),
            (tick * 3 + "html\n" + slash + "<!--\n- [ ] Example only\n" + tick * 3 + "\n", 0),
        )
        for content, expected in controls:
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(control=content, operation=operation):
                    result = self.run_cli(operation, prefix + content)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if expected:
                        self.assertIn("[ ] Pending", result.stdout)
                        self.assertNotIn("SUCCESS", result.stdout)

    def test_list_code_requires_blank_boundary_and_content_indent(self):
        prefix = "## Implementation Steps\n- [X] Parent\n"
        cases = {
            "blank-six": ("\n      - [ ] Code example only\n", 0),
            "blank-eight": ("\n        - [ ] Code example only\n", 0),
            "blank-tabs": ("\n\t\t- [ ] Code example only\n", 0),
            "code-continuation": ("\n      - [ ] Code example only\n      - [ ] Another code example\n", 0),
            "no-blank-six": ("      - [ ] Unsupported child\n", 1),
            "no-blank-eight": ("        - [ ] Unsupported child\n", 1),
            "no-blank-tabs": ("\t\t- [ ] Unsupported child\n", 1),
            "blank-shallow-two": ("\n  - [ ] Unsupported child\n", 1),
            "blank-shallow-four": ("\n    - [ ] Unsupported child\n", 1),
            "code-exit-pending": ("\n      - [ ] Code example only\n\n- [ ] Visible pending\n", 1),
            "tab-code-exit-pending": ("\n\t\t- [ ] Code example only\n- [ ] Visible pending\n", 1),
            "code-exit-shallow-child": ("\n      - [ ] Code example only\n  - [ ] Unsupported child\n", 1),
            "code-comment-tokens": ("\n      <!--\n      - [ ] Code example only\n- [ ] Visible pending\n", 1),
        }
        for name, (body, expected) in cases.items():
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(fixture=name, operation=operation):
                    result = self.run_cli(operation, prefix + body)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if "Visible pending" in body:
                        self.assertIn("[ ] Visible pending", result.stdout)
                        self.assertNotIn("[ ] Code example only", result.stdout)

    def test_raw_html_attributes_do_not_open_comment_mode(self):
        prefix = "## Implementation Steps\n- [X] Done\n"
        tick = chr(96)
        for quote in (chr(34), chr(39)):
            for literal in ("<!--", "> <!--", tick + " <!-- >"):
                body = ("<span title=" + quote + literal + quote + ">\n"
                        "- [ ] Real pending\n<span title=" + quote + "-->" + quote + ">\n")
                for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                    with self.subTest(quote=quote, literal=literal, operation=operation):
                        result = self.run_cli(operation, prefix + body)
                        self.assertEqual(result.returncode, 1, result.stderr)
                        self.assertIn("[ ] Real pending", result.stdout)
        controls = (
            ("<span title=\"<!--\"\n- [ ] Real pending\n<span title=\"-->\">\n", 1),
            ("<span title=<!-->\n- [ ] Real pending\n<span title=\"-->\">\n", 1),
            ("<!-- real\n- [ ] Comment example only\n<span title=\"-->\">\n- [ ] Real pending\n", 1),
            (tick + '<span title="<!--">' + tick + "\n- [ ] Real pending\n", 1),
            (tick * 3 + "html\n<span title=\"<!--\">\n- [ ] Code example only\n<span title=\"-->\">\n" + tick * 3 + "\n", 0),
        )
        for index, (body, expected) in enumerate(controls):
            for operation in ("check_all_succeeded", "check_impl_steps_succeeded"):
                with self.subTest(control=index, operation=operation):
                    result = self.run_cli(operation, prefix + body)
                    self.assertEqual(result.returncode, expected, result.stderr)
                    if index in (2, 3):
                        self.assertIn("[ ] Real pending", result.stdout)
                        self.assertNotIn("[ ] Comment example only", result.stdout)

if __name__ == "__main__":
    unittest.main()
