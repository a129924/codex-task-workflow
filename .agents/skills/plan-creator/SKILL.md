---
name: plan-creator
description: "Author a repository topic plan with explicit scope, artifacts, workflow gates, and handoff criteria."
complexity: high
risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff
use_when:
  - a new repository topic needs `plan/<topic>/<topic>.plan.md`
  - an existing topic plan is missing workflow-critical contract sections
  - the user wants a repo-visible handoff artifact before Implementer implementation starts
do_not_use_when:
  - the main task is to implement the skill or code artifact itself
  - the task is to review or approve a finished topic plan
  - the task is a tiny wording edit to an already-valid topic plan
  - the request is for a generic project plan outside this repository
inputs:
  - verified actual active engine mode and exact existing selected-feature write authority
  - the topic name
  - the intended outcome of the topic
  - the in-scope and out-of-scope boundaries
  - the expected repo-visible artifact paths
  - whether the topic affects stable-library surfaces
  - any locked decisions that should not be rediscovered during implementation
  - optional analysis-layer artifacts at `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md`
  - any clear user revision to the analysis baseline, including its affected scope
  - the current workflow contract from `plan/agent-handoff-workflow.md`
  - the shared topic-plan contract from `plan/topic-plan-contract.md`
outputs:
  - mode-appropriate topic plan: authorized Default feature file, otherwise conversation draft with intended path
  - analysis revisions written only under exact Default authority; otherwise conversation proposals with unchanged disk baseline
  - explicit scope, boundaries, locked decisions, and analysis-layer routing for the topic
  - exact artifact paths and workflow transitions
  - clear stable-library intent declared or explicitly absent
  - explicit semantic warnings when analysis inputs are missing or incomplete
  - complete planning draft for independent review; only genuine subsequent approval permits Implementer handoff
---

# Purpose
Create a valid topic plan for this repository's workflow.

# Trigger / When to use
Use this skill when:
- a new repository topic needs `plan/<topic>/<topic>.plan.md`
- an existing topic plan is missing workflow-critical contract sections
- the user wants a repo-visible handoff artifact before Implementer implementation starts

Do not use this skill when:
- the main task is to implement the skill or code artifact itself
- the task is to review or approve a finished topic plan
- the task is a tiny wording edit to an already-valid topic plan
- the request is for a generic project plan outside this repository

# Inputs
- actual active engine mode; controlled labels are policy inputs, not engine proof
- selected feature and exact existing authorized paths for any Default file writes
- the topic name
- the intended outcome of the topic
- the in-scope and out-of-scope boundaries
- the expected repo-visible artifact paths
- whether the topic affects stable-library surfaces
- any locked decisions that should not be rediscovered during implementation
- optional analysis-layer artifacts at `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md`
- any clear user revision to the analysis baseline, including its affected scope
- the current workflow contract from `plan/agent-handoff-workflow.md`
- the shared topic-plan contract from `plan/topic-plan-contract.md`

# Process
0. Verify actual active mode and the exact existing authorized target set before
   any write. Actual Plan Mode or Default without file-write authority returns a
   complete frozen-input conversation draft only, with intended paths and proposed
   state fields, never disk-created/current-state/approval claims. Unknown mode
   stops without writes. Default writes require the selected feature and exact
   authorized paths; do not ask again when authority already exists. No subagent
   bypass. Controlled mode labels cannot certify actual Plan-engine execution.
   Apply the resolved-output containment gate below before every file operation.
1. Confirm the task is really topic-plan authoring, not implementation drafting, review, publish, or release execution.
2. Read the current workflow contract and the shared topic-plan contract, then start from `templates/topic-plan-template.md` instead of drafting the plan from scratch.
3. Inspect `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md` if either exists before deciding the plan scope.
4. Route analysis-layer priority before drafting:
   - if both files exist, enter strict mode: treat `analysis/<topic>/technical-spec.md` as the execution-facing source of truth, use `analysis/<topic>/requirements.md` as the business-intent guardrail, and map the output plan 100% to the technical spec instead of inventing alternative work from chat context
   - if one file exists without the other, emit an explicit semantic warning that names the missing companion artifact and explains that the analysis layer is incomplete
   - if neither file exists, emit an explicit semantic warning that the plan is being authored without the optional analysis layer
   - analysis artifacts are the recorded baseline; a clear later user revision updates that baseline without requiring a magic word. Record the affected contract and synchronize only exactly authorized Default artifacts before downstream use; otherwise propose the revision in the conversation without claiming changed disk baseline
5. Declare local development intent with stable-library intent absent. A README
   navigation link alone is not promotion. If stable publishing is requested,
   stop for a separately approved publishing contract; do not import upstream
   VERSION, registry, release or tag governance.
6. Lock scope, boundaries, and role ownership before drafting the plan body in the local template.
7. Enumerate exact `Artifact Paths`; do not use vague catch-all path descriptions.
8. Produce required sections in canonical order: exactly authorized Default file or complete conversation draft with intended path under the mode gate.
9. Explicitly state no automatic post-merge/release actions for local work.
   Separately authorized publication must have exact topic paths and stop at
   human review; it is not an automatic lifecycle.
10. Use only canonical transitions and declare reviewer JSON as a schema, not a verdict. Conversation draft state is proposed, not actual disk phase. For authorized phase recording, the owner advances review-ready to reviewer-in-progress only after a genuine independent Reviewer start acknowledgement and before resumed review; record approved/needs-rework only after that Reviewer returns its native verdict. Never invent acknowledgement, phase history or approval.
11. If scope, artifact paths, role ownership, stable-library timing, stable-library metadata, release intent, or analysis-layer priority is unclear, stop and ask instead of filling placeholders.

## Resolved-output containment gate

Immediately before EVERY actual write, mkdir, temporary-file creation,
no-overwrite promotion or owner-phase update, recheck actual Default mode and
existing exact authority against the selected feature's verified canonical root.
This includes plan, optional analysis revisions and every phase-recording write.
Resolve the target and existing parent symlink chains; for an absent target or
parent, strictly resolve the nearest existing ancestor and append the exact
prospective suffix. Inspect existing components so dangling symlinks, unreadable
or ambiguous chains never become silently accepted prospective directories.
Require both resolved destination and parent/ancestor to stay within that selected
canonical feature, and require the resolved destination to match the exact
canonical destination covered by existing authority, as well as its declared
lexical path. Recheck immediately before each individual operation, including
before directory creation and before promotion; an earlier batch check is not
sufficient. Outside-root/development/external aliases, unknown root/authority,
dangling or ambiguous targets stop before any mutation. Reuse authority already
given; never infer new destination permission from lexical containment alone.
Plan/no-authority conversation drafts remain non-writing. This is prompt policy,
not an executable sandbox or a guarantee against unprovoked TOCTOU races.

# Examples
- **Positive**: Draft `plan/offline-order-capture/offline-order-capture.plan.md` so it uses exact artifact paths, canonical transitions, and JSON reviewer handoff, while entering strict mode because both `analysis/offline-order-capture/requirements.md` and `analysis/offline-order-capture/technical-spec.md` exist.
- **Negative**: Ignore existing analysis files because a newer chat instruction sounds easier, skip semantic warnings when analysis inputs are missing, or draft a plan that says `README/VERSION maybe later`.

# Outputs
- authorized Default topic file, or conversation draft with intended plan path and proposed state only
- analysis revisions written only under exact Default authority; otherwise conversation proposals with unchanged disk baseline
- explicit scope, boundaries, locked decisions, and analysis-layer routing for the topic
- exact artifact paths and workflow transitions
- clear stable-library intent: declared or explicitly absent
- explicit semantic warnings when analysis inputs are missing or incomplete
- a plan for independent review; Implementer receives it only after genuine approval

# Validation

## Required Checks
- verify actual mode and exact existing target authority first; apply the canonical-root/target/parent containment gate immediately before every write/mkdir/temp/promote/phase/analysis operation; draft-only output makes no disk/current-phase/approval claims
- missing optional analysis is a named warning, not a new globally required file; incomplete supplied frozen scope/baseline never authorizes invented facts or a review-ready claim
- PASS: topic name, outcome, scope, and artifact paths are all provided
- PASS: the workflow contract at `plan/agent-handoff-workflow.md` is readable
- PASS: the shared topic-plan contract at `plan/topic-plan-contract.md` is readable
- SOFT FAIL: analysis-layer artifacts are missing or incomplete — emit an explicit semantic warning naming what is absent and continue with incomplete-layer routing
- BLOCKED: scope, artifact paths, or stable-library timing cannot be determined without guessing — stop and ask before drafting

## Quality Checks
- all required topic-plan sections are present in canonical order and match `plan/topic-plan-contract.md`
- current status and allowed transitions are explicit and canonical
- `Artifact Paths` are exact, bounded, and role-labeled (see `references/artifact-path-rule.md`)
- reviewer handoff is a single machine-consumable JSON object
- post-merge / release timing matches the topic's actual scope
- stable-library intent is explicitly declared or explicitly absent (see `references/stable-library-rule.md`)
- analysis-layer priority routing is stated before the plan body begins
- strict mode maps the plan 100% to `analysis/<topic>/technical-spec.md` when both analysis artifacts exist
- missing analysis artifacts produce explicit semantic warnings instead of silent fallback
- clear user revisions are reflected in the affected baseline; ambiguous contradictions are surfaced before handoff

## On Soft Fail
- mark incomplete-layer routing as INCOMPLETE and name absent optional analysis; draft only known frozen scope, never fill missing required scope by guessing or claim actual review-ready disk state
- emit a named semantic warning when one analysis file exists without its companion
- do not silently fall back to chat context when analysis artifacts exist but are partial

# Red Flags
- the plan mixes review-ready-only work with undeclared stable-library publish intent
- the plan says `TBD`, `later`, or `follow normal process` where the workflow needs an explicit contract
- artifact paths are broad labels instead of concrete repo-visible paths
- creator, reviewer, and Observer ownership are blended together
- reviewer handoff is written as Markdown notes instead of JSON
- existing analysis artifacts are ignored because chat context points somewhere else

# Common Rationalizations
- `Reviewer can infer the missing contract later.`
- `We can decide whether this touches README or VERSION after implementation.`
- `Artifact paths do not need to be exact as long as the scope sounds right.`
- `A rough status model is good enough if the intent is obvious.`
- `An ambiguous chat remark silently replaces the entire analysis baseline.`

# Boundaries
- Do not implement the topic's actual skill or code artifact.
- Do not review, approve, or publish the topic.
- Do not guess stable-library timing or release intent.
- A complete explicitly supplied frozen conversation baseline may support a mode-appropriate draft; do not invent missing analysis, imply an intended path exists, or claim the draft is disk-readable/current review-ready.
- Do not let absent analysis files fail silently; warn explicitly.
- Do not treat ambiguous remarks as blanket permission to discard analysis; honor clear revisions and update only affected contracts.
- Do not generate a generic project-management plan for another repository.
- `plan/topic-plan-contract.md` is the shared repo-level fallback contract when the topic-plan template is absent.

# Failure Handling

## Missing Context
- BLOCKED — if the topic name, outcome, or scope is absent, stop and ask before drafting
- BLOCKED — if the workflow contract at `plan/agent-handoff-workflow.md` or the shared topic-plan contract at `plan/topic-plan-contract.md` cannot be read, stop before drafting

## Ambiguous Requirement
- if stable-library timing is unclear, stop and ask rather than guessing; do not fill with `TBD` or `later`
- if artifact paths cannot be determined exactly, stop and list what is missing
- if a conflict remains ambiguous after reading the latest user intent and baseline, ask which contract is intended; a clear revision does not require another confirmation

## Execution Limitation
- if the topic-plan template is absent, fall back to the required section list in `plan/topic-plan-contract.md` rather than inventing a new shape
- if a revision is ambiguous about which contract changes, ask before discarding analysis content

# Workflow State Contract

When participating in a multi-agent plan-authoring and review workflow, include:
- current_step: <step name from Process>
- next_step: <next step or DONE>
- status: IN_PROGRESS | COMPLETE | INCOMPLETE | BLOCKED

Omit this section when the plan is authored outside a multi-agent handoff flow.

# Local references
- `reference.md`: overview of stable authoring rules with pointers to each topic in `references/`
- `plan/topic-plan-contract.md`: shared repo-level authority for required topic-plan sections, fallback behavior, and contract-level blocking semantics
- `references/required-section-meaning.md`: what each mandatory topic-plan section means and must contain
- `references/stable-library-rule.md`: local development intent, README navigation and unsupported stable publishing
- `references/artifact-path-rule.md`: how to declare exact, role-labeled, executable artifact paths
- `references/role-boundary-rule.md`: how to keep Plan-Creator, Implementer, Plan-Reviewer, Reviewer, and Observer roles distinct
- `references/stop-and-ask-triggers.md`: conditions that require stopping and asking before drafting or continuing
- `references/template-usage-rule.md`: how to use and complete the topic-plan template without leaving scaffolding
- `examples.md`: detailed good and bad topic-plan scenarios, including stable and non-stable cases
- `checklist.md`: repeatable checks for a higher-risk planning skill
- `templates/topic-plan-template.md`: canonical topic-plan skeleton and section prompts for this repository
