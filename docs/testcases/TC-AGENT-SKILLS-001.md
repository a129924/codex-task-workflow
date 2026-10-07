# TC-AGENT-SKILLS-001

One acceptance case with six groups. Intended to certify the ten installed
skills' bounded supported behavior in the observed environment, not every
model/environment. The CLI harness verifies tracker behavior only. Prompt
skills require real separated agents and independent source-backed review.

## Preconditions and evidence

Use the selected feature worktree and installed .agents/skills entrypoints.
Python >=3.11, Git and a Codex runtime supporting actual separated agent dispatch
are required. No package installation. Save commands, stdout/stderr, exit codes,
real dispatch/result IDs, artifacts, independent verdicts and source revision
under the recorded per-run external evidence root. Do not write test fixtures
or evidence into source checkout, dev worktree, globals or Task product files.

For every new run, select and record a resolved external root using the
platform default; derive every new report and fixture path from that root.
An explicitly authorized configurable external root may be used instead.
For example, from the selected feature root:

```sh
EVIDENCE_ROOT="$(python3 - <<'PYROOT'
from pathlib import Path
import json
import tempfile

root = Path(tempfile.mkdtemp(prefix="agent-skill-acceptance-")).resolve()
(root / "fixtures").mkdir()
(root / "reports").mkdir()
(root / "root-selection.json").write_text(
    json.dumps({"evidence_root": str(root), "selection": "platform-default tempfile.mkdtemp"}, indent=2) + "\n",
    encoding="utf-8",
)
print(root)
PYROOT
)"
export EVIDENCE_ROOT
```

Use `<recorded-evidence-root>/fixtures/` for owned disposable repositories and
`<recorded-evidence-root>/reports/` for outputs; record actual absolute paths and
ownership before use. Set TMPDIR to that existing fixtures directory for the
CLI harness so its TemporaryDirectory fixtures also derive from the same root.
No /private/tmp requirement or Linux execution claim follows from this portable
procedure. Historical /private/tmp evidence paths in the evaluation sections
remain unchanged local observations, unavailable through the PR.

The user authorized this exact TestCase's disposable fixture creation/cleanup.
Record per-run fixture ownership before any destructive operation. Authorization
never applies to this topic's actual feature worktree or an existing worktree.

For prompt exercises create a disposable development repo under that external
evidence directory. Copy only the two installed development contracts as fixture
inputs; use installed absolute SKILL.md entrypaths from the feature repo for
agent invocation. Freeze the requirements below; store requirements/spec/plan/
step and separate review artifacts in the fixture, never manufacture transcripts.

Fixture business request: "A local report must show completed and pending steps
for one topic. Implementation completion must be distinguishable from whole
workflow completion. It must read only and warn on lowercase x; no background
watching, marker updates, remote calls or multi-topic aggregation."
Success criteria: correct selection, pending distinction, no source changes.
The technical spec maps every requirement to the existing installed tracker CLI;
no additional implementation is requested.

## 1. Actual discovery

Launch a fresh/reloaded Codex session rooted at the feature worktree. Capture
runtime skill catalog showing all 10 exact names and local .agents/skills paths.
Use those installed entries in later groups. Passing requires runtime discovery,
not rg/file existence or manual read. Existing discovery.txt/discovery.jsonl
records initial actual discovery only; it does not certify the later use groups.

## 2. Analysis pair

Dispatch a real bounded business-intent-alignment author for the fixture request.
Require measurable requirements and explicit Non-Goals, freeze that output,
then apply business-to-technical-translation to the frozen artifact. The same
real author may apply both skills in order; a second author dispatch is optional,
never a required acceptance gate. Store analysis/smoke/requirements.md and
analysis/smoke/technical-spec.md in the fixture. A different independent
Reviewer compares both against the frozen request, checks complete requirement
mapping, no extra watcher/write/remote feature, feasibility and missing-input
stop behavior. Preserve actual dispatch/result IDs, artifact hashes and the
actual order report. Current files/hashes alone cannot reconstruct the full
historical freeze sequence; do not claim that stronger proof or invent a second
dispatch. Passing requires useful sequential artifacts and independent review,
not template copies.

## 3. Planning and Base step

A real Plan-Creator uses installed skill/template and fixture contracts to create
plan/smoke/smoke.plan.md with all 11 canonical sections, exact artifact paths,
non-stable intent, one current planned state, allowed next creator-in-progress,
next actor Plan-Creator, stage-local authoring action, verbatim implementation
items and local-delivery/no-release stop truth. The selector is topic=smoke,
branch=chore/a129924/agent-skills-smoke, managed-path-intent=<fixture sibling>
agent-YYYYMMDD-smoke, primary-worktree=false. No intent asserts actual creation.
Capture the complete canonical sequence in fresh disposable fixture versions as
each actual role produces it, not as historical backfill:

| Current state | Actual responsible action | Allowed next planning edge / next actor |
| --- | --- | --- |
| planned | Plan-Creator records initial bounded source | planned -> creator-in-progress / Plan-Creator starts authoring |
| creator-in-progress | Plan-Creator authors all required sections | creator-in-progress -> review-ready / Plan-Creator completes review inputs |
| review-ready | Plan-Creator hands the complete source to a distinct Plan-Reviewer | review-ready -> reviewer-in-progress / Plan-Reviewer starts independent review |
| reviewer-in-progress | After distinct Plan-Reviewer actually acknowledges start, the authorized owner records this phase before resumed Reviewer returns fixed native JSON | reviewer-in-progress -> approved or needs-rework / Plan-Reviewer judges |
| approved | Plan owner records approved only after the actual independent approved verdict | []/none / Implementer bounded implementation action |

Record ordered versions and hashes, exact authorized fixture paths, actual
dispatch/result identities and the independent native verdict. If needs-rework,
retain it and follow the existing rework edge; do not invent approval to advance.
Pre-review failure (missing/unreadable plan/contracts/start evidence or an ineligible current phase) returns BLOCKED coordination with no native verdict. Reviewer keeps source body/phase metadata read-only; only the exactly authorized owner records reviewer-in-progress after the actual start acknowledgement. Preserve source body hash through the pause, then resume the distinct Reviewer. The plan owner then retains explicit empty next planning transitions, Implementer
and the bounded source action. This fresh fixture approval does not reapprove
the already-authorized production topic. Keep genuine verdict identity. A
step-creator agent then creates an absent plan/smoke/smoke.step.md with explicit base-plan, exact
source item mirrors, evidence-pending markers and local shell; independent
Reviewer checks fidelity, no publish/release/cleanup, no overwrite or self-approval.

Negative inputs are separate disposable copies, each with no existing target:

| Input | Expected result |
| --- | --- |
| Missing either shared contract | BLOCKED before any successful plan/step artifact; Plan-Reviewer issues no verdict without contracts |
| Plan missing a mandatory section | Plan-Reviewer native needs-rework naming file/fix |
| profile agent-skill-plan or python-implementation-plan | BLOCKED before temporary/final step creation, no fallback |
| Existing step destination | BLOCKED, existing bytes untouched |
| Competing selector or nested-only Implementation Steps | BLOCKED, no successful step artifact |

## 4. Real workflow handoffs

Use installed subagent-dispatch-policy to select exactly one role for the bounded
planning slice. A separate context-package-builder handoff packages only frozen
fixture truth, mode, allowed paths, role and stop boundary. Actually dispatch
that selected role with separate instructions/context and obtain its result;
then run installed handoff-routing-policy against that actual result.

For route scenarios use real distinct role dispatches with explicit result
contracts. Preserve returned payload and dispatch/result IDs. A controlled
malformed-result fixture may be input to the routing role's real invocation;
label it a negative input, never an actually executed implementation verdict.

| Role/result input | Expected route |
| --- | --- |
| Plan-Reviewer approved + declared next Implementer | Implementer; preserve approved native |
| Plan-Reviewer approved without declared next, or with Tester/Reviewer | stop |
| Plan-Reviewer needs-rework | Plan-Creator |
| Implementer PASS + declared next Tester | Tester |
| Reviewer PATCH_REQUIRED | Implementer |
| Reviewer REPLAN_REQUIRED | Plan-Creator |
| MISSING_EVIDENCE + known allowed Tester owner | Tester |
| MISSING_EVIDENCE owner unknown, BLOCKED or unknown verdict | stop |
| Implementer approved or Plan-Reviewer PASS | stop: role incompatible |
| No real dispatch capability/evidence | dispatch stop; context produces no package; routing stop |

Confirm seven roles and Code aliases, with no extra role. Independently review
actual selection, minimal context, real dispatch and route; static text is
supplementary. Plan Mode negative boundary permits no writes from any role.

## 5. Installed tracker CLI

Run `TMPDIR="$EVIDENCE_ROOT/fixtures" PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` from
feature root. It executes the installed script against temporary target-root
fixtures, using one unittest TestCase class with subtests and no third-party
runtime. Capture complete output/exit code and inspect no source edits.

| Fixture | Expected operations |
| --- | --- |
| Implementation and lifecycle all [X] | Five operations exit 0; read filters correct |
| Implementation [X], lifecycle [ ] | implementation completion 0; whole completion 1; read filters correct |
| Implementation [x] | stderr warning, both completion operations 1; reads retain pending meaning |
| Missing / empty / duplicate Implementation section with other done checkbox | only implementation completion 1; reads/whole checks retain source semantics |
| Missing .step.md | All five operations exit 1 with file-not-found error |
| Only fenced example checkboxes | Both completion checks 1; examples are not evidence |

The new PR-comment regression additions verify every operation rejects unsafe
topics and external symlink targets without outside output or traceback; they
cover read/encoding failures, true fence closure, nested-checklist refusal,
H1/H2 implementation boundaries and platform-default temporary directories.
Actual targeted Tester completed the fixes' own final 12-method / 128-call
suite and four exact G11 rechecks; the original 5-test / 37-call result below
remains historical.

The five operations are read_all, read_not_run, read_success, check_all_succeeded,
check_impl_steps_succeeded. Missing/empty/duplicate section expectations do not
change whole-check semantics. Pytest companion tests are preserved but optional;
pytest absence is recorded, not resolved by installation. Marker success does
not validate external test/review/worktree evidence.

## 6. Disposable worktree lifecycle and refusal gates

A real worktree-manager agent guides operations in an independently initialized
fixture Git repo under the evidence root. Use a local initialization commit
only there; no remote. Before create record repo root, common Git dir, initial
HEAD and exact intended branch/path. Managed path is its canonical sibling
`<fixture-repo>.worktrees/agent-YYYYMMDD-smoke`; verify actual Git inventory.

1. In actual Default with exact existing create selector/operation authorization,
   create a new branch/worktree with no collision; verify path outside repo,
   attached branch and create_result path/branch/next_step.
2. Inspect; require all seven get_worktree fields and observed clean state.
3. Declare the fixture lineage explicitly abandoned (test complete, no merge
   required). Release returns full evidence with destructive_action_allowed false;
   verify directory and Git registration remain unchanged.
4. Recheck exact same-run ownership, non-primary managed path, branch uniqueness,
   clean/no-untracked/no-lock state and no unique commits or refs to preserve.
   Remove under this TestCase's prior user authorization without force; verify
   only that selected fixture disappears and the primary repo remains.

Before final clean removal, use separate reversible fixture variants/requests:

| Variant | Expected refusal |
| --- | --- |
| Branch already exists / path collision | Stop for reuse-or-rename decision; no silent reuse |
| Tracked dirty or untracked file | needs-human-decision; no remove |
| Locked/detached or branch ambiguity | needs-human-decision; no remove |
| Primary or outside-this-run selector | stop; no fixture authorization |
| Missing test authorization or creation evidence | stop; no remove |
| Unique fixture commit/ref requiring preservation | stop; no removal |

Capture file/directory existence before and after refusals. Restore fixture
state with explicit owner evidence only inside that disposable repo before
attempting the final authorized removal. Do not delete actual topic branch,
worktree, source checkout, dev worktree, existing worktrees or any remote refs.

## Evaluation and current state

For the original delivery head `2afebb1a259b163ee47d3b95c6d11ef199dc7591`,
actual Tester `/root/tester` reported all six original groups PASS. Independent
Reviewer `/root/explorer` returned overall bounded PASS with no blocking issues
on 2026-10-07. The final review checks the original TestCase and ten-entry mapping,
not universal availability, Task product behavior, publication or human merge.

| Group | Actual result |
| --- | --- |
| 1. Fresh runtime discovery | PASS: all ten installed catalog entries |
| 2. Analysis pair | PASS: sequential real author and separate independent review |
| 3. Planning / Base / refusals | PASS: native approved/needs-rework, Base fidelity and nine creator refusal cases |
| 4. Dispatch / context / routing | PASS: actual separated handoffs and thirteen route cases |
| 5. Tracker | PASS: five tests / thirty-seven installed CLI calls |
| 6. Worktree | PASS: four actual lifecycle operations and eleven refusal gates |

Evidence: `/private/tmp/agent-skill-implementation-review/test-report.md`,
`/private/tmp/agent-skill-implementation-review/test-report.json`,
`/private/tmp/agent-skill-implementation-review/code-review/final-review.md`
and `/private/tmp/agent-skill-implementation-review/code-review/final-review.json`.
The earlier Tester index pending overall-gate field is historical; the separate
final-review result provides the later independent gate. Tests were not rerun
for this documentation closeout.

PASS applies to the observed macOS feature worktree, actual Codex runtime,
Python >=3.11, Git and retained disposable fixtures, supported Base-only scope.
Failed CLI startup, outer sandbox and network attempts remain in the index and
are excluded from success evidence. Negative inputs and hypothetical Plan Mode
requests are controlled fixtures; actual mode remained Default. Current hashes
cannot independently reconstruct historical freeze chronology. Preserve the
actual IDs, order reports/digests and independent mapping with that limit.
Optional source pytest was neither installed nor run; no universal guarantee,
product implementation, publishing or human-review approval is inferred.
The real feature worktree remains available for human review; only the verified
same-run disposable child was removed. External evidence and temporary primary
fixtures are retained. The original documentation delta completed its independent PASS in
`/private/tmp/agent-skill-implementation-review/code-review/doc-sync-review.json`.
These code-formatted evidence paths are local-session only and unavailable
through the PR; nothing is uploaded. The Round1 PR-comment fixes at
`f0f484e27c06cb0387a48f16d712eaf5830ecea0` have
separate actual targeted Tester `/root/tester` PASS and independent Reviewer
`/root/explorer` PASS covering 14 groups / all 18 threads. Final suite: 12 test
methods / 128 CLI calls; four exact G11 notes/description continuation rechecks
return exit 1 without false success. The prior 43-input replay is retained at
its initial-fixed runtime version; it was not repeated or attributed to the
final runtime. No unchanged full-six-group/analysis/discovery sessions were
repeated. Neither historical six-group PASS nor 5 tests / 37 calls substitutes
for that Round1 runtime evidence.

Actual installed-byte-equal prompt snapshot applications cover seven routing
cases, three selection/prelaunch cases and the template. Controlled contextual
inputs and genuinely reused result IDs remain labeled; no new dispatch or
native planning approval is invented. Forty-two captured Git fixture commands
verify absolute root/child anchoring, internal/symlink refusal, preserved refs
and guarded same-run clean child removal, with actual feature retained.

Current local-only evidence:
`/private/tmp/agent-skill-implementation-review/pr-comment-review/targeted-test-report.json`,
`/private/tmp/agent-skill-implementation-review/pr-comment-review/targeted-test-report.md`,
`/private/tmp/agent-skill-implementation-review/pr-comment-review/final-review.json`
and `/private/tmp/agent-skill-implementation-review/pr-comment-review/final-review.md`.
Observed current suite environment is macOS / Python3.14.0 / default tempfile;
no Linux/universal model claim. Historical failed-attempt/freeze limits, original
doc-sync chronology and source-license limitation remain. These paths cannot
be downloaded through the PR. Human review is still the stop; thread resolution
has not been inferred from the implementation PASS.

## Round2 targeted regression and handoff procedure

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

The completed procedure replayed the six baseline inputs/twelve operations,
ran the updated suite once, exercised true Base all-controlled-[X] wire success
and unknown Handoff action refusal, and applied routing to retained genuine
result identities plus explicitly controlled incompatible copies. Native planning
results remained unchanged; no new actor verdict was fabricated.

Disposable Base generation used the genuinely reviewed approved source; five
otherwise complete copies (planned, creator-in-progress, review-ready,
reviewer-in-progress, needs-rework) each BLOCKED before temporary/final output
with protected inputs unchanged. The exact readable disposable requirements,
spec and plan paths survived context packaging. Independent Reviewer judged
all seven groups PASS. Preserve the observed-environment and fixture limits
above; no merge/release, real feature cleanup or new schema/dependency occurred.

## Round3 targeted procedure and current evidence

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
