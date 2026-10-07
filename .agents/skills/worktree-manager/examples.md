# worktree-manager examples

Use this file for concrete lifecycle scenarios. It expands the concise `SKILL.md`
examples without redefining the core contract.

All execution examples below require actual Default mode, exact existing
operation/selector/path/branch authorization and all original safety checks.
They are illustrative, not evidence that these paths were created. In Plan Mode
(or unknown mode), give conversation planning/inspection only with intended
paths and a stop; do not run mutations or claim creation/existence/`cd`.

## Scenario 1: create a managed worktree

User intent:
- "Create a worktree for the `worktree-skill` topic from the current repo."

Correct handling:
- validate that the current directory belongs to the target Git repository
- resolve absolute Git top-level; from `/workspace/agent-skills` or its nested
  child, construct the same managed sibling path such as `/workspace/agent-skills.worktrees/agent-20260507-worktree-skill`
- create the intended branch/worktree only in actual Default under exact existing
  authorization, after confirming all safety conditions and no branch collision
- return the path, branch, and immediate next step

Example output after actual authorized creation and verification:

```yaml
create_result:
  path: "/workspace/agent-skills.worktrees/agent-20260507-worktree-skill"
  branch: "feat/andrew/worktree-skill"
  next_step: "cd /workspace/agent-skills.worktrees/agent-20260507-worktree-skill && continue work inside this worktree"
notes:
  - "Coordinate planner / observer owned files if multiple worktrees may touch them."
```

## Scenario 2: branch collision during create

User intent:
- "Create a worktree for `feat/andrew/worktree-skill`."

Observed condition:
- the preferred branch already exists

Correct handling:
- stop before creating the worktree
- ask whether to reuse the existing branch lineage or choose a new branch name
- do not silently attach a new worktree to the existing branch

Incorrect handling:
- automatically create the worktree on the existing branch without an explicit reuse decision

## Scenario 3: clean managed worktree ready for release

User intent:
- "Release this completed worktree."

Observed condition:
- managed path
- clean working tree
- no untracked files
- merged PR or explicit statement that the task is abandoned and does not need merge

Correct handling:
- produce `release_evidence`
- keep `destructive_action_allowed: false`
- recommend `release` as response-only guidance, with no automatic metadata write
- explain that release removes the worktree from the active working set but does not imply deletion

Example output:

```yaml
release_evidence:
  task_status: completed
  worktree_clean: true
  untracked_files: false
  branch_status: merged
  pr_status: merged
  push_status: pushed
  user_intent: release
  destructive_action_allowed: false
  evidence_notes:
    - "Task merged; safe to offboard from active working set."
recommendation: release
reason: "Managed worktree is clean and the lineage is complete."
next safe action: "Retain this release recommendation in the conversation. Persist offboarding metadata only in Default with exact existing authorization; remove later only on an explicitly authorized safe remove path."
```

## Scenario 4: dirty or untracked worktree

User intent:
- "Release this worktree."

Observed condition:
- modified tracked files or untracked files are present

Correct handling:
- return `needs-human-decision`
- explain that the current state could still matter
- recommend reviewing, committing, shelving, or explicitly abandoning the remaining state before any release or remove decision

Incorrect handling:
- release or remove automatically because the task sounds finished

## Scenario 5: unmanaged worktree

User intent:
- "Clean up `/some/other/path/my-worktree`."

Observed condition:
- the path does not match `<resolved-git-root-parent>/<repo-name>.worktrees/<prefix>-YYYYMMDD-<worktree-name>`

Correct handling:
- classify it as unmanaged
- allow inspection only by default
- report status, recommendation, reason, and next safe action
- if the human later asks for destructive cleanup, restate that the worktree is unmanaged and require the full remove gate

Example output:

```yaml
path: "/some/other/path/my-worktree"
branch: "unknown"
status: "unmanaged"
dirty state: "unknown"
recommendation: "needs-human-decision"
reason: "Path is outside the managed worktree family, so ownership cannot be assumed."
next safe action: "Inspect the worktree manually and obtain explicit destructive approval before any remove path."
```

## Scenario 6: stale registration during get-worktree

User intent:
- "Get worktree status."

Observed condition:
- `git worktree list` still reports a worktree, but the path no longer exists

Correct handling:
- report the worktree as a stale registration
- set the recommendation to `prune-candidate`
- explain that the registration appears stale
- do not auto-prune during `get-worktree`

## Scenario 7: explicit destructive remove confirmation

User intent:
- "Remove this worktree. Destructive cleanup is approved."

Observed condition:
- selector resolves clearly
- clean state
- no untracked files
- no lock or detached / unknown branch state

Correct handling:
- restate that `remove worktree` is destructive
- confirm the explicit human approval is present
- proceed only if the latest safety checks still pass

Incorrect handling:
- treat an earlier release request as implied permission to delete now

## Scenario 8: request outside the repository

User intent:
- "Create a worktree here."

Observed condition:
- current directory is not the intended Git repository

Correct handling:
- return `BLOCKED`
- tell the operator to switch to the correct repository first
- make no worktree mutation

## TC-AGENT-SKILLS-001 fixture-only authorization

The user's authorization to execute this TestCase includes removing only a
worktree created in that same run inside an independently initialized disposable
Git repository. It is not a blanket exception for ordinary or existing worktrees.
Record the original primary repo, initialization commit, exact created path,
attached branch and creation command; all must match the removal selector.
Verify canonical managed sibling path, non-primary worktree, clean tracked
state, no untracked files, no lock/detached/ambiguous branch, no unique commits
or refs requiring preservation and no unknown state. Fixture lineage is explicitly
abandoned for this test; release remains non-destructive with
`destructive_action_allowed: false`. For remove, cite the existing TestCase
user authorization and exact selector rather than ask again. No --force.

Missing authorization, selector outside this run's created fixture, unknown
ownership, dirty/untracked/locked state, branch collision or unique commits/refs
stops for human decision without deletion. Existing ordinary worktrees still
require explicit human destructive approval and all original safety gates.
The feature worktree for this topic is not a fixture and must remain for human
review. Do not clean it up. Evidence must precede any fixture removal.

## Nested invocation and symlink refusal

Calling create from `/workspace/agent-skills/src/nested` anchors at the resolved
Git root `/workspace/agent-skills`, so the same example selector returns
`/workspace/agent-skills.worktrees/agent-20260507-worktree-skill`. After actual authorized Default creation the returned
cd is absolute; Plan/unknown-mode guidance reports an intended path and stop only. If a candidate family/destination symlink resolves inside
`/workspace/agent-skills`, stop before mutation. These are illustrative paths,
not claims of actually created worktrees. Collisions and destructive gates remain.

## Mode boundary example

A Plan Mode create request returns the intended managed path and explains that
creation waits for actual Default mode and exact authority. It does not run
`git worktree add`, create a branch/directory/registration, or offer `cd` as if
the path exists. A Plan/unknown-mode remove request returns inspection/guidance
without deletion; release evidence remains in the conversation. An actual
Default request with missing authorization also stops. Existing exact Default
authorization is reused once all original gates pass, without asking again.
Controlled mode inputs test this policy only, not actual Plan-engine execution.
