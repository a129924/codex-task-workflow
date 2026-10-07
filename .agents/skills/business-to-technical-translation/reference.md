# Business-to-Technical Translation Reference

Use this file after `SKILL.md` has already narrowed the task to translating a frozen business baseline into a technical specification.

## Baseline gate

A readable frozen `analysis/<topic>/requirements.md`, or an explicitly identified
complete frozen conversation requirements draft in actual Plan Mode, must provide:
- named actors and measurable outcomes
- explicit constraints and non-goals
- resolved contradictions or clearly marked blockers
- enough business meaning that technical work can be traced back honestly

If the baseline still says `fast`, `simple`, `better`, or similar soft language without a measurable interpretation, roll back to `business-intent-alignment` instead of inventing technical certainty.

## Recommended technical-spec shape

A strong `analysis/<topic>/technical-spec.md` usually includes:
- source baseline summary and traceability table
- required technical tasks and artifacts
- dependency and integration notes
- cost-of-realization assessment
- architecture-compliance self-check
- conflicts, blockers, and rollback triggers

Useful traceability framing:

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| measurable business requirement | component, interface, or operational work | systems, teams, or data needs | build + run cost | feasible / blocked / rollback |

## Pessimistic implementer defaults

Assume these concerns count unless the baseline or system facts prove otherwise:
- migration and backfill work
- monitoring, alerting, and audit needs
- permission and role enforcement
- retry, duplicate, and partial-failure handling
- data retention, privacy, and regulatory constraints
- operational support load after launch

A technically complete answer is not only `what to build`; it must also say what makes the build hard, expensive, or risky.

## Architecture-compliance self-check

Review at least these dimensions:
- existing repository or platform boundaries
- approved storage, messaging, and integration patterns
- security and compliance expectations
- observability and rollback support
- dependency direction and ownership boundaries

Name the result explicitly:
- `fits existing architecture`
- `fits with prerequisites`
- `needs waiver`
- `conflicts with current architecture`

## Rollback-to-alignment triggers

Roll back to business alignment when:
- the required metric cannot be implemented on the approved platform
- the timeline assumes unavailable teams, systems, or approvals
- compliance or security rules make the current business promise invalid
- the cheapest feasible implementation violates a non-negotiable business constraint
- a hidden prerequisite changes the meaning of the original requirement

Rollback notes should name:
1. the failing business assumption
2. the technical fact that contradicts it
3. the decision or renegotiation needed before planning can continue

## Actual mode and output boundary

Verify the actual active engine mode before artifact output. Controlled prompt
mode labels test policy only and cannot certify actual Plan Mode. In Plan Mode
return conversation-only drafts with explicit intended paths and no file writes,
existence claims or subagent bypass. In Default execution, file writes require
the selected feature worktree and exact authorized output paths. Unknown or
unverified mode never implies write permission; block file output and disclose
the limit. Preserve measurable baseline content and explicit freeze/blocker state.

A Plan Mode conversation baseline must be complete, explicitly frozen and identified;
missing/vague/unfrozen input blocks translation. Name intended requirements path
and content identity, never claim a file was read or exists when only a draft
was supplied. Default continues to require the readable frozen file baseline.
