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
under /private/tmp/agent-skill-implementation-review/. Do not write test fixtures
or evidence into source checkout, dev worktree, globals or Task product files.

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
A different Plan-Reviewer returns the fixed native JSON. The plan owner then
records actual approved state from that returned verdict, explicit []/none
next planning transitions, next actor Implementer and the bounded implementation
action. Keep the genuine verdict ID as evidence, never invent approval. A
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

Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` from
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

1. Create a new branch/worktree with no collision; verify path outside repo,
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
