---
name: step-creator
description: "Create a topic step artifact from an eligible plan with the explicitly selected base-plan profile."
complexity: high
risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff
  - code_modification
inputs:
  - topic name
  - "explicit profile: base-plan"
  - readable source plan at plan/<topic>/<topic>.plan.md
  - repo-visible progression and completion evidence for non-pending markers
outputs:
  - one newly created plan/<topic>/<topic>.step.md
---

# Purpose

Create one new tracker from a complete, independently approved local topic plan. Generate a tracking
artifact only; never execute the listed actions or update existing trackers.

# Trigger / When to use

Use for an explicit path-safe topic and base-plan profile, readable eligible
plan and absent destination. Do not infer profiles or repair existing output.

# Inputs

Read plan/agent-handoff-workflow.md, plan/topic-plan-contract.md, the exact
source plan and any named evidence. The caller supplies exactly base-plan.
agent-skill-plan and python-implementation-plan are unsupported here: BLOCKED
before any write, with no fallback or dependency installation.

# Process

1. Resolve plan/<topic>/<topic>.plan.md and the absent .step.md destination.
   Missing contracts, unsafe topic, unreadable source or existing output is
   BLOCKED with no temporary or final artifact.
2. Require explicit base-plan and read reference.md plus
   references/base-plan-profile.md. Run the complete eligibility preflight.
   Require terminal approved, explicit []/none planning transitions, next actor
   Implementer and a bounded implementation action before any temporary/final
   write. All five earlier/rework states are BLOCKED even with canonical edges.
   Missing, duplicate, contradictory or nested-only required input is BLOCKED.
3. Freeze one tuple: topic, governed branch, managed path intent,
   primary-worktree=false. Competing tuples stop. Planned intent does not prove
   a worktree exists. Source states the local delivery stop point and no release.
4. Render the Base wire: fixed head, source-faithful contextual action,
   one-to-one verbatim ordered Implementation Steps, fixed tail, handoff notes.
   Observer rows only dispatch; concrete work belongs to an allowed role.
5. Every checkbox is [X] with exact one-to-one evidence or [ ] if pending.
   Lowercase source [x] is pending and warns. Initial generation permits
   pending worktree actions; do not invent evidence, approval or test results.
6. Validate the entire rendered content and destination absence. Only then
   create a same-directory temporary file, validate it, recheck absence and
   atomically promote without overwrite. On failure or destination race,
   remove the temporary file, preserve existing output and leave no partial
   final artifact. If atomic no-overwrite creation is unavailable, INCOMPLETE.
7. Return review-ready with profile, generated path, evidence, warnings and
   an independent Reviewer handoff. Do not self-approve or execute lifecycle.

# Validation

Source uses the 11 canonical sections, exactly one top-level Implementation
Steps, terminal approved with empty next planning transitions, exact Implementer
next actor and bounded implementation action,
and one complete selector. Only base-plan is supported. Frozen wire and
source fidelity hold; all markers are [X] or [ ]; every [X] has evidence.
Only the new destination is written. Plan Mode forbids even this write for all
roles; draft only in conversation when Plan Mode is active.

# Failure Handling

BLOCKED: missing required inputs/contracts, unsupported profile, existing
output, ambiguous source/selector/evidence or changed scope. Name the exact
missing field without manufacturing it. INCOMPLETE: tool/atomic creation
limitation; no partial output. Scope drift requires Plan-Creator, not repair
inside this skill.

# Verification

check_all_succeeded covers head, contextual, Implementation Steps and tail;
check_impl_steps_succeeded covers only the Implementation Steps section.
Neither proves external artifacts or actual gates. The installed tracker
entry is .agents/skills/plan-step-tracker/scripts/step_tracker.py, from repo root.

# Boundaries

Do not modify source plans, existing trackers, README, VERSION, projections or
skills. Do not execute Git, commit/push/PR, merge/release, deletion or cleanup.
Do not add profiles or require the absent python-plan-authoring skill.

# Workflow State Contract

current_step: preflight | render | validate
next_step: review-ready | BLOCKED
status: IN_PROGRESS | COMPLETE | INCOMPLETE | BLOCKED

# Local references

- reference.md: generation, evidence and lifecycle rules
- references/base-plan-profile.md: eligibility and frozen wire
- references/agent-skill-plan-profile.md: unsupported-profile stop
- references/python-plan-authoring-adapter.md: unsupported-profile stop
- templates/shared-lifecycle-shell.md: fixed local-delivery renderer
- checklist.md: preflight and validation
- examples.md: valid and blocked cases
