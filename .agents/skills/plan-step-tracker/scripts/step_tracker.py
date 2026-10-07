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
    """Only column-zero H1/H2 end implementation scope; H3+ stay inside."""
    return re.match(r"^#{1,2}(?:\s|$)", line) is not None


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

    for line in _visible_completion_lines(lines):
        if line == "## Implementation Steps":
            in_impl_section = True
            continue

        if in_impl_section and _ends_implementation_section(line):
            break

        if in_impl_section:
            impl_lines.append(line)

    return _parse_step_lines(impl_lines)


def _raw_quote_content(line: str) -> tuple[int, str]:
    """Separate an explicit raw blockquote prefix; no lazy Markdown parsing."""
    depth = 0
    content = line
    while True:
        prefix = re.match(r"^ {0,3}>[ \t]?", content)
        if prefix is None:
            return depth, content
        depth += 1
        content = content[prefix.end():]


def _inline_tick_end(line: str, start: int) -> int:
    """Protect one raw same-line balanced equal-length span, never multiline."""
    tick = chr(96)
    end = start
    while end < len(line) and line[end] == tick:
        end += 1
    width = end - start
    for run in re.finditer(re.escape(tick) + "+", line[end:]):
        if len(run.group()) == width:
            return end + run.end()
    if "<!--" in line[end:] or "-->" in line[end:]:
        raise ValueError("Ambiguous inline-code comment tokens in completion evidence")
    return end  # No comment tokens: preserve unmatched literal ticks.


def _visible_completion_lines(lines: list[str]) -> list[str]:
    """Exclude genuine code/comments while preserving unsupported task evidence."""
    visible: list[str] = []
    fence: tuple[str, int, int] | None = None
    list_context = False
    in_comment = False

    for raw_line in lines:
        quote_depth, raw_content = _raw_quote_content(raw_line.rstrip("\r\n"))
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", raw_content)
        if fence is not None:
            if quote_depth < fence[2]:
                fence = None  # Container ended; re-process this visible boundary line.
            else:
                if quote_depth == fence[2] and marker:
                    token, suffix = marker.groups()
                    if token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                        fence = None
                continue
        if not in_comment and raw_line.startswith(("    ", "\t")):
            nested_checkbox = re.match(r"^(?:(?:[-*+]|\d+[.)])\s+)?\[[^\]]*\]", raw_line.strip())
            if not (list_context and nested_checkbox):
                continue  # Real indented code; its comment tokens have no effect.
        if not in_comment and marker:
            token, suffix = marker.groups()
            if token[0] != "`" or "`" not in suffix:
                fence = (token[0], len(token), quote_depth)
                continue  # Comment tokens in a valid fence's info are code too.
        invalid_raw_fence = bool(marker and marker.group(1).startswith(chr(96))
                                 and chr(96) in marker.group(2))
        # Only an invalid raw opener's initial tick run is literal. Later
        # balanced same-line spans still protect their inline comment tokens.
        # Genuine comment mode consumes raw closing markers even inside ticks.
        # Outside it, protect only balanced same-line equal-length code spans.
        fragments: list[str] = []
        position = 0
        while position < len(raw_line):
            if in_comment:
                closing = raw_line.find("-->", position)
                if closing < 0:
                    break
                position = closing + 3
                in_comment = False
            else:
                opening = raw_line.find("<!--", position)
                tick = raw_line.find(chr(96), position)
                if tick >= 0 and (opening < 0 or tick < opening):
                    fragments.append(raw_line[position:tick])
                    if invalid_raw_fence and tick == raw_line.find(chr(96)):
                        end = tick + len(marker.group(1))
                    else:
                        end = _inline_tick_end(raw_line, tick)
                    fragments.append(raw_line[tick:end])
                    position = end
                elif opening >= 0:
                    fragments.append(raw_line[position:opening])
                    position = opening + 4
                    in_comment = True
                else:
                    fragments.append(raw_line[position:])
                    break
        line = "".join(fragments)
        visible.append(line)
        if line.strip() and not line[0].isspace():
            # Indented descriptions/sub-lists retain their enclosing list.
            list_context = re.fullmatch(r"- \[[ Xx]\] \S.*", line.rstrip()) is not None
    if in_comment:
        raise ValueError("Unclosed HTML comment in completion evidence")
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
        lines = _visible_completion_lines(_read_step_lines(topic, plan_dir))
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


_HANDOFF_METADATA_KEYS = frozenset({
    "Selected profile", "Source plan", "Shared lifecycle shell",
    "Managed worktree intent", "Progression truth inputs",
    "Completion evidence inputs", "Marker semantics", "Tracker semantics",
    "Owner-only updates",
})


def _validate_completion_lines(lines: list[str], *, implementation: bool = False) -> None:
    """Reject unsupported tasks; only the frozen Base metadata is non-task data."""
    in_handoff_notes = False
    checkbox_parent = False
    for line in lines:
        stripped = line.strip()
        if _ends_implementation_section(line):
            in_handoff_notes = stripped == "## Handoff / Gate Notes"
        list_checkbox_like = re.match(
            r"^(?:[-*+]|\d+[.)])\s+\[[^\]]*\](?![(:])", stripped
        )
        bare_checkbox_like = re.match(
            r"^\[(?:\s|[^\]\s]|\?+)?\](?![(:])", stripped
        )
        quote = re.match(r"^(?:>\s*)+(.*)$", stripped)
        if quote and (
                re.match(r"^(?:(?:[-*+]|\d+[.)])\s+)?\[[^\]]*\](?![(:])", quote.group(1))
                or re.match(r"^(?:[-*+]|\d+[.)])\s+", quote.group(1))):
            raise ValueError(f"Unsupported quoted completion step: {line}")
        list_item = re.match(r"^(?:[-*+]|\d+[.)])\s+", stripped)
        if line and not line[0].isspace() and stripped:
            checkbox_parent = re.fullmatch(r"- \[[ Xx]\] \S.*", line.rstrip()) is not None
        if line[:1].isspace() and checkbox_parent and not (list_checkbox_like or bare_checkbox_like):
            continue  # Descriptive children are prose; nested checkboxes still fail.
        metadata = re.fullmatch(r"- ([^:]+): (\S.*)", line.rstrip())
        if (not implementation and in_handoff_notes and not list_checkbox_like
                and metadata and metadata.group(1) in _HANDOFF_METADATA_KEYS):
            continue
        if list_checkbox_like or bare_checkbox_like or list_item:
            if not re.fullmatch(r"- \[[ Xx]\] \S.*", line.rstrip()):
                raise ValueError(f"Malformed or unsupported completion step: {line}")


def check_impl_steps_succeeded(topic: str, plan_dir: Path = Path("plan")) -> int:
    """Check if all implementation steps are complete. Exit 0 if yes, 1 if any pending."""
    try:
        lines = _visible_completion_lines(_read_step_lines(topic, plan_dir))
        headings = [i for i, line in enumerate(lines) if line == "## Implementation Steps"]
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
