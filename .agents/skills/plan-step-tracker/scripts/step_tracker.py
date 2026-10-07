# /// script
# requires-python = ">=3.11"
# ///
"""Step status tracker for plan/<topic>/<topic>.step.md files.

Usage:
  python3 step_tracker.py read_all <topic>
  python3 step_tracker.py read_not_run <topic>
  python3 step_tracker.py read_success <topic>
  python3 step_tracker.py check_all_succeeded <topic>
  python3 step_tracker.py check_impl_steps_succeeded <topic>
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Literal
import argparse


@dataclass
class Step:
    """Represents a single step in the tracking file."""

    text: str
    status: Literal["done", "pending"]
    bracket: str  # Original bracket marker: [X], [x], or [ ]


def _step_path(topic: str, plan_dir: Path) -> Path:
    """Resolve one topic inside the intended plan root, before reading it."""
    if not topic or topic in {".", ".."} or Path(topic).is_absolute() or "/" in topic or "\\" in topic:
        raise ValueError("Topic must be a single non-empty path component, not a path")
    declared_root = Path(plan_dir).absolute()
    intended_root = declared_root.parent.resolve() / declared_root.name
    plan_root = declared_root.resolve()
    if plan_root != intended_root:
        raise ValueError("Plan directory resolves outside its intended location")
    step_file = Path(plan_dir) / topic / f"{topic}.step.md"
    resolved_file = step_file.resolve()
    if not resolved_file.is_relative_to(plan_root):
        raise ValueError("Step file resolves outside the plan directory")
    if not resolved_file.exists():
        raise FileNotFoundError(f"File not found: {step_file}")
    return resolved_file


def _read_step_lines(topic: str, plan_dir: Path) -> list[str]:
    """Use the same bounded path and UTF-8 read for every operation."""
    return _step_path(topic, plan_dir).read_text(encoding="utf-8").splitlines()


def _ends_implementation_section(line: str) -> bool:
    """H1/H2 headings end an implementation section; H3+ stay inside it."""
    return re.match(r"^#{1,2}(?:\s|$)", line.strip()) is not None


def parse_steps(topic: str, plan_dir: Path = Path("plan")) -> list[Step]:
    """Parse steps from plan/<topic>/<topic>.step.md.

    Args:
        topic: Topic name (e.g., 'my-feature')
        plan_dir: Base plan directory (default: 'plan')

    Returns:
        List of Step objects

    Raises:
        FileNotFoundError: If .step.md file does not exist
    """
    return _parse_step_lines(_read_step_lines(topic, plan_dir))


def parse_impl_steps(topic: str, plan_dir: Path = Path("plan")) -> list[Step]:
    """Parse only steps in the '## Implementation Steps' section."""
    lines = _read_step_lines(topic, plan_dir)

    impl_lines: list[str] = []
    in_impl_section = False

    for line in _without_fenced_code(lines):
        stripped = line.strip()
        if stripped == "## Implementation Steps":
            in_impl_section = True
            continue

        if in_impl_section and _ends_implementation_section(line):
            break

        if in_impl_section:
            impl_lines.append(line)

    return _parse_step_lines(impl_lines)


def _without_fenced_code(lines: list[str]) -> list[str]:
    """Exclude code examples while keeping unsupported nested task evidence."""
    visible: list[str] = []
    fence: tuple[str, int] | None = None
    list_context = False

    for line in lines:
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence is not None:
            if marker:
                token, suffix = marker.groups()
                if token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                    fence = None
            continue
        if line.startswith(("    ", "\t")):
            nested_checkbox = re.match(r"^(?:(?:[-*+]|\d+[.)])\s+)?\[[^\]]*\]", line.strip())
            if list_context and nested_checkbox:
                visible.append(line)  # Existing validator rejects unsupported nesting.
            continue
        if marker:
            token = marker.group(1)
            fence = (token[0], len(token))
            continue
        visible.append(line)
        if line.strip() and not line[0].isspace():
            # Indented descriptions/sub-lists retain their enclosing list.
            # Only a real top-level non-list boundary clears that ancestry.
            list_context = re.match(r"^(?:[-*+]|\d+[.)])\s+", line) is not None

    return visible

def _parse_step_lines(lines: list[str]) -> list[Step]:
    """Parse checkbox step lines into Step objects."""
    steps: list[Step] = []
    pattern = re.compile(r"^\- \[(.)\](.*)")

    for line_num, line in enumerate(lines, start=1):
        match = pattern.match(line.rstrip())
        if match:
            bracket_char = match.group(1)
            step_text = match.group(2).strip()
            bracket = f"[{bracket_char}]"

            if bracket_char == "X":
                status = "done"
            elif bracket_char == " ":
                status = "pending"
            elif bracket_char == "x":
                status = "pending"
                print(
                    f"Warning: Found lowercase [x] at line {line_num}; treating as pending",
                    file=sys.stderr,
                )
            else:
                status = "pending"
                print(
                    f"Warning: Found unexpected bracket content [{bracket_char}] at line {line_num}; treating as pending",
                    file=sys.stderr,
                )

            steps.append(Step(text=step_text, status=status, bracket=bracket))

    return steps


def format_step(step: Step) -> str:
    """Format a step for display using original bracket."""
    return f"{step.bracket} {step.text}"


def read_all(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display all steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except (OSError, UnicodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    for step in steps:
        print(format_step(step))

    return 0


def read_not_run(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display only pending steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except (OSError, UnicodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    for step in pending_steps:
        print(format_step(step))

    return 0


def read_success(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Read and display only completed steps."""
    try:
        steps = parse_steps(topic, plan_dir)
    except (OSError, UnicodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    done_steps = [s for s in steps if s.status == "done"]

    for step in done_steps:
        print(format_step(step))

    return 0


def check_all_succeeded(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Check if all steps are complete. Exit 0 if yes, 1 if any pending."""
    try:
        lines = _without_fenced_code(_read_step_lines(topic, plan_dir))
        _validate_completion_lines(lines)
        steps = _parse_step_lines(lines)
    except (OSError, UnicodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    if not steps:
        print("❌ BLOCKED: No valid steps found", file=sys.stderr)
        return 1

    if not pending_steps:
        total = len(steps)
        print(f"✅ SUCCESS: All {total} steps complete")
        return 0

    print(f"❌ BLOCKED: {len(pending_steps)} steps pending (exit code 1)")
    for step in pending_steps:
        print(format_step(step))

    return 1


def _validate_completion_lines(lines: list[str], *, implementation: bool = False) -> None:
    """Reject malformed checkbox evidence without changing read-only queries."""
    for line in lines:
        stripped = line.strip()
        list_checkbox_like = re.match(
            r"^(?:[-*+]|\d+[.)])\s+\[[^\]]*\](?![(:])", stripped
        )
        bare_checkbox_like = re.match(
            r"^\[(?:\s|[^\]\s]|\?+)?\](?![(:])", stripped
        )
        top_level_list_item = implementation and re.match(
            r"^(?:[-*+]\s|\d+[.)]\s)", line
        )
        if list_checkbox_like or bare_checkbox_like or top_level_list_item:
            if not re.fullmatch(r"- \[[ Xx]\] \S.*", line.rstrip()):
                raise ValueError(f"Malformed or unsupported completion step: {line}")


def check_impl_steps_succeeded(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Check if all implementation steps are complete. Exit 0 if yes, 1 if any pending."""
    try:
        lines = _without_fenced_code(_read_step_lines(topic, plan_dir))
        headings = [i for i, line in enumerate(lines) if line.strip() == "## Implementation Steps"]
        if len(headings) != 1:
            raise ValueError("Expected exactly one Implementation Steps section")
        section = []
        for line in lines[headings[0] + 1:]:
            if _ends_implementation_section(line):
                break
            section.append(line)
        _validate_completion_lines(section, implementation=True)
        steps = _parse_step_lines(section)
        if not steps or any(not step.text for step in steps):
            raise ValueError("Implementation Steps must contain non-empty checkbox steps")
    except (OSError, UnicodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    pending_steps = [s for s in steps if s.status == "pending"]

    if not pending_steps:
        total = len(steps)
        print(f"✅ SUCCESS: All {total} implementation steps complete")
        return 0

    print(f"❌ BLOCKED: {len(pending_steps)} implementation steps pending (exit code 1)")
    for step in pending_steps:
        print(format_step(step))

    return 1


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Query step status in plan/<topic>/<topic>.step.md files"
    )
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # read_all
    read_all_parser = subparsers.add_parser(
        "read_all", help="Read all steps (pending and done)"
    )
    read_all_parser.add_argument("topic", help="Topic name")

    # read_not_run
    read_not_run_parser = subparsers.add_parser(
        "read_not_run", help="Read only pending steps"
    )
    read_not_run_parser.add_argument("topic", help="Topic name")

    # read_success
    read_success_parser = subparsers.add_parser(
        "read_success", help="Read only completed steps"
    )
    read_success_parser.add_argument("topic", help="Topic name")

    # check_all_succeeded
    check_all_parser = subparsers.add_parser(
        "check_all_succeeded",
        help="Check if all steps complete; exit 0 if yes, 1 if any pending",
    )
    check_all_parser.add_argument("topic", help="Topic name")

    # check_impl_steps_succeeded
    check_impl_steps_parser = subparsers.add_parser(
        "check_impl_steps_succeeded",
        help="Check if implementation steps complete; exit 0 if yes, 1 if any pending",
    )
    check_impl_steps_parser.add_argument("topic", help="Topic name")

    args = parser.parse_args()

    topic = args.topic
    plan_dir = Path("plan")

    if args.operation == "read_all":
        return read_all(topic, plan_dir)
    elif args.operation == "read_not_run":
        return read_not_run(topic, plan_dir)
    elif args.operation == "read_success":
        return read_success(topic, plan_dir)
    elif args.operation == "check_all_succeeded":
        return check_all_succeeded(topic, plan_dir)
    elif args.operation == "check_impl_steps_succeeded":
        return check_impl_steps_succeeded(topic, plan_dir)

    return 1


if __name__ == "__main__":
    sys.exit(main())
