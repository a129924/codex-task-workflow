# Topic plan template

Use this template to draft `plan/<topic>/<topic>.plan.md` for this repository.
Delete prompt text after replacing it with real topic-specific content.

## Goal / Outcome

- State the concrete repository-visible result of this topic.
- Say what should exist or be true when the topic is complete.

## Scope

- **In scope**:
  - List the concrete files, folders, or repository-visible outcomes this topic will change.

- **Out of scope**:
  - List nearby work this topic will not do.

## Locked Decisions

- Record decisions downstream roles should not rediscover.
- Say that this topic is local development work with stable-library intent absent;
  stable promotion requires a separate publishing contract and is BLOCKED here
- If this topic uses correction artifacts, lock whether the workflow body stays slim and where detailed correction schema guidance belongs.
- If this topic is a correction-lifecycle refresh, state whether standalone skill extraction is explicitly deferred and what later conditions could justify a separate topic.

## Boundaries / Exclusions

- State the role and scope boundaries that must remain intact.
- Call out adjacent tasks that belong in a different topic.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: Plan-Creator -> independent Plan-Reviewer; after approved,
  Implementer -> Tester -> independent Reviewer -> local reviewable delivery.
- **Next actor**: Plan-Creator
- **Stage-local action**: Author the bounded topic plan.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`

Only list valid outgoing transitions for the declared current status. When that
status changes, replace this edge and the matching next actor/action using the
shared canonical authority; do not copy the whole lifecycle into this field.
Implementation proceeds
only after independent approval; do not add publish, merge or release states.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/<topic>/<topic>.plan.md` | Plan-Creator | Repo-visible execution contract for this topic |
| [artifact name] | `[exact/path]` | [role] | [why it exists in this topic] |

Artifact path notes:

- Say explicitly whether this topic modifies `README.md`, `VERSION`, or `.github/copilot-instructions.md`.
- Treat listed paths as an executable contract.
- If the topic uses correction artifacts, list each exact parent artifact, each exact correction artifact, and any repo-visible `review-log` / equivalent handoff artifact only when reviewer feedback controls routing or multi-round rework.
- Do not use vague evidence labels such as `merged implementation`, `correction files`, or `latest feedback`.
- Say what should happen if later work drifts outside these paths.

## Implementation Steps

- Describe what Implementer work will produce.
- Keep the steps inside the topic's locked boundaries.
- Keep the steps Implementer-owned; do not assign reviewer verdict logging or Observer routing work here.
- If correction lifecycle guidance is part of the topic, keep the workflow body focused on lifecycle / routing contract and move field-level correction artifact schema or long examples into reference / example surfaces.
- If correction artifacts are part of the topic, make sure some allowed reference / example surface defines the minimum `correction-plan` and `correction-step` content instead of pushing that schema into the workflow body.

## Validation / Acceptance Checks

- List the signals reviewer and main agent should verify.
- Include workflow-critical checks such as path exactness, status correctness,
  and reviewer handoff shape when relevant.
- When correction artifacts are used, include parent-sync closure, current-truth versus historical-truth separation, and conditional review-log expectations.

## Reviewer Handoff

- Use a single JSON object, not Markdown prose or tables.

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- Say what happens after merge.
- If no repository release action is required, say so explicitly.
- Stable publishing is BLOCKED without a separately approved publishing contract.
- Preserve the topic feature worktree for human review; no automatic cleanup.

## Open Questions / Unresolved Items

- Keep only the questions that truly remain open.
- If a missing answer blocks correct planning, stop and ask instead of leaving the plan vague.
