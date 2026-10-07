---
name: context-package-builder
description: "Build a minimal context package for one already-bounded, real subagent handoff."
complexity: medium
---

# Purpose

Produce one minimal context package for one bounded handoff.

This skill does not choose the next role and does not route after a result.

# Trigger / When to use

Use this skill when:

- one bounded task slice already exists
- the Observer has already determined that dispatch is allowed or is checking
  whether dispatch can be made real
- a task-specific handoff package must be assembled for one role

Do not use this skill when:

- the task is to decide which role should receive the handoff
- the task is to choose the next route after a verdict
- the task needs a whole conversation dump or multi-task bundle

# Inputs

- one bounded task slice
- the target role name
- frozen source-of-truth artifact paths
- exact write-set constraints, if any
- bounded evidence excerpts needed for the task
- optional topic-local step artifact path when workflow-derived state is needed

# Process

1. Keep the package scoped to one task slice and one target role.
2. Include only the frozen truth, constraints, and evidence the target role
   needs to act.
3. If workflow-derived state is needed, include only the relevant
   `plan/<topic>/<topic>.step.md` fact and do not reconstruct the full
   workflow.
4. Exclude all forbidden context categories:
   - whole conversation history
   - unrelated prior decisions
   - speculative reasoning
   - multiple independent tasks
   - unresolved roadmap material
   - unnecessary platform-specific assumptions
   - role-to-file lookup hints
   - registry identifiers
5. Make unknowns explicit instead of filling gaps with inference.
6. If real dispatch is not available, or if creating the package would require
   workflow binding or runtime semantics, stop and produce no context package.
7. Return one minimal package that can be inserted into an explicit handoff
   payload only when that handoff is real and bounded.

# Examples

- **Positive**: Build a package for `Implementer` that includes the bounded
  write set, frozen requirements/spec/plan paths, and one relevant step-artifact
  fact.
- **Negative**: Attach the whole chat transcript, old topic history, registry
  hints, and speculative route guesses "for safety."

# Outputs

- `target_role`: one allowed role name
- `task_slice`: one bounded task statement
- `frozen_inputs`: exact artifact paths
- `constraints`: bounded rules and stop conditions
- `evidence`: only the excerpts needed for this handoff
- `unknowns`: explicit unresolved items

# Boundaries

- Do not decide the next role.
- Do not choose the next route after a result.
- Do not include unrelated or speculative context.
- Do not include registry keys, catalog entries, or role-to-file hints.
- Do not treat `.github/**`, `.codex/**`, or other platform paths as canonical
  truth.
- Stop without producing a context package if real dispatch is unavailable or
  if runtime semantics would be required to make the handoff meaningful.

# Local references

- `examples.md`: minimal-package examples and forbidden-context counterexamples

## Allowed roles and mode constraints

Target role is Planner, Plan-Creator, Plan-Reviewer, Implementer, Reviewer,
Tester or Explorer. Code-Implementer / Code-Reviewer normalize to Implementer /
Reviewer. Include active mode, selected worktree, exact authorized write/read-only
sets, evidence and stop boundary. In Plan Mode all roles are read-only and
Plan-Creator drafts only in conversation. Reject unknown roles; no package
without real dispatch. A package never grants missing write authorization.
