# Shared step-creator reference

## Generation and eligibility

Only explicit base-plan is supported. Read both shared contracts and the
source plan; require the 11 canonical sections, unique compatible state and
next actor/action, top-level ordered Implementation Steps, one complete
selector tuple and an explicit local-delivery/no-release stop point. The Base
profile also supports repo-local development tools; it does not select or
emulate upstream specialized profiles. Missing/duplicate/ambiguous inputs,
existing output or unsupported profiles stop before any write. Do not repair
source wording. Validate before creating a same-directory temporary file,
then recheck absence and atomically promote without overwrite; clean temporary
output on failure and preserve any existing final artifact.

## Evidence and tracker

[X] means exact one-to-one completion evidence; [ ] pending/planned/unproved.
Source [x] is pending and warns. No exception promotes authoring or approved
status to execution evidence. Every source Implementation Step is preserved
verbatim once in order. Evidence names exact paths/commands/result identifiers.
Initial worktree actions may stay pending without an existing worktree. Freeze
and repeat topic, branch, managed-path-intent, primary-worktree=false in each
selector-bearing row and Handoff Notes. Plans are not inventory proof.

## Lifecycle rendering

Use templates/shared-lifecycle-shell.md exclusively. Observer only dispatches
and stops; named role owners execute bounded work when mode and authorization
permit it. The fixed tail ends at local reviewable delivery; no publish, merge,
release, tag, remote/local branch deletion or worktree cleanup is injected.
Separately requested publishing is a separate explicit handoff, never inferred
from this shell. Whole-file checks cover every rendered checkbox; implementation
checks only Implementation Steps. Both query markers, not external evidence.
