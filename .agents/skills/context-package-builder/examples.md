# context-package-builder examples

## Positive: bounded implementation package

Output:

```json
{
  "target_role": "Implementer",
  "task_slice": "Implement the accepted Feature 1 artifact set within the frozen write set.",
  "frozen_inputs": [
    "accepted topic requirements artifact",
    "accepted topic technical specification artifact",
    "plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md"
  ],
  "constraints": [
    "Write only the bounded artifact set.",
    "Stop if runtime semantics or registry behavior becomes necessary."
  ],
  "evidence": [
    "topic-local step artifact says implementation is the current workflow phase"
  ],
  "unknowns": []
}
```

Why it is valid:

- one target role
- one bounded task slice
- one bounded workflow-derived fact
- no unrelated history

## Positive: reviewer package

Output:

```json
{
  "target_role": "Reviewer",
  "task_slice": "Review whether the bounded Feature 1 artifact set matches the frozen contract.",
  "frozen_inputs": [
    "accepted topic requirements artifact",
    "accepted topic technical specification artifact"
  ],
  "constraints": [
    "Judge only the bounded write set.",
    "Do not broaden into runtime semantics."
  ],
  "evidence": [
    "the implementation write set is complete"
  ],
  "unknowns": [
    "human review timing is not yet available"
  ]
}
```

## Negative: full conversation dump

Bad output:

```json
{
  "target_role": "Implementer",
  "task_slice": "everything we have discussed so far",
  "frozen_inputs": [
    "entire chat transcript"
  ],
  "constraints": [],
  "evidence": [
    "all historical discussion",
    "several unrelated roadmap notes"
  ],
  "unknowns": []
}
```

Why it is invalid:

- uses whole conversation history
- mixes multiple tasks and roadmap material
- abandons bounded handoff shape

## Negative: registry and path hints

Bad output:

```json
{
  "target_role": "Reviewer",
  "task_slice": "review the patch",
  "frozen_inputs": [
    "accepted topic technical specification artifact"
  ],
  "constraints": [
    "launch agent id reviewer-17 from registry observer/default"
  ],
  "evidence": [
    "prefer `.github/agents/...` because that file probably maps to the role"
  ],
  "unknowns": []
}
```

Why it is invalid:

- includes registry identifiers
- includes role-to-file lookup hints
- treats compatibility surfaces as operational routing data

## Stop: real dispatch unavailable

Required result:

No context package is produced. The flow stops.

Why it must stop:

- no real dispatch target is available
- producing the package would require runtime semantics or workflow binding
- the skill may not invent a pseudo-handoff payload just to keep the flow moving
