# handoff-routing-policy examples

## Positive: patch required

Input:

- `result_role`: `Reviewer`
- `verdict`: `PATCH_REQUIRED`
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
- blocker: the required change would expand outside the frozen write set

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

A real Plan-Reviewer dispatch returns the fixed JSON verdict approved. With
an explicitly declared Implementer next handoff, return next_role Implementer;
without a declared next Implementer handoff, stop. A declared Tester, Reviewer
or any other actor also stops: approval terminates planning and hands execution
to Implementer only. Code-Implementer is its permitted alias. Keep approved
native, do not map to PASS. Ordinary PASS still uses its explicitly declared
permitted next role.

## Native plan rework and role incompatibility

Plan-Reviewer needs-rework routes to Plan-Creator. Implementer approved is
role-incompatible and stops. Plan-Reviewer PASS is also incompatible and stops.
Unknown verdicts, BLOCKED and MISSING_EVIDENCE without a known allowed owner stop.
PATCH_REQUIRED and REPLAN_REQUIRED are compatible only with independent
Reviewer / normalized Code-Reviewer. Implementer, Code-Implementer, Tester,
Planner, Plan-Creator and Explorer emitting either review verdict stop.
