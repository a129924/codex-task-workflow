# handoff-routing-policy examples

Positive provenance below is illustrative, not issued IDs/dispatch/authority.
Real routing verifies genuine returned parent-task/actor/result and artifact-version
linkage. Every Reviewer/Code-Reviewer/Plan-Reviewer verdict requires the actual
returned reviewer to differ from the identified actual author, including PASS,
approved, needs-rework, MISSING_EVIDENCE and BLOCKED. Ordinary nonreview PASS
retains its usual explicit next-role rule.
Unexposed provider request IDs are disclosed, never fabricated or replaced by
registry/launcher binding.

## Positive: patch required

Input:

- `result_role`: `Reviewer`
- `verdict`: `PATCH_REQUIRED`
- actual parent dispatch: the bounded review task delivered to the independent Reviewer
- actual returned actor: that dispatched Reviewer, distinct from the recorded actual author
- actual result correlation: returned PATCH_REQUIRED belongs to that same task and actor
- actual author: independently identified implementation author, not a role label
- bounded evidence summary: one accepted artifact is still missing required text

Output:

```json
{
  "next_role": "Implementer",
  "reason": "The reviewer verdict requests a bounded implementation patch.",
  "stop_condition": "none"
}
```

## Positive: replan required

Input:

- `result_role`: `Reviewer`
- `verdict`: `REPLAN_REQUIRED`
- actual dispatch/result correlation and returned actor: verified as above, Reviewer distinct from actual author
- blocker: the required change would expand outside the frozen write set
- policy example only: without a genuine historical REPLAN_REQUIRED result, do not label it actual dispatch or manufacture replan

Output:

```json
{
  "next_role": "Plan-Creator",
  "reason": "The returned verdict requires a bounded replan before implementation can continue.",
  "stop_condition": "none"
}
```

## Positive: initial implementation passes to Tester, then independent Reviewer

Input:

- `result_role`: `Implementer`
- `verdict`: `PASS`
- bounded evidence: implementation for the current slice is ready for assigned testing
- `declared_next_role`: `Tester`
- declaration source: the actual Implementer handoff explicitly names Tester; PASS does not prove tests ran
- evidence identity: retain the actual Implementer dispatch/result identifier and changed artifact paths

Output:

```json
{
  "next_role": "Tester",
  "reason": "The actual Implementer handoff explicitly declares Tester for assigned verification.",
  "stop_condition": "none"
}
```

Only after real Tester execution returns a separate payload, use the second input:

- `result_role`: `Tester`
- `verdict`: `PASS`
- bounded evidence: actual assigned test results and retained evidence paths
- `declared_next_role`: `Reviewer`
- declaration source: the actual Tester handoff explicitly names independent Reviewer
- evidence identity: retain the actual Tester dispatch/result identifier; do not manufacture it from the first PASS

Second output:

```json
{
  "next_role": "Reviewer",
  "reason": "The actual Tester result explicitly declares independent Reviewer with test evidence.",
  "stop_condition": "none"
}
```

These illustrate payload shapes, not execution records or invented dispatch
identifiers. Real routing requires each actual returned payload.

## Negative: invented verdict

Bad input:

- `result_role`: `Implementer`
- `verdict`: `probably_ok`

Required output:

```json
{
  "next_role": "stop",
  "reason": "The result does not use a frozen verdict value.",
  "stop_condition": "invalid verdict"
}
```

## Negative: missing evidence owner

Input:

- `result_role`: `Reviewer`
- `verdict`: `MISSING_EVIDENCE`
- missing evidence owner: unknown

Output:

```json
{
  "next_role": "stop",
  "reason": "Missing evidence cannot be routed without a bounded responsible role.",
  "stop_condition": "missing evidence owner unknown"
}
```

## Negative: runtime-expansion blocker

Input:

- `result_role`: `Planner`
- `verdict`: `BLOCKED`
- blocker: runtime orchestration semantics required

Output:

```json
{
  "next_role": "stop",
  "reason": "The result expands beyond the bounded Observer baseline.",
  "stop_condition": "runtime orchestration semantics required"
}
```

## Native plan approval

A real Plan-Reviewer dispatch returns the fixed JSON verdict approved, bound to
its actual parent task and reviewed snapshot/version; its actual returned actor
is distinct from the identified plan author. With
an explicitly declared Implementer next handoff, return next_role Implementer;
without a declared next Implementer handoff, stop. A declared Tester, Reviewer
or any other actor also stops: approval terminates planning and hands execution
to Implementer only. Code-Implementer is its permitted alias. Keep approved
native, do not map to PASS. Ordinary PASS still uses its explicitly declared
permitted next role.

## Native plan rework and role incompatibility

A genuine Plan-Reviewer needs-rework result with the same actual linkage,
version binding and distinct-author preflight routes to Plan-Creator. Implementer approved is
role-incompatible and stops. Plan-Reviewer PASS is also incompatible and stops.
Unknown verdicts, BLOCKED and MISSING_EVIDENCE without a known allowed owner stop.
PATCH_REQUIRED and REPLAN_REQUIRED are compatible only with independent
Reviewer / normalized Code-Reviewer. Implementer, Code-Implementer, Tester,
Planner, Plan-Creator and Explorer emitting either review verdict stop.

## Hard preflight stop: missing provenance or independence

Reviewer/Code-Reviewer/Plan-Reviewer plus any role-compatible verdict is not
identity proof. This includes PASS, approved, needs-rework and evidence/stop
verdicts, as well as PATCH_REQUIRED/REPLAN_REQUIRED.
Missing actual dispatch/result linkage, returned actor, actual author or identical
author/Reviewer returns next_role stop with that exact gap as stop_condition.
These hard inputs never use soft-fail routing. Alias normalization proves no
independence; positive outputs apply only after these real inputs pass.

## Independent Reviewer PASS

Illustrative input: actual Reviewer PASS, genuine parent-task/returned-result
correlation and reviewed artifact version, identified actual author distinct
from the returned Reviewer, and explicitly declared next permitted role (or
stop). Only after these hard inputs pass may ordinary PASS routing apply.
Missing author, same author or stale/unlinked version stops for any review-role
verdict; do not invent approval, actor identifiers or a real dispatch.
