# Agent skills development installation

This installation is a repo-local development aid. The Task product remains
unimplemented and independent of these skills, plan files and step trackers.
GOAL.md and docs/task-workflow.baseline.md are ReadOnly product authorities.

## Source and inventory

Source: [a129924/agent-skills](https://github.com/a129924/agent-skills/tree/60b3b5b77515c354ed355c1adb28a8ed349dda67),
pinned commit `60b3b5b77515c354ed355c1adb28a8ed349dda67`. Imported exactly 10 complete tracked skill directories,
46 files; no untracked files or caches. Source checkout and global skills were
not modified. Original content for unchanged files is byte-for-byte preserved.
Adaptations are installation-local, not upstream changes.

| Skill | Supported use |
| --- | --- |
| plan-creator | Bounded 11-section local topic plan authoring |
| plan-reviewer | Independent native JSON planning-contract review |
| step-creator | Create-only explicit base-plan step tracker |
| plan-step-tracker | Five read-only CLI operations |
| business-intent-alignment | Measurable business requirements |
| business-to-technical-translation | Frozen requirements to technical spec |
| subagent-dispatch-policy | One permitted role or stop |
| context-package-builder | Minimal real bounded handoff context |
| handoff-routing-policy | Native result to one permitted route or stop |
| worktree-manager | Authorized create, inspect, non-destructive release, gated remove |

## Runtime and contracts

Load this repo's `.agents/skills/` in a new/reloaded Codex session. Real catalog
discovery must be observed; manually reading SKILL.md does not prove discovery.
Prompt skills require an agent runtime with actual separated dispatch for
multi-agent work. No hidden role simulation counts as evidence. All roles obey
active mode; Plan Mode prohibits writes for every role.

Planning uses `plan/agent-handoff-workflow.md` and `plan/topic-plan-contract.md`.
Missing contracts or required inputs stop. The local contracts keep the source
11 mandatory sections and native review JSON fields; they do not import the
source publishing library's VERSION/registry/release workflow. README navigation
alone is not stable publishing. Code aliases map to Implementer and Reviewer.

step-creator supports only base-plan from an independently approved terminal
source with []/none planning transitions, exact Implementer next actor and bounded
implementation action; all five earlier/rework states stop before any write. The
source specialized agent-skill-plan / python-implementation-plan profiles are
explicitly unsupported and stop before any write. No python-plan-authoring or
11th skill is installed. The Base lifecycle ends at local reviewable delivery;
publication needs a separate explicit authorization and retains human review.

Tracker requires Python >=3.11 and only stdlib. Use the python3 command and
run from the target repo root:

```sh
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_all <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_not_run <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_success <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_impl_steps_succeeded <topic>
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The installed tracker runtime was initially copied unchanged. The authorized
PR-comment fixes now adapt its topic/path validation, error handling and Markdown
boundaries. The source checkout and imported companion pytest tests remain
unchanged. pytest is optional for those companion tests; default Python still has no pytest.
Round3 selfcheck uses the previously authorized external pytest9.1.1 venv only;
no runtime dependency is added. The repository's acceptance harness uses unittest. Do not confuse checkbox
completion with actual artifact, approval or test evidence.

worktree-manager requires Git and exact selectors. Ordinary/existing worktree
removal requires explicit human destructive approval. Only this TestCase's
same-run disposable-repo fixture may use the already-granted test authorization,
with proof of exact creation, managed non-primary path, clean/no-untracked state,
no locks/ambiguity or commits/refs requiring preservation. The actual topic
feature worktree is retained for human review and is never a disposable fixture.

## Provenance and limitations

The pinned source root has no LICENSE or COPYING file. No license is invented;
existing source text is preserved. This is a recorded provenance limitation,
not a claim of redistribution permission.

Source-specific absolute paths are provenance only; runtime invocations use
installed entrypoints from the target repo. No global install, hooks, registry,
provider, Task runtime or third-party package dependency is added.

## Verification history and Round1 PR-fix status

At the original delivery head `2afebb1a259b163ee47d3b95c6d11ef199dc7591`,
TC-AGENT-SKILLS-001 completed all six groups with actual Tester `/root/tester`
PASS. Independent Reviewer `/root/explorer` returned overall bounded PASS on
2026-10-07, with no blocking issues. Actual discovery, ten intended uses,
independent planning review/Base step, separated dispatch/native routes, five
tracker operations and four isolated worktree lifecycle operations were reviewed.
Tracker evidence contains 5 tests / 37 installed CLI calls; worktree evidence
contains 11 refusal cases. No static file check substitutes for these exercises.

- `/private/tmp/agent-skill-implementation-review/test-report.md`
  and `/private/tmp/agent-skill-implementation-review/test-report.json`
- `/private/tmp/agent-skill-implementation-review/code-review/final-review.md`
  and `/private/tmp/agent-skill-implementation-review/code-review/final-review.json`
- [TestCase procedure](testcases/TC-AGENT-SKILLS-001.md)

The original bounded documentation closeout also received independent PASS in
`/private/tmp/agent-skill-implementation-review/code-review/doc-sync-review.json`.
These plain paths are local-session evidence only, unavailable through this PR;
no evidence is uploaded. Original PASS establishes the originally reviewed
snapshot, not the runtime and prompt fixes now being applied.

The Round1 PR-comment stage at `f0f484e27c06cb0387a48f16d712eaf5830ecea0` has actual targeted Tester `/root/tester` PASS and
independent Reviewer `/root/explorer` PASS for all 14 groups / 18 threads. The
final suite passed 12 test methods / 128 CLI calls on observed macOS,
Python3.14.0 and platform-default temporary directories. Four exact G11
continuation/sub-list repros now fail closed. Those final checks cover the last
two-file ancestry correction; the earlier 43-input replay remains versioned
to the initial fixed runtime and was not falsely relabeled or repeated.

Actual Tester policy applications checked seven routing cases, three
selection/prelaunch cases and the current-state template using unchanged
installed-byte-equal snapshots. Genuine earlier result identities were reused;
contextual/malformed inputs are controlled cases, not new role sessions or
fabricated dispatch. Forty-two captured Git fixture commands verified root/child
cwd anchoring, internal/symlink refusal and exact guarded fixture-child cleanup.

The separate current evidence is retained locally at
`/private/tmp/agent-skill-implementation-review/pr-comment-review/targeted-test-report.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review/targeted-test-report.md`, with independent review at
`/private/tmp/agent-skill-implementation-review/pr-comment-review/final-review.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review/final-review.md`. These are local-session paths,
unavailable through this PR. Original 5 tests / 37 CLI calls and 62 reviewed
initial evidence refs remain historical; they are not new-runtime proof. No
unchanged analysis/discovery/full-six-group sessions were repeated.

Original bounded use was observed in the macOS feature worktree, actual
Codex runtime and retained disposable fixtures, with Python >=3.11 and Git.
It is not a guarantee for arbitrary models, environments or unsupported profiles.
The earlier Tester index's pending overall-gate snapshot is superseded by the
separate actual final-review PASS; historical records are preserved.

Failed CLI startup/sandbox/network attempts are retained in the evidence index
and excluded from successful-use counts. The historical requirements freeze
sequence cannot be independently reconstructed from current hashes alone;
actual order reports, digests and independent content mapping remain scoped
evidence. Synthetic negative fixtures are explicitly labeled. Actual execution
mode stayed Default; hypothetical Plan Mode cases test boundaries, not a mode
switch. Optional source pytest tests were not installed or run. Evidence remains
external. The Task product is still unimplemented; publication and human review
are separate from this TestCase. Retain the actual topic feature worktree.

## Round2 bounded fixes and current status

Round2 user-authorized fixes address seven additional review threads. The tracker
rejects invalid backtick info openers, excludes HTML comments outside genuine
code before evidence/heading interpretation, and fails closed on unknown plain
task rows throughout the file. The only metadata exception is the existing nine
exact nonempty label/value bullets under exact Handoff / Gate Notes; no entire
section is exempt. Read-query behavior and implementation-only scope remain.

Routing examples now show actual Implementer PASS -> declared Tester followed
by actual Tester PASS -> declared independent Reviewer. PATCH_REQUIRED and
REPLAN_REQUIRED require independent Reviewer / Code-Reviewer; other roles stop.
Immutable Base generation requires terminal approved plus explicit empty planning
transitions, Implementer and bounded action before any temporary/final write;
all five earlier/rework states stop. Context examples use exact illustrative
requirements/spec/plan paths and do not certify files exist.

Round2 actual Tester `/root/tester` returned PASS, and independent Reviewer
`/root/explorer` returned PASS for all seven groups / seven new threads with
no findings. Tester ran one 15-method suite with 189 captured CLI calls on
observed macOS / Python3.14.0 / default tempfile, then retained the twelve
fixed-baseline replay calls showing expected contrasts. The genuine Base wire
control preserves nine metadata rows; unknown Handoff actions block.

Twenty-three actual Tester routing applications passed, including twelve
explicitly controlled incompatible role/verdict copies. Genuine Implementer,
Tester and Reviewer result identities were retained. The historical Reviewer
REPLAN result belongs only to its original controlled drift fixture; it is no
new production judgment or planning approval. Controlled aliases/context inputs
do not represent additional agents or dispatches.

Actual approved-source Base generation preserved three verbatim ordered items,
eleven pending action markers and nine metadata rows. Five canonical unapproved
copies were BLOCKED with no output/temp or protected-byte change. Context
application preserved three exact readable requirements/spec/plan paths; both
positive examples name consistent illustrative paths without certifying their
existence. Pending generation markers and all-[X] CLI controls prove no execution
completion. Independent review includes the generated artifact and these limits.

An initial external capture-schema failure excluded twelve earlier probes from
successful evidence; corrected capture retained the same twelve baseline calls.
The full suite ran once. See local-only
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round2/targeted-test-report.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review-round2/targeted-test-report.md`,
with independent review at
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round2/final-review.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review-round2/final-review.md`.
The excluded attempt is recorded in
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round2/replay-capture-attempt-failure.json`.
These local paths are unavailable from the PR; no evidence was uploaded.
Original 5/37 and Round1 12/128 remain historical snapshots. No original
six-group session, new profile, dependency or native approval was added.
This factual synchronization records completed Round2 verification; its
documentation-only delta remains a separate bounded review artifact.
Human review remains the stop and the actual feature worktree is retained.

## Round3 bounded fix status

Round3 addresses five additional review threads within the same bounded topic.
Raw fence validity cannot be promoted by HTML-comment removal, including a
same-line comment prefix. Visible quoted checkbox rows fail closed while quoted
prose/links and genuine code/comments remain controls. Supported top-level
checkbox parents may have non-task nested descriptions; nested checkboxes,
orphans, unknown plain lifecycle actions and pending/lowercase parents still block.

Both analysis skills now verify actual active mode before output. Actual Plan
Mode returns complete conversation drafts with intended paths and no disk
writes/existence claims. Translation may consume an explicitly identified
complete frozen conversation requirements draft in actual Plan Mode; missing,
vague or unfrozen input still blocks. Default file output requires selected
feature worktree and exact authorized paths; unknown mode never permits writes.
A controlled mode label is policy input, not evidence that the engine changed.

Actual Round3 Tester `/root/tester` returned PASS and independent Reviewer
`/root/explorer` returned PASS for all five bounded groups / five new threads,
with no findings. Tester ran one 18-method suite / 251 CLI calls and all 56
immutable 703-line companion tests using external optional pytest 9.1.1.
Fourteen postfix runtime probes matched expected results. These independent
counts exclude Implementer selfchecks and earlier historical suites.

Eight actual Tester analysis applications distinguish observed Default from
controlled Plan/unknown-mode policy inputs. Actual Default authorized requirements
and spec outputs were observed; controlled Plan drafts, missing/unfrozen refusal
and unknown-mode NoWrite cases support policy only. Actual engine remained
Default: actual Plan Mode execution is still unverified. No controlled label is
presented as an engine switch or additional agent dispatch.

Fresh actual Plan-Creator `/root/round3_plan_creator` produced planned,
creator-in-progress and review-ready versions; distinct Plan-Reviewer
`/root/round3_plan_reviewer` recorded reviewer-in-progress and returned native
approved before the actual owner recorded terminal approved. All five ordered
versions, timestamps, hashes and returned verdict are retained. This disposable
fixture review does not reapprove the already-authorized production topic.
Actual Implementer `/root/implementer` then created the absent Base tracker
atomically/create-only from the genuinely approved source. It mirrors exactly
one complete implementation item with 9 pending actions / 9 metadata / 0 completed,
rather than the older three-item fixture's 11 actions. Report implementation
remains absent; source and protected inventories are unchanged. Approval proves
planning eligibility only, not report execution or implementation completion.

Current installed-source comparison remains pinned to
`60b3b5b77515c354ed355c1adb28a8ed349dda67`: 41 adapted / 5 unchanged / 46 files.
The source checkout's observed HEAD moved externally to
`34f943b26fb007c2d773e37599356a4b9d6c1674` across eight nonimported paths;
source was clean and imported-path overlap is empty. No unchanged-HEAD claim,
reset or repin is made; this task performed no source writes.

Actual formal evidence is retained locally at
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round3/targeted-test-report.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review-round3/targeted-test-report.md`,
with independent review at
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round3/final-review.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review-round3/final-review.md`.
Fresh planning records and Base creation are under
`/private/tmp/agent-skill-implementation-review/pr-comment-review-round3/planning-role-evidence/`.
These plain local paths are unavailable from the PR and not uploaded.
Original 5 tests / 37 calls, Round1 12/128 and Round2 15/189 remain historical,
including their distinct source35/11 comparison; none is relabeled fresh.
Observed macOS/Python 3.14.0/default-temp and actual-mode/control limits remain.
External pytest is only a verification tool; no runtime dependency, new
profile/schema/role, universal guarantee or Task product is added.
This records completed bounded verification; the factual documentation delta
is a separate review artifact. Retain the real feature for human review;
no merge/release/cleanup or report execution is implied.

## Imported-file adaptation manifest

41 files adapted; 5 unchanged. Previous Round2 35/11 remains a historical comparison. Scope: installed paths, local role boundaries,
Base-only profile and shell, native planning verdict routing, fixture-only
worktree authorization, minimal shared contracts and explicit analysis-mode
boundaries. The two analysis examples and tracker companion Python tests remain
unchanged; six analysis instruction/checklist/reference files are now adapted. The installed tracker runtime now
contains the authorized PR-comment safety fixes; source pin remains provenance.

| Imported path | Pin comparison |
| --- | --- |
| `.agents/skills/business-intent-alignment/SKILL.md` | adapted |
| `.agents/skills/business-intent-alignment/checklist.md` | adapted |
| `.agents/skills/business-intent-alignment/examples.md` | unchanged |
| `.agents/skills/business-intent-alignment/reference.md` | adapted |
| `.agents/skills/business-to-technical-translation/SKILL.md` | adapted |
| `.agents/skills/business-to-technical-translation/checklist.md` | adapted |
| `.agents/skills/business-to-technical-translation/examples.md` | unchanged |
| `.agents/skills/business-to-technical-translation/reference.md` | adapted |
| `.agents/skills/context-package-builder/SKILL.md` | adapted |
| `.agents/skills/context-package-builder/examples.md` | adapted |
| `.agents/skills/handoff-routing-policy/SKILL.md` | adapted |
| `.agents/skills/handoff-routing-policy/examples.md` | adapted |
| `.agents/skills/plan-creator/SKILL.md` | adapted |
| `.agents/skills/plan-creator/checklist.md` | adapted |
| `.agents/skills/plan-creator/examples.md` | adapted |
| `.agents/skills/plan-creator/reference.md` | adapted |
| `.agents/skills/plan-creator/references/artifact-path-rule.md` | adapted |
| `.agents/skills/plan-creator/references/required-section-meaning.md` | adapted |
| `.agents/skills/plan-creator/references/role-boundary-rule.md` | adapted |
| `.agents/skills/plan-creator/references/stable-library-rule.md` | adapted |
| `.agents/skills/plan-creator/references/stop-and-ask-triggers.md` | unchanged |
| `.agents/skills/plan-creator/references/template-usage-rule.md` | unchanged |
| `.agents/skills/plan-creator/templates/topic-plan-template.md` | adapted |
| `.agents/skills/plan-reviewer/SKILL.md` | adapted |
| `.agents/skills/plan-reviewer/checklist.md` | adapted |
| `.agents/skills/plan-reviewer/examples.md` | adapted |
| `.agents/skills/plan-reviewer/reference.md` | adapted |
| `.agents/skills/plan-step-tracker/SKILL.md` | adapted |
| `.agents/skills/plan-step-tracker/examples.md` | adapted |
| `.agents/skills/plan-step-tracker/reference.md` | adapted |
| `.agents/skills/plan-step-tracker/scripts/step_tracker.py` | adapted |
| `.agents/skills/plan-step-tracker/tests/test_step_tracker.py` | unchanged |
| `.agents/skills/step-creator/SKILL.md` | adapted |
| `.agents/skills/step-creator/checklist.md` | adapted |
| `.agents/skills/step-creator/examples.md` | adapted |
| `.agents/skills/step-creator/reference.md` | adapted |
| `.agents/skills/step-creator/references/agent-skill-plan-profile.md` | adapted |
| `.agents/skills/step-creator/references/base-plan-profile.md` | adapted |
| `.agents/skills/step-creator/references/python-plan-authoring-adapter.md` | adapted |
| `.agents/skills/step-creator/templates/shared-lifecycle-shell.md` | adapted |
| `.agents/skills/subagent-dispatch-policy/SKILL.md` | adapted |
| `.agents/skills/subagent-dispatch-policy/examples.md` | adapted |
| `.agents/skills/worktree-manager/SKILL.md` | adapted |
| `.agents/skills/worktree-manager/checklist.md` | adapted |
| `.agents/skills/worktree-manager/examples.md` | adapted |
| `.agents/skills/worktree-manager/reference.md` | adapted |
