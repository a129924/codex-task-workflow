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


def _unescaped_comment_opening(line: str, start: int) -> int:
    """Odd contiguous backslashes escape an opener outside raw code/comments."""
    opening = line.find("<!--", start)
    while opening >= 0:
        previous = opening - 1
        while previous >= 0 and line[previous] == chr(92):
            previous -= 1
        if (opening - previous - 1) % 2 == 0:
            return opening
        opening = line.find("<!--", opening + 4)
    return -1


def _raw_html_tag_end(line: str, start: int) -> int:
    """Recognize one valid same-line tag; quoted attributes are literal tokens."""
    quote: str | None = None
    end = start + 1
    while end < len(line):
        char = line[end]
        if quote is not None:
            if char == quote:
                quote = None
        elif char in (chr(34), chr(39)):
            quote = char
        elif char == ">":
            break
        end += 1
    candidate = line[start:end + 1]
    # This narrow tag grammar carries no HTML context onto the next task line.
    name = r"[A-Za-z][A-Za-z0-9-]*"
    attribute = r"[A-Za-z_:][A-Za-z0-9_.:-]*"
    value = r'''(?:"[^"\r\n]*"|'[^'\r\n]*'|[^\s\x22\x27=<>\x60]+)'''
    tag = (r"<(?:/" + name + r"[ \t]*|" + name
           + r"(?:[ \t]+" + attribute + r"(?:[ \t]*=[ \t]*" + value + r")?)*[ \t]*/?)>")
    if end < len(line) and re.fullmatch(tag, candidate):
        return end + 1
    if "<!--" in candidate or "-->" in candidate:
        raise ValueError("Ambiguous HTML tag comment tokens in completion evidence")
    return start + 1


def _raw_link_end(line: str, start: int) -> int:
    """Protect bounded same-line inline link destinations/titles, not blocks."""
    label = r"\[(?:\\.|[^\]\\\r\n])*\]"
    # At most one balanced inner destination pair; deeper/ambiguous token
    # syntax fails closed when it contains comment delimiters.
    destination = r"(?:<[^<>\r\n]*>|(?:\\.|[^\s()\\]|\((?:\\.|[^()\\\r\n])*\))*)"
    title = r'''(?:"(?:\\.|[^"\\\r\n])*"|'(?:\\.|[^'\\\r\n])*'|\((?:\\.|[^()\\\r\n])*\))'''
    pattern = label + r"\([ \t]*" + destination + r"(?:[ \t]+" + title + r")?[ \t]*\)"
    match = re.match(pattern, line[start:])
    if match:
        return start + match.end()
    if "<!--" in line[start:] or "-->" in line[start:]:
        raise ValueError("Ambiguous Markdown link comment tokens in completion evidence")
    return start + 1


def _visible_completion_lines(lines: list[str]) -> list[str]:
    """Exclude genuine code/comments while preserving unsupported task evidence."""
    visible: list[str] = []
    fence: tuple[str, int, int, int] | None = None
    list_content_indent: int | None = None
    blank_boundary = False
    list_code = False
    in_comment = False
    in_cdata = False
    literal_html: tuple[int, int] | None = None  # quote depth, list content indent
    literal_close = re.compile(r"</(?:script|pre|style|textarea)>", re.IGNORECASE)

    for raw_line in lines:
        quote_depth, raw_content = _raw_quote_content(raw_line.rstrip("\r\n"))
        expanded_content = raw_content.expandtabs(4)
        content_indent = len(expanded_content) - len(expanded_content.lstrip(" "))
        container_indent = (fence[3] if fence is not None else
                            list_content_indent if quote_depth == 0 and list_content_indent is not None
                            and content_indent >= list_content_indent else 0)
        relative_content = expanded_content[container_indent:]
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", relative_content)
        if fence is not None:
            if quote_depth < fence[2] or (container_indent and raw_content.strip()
                                         and content_indent < container_indent):
                fence = None  # Container ended; re-process this visible boundary line.
            else:
                if quote_depth == fence[2] and marker:
                    token, suffix = marker.groups()
                    if token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                        fence = None
                continue
        if literal_html is not None:
            depth, required_indent = literal_html
            if quote_depth < depth or (required_indent and raw_content.strip()
                                      and content_indent < required_indent):
                literal_html = None  # Container ended; process this visible line.
            else:
                if literal_close.search(raw_content):
                    literal_html = None
                continue  # Type-1 literal data includes the whole closing line.
        expanded = raw_line.expandtabs(4)
        indent = len(expanded) - len(expanded.lstrip(" "))
        if not in_comment and not in_cdata and not raw_line.strip():
            blank_boundary = True
        elif not in_comment and not in_cdata:
            if list_content_indent is not None:
                if indent >= list_content_indent + 4 and (blank_boundary or list_code):
                    list_code = True
                    continue  # Established indented code inside this supported list.
                list_code = False  # Exit must re-process visible task evidence.
            elif indent >= 4:
                continue  # Ordinary indented code outside a checklist container.
            blank_boundary = False
        if not in_comment and not in_cdata and marker:
            token, suffix = marker.groups()
            if token[0] != "`" or "`" not in suffix:
                fence = (token[0], len(token), quote_depth, container_indent)
                continue  # Comment tokens in a valid fence's info are code too.
        # Recognize only a genuine raw type-1 line start, never an opener
        # promoted from inline text, escaped markup or stripped comments.
        if not in_comment and not in_cdata and re.match(
                r"^ {0,3}<(?:script|pre|style|textarea)(?=[ \t>]|$)",
                relative_content, re.IGNORECASE):
            if not literal_close.search(raw_content):
                literal_html = (quote_depth, container_indent)
            if not container_indent:
                list_content_indent = None  # This top-level block ends ancestry.
                list_code = False
            blank_boundary = False
            continue
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
            elif in_cdata:
                closing = raw_line.find("]]>", position)
                if closing < 0:
                    break
                position = closing + 3
                in_cdata = False
            else:
                opening = _unescaped_comment_opening(raw_line, position)
                tick = raw_line.find(chr(96), position)
                tag_match = re.search(r"</?[A-Za-z]", raw_line[position:])
                tag_start = position + tag_match.start() if tag_match else -1
                link_match = re.search(r"\[(?:\\.|[^\]\r\n])*\]\(", raw_line[position:])
                link_start = position + link_match.start() if link_match else -1
                cdata_start = raw_line.find("<![CDATA[", position)
                first = min((x for x in (opening, tick, tag_start, link_start, cdata_start) if x >= 0), default=-1)
                if first >= 0 and first == link_start:
                    end = _raw_link_end(raw_line, link_start)
                    fragments.append(raw_line[position:end])
                    position = end
                elif first >= 0 and first == cdata_start:
                    fragments.append(raw_line[position:cdata_start])
                    position = cdata_start + len("<![CDATA[")
                    in_cdata = True
                elif first >= 0 and first == tag_start:
                    end = _raw_html_tag_end(raw_line, tag_start)
                    fragments.append(raw_line[position:end])
                    position = end
                elif tick >= 0 and first == tick:
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
            parent = re.fullmatch(r"(-)( )\[[ Xx]\] \S.*", line.rstrip())
            # Content starts after the marker and its following whitespace,
            # not after the checkbox text. Blank lines retain this ancestry.
            list_content_indent = len(parent.group(1) + parent.group(2)) if parent else None
            list_code = False
    if in_comment:
        raise ValueError("Unclosed HTML comment in completion evidence")
    if in_cdata:
        raise ValueError("Unclosed CDATA in completion evidence")
    if literal_html is not None:
        raise ValueError("Unclosed literal HTML block in completion evidence")
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
    parent_content_indent: int | None = None
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
            parent = re.fullmatch(r"(-)( )\[[ Xx]\] \S.*", line.rstrip())
            parent_content_indent = len(parent.group(1) + parent.group(2)) if parent else None
        expanded = line.expandtabs(4)
        indent = len(expanded) - len(expanded.lstrip(" "))
        if (parent_content_indent is not None and indent >= parent_content_indent
                and not (list_checkbox_like or bare_checkbox_like)):
            continue  # Genuine descriptive children only; underindented actions fail.
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
