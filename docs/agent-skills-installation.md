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

step-creator supports only base-plan, including local development tools. The
source specialized agent-skill-plan / python-implementation-plan profiles are
explicitly unsupported and stop before any write. No python-plan-authoring or
11th skill is installed. The Base lifecycle ends at local reviewable delivery;
publication needs a separate explicit authorization and retains human review.

Tracker requires Python >=3.11 and only stdlib. Run from the target repo root:

```sh
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_all <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_not_run <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py read_success <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded <topic>
python3 .agents/skills/plan-step-tracker/scripts/step_tracker.py check_impl_steps_succeeded <topic>
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The source tracker runtime and its companion pytest tests are unchanged. pytest
is optional for those source tests and is not installed as part of this topic;
the repository's acceptance harness uses unittest. Do not confuse checkbox
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

## Verification status

TC-AGENT-SKILLS-001 completed all six groups with actual Tester `/root/tester`
PASS. Independent Reviewer `/root/explorer` returned overall bounded PASS on
2026-10-07, with no blocking issues. Actual discovery, ten intended uses,
independent planning review/Base step, separated dispatch/native routes, five
tracker operations and four isolated worktree lifecycle operations were reviewed.
Tracker evidence contains 5 tests / 37 installed CLI calls; worktree evidence
contains 11 refusal cases. No static file check substitutes for these exercises.

- [Tester report](/private/tmp/agent-skill-implementation-review/test-report.md)
  and [structured index](/private/tmp/agent-skill-implementation-review/test-report.json)
- [Independent final review](/private/tmp/agent-skill-implementation-review/code-review/final-review.md)
  and [native result](/private/tmp/agent-skill-implementation-review/code-review/final-review.json)
- [TestCase procedure](testcases/TC-AGENT-SKILLS-001.md)

This supports normal bounded use in the observed macOS feature worktree, actual
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

## Imported-file adaptation manifest

32 files adapted; 14 unchanged. Scope: installed paths, local role boundaries,
Base-only profile and shell, native planning verdict routing, fixture-only
worktree authorization and minimal shared contracts. Analysis skills and tracker
Python runtime/tests remain unchanged.

| Imported path | Pin comparison |
| --- | --- |
| `.agents/skills/business-intent-alignment/SKILL.md` | unchanged |
| `.agents/skills/business-intent-alignment/checklist.md` | unchanged |
| `.agents/skills/business-intent-alignment/examples.md` | unchanged |
| `.agents/skills/business-intent-alignment/reference.md` | unchanged |
| `.agents/skills/business-to-technical-translation/SKILL.md` | unchanged |
| `.agents/skills/business-to-technical-translation/checklist.md` | unchanged |
| `.agents/skills/business-to-technical-translation/examples.md` | unchanged |
| `.agents/skills/business-to-technical-translation/reference.md` | unchanged |
| `.agents/skills/context-package-builder/SKILL.md` | adapted |
| `.agents/skills/context-package-builder/examples.md` | unchanged |
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
| `.agents/skills/plan-step-tracker/scripts/step_tracker.py` | unchanged |
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
| `.agents/skills/subagent-dispatch-policy/examples.md` | unchanged |
| `.agents/skills/worktree-manager/SKILL.md` | adapted |
| `.agents/skills/worktree-manager/checklist.md` | adapted |
| `.agents/skills/worktree-manager/examples.md` | adapted |
| `.agents/skills/worktree-manager/reference.md` | adapted |
