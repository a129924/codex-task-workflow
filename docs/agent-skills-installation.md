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

worktree-manager requires Git, verified actual active mode and exact selectors.
Plan/unknown mode permits conversation planning/inspection only, no lifecycle
or metadata mutation. Default uses existing exact authorization and every
safety gate; a planned-only result never claims creation or cd. Ordinary/existing worktree
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

## Round4 bounded PR fixes — independent verification PASS

The five-group correction received actual independent Tester /root/tester
PASS and independent Reviewer /root/explorer PASS. The once-run affected suite
passed 21 tests / 303 CLI calls, and the unchanged 703-line companion passed
56/56 once using the existing external pytest 9.1.1 venv. Twenty separate CLI
replays over ten immutable fixtures verified seven corrected bug outcomes.
Earlier 18 tests / 251 CLI calls and 56 companion tests remain historical Round3
observations; original 5/37, Round1 12/128 and Round2 15/189 stay separate.

The installed tracker now uses column-zero Implementation Steps openers and
H1/H2 boundaries consistently; nested headings cannot cut or reopen scope or
manufacture metadata sections. Explicit raw blockquote fence containers preserve
quote depth and raw info validity; container exit/lower depth is reprocessed as
visible evidence. Naked quoted task rows remain unsupported. This is bounded
syntax handling, not a full Markdown parser.

worktree-manager checks actual active mode before any lifecycle mutation.
Plan/unknown mode gives conversation planning/inspection only; no Git/ref,
directory/registration or offboarding-metadata writes. Default mutation still
requires exact existing operation/selector authorization and all original safety
gates. Controlled labels are policy-only; actual Plan-engine behavior remains
unverified. A planned-only path is intended, never a created-path or cd claim.

New evidence and disposable fixtures derive from one recorded resolved
platform-default tempfile.mkdtemp root (or an explicitly authorized configurable
root). Historical /private/tmp references below remain actual local observations,
not requirements for a new run and not downloadable through the PR. No Linux
execution or full original six-group retest is claimed.

This Round4 run's actual platform-selected local evidence root is
`/private/var/folders/x9/3v967ts5131dfn6x4bsy9th00000gn/T/agent-skill-review-round4-xd8la0hj`.
Its targeted-test-report.json / targeted-test-report.md record the actual
Tester result, and final-review.json / final-review.md the later independent
Reviewer PASS. The Tester index originally pending overall-review field is a
historical handoff snapshot; the separate final-review artifact records completion.
These paths are local-only and unavailable through the PR; no evidence is uploaded.

Actual Default created and inspected one owned disposable managed worktree using
15 recorded fixture Git commands. Five controlled Plan/unknown/missing-authority
cases caused no file, ref or registration mutation. The child remains retained;
no remove or offboarding metadata write was executed. Reviewer originally selected
this run root with host-default tempfile.mkdtemp. Separately, Tester ran the
documented selector once using explicitly authorized configurable TMPDIR under
this root: that proves the configured variant, not an unoverridden host-default
selection by Tester. Actual Plan-engine behavior and Linux remain unverified.

The preserved external guard-capture correction records an overly narrow literal
None suffix assertion; comparing exact original Open Questions bytes then passed.
It was a capture error, not a runtime failure, and caused no repository edit or
test rerun. Implementer selfcheck is not independent evidence. No original
six-group retest or fresh planning approval cycle was performed. All 46 imports remain pinned to
60b3b5b77515c354ed355c1adb28a8ed349dda67; current comparison is still 41 adapted /
5 unchanged. No source/global/dev/product or immutable companion changes.
Last read-only source HEAD observation is the externally moved
34f943b26fb007c2d773e37599356a4b9d6c1674,
without reset or repin. Retain the production feature for human review; no
merge, release or cleanup.

## Round5 bounded fixes — independent verification PASS

The authorized five-group Round5 correction passed actual independent Tester
and Reviewer verification. The Tester ran 23 methods / 378 CLI calls once and
all 56 immutable companion items once, with 14 separate baseline replays across
seven fixtures correcting six false-success outcomes. Round4 21 tests / 303 CLI
calls and 56/56 companion results remain historical. Original 5/37, Round1
12/128, Round2 15/189 and Round3 18/251 evidence remains separately recorded.

Visible quoted plain/ordered actions now fail closed along with quoted task
checkboxes; quoted prose/links and genuine quoted code remain supported.
HTML-comment scanning protects only raw same-line balanced equal-length
inline tick spans while retaining original line/step text. Ambiguous/unmatched
or multiline comment-token syntax fails closed; real active HTML-comment mode
consumes raw closing markers regardless of ticks. This is bounded syntax
handling, not a full Markdown parser or new dependency.

Plan-Creator checks actual mode and exact existing selected-feature authority
before writes. Plan or Default without file authority returns a complete
frozen-input conversation draft with intended paths/proposed states only;
unknown mode stops without writes. Optional analysis stays optional, with named
warnings and no invented missing baseline facts or disk/approval claims.

Plan-Reviewer preflight requires readable plan/contracts, genuine independent
actual start acknowledgement, then the authorized owner's recorded current
reviewer-in-progress before either native verdict. Otherwise it returns BLOCKED
coordination without approved/needs-rework. Reviewer leaves source body/phase
read-only; owner records actual start phase before resumed review and returned
verdict phase afterward. Eligible fixed JSON shape remains unchanged. Any new
verification fixture records genuine distinct actors/chronology; no main topic
reapproval, Base creation or report execution is part of this correction.

The positive implementation Reviewer context example now includes exact
illustrative changed-artifact/current-diff/actual-Tester-result paths with version
binding. A real package verifies required proof is readable/current; absent or
stale proof stops. Illustrative paths assert no existence or test PASS and do
not add requirements to unrelated roles.

All new Round5 reports and owned fixtures derive from the actual recorded
platform-selected evidence root:
`/private/var/folders/x9/3v967ts5131dfn6x4bsy9th00000gn/T/agent-skill-review-round5-jgvpi3w2`.

Its baselines.json preserves 14 actual CLI calls / seven immutable fixtures:
six false-success outcomes and eight correct controls. runtime-test-result.json
records the independent once-run 23 methods / 378 CLI calls, 56/56 companion
items and 14 successful replay comparisons. The existing external pytest 9.1.1
environment is optional verification tooling, not a runtime dependency or a
new installation prerequisite.

planning-and-package-test-result.json records actual authorized Default file
authoring and four separate mode/input applications: the Default no-authority
conversation draft plus three controlled policy inputs (Plan, unknown mode
and incomplete inputs).
The positive fresh fixture followed all five actual planning states with
distinct Plan-Creator and Plan-Reviewer actors. Eight controlled preflight
refusals returned BLOCKED with zero native verdicts. Two genuine Reviewer
start acknowledgements preceded owner-only reviewer-in-progress records;
resumed eligible review returned the actual native approved and needs-rework
verdicts, then the owner recorded each result. Reviewer preserved both
non-status source bodies. Only approved is planning-terminal; needs-rework
retains its creator-in-progress edge. The broken fixture's initial review-ready
state was synthetic; its subsequent start, owner records and native review
were actual. No main-topic reapproval, Base creation or report execution occurred.

The actual Tester package supplied 12 readable current references for changed
artifacts, diff and Tester proof. The independently dispatched implementation
Reviewer consumed that package and returned bounded PASS; a controlled
missing-proof case stopped without a package. targeted-test-report.json records
the formal Tester PASS and final-review.json records the independent Reviewer
PASS for all five groups. These records do not certify every environment or
repeat the original full six-group acceptance cycle.

Author failed/intermediate/final selfchecks remain separately retained in
selfcheck-first-failure.json, selfcheck-intermediate-before-inline-interaction.json
and implementation-result.json. They are not independent test counts. The
initial aggregation hash guard compared a historical preflight hash against
an owner-updated source; aggregation-first-attempt.json retains that failure.
The final aggregation used the retained review-ready snapshot and verified the
owner's final source separately, without a test rerun.

Evidence is local-only, not uploaded or downloadable through this PR.
Historical /private/tmp paths remain original provenance. Observed actual
Default on macOS/Python 3.14 and controlled Plan policy remain distinct;
actual Plan-engine execution and Linux remain unverified.

Immutable import provenance stays pinned to 60b3b5b77515c354ed355c1adb28a8ed349dda67;
current 46-file comparison remains 41 adapted / 5 unchanged. Source last observed
external HEAD34f943b is not the import authority and is not reset or repinned.
No dev/source/global/product/immutable 703-line companion changes. Preserve
the original main approval, eleven canonical sections/nine scope fields and
Open Questions bytes. Retain feature and owned fixtures for human review;
no merge, release or cleanup.

## Round6 bounded fixes — independent verification PASS

Round6's five bounded corrections passed actual independent Tester and Reviewer
verification. Once-run results: 24 methods / 400 CLI calls, all 56 immutable
companion items, plus 12 separate baseline replays across six fixtures correcting
four false-success outcomes and retaining eight controls. Author selfchecks are
separate readiness evidence; prior Round5 23/378 and earlier counts remain
historical, not fresh runs. No new runtime dependency or global install.

The actual distinct Plan-Reviewer applied the missing-plan fallback and returned
BLOCKED coordination without native verdict. A genuine returned independent
Reviewer PATCH_REQUIRED routed to Implementer with actual task/result correlation
and distinct author identity; five other routing cases were controlled policies.
Implementer actually consumed 27 readable version-bound package references;
five controlled missing-boundary package inputs stopped.

Normal actual Default step creation used the unchanged genuine approved source,
canonical source-topic/verified-root destination and separate exact caller final/
temp authority. No additional source step row or exception was required; explicit
source conflicts still block. The earlier limited-exception record was superseded,
retained and never executed. Exact exclusive temp creation, full gate recheck and
atomic no-overwrite promotion produced one retained-fixture Base step: one
verbatim implementation item / nine pending actions / zero completed / nine
metadata fields. Before creation, two complete proposed conversation drafts and
three no-write BLOCKED inputs preserved all paths. Existing final subsequently
blocked before temp creation with unchanged bytes. All 111 prior protected entries
remained identical; the step was the only new final, and its temp is absent.

No production Base, new main approval, planning cycle or report/lifecycle execution
occurred; the retained fixture Base was created once. Original source/native/
owner approval proof and report absence remain unchanged. Tracker escape parity,
real routing provenance and step mode/root/final+temp/no-overwrite gates are
bounded corrections, not a full parser or new profile.

Actual evidence: `/private/var/folders/x9/3v967ts5131dfn6x4bsy9th00000gn/T/agent-skill-review-round6-rn4zhz_2`.
`targeted-test-report.json` and `final-review.json` record Tester/Reviewer PASS;
`implementer-step-application-result.json` records the actual generated artifact.
These are local-only paths unavailable for download through this PR. Actual
Default/macOS was observed; Plan/unknown/REPLAN variants are policy controls.
Actual Plan engine, Linux and an unprovoked destination race remain unverified;
unexposed provider request IDs were not fabricated. Existing external pytest
is optional verification tooling. Current immutable 60b3b5b77515c354ed355c1adb28a8ed349dda67
import comparison remains 41 adapted / 5 unchanged / 46 files. External source
HEAD is separately observed without reset/repin. Preserve original topic approval,
eleven sections/nine fields/Open Questions, product readOnly and feature/fixtures.
Ready human review remains the stop; no merge, release or cleanup.

## Round7 bounded fixes — independent verification PASS

Round7's five bounded corrections have actual Tester /root/tester PASS and
independent Reviewer /root/explorer PASS. The once-run stdlib suite passed
26 methods / 448 CLI calls; the unchanged companion passed 56 items once.
Separate 28 CLI replays across 14 fixtures corrected six false-success outcomes
and six valid-code rejections; real pending stdout after code was verified.
G01's real independent Reviewer consumed 22 current refs; six controlled missing
boundaries stopped packaging. G04 applied four genuine review payloads and an
ordinary nonreview PASS; 14 controlled missing/same-author inputs across seven
review verdict types stopped. Alias/REPLAN examples remain controlled policy.
G05's actual Implementer consumed 26 refs, verified genuine historical native/
owner/current-source binding with legitimate Status-only version changes, then
refused the existing final before temp/draft. Four synthetic proof failures
blocked; all 112 retained fixture entries stayed unchanged. Existing step d47aed…
remains; temp/report are absent. No fresh Base, native cycle or approval was
created this round. Earlier rounds' counts and results remain historical.
Actual Default/macOS only: actual Plan engine, Linux and unprovoked races remain
unverified; no full Markdown conformance or new dependency is claimed. External
pytest is optional verification tooling, not a runtime dependency. Imports remain
41 adapted / 5 unchanged against immutable pin 60b3b5b77515c354ed355c1adb28a8ed349dda67;
source external HEAD 34f943… is separate and was not reset/repinned. Current dev
startup 692d33… stays clean with 23 guarded files, distinct from historical 994b509.
Local-only evidence: /private/var/folders/x9/3v967ts5131dfn6x4bsy9th00000gn/T/agent-skill-review-round7-a80fg_d3/final-review.json and /private/var/folders/x9/3v967ts5131dfn6x4bsy9th00000gn/T/agent-skill-review-round7-a80fg_d3/targeted-test-report.json;
these paths are unavailable from GitHub and no evidence assets were uploaded.
