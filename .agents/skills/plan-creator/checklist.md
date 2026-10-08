# Plan-Creator Checklist

Use this checklist when drafting or sanity-checking a topic plan before handing it to a reviewer or the Observer for execution.

- [ ] Actual mode and exact existing selected-feature write authority checked first; Plan or Default without authority returns conversation-only draft, unknown mode stops without writes.
- [ ] The topic plan is an authorized Default file, or an intended-path conversation draft (proposed state, no existence/current-phase/approval claim) at `plan/<topic>/<topic>.plan.md`.
- [ ] `Goal / Outcome`, `Scope`, `Locked Decisions`, and `Boundaries / Exclusions` are explicit.
- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [ ] Written current status matches actual phase; conversation-only fields remain proposed. Owner records reviewer-in-progress only after genuine independent start acknowledgement, then approval only after returned native verdict.
- [ ] `Artifact Paths` are exact, repo-visible, and role-labeled, not catch-all labels.
- [ ] If correction artifacts are used, each parent artifact, correction artifact, and any review-log / equivalent handoff artifact is listed with an exact path, owner, and role.
- [ ] If correction artifacts are used, the minimum correction artifact contract is defined in reference / examples: `correction-plan` covers trigger, scope, what stays / changes, acceptance delta, affected artifacts, parent sync, and retention intent; `correction-step` appears only when multi-step repair / backfill is needed.
- [ ] `Implementation Steps` stay Implementer-owned; reviewer verdict logging, reviewer acceptance work, and Observer routing work are not written into Implementer steps.
- [ ] When correction lifecycle text appears in the plan, the workflow body stays slim and does not become a field-by-field correction artifact schema dump.
- [ ] Parent-sync closure is explicit when correction artifacts are used: parent artifacts return to current truth only after backfill.
- [ ] `review-log` or equivalent handoff is required only when reviewer feedback controls routing or multi-round rework.
- [ ] Any round cap is declared as topic policy, not as a repository-wide default.
- [ ] Correction-lifecycle refresh topics explicitly defer any standalone correction skill to a later topic unless repeated instability or cross-workflow reuse justifies extraction.
- [ ] Stable-library intent is explicit:
  - [ ] clearly absent for non-stable topics, or
  - [ ] declared with timing when stable-library surfaces are involved
- [ ] `Reviewer Handoff` is a single JSON object contract.
- [ ] `Post-merge / release actions` match the actual topic scope and timing.
- [ ] Plan-Creator, Implementer, Plan-Reviewer, Reviewer, and Observer roles are not mixed.
- [ ] No placeholder wording remains where workflow needs a real contract.

- [ ] Optional analysis remains optional, with named absent/incomplete-layer warnings;
  complete explicitly frozen input is used without inventing missing analysis facts.
- [ ] All baseline/analysis revisions obey the same exact Default authority gate;
  draft-only proposals never claim that files or recorded baselines changed.

- [ ] Immediately before EVERY plan/analysis/owner-phase write, mkdir, temp creation and promotion, recheck Default mode, verified canonical selected root and exact lexical/resolved destination authority.
- [ ] Target and parent symlink chains (or strict nearest existing ancestor plus exact prospective suffix) are inside the selected root; resolved destination matches existing canonical authority.
- [ ] Escapes, development/external aliases, dangling/unreadable/ambiguous components stop before mutation; no earlier batch check substitutes for each operation.
- [ ] The containment gate is prompt policy only; no executable sandbox or unprovoked race-proof claim.
