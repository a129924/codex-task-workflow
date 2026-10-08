# Shared topic-plan contract

This is the fallback authority if the local plan-creator template is unavailable.
Read this together with plan/agent-handoff-workflow.md before creating or
reviewing a plan. Missing contracts or required inputs are BLOCKED: do not
create success artifacts or approve by inference. These contracts describe
repo development only; GOAL.md and docs/task-workflow.baseline.md remain the
Task product authorities and are not changed by importing skills.

## Required sections

Each topic plan uses exactly these mandatory level-two headings, in this order:

1. Goal / Outcome
2. Scope
3. Locked Decisions
4. Boundaries / Exclusions
5. Status / Allowed Transitions
6. Artifact Paths
7. Implementation Steps
8. Validation / Acceptance Checks
9. Reviewer Handoff
10. Post-merge / release actions
11. Open Questions / Unresolved Items

Goal states the result; Scope enumerates in/out scope; Locked Decisions freezes
choices; Boundaries separates roles and adjacent work; Status gives the actual
planning state, canonical allowed transitions, next actor and stage-local action;
Artifact Paths gives exact role-owned paths; Implementation Steps contains
ordered executable Implementer-owned work; Validation gives acceptance evidence;
Reviewer Handoff supplies the independent JSON contract; Post-merge explicitly
states the stop point and whether release applies; Open Questions lists only
actual unresolved inputs. Missing, renamed, duplicate or merged sections fail
review. Do not add nine new mandatory shared headings: topic-specific Goal,
Non-Goal, In-Scope, Out-Of-Scope, ReadOnly, Written, Modify, Deleted, TestCase
fields belong inside the existing sections when requested.

## Paths and boundaries

Plans live at plan/<topic>/<topic>.plan.md and new step artifacts at
plan/<topic>/<topic>.step.md. Enumerate each intended output and owner in the
Artifact Paths table. Directory rows are allowed only for an explicitly bounded
skill directory whose complete pinned tracked manifest is declared; they never
authorize arbitrary future files. Declare modifications/deletions separately
and preserve ReadOnly files. Path drift stops for a bounded plan revision.

Plan-Creator authors; independent Plan-Reviewer judges contracts; Implementer
owns code and fixes; Tester supplies test evidence; Reviewer judges implementation.
Observer dispatches and stops. approved is terminal for planning: declare [] or
none for allowed next planning transitions, next actor Implementer and a bounded
implementation action. Other states require an outgoing canonical transition
and matching actor/action. No review verdict/logging inside implementation
steps. No hidden publish authority follows from plan approval.

## Analysis priority

If both analysis/<topic>/requirements.md and technical-spec.md exist, use the
technical spec as execution truth and requirements as business guardrail. One
missing companion produces an explicit incomplete-analysis warning. If neither
exists, name both missing files and warn that the optional analysis layer is
absent; this is a semantic warning, not by itself a blocker. Clear authorized
user revisions synchronize only the affected baseline before downstream use;
ambiguous conflicts stop. Do not silently replace existing analysis with chat.

## Stable-library and profile boundary

Repo-local development skills are not a stable publishing library. A README
navigation link alone does not require VERSION, registry, release notes or tag
work. Declare stable-library intent absent and no release action for local work.
Stable-library promotion is outside this contract and requires a separately
approved publishing contract; absent that contract it is BLOCKED. step-creator
supports base-plan only. agent-skill-plan and python-implementation-plan are
unsupported and stop before writing; do not substitute a different profile.

## Independent reviewer JSON

For eligible independent reviews only, return exactly one JSON object with no
trailing prose. First verify readable plan/contracts, genuine independent
actual start acknowledgement and authorized owner-recorded current
reviewer-in-progress. Missing eligibility returns BLOCKED coordination,
not a native approved/needs-rework verdict:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {"ADDRESS": [], "DISCUSS": [], "SKIP": []}
}
```

The verdict must be one native value. blocking_issues entries contain issue,
file, fix; ADDRESS entries contain comment, location, why; DISCUSS entries
contain comment, optional, why; SKIP entries contain comment, why. Missing
feedback means empty arrays. A blocker requires needs-rework, never partial
approval. Internal workflow state does not belong in the output JSON. The
schema above is a template, not a real review result. Missing, unresolved or
unreadable plan/contracts/start/owner eligible-phase proof stops with BLOCKED
coordination and no native verdict. Name the exact missing path or evidence.
After eligibility passes, structural defects use unchanged native needs-rework.
