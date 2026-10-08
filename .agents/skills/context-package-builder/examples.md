# context-package-builder examples

The positive paths below are exact illustrative paths for one topic, not a
claim these files exist. Real handoff verifies supplied exact paths are readable;
missing required input is recorded and stops the package. No example grants
permission or manufactures artifacts/dispatch.

## Positive: bounded implementation package

Output:

```json
{
  "target_role": "Implementer",
  "task_slice": "Implement the accepted Feature 1 artifact set within the frozen write set.",
  "frozen_inputs": [
    "analysis/observer-dispatcher-canonical-baseline/requirements.md",
    "analysis/observer-dispatcher-canonical-baseline/technical-spec.md",
    "plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md"
  ],
  "constraints": [
    "Actual mode: Default, illustrative only; verify the real engine mode.",
    "Selected owned feature: /example/project.worktrees/agent-20261007-observer-dispatcher-canonical-baseline; verify actual ownership/selection.",
    "Exact authorized Written: .agents/skills/example/SKILL.md, owned by Implementer in the selected feature; no other file/temp authority is implied.",
    "ReadOnly: analysis/observer-dispatcher-canonical-baseline/requirements.md, analysis/observer-dispatcher-canonical-baseline/technical-spec.md, plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md, plan/agent-handoff-workflow.md, plan/topic-plan-contract.md, GOAL.md, docs/task-workflow.baseline.md, all other feature paths, dev/source/global.",
    "Stop after bounded implementation handoff to Tester then independent Reviewer; no commit/push/PR, merge/release or cleanup authority.",
    "Missing/ambiguous actual mode/root/exact path authority stops packaging before writes; runtime or registry expansion also stops."
  ],
  "evidence": [
    "plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md: verify actual approved status and exact owner/action; illustrative, not issued approval"
  ],
  "unknowns": []
}
```

Why it is valid:

- one target role
- one bounded task slice
- concrete illustrative mode, selected-root, write/read-only ownership and stop boundaries
- no unrelated history

These strings confer no authority or existence. Real Implementer packages
verify actual mode, selected owned feature, exact existing final/necessary temp
write authority, readable frozen inputs, read-only sets and explicit Tester/
Reviewer stop. Missing required boundaries stops packaging before mutation.
Actual Default is distinct from controlled Plan policy; Plan permits no writes.

## Positive: reviewer package

Output:

```json
{
  "target_role": "Reviewer",
  "task_slice": "Review whether the bounded Feature 1 artifact set matches the frozen contract.",
  "frozen_inputs": [
    "analysis/observer-dispatcher-canonical-baseline/requirements.md",
    "analysis/observer-dispatcher-canonical-baseline/technical-spec.md",
    "plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md",
    ".agents/skills/example/SKILL.md",
    "artifacts/observer-dispatcher-canonical-baseline/changed-artifacts.json",
    "artifacts/observer-dispatcher-canonical-baseline/implementation.diff",
    "artifacts/observer-dispatcher-canonical-baseline/tester-result.json"
  ],
  "constraints": [
    "Actual mode: Default, illustrative only; verify the real engine mode before packaging.",
    "Selected owned feature: /example/project.worktrees/agent-20261007-observer-dispatcher-canonical-baseline; verify actual selection and ownership.",
    "Repo write set: empty. Reviewer may not modify any source, artifact, diff, test input or other repository path.",
    "External evidence output: only /example/review-evidence/feature-1-review.json if that exact external path is separately authorized; otherwise return the result in conversation without writes.",
    "ReadOnly: all frozen source, plan, changed-artifact, bounded diff and actual Tester inputs; all other feature paths, dev/source/global, Git and existing evidence.",
    "Stop after the bounded independent review result; no implementation, Git, publication, cleanup or runtime expansion authority.",
    "Missing or ambiguous actual mode, selected root, empty repo write boundary, exact external authority/read-only set or stop boundary stops packaging."
  ],
  "evidence": [
    "artifacts/observer-dispatcher-canonical-baseline/changed-artifacts.json: exact changed paths and current content hashes",
    "artifacts/observer-dispatcher-canonical-baseline/implementation.diff: current bounded diff",
    "artifacts/observer-dispatcher-canonical-baseline/tester-result.json: actual Tester identity, command/results and version binding"
  ],
  "unknowns": [
    "human review timing is not yet available"
  ]
}
```

These exact paths are illustrative, not existing artifacts or successful tests.
For a real implementation Reviewer handoff, verify every required changed
artifact, bounded diff and actual Tester result is readable and current for the
same supplied revision/hash. Include bounded contents only with actual provenance.
Absent or stale required proof stops packaging; a completion assertion is not
evidence. Every real Reviewer package also verifies the concrete mode/root,
empty repo write set, full read-only set, exact separately authorized external
output (or conversation-only result) and stop boundaries above. Omitting any
required boundary stops packaging. These inputs apply to implementation Reviewer,
not every unrelated role.

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
