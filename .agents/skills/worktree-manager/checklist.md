# worktree-manager checklist

Use this checklist for repeatable safety checks. It is operational, not a policy
summary.

## Mode and authorization checks

- [ ] Actual active engine mode verified; controlled mode labels are policy inputs only.
- [ ] Plan Mode or unknown mode returns conversation planning/inspection only,
  with no branch/ref/directory/registration/add/remove/offboarding-metadata write.
- [ ] Default mutations have exact existing operation/selector/path/branch authority
  and every original safety gate; do not request permission again when already given.
- [ ] Planned-only paths are intended, with no existence/created/`cd` claim.

## Verified primary root and caller context

Retain the actual caller cwd and its canonical current-worktree top-level
separately. show-toplevel identifies that caller's worktree, not the primary.
Read git rev-parse --path-format=absolute --git-common-dir and git worktree list
--porcelain -z without mutations. Parse NUL-terminated attributes/records, never
split paths on whitespace or assume cwd/common-dir.parent is primary. The first
inventory entry identifies the main worktree; bare entries are unsupported.
Resolve its path aliases and verify it exists, is a non-bare working tree, its
own show-toplevel equals that candidate and its absolute common Git directory
matches the caller's. Confirm caller and selected worktree registration in the
same inventory/common metadata. Missing/stale/ambiguous/inconsistent primary,
bare repository or unreadable metadata is BLOCKED before any mutation.
Use that verified primary as resolved_root for all sibling family/path checks:
primary.parent / (primary.name + ".worktrees"). Primary, linked and nested caller
contexts must derive the same family. Preserve caller identity in evidence;
never derive caller-feature.worktrees. Resolve final symlinks and preserve all
original mode, exact-authority, containment, selector, collision and removal
gates; this inspection grants no creation/removal authority.
Git references: [worktree list/porcelain](https://git-scm.com/docs/git-worktree#_list_output_format),
[common Git directory](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---git-common-dir).

## Pre-create checks

- [ ] Current directory resolves to the intended Git repository root or a child of it.
- [ ] Requested operation is clearly `create`, not `get-worktree`, `release worktree`, or `remove worktree`.
- [ ] Managed path follows `<resolved-git-root-parent>/<repo-name>.worktrees/<prefix>-YYYYMMDD-<worktree-name>`.
- [ ] Caller root retained separately; primary verified from first non-bare NUL-safe porcelain record plus matching absolute common Git metadata and primary show-toplevel, never caller show-toplevel alone.
- [ ] Bare/stale/ambiguous/inconsistent primary blocks; spaces/aliases preserve exact paths.
- [ ] Primary/linked/nested caller contexts derive the same primary-root sibling family.
- [ ] Sibling family computed from verified primary root.parent/root.name, not cwd or linked root.
- [ ] Final destination resolved, outside Git root and within intended family;
  symlink aliases into the Git root block before any mutation.
- [ ] After actual authorized Default creation, absolute create_result path / cd target is identical from root/child cwd; guidance-only output never claims creation.
- [ ] Managed path stays outside the repository root.
- [ ] Preferred branch name is known.
- [ ] If the preferred branch name already exists, the human has made an explicit reuse-or-rename decision.
- [ ] Target path does not already exist as an unrelated directory or conflicting worktree.
- [ ] Shared planning or governance files that may be edited across worktrees are called out with a coordination warning.
- [ ] Actual create_result includes `path`, `branch`, and `next_step` after creation is verified; planned-only output labels intended path and the stop.

## Pre-release checks

- [ ] Requested operation is clearly `release worktree`.
- [ ] Target worktree selector resolves to the intended worktree.
- [ ] Worktree is managed, or the operator has been told that unmanaged worktrees are inspect-only by default.
- [ ] `release_evidence.task_status` is filled.
- [ ] `release_evidence.worktree_clean` is filled and currently `true`.
- [ ] `release_evidence.untracked_files` is filled and currently `false`.
- [ ] `release_evidence.branch_status`, `pr_status`, and `push_status` are filled or explicitly marked `unknown`.
- [ ] Lineage is merged, or the human explicitly states the task is abandoned / does not need merge.
- [ ] `release_evidence.user_intent` is `release`.
- [ ] `release_evidence.destructive_action_allowed` remains `false`.
- [ ] Output explains that release does not imply deletion or a Git-state change.
- [ ] Evidence is response-only; Plan/unknown mode never persists offboarding metadata,
  and any Default metadata write requires its exact existing authorization.

## Pre-remove checks

- [ ] Requested operation is clearly `remove worktree`.
- [ ] Explicit human destructive approval is already present for this exact selector/operation in the session; no repeated request if authorized.
- [ ] Target worktree selector resolves to exactly one worktree.
- [ ] Latest state check shows no tracked changes.
- [ ] Latest state check shows no untracked files.
- [ ] Latest state check shows no unpushed commits, detached HEAD, unknown branch state, or lock that would require human review.
- [ ] The request does not rely on a previous `release worktree` as implied delete permission.
- [ ] If the worktree is unmanaged, the response restates that ownership is not assumed and uses the same destructive gate.

## Unmanaged-worktree checks

- [ ] Path classification is based on canonical managed-path family first.
- [ ] Unmanaged worktrees are limited to inspection and status reporting by default.
- [ ] No automatic release, remove, delete, prune, rename, or branch deletion is implied for unmanaged paths.
- [ ] Recommendation and next safe action tell the operator what human decision is still required.

## Non-repo and ambiguous-state checks

- [ ] If repo-root validation fails, the result is `BLOCKED` and no mutation occurs.
- [ ] If the user says "clean up" or similar ambiguous wording, the response asks whether they mean `release worktree` or `remove worktree`.
- [ ] Dirty, untracked, unpushed, detached, locked, or unknown states route to `needs-human-decision`.
- [ ] Missing-path-but-registered worktrees route to `prune-candidate` and are not auto-pruned.
- [ ] Every `get-worktree` entry includes `path`, `branch`, `status`, `dirty state`, `recommendation`, `reason`, and `next safe action`.

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
