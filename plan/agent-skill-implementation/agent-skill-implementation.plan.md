# agent-skill-implementation

Recorded from the user-approved conversation plan, without reopening its locked
scope. The user subsequently authorized feature-worktree implementation and
commit-by-topic -> push -> Draft PR -> human review. Those delivery actions
supersede the earlier local-only delivery stop for this topic only; they do not
make publication automatic for installed skills. Actual Tester six-group PASS
and independent Reviewer `/root/explorer` overall bounded PASS now have external
evidence; this recorded plan itself is not the approval or test evidence. The
final documentation delta still requires bounded review before publication.

Optional analysis warning: analysis/agent-skill-implementation/requirements.md
and analysis/agent-skill-implementation/technical-spec.md are absent. The approved
conversation plan is the recorded baseline; no alternate requirements are added.

## Goal / Outcome

- **Goal**: Install all 10 bounded development skills and establish actual
  discovery, intended-use and required-handoff evidence under one TestCase.
- **Non-Goal**: Implement the Task product, a complete publishing workflow,
  an 11th skill, all profiles or a guarantee for arbitrary models/environments.

## Scope

- **In-Scope**: Complete pinned skill directories, necessary paths/roles/Base
  profile adaptations, two minimal shared contracts, README navigation,
  provenance, one TestCase, stdlib tracker tests and independent verification.
- **Out-Of-Scope**: Global installs, source repo changes, Task baseline changes,
  real worktree cleanup, merge/release or additional skill/profile support.
  The later user authorization permits this topic's feature creation and
  commit/push/Draft PR only, followed by human review.

## Locked Decisions

- Source commit: 60b3b5b77515c354ed355c1adb28a8ed349dda67 from a129924/agent-skills.
- Exactly 10 directories / 46 pinned tracked files; full companion files retained.
  Installation-local adaptations are documented in the complete manifest.
- Seven permitted roles with Code aliases; independent reviews; native
  approved/needs-rework JSON; no simulated dispatch or claimed gate evidence.
- base-plan is supported; both source specialized profiles block preflight.
- Tracker Python >=3.11, stdlib, unchanged runtime semantics; installed script
  path and target-root cwd, no source checkout dependency during use.
- Stable-library intent absent; README navigation is not promotion; no VERSION,
  registry, publishing library, tag or release dependency.
- Branch: chore/a129924/agent-skill-implementation.
- Frozen selector: topic=agent-skill-implementation;
  branch=chore/a129924/agent-skill-implementation;
  managed-path-intent=/Users/andrew/code/plugins/codex-task-workflow.worktrees/agent-20261005-agent-skill-implementation;
  primary-worktree=false.
- The actual feature worktree is retained for human review. Disposable fixture
  cleanup is only the exact same-run TestCase fixture with preserved evidence.

## Boundaries / Exclusions

- **ReadOnly**: GOAL.md, docs/task-workflow.baseline.md, source checkout,
  global skills and every repo file outside the enumerated paths.
- **Modify**: README.md navigation only; installed-directory adaptations are
  newly Written files, not edits to the source checkout.
- **Deleted**: No repository files. Test cleanup may remove only independently
  created disposable fixtures after exact-selector safety verification.
- Implement exclusively in the selected feature worktree, never the dev
  worktree. Observer dispatches; Implementer writes; Tester verifies;
  independent Reviewer judges implementation; human handles merge decision.
- Every role obeys current execution mode and authorized write sets. Plan Mode
  forbids implementation/commit/push/PR for every role.

## Status / Allowed Transitions

- **Current**: approved (the conversation planning baseline accepted by user;
  this file records that baseline, not a new independent reviewer verdict).
- **Allowed next planning transitions**: none; approved ends planning.
- **Next actor**: Implementer.
- **Stage-local action**: Complete bounded installation and verification handoff.
- Canonical planning transitions retained: planned -> creator-in-progress ->
  review-ready -> reviewer-in-progress -> approved or needs-rework;
  needs-rework -> creator-in-progress.
- Execution: Implementer -> Tester -> independent Reviewer. PATCH_REQUIRED
  returns to Implementer; REPLAN_REQUIRED to Plan-Creator; missing evidence to
  its known owner or stop; BLOCKED/unknown/incompatible result stops.
- On Reviewer PASS, separately authorized Implementer topic commit/push/Draft
  PR may proceed, then stop at human review. No merge/release/cleanup route.

## Artifact Paths

- **Written**: The exact bounded outputs below; each imported directory is
  constrained to its pinned tracked manifest in the installation document.

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Planning skill | .agents/skills/plan-creator/ | Implementer | Complete pinned directory plus local adaptation |
| Planning review | .agents/skills/plan-reviewer/ | Implementer | Complete pinned directory plus local adaptation |
| Step creation | .agents/skills/step-creator/ | Implementer | Complete pinned directory plus Base-only adaptation |
| Tracker | .agents/skills/plan-step-tracker/ | Implementer | Unchanged Python runtime and installed-path guidance |
| Business analysis | .agents/skills/business-intent-alignment/ | Implementer | Complete unchanged pinned directory |
| Technical translation | .agents/skills/business-to-technical-translation/ | Implementer | Complete unchanged pinned directory |
| Dispatch | .agents/skills/subagent-dispatch-policy/ | Implementer | Seven bounded roles and real dispatch |
| Context | .agents/skills/context-package-builder/ | Implementer | Bounded real handoff package |
| Routing | .agents/skills/handoff-routing-policy/ | Implementer | Native verdict routing and hard stops |
| Worktree | .agents/skills/worktree-manager/ | Implementer | Safe lifecycle and fixture-only test authorization |
| Development workflow | plan/agent-handoff-workflow.md | Implementer | Minimal approved local workflow |
| Shared plan contract | plan/topic-plan-contract.md | Implementer | Source 11-section fallback and JSON schema |
| Topic record | plan/agent-skill-implementation/agent-skill-implementation.plan.md | Plan-Creator | Approved conversation contract recorded by Implementer |
| Installation provenance | docs/agent-skills-installation.md | Implementer | Source manifest, limitations and evidence status |
| TestCase | docs/testcases/TC-AGENT-SKILLS-001.md | Implementer | One case with six verification groups |
| CLI acceptance harness | tests/test_agent_skills.py | Implementer | Stdlib observable CLI behavior |
| Navigation modification | README.md | Implementer | Development-tool entry only |

No VERSION, .github configuration, hooks or product files are added. External
verification artifacts live under /private/tmp/agent-skill-implementation-review/
and do not enlarge the repo write set. Path drift stops for bounded plan review.

## Implementation Steps

1. Import all 46 tracked files from the pinned 10 source directories; preserve
   provenance and leave source/global skills untouched.
2. Apply only the locked local path, role, native JSON, Base-only lifecycle and
   fixture-authorized worktree adaptations, synchronizing all companion text.
3. Add the two minimal development contracts without changing shared mandatory
   section count, Task authority or source tracker runtime behavior.
4. Record this approved topic contract, install provenance, complete adaptation
   manifest, TestCase procedure, stdlib harness and README navigation.
5. Return the bounded diff and actual self-check evidence for Tester and
   independent Reviewer, preserving pending status for unevaluated prompt use.

## Validation / Acceptance Checks

- **TestCase**: TC-AGENT-SKILLS-001. Six groups: real fresh-session discovery,
  analysis artifacts plus review, planning/Base/negative cases, actual separated
  workflow handoffs/native routes, five tracker operations, disposable worktree
  lifecycle/refusal cases.
- Actual successful use and independent evidence are required; no copied files,
  manual skill reads, simulated transcripts or marker checks certify prompt skills.
- Tracker distinguishes implementation completion from pending lifecycle,
  lowercase [x] remains pending with warning, missing/empty/duplicate sections
  fail only the implementation completion operation while other behavior stays.
- Source manifest exact; unchanged runtime and companions byte-for-byte;
  adapters reviewed; product ReadOnly hashes unchanged; no unapproved paths.
- No all-skills-usable claim while any group is pending, blocked or unverified.

## Reviewer Handoff

The following object declares the independent output schema only. It is not a
completed review result or approval authored by Implementer.

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {"ADDRESS": [], "DISCUSS": [], "SKIP": []}
}
```

## Post-merge / release actions

None. Stop at human review after the separately authorized topic commit, push
and Draft PR. Retain the topic feature worktree; no automatic merge, release,
tag, branch deletion or cleanup. PR Lens runs locally outside the repo; graphify
uses existing graph navigation or targeted source fallback, not an implicit build.

## Open Questions / Unresolved Items

No unresolved scope decisions. Actual Tester `/root/tester` six-group PASS and
independent Reviewer `/root/explorer` overall bounded PASS are recorded in
[test-report.json](/private/tmp/agent-skill-implementation-review/test-report.json)
and [final-review.json](/private/tmp/agent-skill-implementation-review/code-review/final-review.json),
with readable [test report](/private/tmp/agent-skill-implementation-review/test-report.md)
and [final review](/private/tmp/agent-skill-implementation-review/code-review/final-review.md).
This establishes the ten installed skills' bounded supported uses in the observed
macOS/Codex/Python >=3.11/Git fixture environment, Base profile only. Failed CLI
attempts are retained and excluded from successful counts; current hashes cannot
independently reconstruct the historical analysis freeze sequence. Source
LICENSE/COPYING absence and optional pytest not run remain documented limits.
No universal guarantee, Task product implementation, publication or human-review
approval is implied. The final status-documentation delta awaits bounded
independent checking, then the separately authorized topic publication handoff
stops at human review and preserves the actual feature worktree.
