---
name: plan-step-tracker
description: "Query topic step status or check completion; reject invalid completion evidence."
complexity: medium
risk_profile:
  - external_tooling
inputs:
  - topic name that maps to plan/<topic>/<topic>.step.md
  - "operation: read_all, read_not_run, read_success, check_all_succeeded, or check_impl_steps_succeeded"
outputs:
  - Python CLI stdout with matching step lines or success/blocked summary
  - exit code 0 or 1 that the caller can use as a workflow gate
  - stderr warning/error text for lowercase [x] or missing files
use_when:
  - you need a read-only status query for one topic's .step.md file
  - you need exit-code blocking before continuing a workflow or review step
  - you need fallback grep guidance when the Python CLI cannot run
do_not_use_when:
  - you need to modify step files or mark steps complete
  - you need to aggregate multiple topics or verify evidence outside the checkbox file
  - you need live monitoring or richer states than done versus pending
---

# Purpose

Provide a low-token, read-only way to query `plan/<topic>/<topic>.step.md` and enforce blocking when incomplete work remains.

# Trigger / When to use

Use this skill when:
- you need the status of one topic's `.step.md` file without reading the whole file
- you need a blocking gate that stops follow-on work when any step is still pending
- you need the canonical Python CLI contract for step queries
- you need grep fallback guidance because the Python CLI cannot run

Do not use this skill when:
- you need to edit `.step.md` files or change checkbox markers
- you need to query more than one topic in one pass
- you need to prove that external artifacts exist beyond what the checkbox file declares
- you need a watcher, daemon, or real-time progress monitor

# Inputs

- `<topic>`: one non-empty path component, excluding absolute paths, either
  separator and dot/dotdot. Resolves only within the intended repo-local plan
  root; external symlink targets are rejected before reading.
- `<operation>`: one of `read_all`, `read_not_run`, `read_success`, `check_all_succeeded`, or `check_impl_steps_succeeded`
- current working directory at repository root so the Python CLI and fallback paths resolve correctly

# Process

1. Resolve `plan/<topic>/<topic>.step.md` and keep the interaction read-only.
2. Prefer the Python CLI:
   ```bash
   python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>
   ```
3. Interpret checkbox markers exactly as the CLI does:
   - `[X]` = done
   - `[ ]` = pending
   - `[x]` = pending, with a warning on stderr
4. Preserve the command contract by honoring exit codes:
   - `read_all`, `read_not_run`, `read_success` return exit code `0` on successful reads
   - `check_all_succeeded` returns exit code `0` only when nothing is pending
   - `check_impl_steps_succeeded` returns exit code `0` only when `## Implementation Steps` contains no pending items
   - missing `.step.md` returns exit code `1` and is blocking
5. If Python CLI execution is unavailable, use the grep fallback from `reference.md`, and explicitly note that grep cannot reproduce the lowercase `[x]` warning by itself.
6. Never modify `.step.md`, normalize checkbox casing, or continue past a blocking `check_all_succeeded` result.

# Examples

**Positive: Use the blocking command before a gated handoff**
```bash
$ python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded my-feature
❌ BLOCKED: 2 steps pending (exit code 1)
[ ] implementation-review
[x] code-review
```
The caller stops and reports the pending steps.

**Negative: Treat lowercase `[x]` as complete or ignore exit code 1**
```bash
$ python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded my-feature
Warning: Found lowercase [x] at line 18; treating as pending
❌ BLOCKED: 1 steps pending (exit code 1)
[x] code-review
```
Wrong follow-up: continuing anyway or rewriting the file inside this skill.

# Outputs

- `read_all`: all parsed checkbox lines on stdout; exit code `0`
- `read_not_run`: pending lines on stdout, including lowercase `[x]`; exit code `0`
- `read_success`: completed `[X]` lines on stdout; exit code `0`
- `check_all_succeeded`: success summary with exit code `0`, or blocked summary plus pending lines with exit code `1`
- `check_impl_steps_succeeded`: implementation-only success summary with exit code `0`, or blocked summary plus pending implementation lines with exit code `1`
- errors: `Error: File not found: plan/<topic>/<topic>.step.md` on stderr with exit code `1`

# Validation

## Required Checks
 - run only one of the five supported operations
- keep the command path as `python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>`
- treat exit code `1` from `check_all_succeeded` or missing files as blocking
- treat exit code `1` from `check_impl_steps_succeeded` as an implementation-only blocking signal
- treat lowercase `[x]` as pending, not done
- keep the workflow read-only

## Quality Checks (best effort)
- prefer the Python CLI over grep so warning and exit-code semantics stay exact
- if fallback grep is used, disclose the lowercase `[x]` limitation explicitly
- keep output concise by returning only the requested subset of steps

## On Soft Fail
- mark the result `INCOMPLETE` when the caller's desired operation is unclear
- state any fallback limitations explicitly
- do not fabricate completion state beyond the file contents

# Failure Handling

## Missing Context
- if `<topic>` is missing or does not resolve to a single expected path, mark the result `BLOCKED` and request the exact topic name
- if the caller does not specify an operation and intent does not clearly imply one, mark the result `INCOMPLETE`

## Ambiguous Requirement
- if the caller asks a broad question like "check the plan" without saying whether they need pending steps, completed steps, all steps, or a blocking gate, do not guess when that choice could change downstream behavior
- if a fallback command is used, say that warning behavior for lowercase `[x]` must be checked manually

## Execution Limitation
- if Python CLI execution is unavailable, fall back to grep guidance from `reference.md`
- if neither Python nor grep can be run safely, stop at `BLOCKED` rather than inferring status from memory

# Verification

- verify exit code `0` from `check_all_succeeded` before continuing a gated workflow
- verify exit code `1` blocks continuation when any pending step or missing file is reported
- verify `check_impl_steps_succeeded` inspects only `## Implementation Steps` and ignores pending items outside that section
- verify lowercase `[x]` remains pending and produces a warning when the Python CLI is used
- verify fallback grep guidance is presented as an approximation, not as a replacement for the CLI warning behavior

# Boundaries

- read-only only; this skill does not update step files
- single-topic only; no aggregation across multiple plan folders
- checkbox-state only; no evidence validation for artifacts outside the `.step.md` file
- no extra status model beyond done versus pending
- no behavior changes to the local Python CLI contract

# Local references

- `reference.md`: stable CLI contract, path rules, exit-code semantics, and grep fallback limitations
- `examples.md`: detailed command examples, blocking cases, edge cases, and fallback usage patterns
- `scripts/step_tracker.py`: local Python CLI that implements the preserved command and exit-code contract
- `tests/`: pytest coverage for parsing, filtering, blocking, missing-file handling, and lowercase `[x]` behavior

## Installed runtime safety

All five operations use one bounded topic/path resolver. Invalid topics,
symlink escapes, unreadable files or invalid UTF-8 return exit 1 with stderr
and no traceback/outside content. Completion checks close fences only on a
matching marker with whitespace-only suffix. Unsupported nested checklist rows,
including four-space children, fail closed; real fenced/indented code examples
remain excluded. Implementation scope ends at a non-fenced H1 or H2, while H3+
subheadings remain inside. These are installed PR-review fixes; source unchanged.

## Round2 visible completion evidence

Only valid backtick fence openers (no backtick in the info suffix) and valid
tilde fences enter code mode. Matching whitespace-only closing rules remain.
Outside genuine fenced/indented code, HTML comment spans are removed before
headings or checkbox evidence are interpreted; text outside closed spans stays
visible. Unclosed comments return a blocking error. The public implementation
parser and both completion gates share these boundaries; read queries remain
permissive. This is bounded evidence handling, not a full Markdown parser.

The whole-file completion gate rejects unknown/plain task-like list rows too.
Only under exact `## Handoff / Gate Notes`, exact top-level `- Label: value`
rows with nonempty values for these existing nine labels are metadata:
Selected profile, Source plan, Shared lifecycle shell, Managed worktree intent,
Progression truth inputs, Completion evidence inputs, Marker semantics,
Tracker semantics, Owner-only updates. Other labels, empty values, checkbox
rows or the same labels under other sections are not exempt. The section itself
is never exempt; implementation-only scope stays Implementation Steps.

## Round3 evidence boundaries

Fence opening validity uses raw backtick info: removing HTML comments cannot
promote a raw invalid opener or a marker embedded after a same-line comment
prefix. A legitimate raw opener on a following line remains eligible. Visible quote-prefixed task checkboxes are unsupported
and block both completion gates, including nested quote prefixes and completed
or unknown markers; ordinary quoted prose/links and genuine code/comments are
not task evidence. Non-checkbox indented descriptions under a supported
top-level checkbox are prose; a pending/lowercase parent still blocks.
Nested checkboxes remain unsupported across descriptive children. Genuine
top-level boundaries reset ancestry; orphan/unknown plain actions and the exact
nine-metadata rule retain fail-closed semantics.

## Round4 supported heading and quoted-code scope

Only column-zero `## Implementation Steps` opens implementation scope; only
column-zero H1/H2 ends it or changes the Handoff / Gate Notes metadata section.
Nested headings stay within their parent and cannot cut/reopen scope; genuine
code/comments remain excluded and nested tasks still block. Explicit raw
blockquote prefixes support quoted fences at their recorded depth. Raw info
validity is checked before comment masking; closure requires matching depth,
marker type, sufficient length and whitespace-only suffix. Leaving a quote
container or moving to lower depth ends that fence and reprocesses the visible
line. Naked quoted tasks still block; quoted prose and genuine quoted code pass.
This adds no full Markdown parser or dependency.

## Round5 quoted actions and inline comment-token evidence

Visible quote-prefixed plain/ordered lists are unsupported task evidence just
like quoted checkboxes, with no quoted-metadata exception. Quoted prose/links
and genuinely quoted code remain non-task controls. Outside real code/comments,
raw same-line balanced equal-length tick spans protect inline comment tokens
without changing line or step text. Unmatched/ambiguous/multiline comment-token
syntax fails closed rather than hiding later pending steps; real HTML-comment
mode consumes raw closing markers even inside ticks. Raw fence validity and
quote-container boundaries remain prior to masking. No full Markdown parser.

## Escaped HTML opener boundary

Outside genuine raw comment/code, contiguous backslash parity before the raw
opener controls recognition: odd literal, even eligible. Continue looking for
a later genuine same-line opener. Balanced inline spans and genuine fences
remain code. In active real HTML comment mode, raw closing markers retain
precedence regardless of backslashes/ticks. No full Markdown parser is added.

## Narrow list-code and raw-tag boundaries

Under a supported top-level checkbox parent, indented code requires an actual
blank/block boundary (or continuation of that code) and at least four columns
beyond list content indentation. Content indentation is the marker width plus
following whitespace, not checkbox text width; tabs use four-column stops.
Shallow nested tasks and deep no-blank task ambiguity remain unsupported and
block. Code exit reprocesses visible pending evidence; descriptions retain
parent ancestry. This is a narrow evidence lexer, not full Markdown support.
Raw valid same-line HTML tags protect quoted attribute tokens, including literal
comment markers, greater-than characters and ticks, without masking following
task lines or changing original text. Invalid/unclosed comment-token tag syntax
blocks. A genuine active comment's raw close takes precedence; earlier-starting
balanced inline code, raw fences and escaped opener parity retain their rules.

## Bounded link, list-container and CDATA evidence

Valid same-line inline link destinations/titles protect literal comment tokens;
ambiguous comment-token link syntax fails closed without multiline inline
masking. Genuine raw active comments retain raw-close precedence. List fences
use supported parent content indentation plus zero-to-three columns, including
no-blank openings, matching marker/length and whitespace-only closure; dedent
or quote-container exit reprocesses visible pending evidence. Ordinary indented
list code still needs its established blank boundary. Descriptive child prose
requires at least the supported parent's content indent; one-space unordered/
ordered action rows block. Nine exact Base metadata keys stay unchanged.
Genuine bounded CDATA ends only at its raw closing delimiter; literal comment
tokens inside cannot open global comments. Pending after closure stays visible,
unclosed/ambiguous evidence blocks, and an already-active real HTML comment's
raw closing marker takes precedence. This remains a narrow stdlib evidence
lexer, not full Markdown conformance.

## Bounded literal HTML blocks

Completion visibility recognizes raw type-1 script/pre/style/textarea line starts,
case-insensitive tag-name boundaries and zero-to-three relative spaces in the
supported quote/list container. Literal data, including comment tokens, stays
inside that block through its closing line; any of the four exact closing tags
ends it. Container exit reprocesses real visible evidence. Active genuine comments
and code retain precedence; inline/escaped or comment-stripped text never opens
a new block. Unclosed supported literal blocks fail closed. This narrow lexer
is not full HTML or Markdown conformance.
See [CommonMark HTML blocks](https://spec.commonmark.org/0.31.2/#html-blocks).
