# Plan-Creator Reference

Overview of the stable rules that keep topic-plan authoring aligned with the repository workflow. Detailed rules for each topic are split into the `references/` files listed below.

- **Shared topic-plan contract**: `plan/topic-plan-contract.md` is the repo-level authority for required sections, fallback behavior, and contract-level blocking semantics. Local references in this skill must not redefine that authority.
- **Required section meaning**: what each mandatory topic-plan section means and what it must contain. See `references/required-section-meaning.md`.
- **Stable-library rule**: how to declare stable-library intent absent and stop unsupported promotion. See `references/stable-library-rule.md`.
- **Artifact path rule**: how to declare exact, role-labeled, executable artifact paths instead of vague descriptions. See `references/artifact-path-rule.md`.
- **Correction lifecycle rule**: when a topic uses correction / delta artifacts, keep the workflow body limited to lifecycle / routing contract, list parent and correction artifacts exactly, keep parent-sync closure explicit, and make `review-log` or equivalent handoff conditional on routing-controlling feedback rather than universal.
- **Minimum correction artifact contract**: put field-level requirements in reference / examples, not the workflow body. A repo-visible `*.correction-plan.md` should define at least the trigger / evidence, scope, what stays current, what changes, acceptance delta, affected artifacts, parent-sync note, and retention / closure intent. Add `*.correction-step.md` only when the repair or backfill is multi-step; it should name the ordered repair, backfill, review, and closure checkpoints.
- **Future extraction boundary**: correction-lifecycle refresh topics should update existing workflow / plan surfaces now, not create a standalone correction skill in the same topic. Defer standalone extraction to a later topic only if repeated authoring / review instability or cross-workflow reuse justifies it.
- **Role boundary rule**: how to keep Plan-Creator, Implementer, Plan-Reviewer, Reviewer, and Observer responsibilities distinct, including Implementer-owned `Implementation Steps`. See `references/role-boundary-rule.md`.
- **Examples**: use `examples.md` for field-level correction artifact samples, bounded-path examples, workflow-body versus reference-body separation, and future-extraction boundary examples. Do not embed long correction schemas directly in the workflow body.
- **Stop-and-ask triggers**: conditions that require stopping and asking before drafting or continuing. See `references/stop-and-ask-triggers.md`.
- **Template usage rule**: how to use and complete `templates/topic-plan-template.md` without leaving scaffolding in the final plan. See `references/template-usage-rule.md`.

## Actual mode, authority and drafting

Before any write verify actual active mode, selected feature and exact existing
path authority. Plan Mode and Default without file authority produce complete
frozen-input conversation drafts only; intended paths/state fields are proposed,
not disk existence or actual current-phase/approval evidence. Unknown mode stops
without writes. Reuse existing exact Default authority, no subagent bypass or
new permission request when already authorized. Controlled labels are policy only.
Optional analysis remains optional: warn by name when absent/incomplete, obey
strict baseline routing when supplied, and never invent missing frozen facts.
Only authorized Default revisions change disk analysis; other revisions are
conversation proposals. Incomplete required scope/baseline stops authoring.

Only the authorized plan owner records phase metadata: independent actual start
acknowledgement precedes reviewer-in-progress; native verdict follows resumed
eligible review, then owner records approved/needs-rework. Preserve source body
across review, keep author/reviewer distinct and never create approval/history.

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
