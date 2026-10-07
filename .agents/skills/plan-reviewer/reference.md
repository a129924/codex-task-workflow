# Plan Reviewer Reference

Use this file to keep repo-visible topic-plan review aligned with the repository workflow.

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

## Review basis

Review topic plans against the shared contract sources together:

1. `plan/agent-handoff-workflow.md`
2. `plan/topic-plan-contract.md`
3. this skill's local `reference.md`, `checklist.md`, and `examples.md`

Do not treat any one source as sufficient by itself. The workflow defines the canonical execution contract, `plan/topic-plan-contract.md` defines the canonical topic-plan section and fallback contract, and this skill's local materials define review heuristics and common failure signals.

When a topic uses correction / delta artifacts, also verify that the plan keeps the workflow body slim, lists exact parent/correction paths, makes parent-sync closure explicit, keeps review-log usage conditional on routing-controlling feedback, and leaves the minimum correction artifact contract in reference / examples instead of the workflow body.

If the topic is a correction-lifecycle contract refresh, verify that it refreshes existing workflow / plan surfaces now and does not create a standalone correction skill unless a separate topic explicitly justifies extraction because repeated instability or cross-workflow reuse has been demonstrated.

## What counts as blocking

Treat these as blocking issues:

- missing required sections
- invalid or non-canonical transitions
- vague or drifting `Artifact Paths`
- undeclared or mixed stable-library intent
- non-JSON reviewer handoff
- wrong post-merge or release timing
- mixed role ownership
- placeholders where the workflow needs an explicit contract
- vague correction evidence paths such as `merged implementation`
- missing parent-sync closure logic when correction artifacts are used
- reviewer-owned logging or verdict work inside Implementer `Implementation Steps`
- workflow-body bloat that turns the plan into a field-by-field correction schema
- unconditional review-log requirements when routing control or multi-round rework is absent
- turning a sample round cap into a repository-wide invariant
- a correction-lifecycle refresh topic that quietly broadens into standalone-skill creation without separate justification

Do not raise blocking issues for tone, phrasing, or layout preferences that do not change contract meaning.

## Workflow position

`plan-reviewer` runs after a repo-visible topic plan exists and before later execution begins under `plan/agent-handoff-workflow.md`.

Typical operating sequence:

1. `plan-creator` authors `plan/<topic>/<topic>.plan.md`
2. Observer dispatches a distinct Reviewer who actually acknowledges review start
3. exactly authorized owner records reviewer-in-progress after that acknowledgement
4. resumed independent Reviewer issues native verdict only on the readable eligible source
5. owner records approved/needs-rework after actual returned verdict; fixes follow canonical rework before later execution

This skill is a planning-contract gate. It does not replace the existing independent implementation Reviewer check, and it does not create a new numbered phase by itself.

## Output rule

Only after pre-review eligibility, return exactly one unchanged JSON object with:

- `verdict`
- `blocking_issues`
- `copilot_feedback_triage`
  - `ADDRESS`
  - `DISCUSS`
  - `SKIP`

For eligible review keep reasoning inside structured fields and no trailing prose. Eligibility failure is separate BLOCKED coordination, never a native verdict.
