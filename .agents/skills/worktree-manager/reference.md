# worktree-manager reference

Use this file for stable operational details that would make `SKILL.md` too dense.

## Actual mode and mutation authority

Verify actual active engine mode before any lifecycle mutation. Plan Mode gives
conversation planning/inspection only; no add/remove, branch/ref, directory,
registration or offboarding-metadata write. Unknown/unverified mode supplies no
mutation permission. Read-only inspection stays available. Default mutation
requires exact existing operation/selector/path/branch authorization plus all
original safety checks; do not request the same permission again. Controlled
mode labels are policy evidence, never actual engine proof. Planned-only output
labels intended paths and the stop, with no created/existence/`cd` claim.

Release evidence is response-only guidance. It neither deletes a worktree nor
changes Git state, and cannot silently persist metadata in Plan/unknown mode.
A Default offboarding write requires exact already-authorized path/action.

## Lifecycle terminology

- `create`: create a managed worktree and its intended branch lineage at the canonical path.
- `get-worktree`: inspect worktree state and return a structured recommendation.
- `release worktree`: non-destructive offboarding from the active working set.
- `remove worktree`: destructive removal of the worktree directory and Git registration after an explicit human gate.

Never collapse `release worktree` and `remove worktree` into one action.

## Selector notes

A selector should resolve to one worktree without guessing. Prefer, in order:

1. explicit path
2. explicit branch name
3. explicit worktree name / slug when it maps to one known worktree

If a selector matches more than one candidate or cannot be verified, stop at
inspection or ask for clarification instead of mutating state.

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

## Managed-path policy

Managed worktrees use this path family:

`<resolved-git-root-parent>/<repo-name>.worktrees/<prefix>-YYYYMMDD-<worktree-name>`

Rules:
- Derive and verify the primary root with the common-metadata/porcelain checks above; retain caller show-toplevel separately.
- Compute the sibling family from primary.parent / (primary.name + ".worktrees");
  never use invocation cwd to interpret `..`, even from a nested child.
- Resolve the final destination and verify it is outside that Git root, within
  the intended managed family, with no symlink alias into the root.
- After actual verified Default creation, return absolute path / cd targets.
  Planned-only output gives an intended absolute path and mode/authorization stop.
- managed worktrees live outside the repository root
- default `<prefix>` is `agent`
- a human may explicitly override the prefix
- path policy decides managed vs unmanaged ownership in v1
- metadata or plan context may add notes, but they do not replace path policy

Examples:
- managed: `/workspace/agent-skills.worktrees/agent-20260507-worktree-skill`
- unmanaged: `../scratch/worktree-skill`
- unmanaged: `.github/worktrees/worktree-skill`

## Inspect output contract

Every reported worktree must include:

```yaml
path: "<absolute or repo-relative path>"
branch: "<branch-name|detached|unknown>"
status: "<summary status>"
dirty state: "clean|dirty|untracked|dirty+untracked|unknown"
recommendation: "keep|release|remove|needs-human-decision|prune-candidate"
reason: "<why this recommendation fits the observed state>"
next safe action: "<concrete next step>"
```

Notes:
- `status` is a concise summary of the current condition; it should not replace the `reason`
- `dirty state` must stay explicit even when the recommendation is already `needs-human-decision`
- `prune-candidate` is reserved for missing-path-but-still-registered worktrees

## Recommendation matrix detail

| Condition | Recommendation | Required reasoning |
| --- | --- | --- |
| clean + branch still active + task ongoing | `keep` | active workspace still in use |
| clean + task done + merged or explicitly abandoned | `release` | safe to leave active working set, not yet delete |
| clean + already released or no longer needed + destructive approval handled separately | `remove` | destructive cleanup may be appropriate only on the explicit remove path |
| dirty tracked changes | `needs-human-decision` | tracked edits may still matter |
| untracked files | `needs-human-decision` | local state may still matter |
| unpushed commits | `needs-human-decision` | unpublished commits may be lost |
| detached HEAD or branch not found | `needs-human-decision` | lineage is ambiguous |
| unmanaged path | `needs-human-decision` | ownership cannot be assumed |
| missing path but still registered | `prune-candidate` | registration appears stale |
| locked worktree | `needs-human-decision` | another process or policy may own the state |

## Release evidence schema

Use this exact field set before recommending `release worktree`:

```yaml
release_evidence:
  task_status: completed | paused | abandoned | unknown
  worktree_clean: true | false | unknown
  untracked_files: true | false | unknown
  branch_status: merged | unmerged | no_branch | unknown
  pr_status: merged | closed | open | none | unknown
  push_status: pushed | unpushed | no_remote | unknown
  user_intent: release | remove | keep | unknown
  destructive_action_allowed: true | false
  evidence_notes:
    - "<short note>"
```

Minimum release gate:
- `worktree_clean: true`
- `untracked_files: false`
- `branch_status: merged` or `pr_status: merged`, unless the human explicitly says the task is abandoned or does not need merge
- `destructive_action_allowed: false` by default

## Safety routing notes

- Outside a valid Git repository: `BLOCKED`
- Branch collision during create: stop for explicit reuse-or-rename decision
- Dirty, untracked, unpushed, detached, locked, or unknown state: `needs-human-decision`
- Shared planning or governance files across worktrees: surface a planner / observer coordination warning
- Stale registration during `get-worktree`: `prune-candidate`, never auto-prune as part of inspection
- Unmanaged worktrees: inspect-only by default; destructive paths require explicit human authorization plus the full remove gate

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
