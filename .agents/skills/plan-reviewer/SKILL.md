---
name: plan-reviewer
description: "Independently review an authored repository topic plan before execution."
complexity: high
risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff
use_when:
  - "a repo-visible `plan/<topic>/<topic>.plan.md` already exists"
  - "the plan needs an independent review before branch preparation or Implementer implementation begins"
  - "an existing topic plan was revised and needs contract re-review"
  - "Observer is routing plan review through a separate independent reviewer path"
do_not_use_when:
  - "the main task is to author or revise the topic plan itself"
  - "the task is to review a skill folder or implementation draft"
  - "the request is for a generic project plan outside this repository"
  - "the task is to rewrite the canonical workflow spec itself"
inputs:
  - genuine independent start acknowledgement and authorized owner-recorded current reviewer-in-progress source
  - "the target `plan/<topic>/<topic>.plan.md`"
  - "the current workflow contract from `plan/agent-handoff-workflow.md`"
  - "the shared topic-plan contract from `plan/topic-plan-contract.md`"
  - "any contextual review feedback, including Copilot feedback, if it exists"
outputs:
  - "eligible review: exactly one fixed native JSON object; preflight failure: BLOCKED coordination without native verdict"
  - "verdict set to approved or needs-rework"
  - "blocking_issues list with issue, file, and fix for each contract-breaking problem"
  - "copilot_feedback_triage with ADDRESS, DISCUSS, and SKIP arrays"
---

# Purpose
Review a repo-visible topic plan as a planning-contract gate before execution proceeds.

# Trigger / When to use
Use this skill when:
- a repo-visible `plan/<topic>/<topic>.plan.md` already exists
- the plan needs an independent review before branch preparation or Implementer implementation begins
- an existing topic plan was revised and needs contract re-review
- Observer is routing plan review through a separate independent reviewer path

Do not use this skill when:
- the main task is to author or revise the topic plan itself
- the task is to review a skill folder or implementation draft
- the request is for a generic project plan outside this repository
- the task is to rewrite the canonical workflow spec itself

# Inputs
- the target `plan/<topic>/<topic>.plan.md`
- the current workflow contract from `plan/agent-handoff-workflow.md`
- the shared topic-plan contract from `plan/topic-plan-contract.md`
- any contextual review feedback, including Copilot feedback, if it exists

## Pre-review eligibility and owner coordination

Before either native verdict, require readable target plan and both contracts,
a genuine independent actual review-start acknowledgement, and the authorized
owner's recorded current reviewer-in-progress phase referencing that start.
Author and Reviewer must be distinct. At review-ready, the Reviewer may actually
acknowledge start and return BLOCKED coordination asking the authorized owner
to record the canonical phase; no native approved/needs-rework yet. Resume only
after the recorded eligible source is readable. Other stages, missing/unresolved
plan/contracts/start/owner-record evidence stop with BLOCKED coordination and no
native verdict, even for standalone invocation. These are eligibility failures,
not structural needs-rework verdicts.

Reviewer keeps the source plan body and phase metadata read-only. Only an
exactly authorized owner records reviewer-in-progress after the real start event
and approved/needs-rework after returned native verdict. Preserve source body
hash/current review basis across the pause; no fake acknowledgement/history,
self-review or new state/schema. In Plan Mode nobody writes; inspect existing
eligible evidence or stop for owner coordination, never bypass the mode gate.

# Process
0. Check pre-review eligibility above before judging structure or issuing either native verdict. If not eligible, return BLOCKED coordination with the exact gap; do not generate the fixed verdict object.
1. Confirm the task is topic-plan review, not plan authoring, skill review, publish routing, or workflow-spec editing.
2. Read the target topic plan plus the shared contract sources before judging the plan.
3. Verify the topic plan path, required sections, canonical status model, artifact-path exactness, stable-library intent, reviewer handoff JSON shape, post-merge timing, and role boundaries.
4. Treat placeholders such as `TBD`, `later`, or `follow normal process` as contract failures when the workflow requires explicit decisions.
5. Treat missing sections, invalid transitions, vague artifact paths, undeclared stable intent, wrong timing, non-JSON reviewer handoff, and role-boundary confusion as blocking issues.
6. Keep the review focused on contract-breaking issues rather than wording polish or stylistic preferences that do not change workflow meaning.
7. Only for an eligible review, return exactly one JSON object with the unchanged fixed schema:
   - `verdict`: `approved` or `needs-rework`
   - `blocking_issues[]`: objects with `issue`, `file`, and `fix`
   - `copilot_feedback_triage.ADDRESS[]`: objects with `comment`, `location`, and `why`
   - `copilot_feedback_triage.DISCUSS[]`: objects with `comment`, `optional`, and `why`
   - `copilot_feedback_triage.SKIP[]`: objects with `comment` and `why`

# Examples
- **Positive**: Review `plan/python-docstrings/python-docstrings.plan.md` after the plan exists, reject no contract-breaking issues, and return one JSON object that confirms non-stable intent, exact artifact paths, canonical transitions, and machine-consumable reviewer handoff.
- **Negative**: Use this skill to draft the topic plan, approve a plan that says `README/VERSION maybe later`, or return Markdown prose instead of the required JSON verdict.

# Outputs
- preflight failure: BLOCKED coordination and no native verdict
- eligible review: exactly one machine-consumable fixed JSON object and no trailing prose
- `verdict`: `approved` or `needs-rework`
- `blocking_issues`: only true contract-breaking problems; each item contains `issue`, `file`, and `fix`
- `copilot_feedback_triage.ADDRESS`: direct required feedback items; each item contains `comment`, `location`, and `why`
- `copilot_feedback_triage.DISCUSS`: optional discussion items; each item contains `comment`, `optional`, and `why`
- `copilot_feedback_triage.SKIP`: explicitly inapplicable feedback items; each item contains `comment` and `why`

# Verification
- verify readable plan/contracts, genuine distinct-reviewer start and authorized owner-recorded reviewer-in-progress before any native verdict
- confirm the review basis explicitly includes `plan/agent-handoff-workflow.md` and `plan/topic-plan-contract.md`
- confirm required sections are present and named correctly
- confirm transitions stay canonical and execution timing is coherent
- confirm `Artifact Paths` are exact, bounded, and repo-visible
- confirm stable-library intent is explicit: clearly absent or explicitly declared
- confirm the verdict stays JSON-only with no prose outside the object

# Red Flags
- the plan invents a new status model or skips canonical phases
- `Artifact Paths` use broad labels such as `docs`, `skill folder`, or `maybe version files`
- stable-library timing is implied but not declared
- `Reviewer Handoff` is a table, prose note, or mixed-format report instead of one JSON object
- Plan-Creator, Implementer, Plan-Reviewer, Reviewer, and Observer responsibilities are blended together

# Common Rationalizations
- "The reviewer can infer the missing contract later."
- "The exact paths are obvious from context."
- "We can decide stable-library timing after implementation."
- "A rough status model is good enough if everyone understands the goal."

# Boundaries
- Do not rewrite the topic plan on behalf of the Plan-Creator.
- Do not invent a second topic-plan schema that conflicts with `plan-creator` or the canonical workflow.
- Do not approve a plan that still has contract-breaking ambiguity.
- Do not turn this skill into implementation review, branch preparation, or publish execution.
- For eligible reviews emit only the single unchanged JSON verdict. Preflight failures emit BLOCKED coordination, never native approved/needs-rework.

# Validation

## Required Checks
- PASS: the shared contract sources are readable before review begins
- PASS: readable target and actual start proof are present, with authorized owner-recorded current reviewer-in-progress
- BLOCKED: missing/unreadable plan, contracts, actual start or owner-recorded eligible phase — coordination only, no native verdict

## Quality Checks
- all required topic-plan sections are present and named correctly
- canonical status model and transitions are used without invention
- artifact paths are exact, bounded, and repo-visible
- stable-library intent is explicitly declared or explicitly absent
- reviewer handoff is exactly one JSON object with no trailing prose
- post-merge timing is coherent with the topic scope

## On Soft Fail
- treat placeholder text (`TBD`, `later`, `follow normal process`) as a contract failure, not a soft gap
- after eligibility passes, a plan with any structural blocking issue returns needs-rework; partial approval is not allowed

# Failure Handling

## Missing Context
- BLOCKED — if `plan/agent-handoff-workflow.md` or `plan/topic-plan-contract.md` cannot be read, stop before issuing any verdict
- BLOCKED — if target plan path cannot be resolved, report coordination gap without a native verdict; never guess a path

## Ambiguous Requirement
- if a section name is subtly wrong but the intent is clear, flag it as a contract failure rather than silently accepting it
- if the plan's stable-library intent is partially declared, treat partial declaration as undeclared

## Execution Limitation
- if a plan section is ambiguously present (e.g., combined with another section), flag it and return `needs-rework` rather than accepting ambiguous structure
- if Copilot feedback input is absent, populate the `ADDRESS`, `DISCUSS`, and `SKIP` lists as empty arrays rather than omitting them

# Workflow State Contract

When participating in a multi-agent plan review or creator-reviewer handoff, include:
- current_step: <step name from Process>
- next_step: <next step or DONE>
- status: APPROVED | NEEDS_REWORK | INCOMPLETE | BLOCKED

These fields are for internal agent state coordination only and MUST NOT appear inside the final JSON verdict object; eligible delivered reviews remain the single fixed-schema JSON object in all modes and standalone/multi-agent uses. Preflight failures instead return BLOCKED coordination with no native verdict; these state fields never enter native JSON.

Omit this section when the review is performed as a standalone action.

# Local references
- `reference.md`: stable review basis, severity rules, and workflow-position guidance for topic-plan review
- `plan/topic-plan-contract.md`: shared repo-level authority for required topic-plan sections, fallback behavior, and contract-level blocking semantics
- `examples.md`: approved and needs-rework plan-review scenarios, including stable and non-stable cases
- `checklist.md`: repeatable contract checks for this higher-risk planning gate
