# `base-plan` profile

## Independent approval and current-source binding

Terminal approved fields alone are not approval evidence. Before any draft or
write, require the genuinely returned independent Plan-Reviewer native approved
result, actual distinct author/reviewer and parent-task/reviewed-version linkage,
and the authorized owner's recorded reviewer-in-progress to approved transition.
Bind the native result to the reviewed snapshot/hash and the owner's transition
to both reviewed and approved snapshots. The current source whole-file hash must
match that owner-approved snapshot; compare bytes outside the exact authorized
Status/Allowed next transitions metadata against the reviewed snapshot. Those
remaining bytes must be unchanged. Legitimate owner status metadata can change
the whole-file hash; do not require equality of reviewed and approved whole hashes.
Missing, forged, stale/version-mismatched proof or body changes under nominal
approved fields are BLOCKED without writes, including draft-only requests.
Keep source, native result, owner trace and snapshots read-only. Recheck all
approval/version/body bindings before temp creation and immediately before
no-overwrite promotion, alongside mode/root/exact authority/absence. Approval
proves source eligibility only, never action completion or permission.

## Actual mode and selected-output authority

Before rendering-for-write or any temporary/final artifact, verify actual engine
mode, selected owned feature and canonical source-consistent destination
plan/<topic>/<topic>.step.md derived from the source topic and verified root.
Verify exact final plus narrowly recorded necessary same-directory temp authority.
A separate step row in source Artifact Paths is not required; explicit source
path/selector conflicts remain BLOCKED. Reuse existing
authorization without repeated permission. Plan or known Default with explicitly
absent output authority returns a complete eligible source-faithful conversation
draft with intended path/proposed fields, no artifact/current-phase/execution
claims. Unknown mode, missing/ambiguous selection or unresolved/mismatched/outside
authority is BLOCKED without writes. Controlled mode labels are policy only.
Keep genuine source/native/owner proof read-only; relocating a controlled copy
does not issue new approval or reconcile explicit source path/selector conflicts.

Authorized Default validates before its exactly authorized temp creation, then
rechecks actual mode, selected-root containment, exact final/temp authority and
absence immediately before atomic no-overwrite promotion. Lost authority or
destination race stops, preserves existing final bytes and cleans only the
just-created owned temporary artifact under its existing authority. No action
executes. Unsupported/source-ineligible inputs remain BLOCKED in draft-only cases.

## Eligibility preflight

Accept only a source plan that:

- has every canonical topic-plan section required by `plan/topic-plan-contract.md`;
- uses the local shared contract, not an upstream specialized Agent Skill or Python profile;
- declares terminal current status `approved`, an explicitly empty next planning
  transition set (`[]` or `none`), exact next actor `Implementer`, and a bounded
  implementation action consistent with the shared contract;
- has exactly one top-level `## Implementation Steps` section with executable
  ordered items; and
- declares one complete selector and the local-delivery/no-release stop point; and
- has no conflicting selector, completion or source extraction truth.

Terminal `approved` is required before any temporary or final tracker write.
It requires no invented outgoing planning transition. `planned`,
`creator-in-progress`, `review-ready`, `reviewer-in-progress` and `needs-rework`
are all BLOCKED even with valid outgoing transitions and matching actor/action.
Keep the canonical planning lifecycle unchanged; do not freeze mutable steps
before independent approval. Approval alone proves no action completed.

Missing, ambiguous, duplicated, contradictory, nested-only, or specialized
inputs are `BLOCKED`. This profile does not repair source wording.

## Frozen output wire

```markdown
---
topic: <topic>
step_profile: base-plan
source_plan: plan/<topic>/<topic>.plan.md
created: YYYY-MM-DD
---

# <topic> — Step Tracking

## Workflow Stages

| Current status | Allowed next transitions | Next actor |
| --- | --- | --- |
| <exact source-plan status> | <exact canonical allowed transition(s)> | <exact source-plan next actor> |

## Actionable Steps

### Observer — Fixed Head

<rendered shared fixed head>

### Contextual Actions

- <resolved-checkbox> **Actor:** <source actor> — **Action:** <preserved stage-local action>

## Implementation Steps

- <resolved-checkbox> 1. <source Implementation Step 1, verbatim>

## Observer Actionable Steps — Fixed Tail

<rendered shared fixed tail>

## Handoff / Gate Notes

- Selected profile: base-plan
- Source plan: plan/<topic>/<topic>.plan.md
- Shared lifecycle shell: .agents/skills/step-creator/templates/shared-lifecycle-shell.md
- Managed worktree intent: topic=<topic>; branch=<selector>; managed-path-intent=<intent>; primary-worktree=false
- Progression truth inputs: <exact paths>
- Completion evidence inputs: <exact paths/identifiers>
- Marker semantics: `[X]` exact one-to-one evidence; `[ ]` pending/planned/unproved; lowercase source `[x]` is pending and warns.
- Tracker semantics: `check_all_succeeded` covers rendered head/contextual/Implementation/tail checkboxes; `check_impl_steps_succeeded` covers only Implementation Steps.
- Owner-only updates: only the action owner may update after exact evidence; step-creator never updates an existing output.
```

The frozen profile wire owns the `### Observer — Fixed Head` heading; the
shared shell supplies its two rows only. Render actual `[X]` or `[ ]` in place
of every `<resolved-checkbox>` placeholder; no other marker is literal output.
Every selector-bearing shared-shell row must carry the complete frozen tuple,
including `primary-worktree=false`, exactly as Handoff / Gate Notes does.
Preserve contextual source wording and order. Follow the shared reference for
exact collective dedup and one-to-one mapping.
