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

## Positive: pass then review

Input:

- `result_role`: `Implementer`
- `verdict`: `PASS`
- bounded evidence: implementation for the current slice is complete and needs an independent check
- `declared_next_role`: `Reviewer`
- declaration source: the actual returned handoff payload explicitly names independent Reviewer as the next bounded owner; this is supplied input, not inferred from PASS

Output:

```json
{
  "next_role": "Reviewer",
  "reason": "The actual handoff explicitly declares Reviewer as the next bounded role after PASS.",
  "stop_condition": "none"
}
```

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
without a declared next handoff, stop. Keep approved native, do not map to PASS.

## Native plan rework and role incompatibility

Plan-Reviewer needs-rework routes to Plan-Creator. Implementer approved is
role-incompatible and stops. Plan-Reviewer PASS is also incompatible and stops.
Unknown verdicts, BLOCKED and MISSING_EVIDENCE without a known allowed owner stop.
