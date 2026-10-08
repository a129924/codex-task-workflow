---
name: handoff-routing-policy
description: "Choose the next allowed role or stop after one explicit subagent result."
complexity: medium
---

# Purpose

Choose the next route after one explicit subAgent result.

This skill works only after a real dispatch has already occurred and a result
payload has been returned.

# Trigger / When to use

Use this skill when:

- one explicit subAgent result has been returned
- the Observer is in `ROUTING`
- the result includes one frozen verdict value

Do not use this skill when:

- the task is still deciding whether to dispatch
- the task is to build the context package
- the task requires full workflow reconstruction or runtime orchestration logic

# Inputs

- `result_role`: one of `Planner` | `Plan-Creator` | `Plan-Reviewer` | `Implementer` | `Reviewer` | `Tester` | `Explorer`
- `verdict`: one of
  - `approved` (native Plan-Reviewer only)
  - `needs-rework` (native Plan-Reviewer only)
  - `PASS`
  - `PATCH_REQUIRED` (independent Reviewer / Code-Reviewer only)
  - `REPLAN_REQUIRED` (independent Reviewer / Code-Reviewer only)
  - `MISSING_EVIDENCE`
  - `BLOCKED`
- actual returned actor identity and genuine parent dispatch/returned-result correlation
- actual author identity for every Reviewer / Code-Reviewer / Plan-Reviewer verdict; actual returned reviewer must differ from author
- bounded evidence summary
- explicit blocker list, if any
- optional evidence owner for `MISSING_EVIDENCE`
- explicitly declared next role for PASS: Implementer requires Tester; Tester requires Reviewer (normalize Code aliases); other compatible PASS keeps its bounded declaration
- for REPLAN_REQUIRED: current source/body/version, known authorized Plan-Creator owner, eligible canonical rework source or distinct new canonical topic/path intent with complete frozen initial inputs and exact existing mode/root/path authority
- for native approved: genuine native/reviewer proof, authorized owner transition, reviewed/approved snapshots and readable current approved source with version/body binding; explicit Implementer (or Code alias) next role

# Process

1. Confirm actual actor identity and genuine parent dispatch/returned-result
   correlation before routing. Bind the actual bounded task, dispatched actor
   and returned result using exposed receipts or retained parent task/result
   provenance. A role label is not proof. Unexposed provider request IDs are
   disclosed, never fabricated or replaced by registry/launcher identifiers.
   Missing linkage or actor identity stops. Every verdict owned by Reviewer
   (including Code-Reviewer) or Plan-Reviewer also requires actual author identity
   distinct from that actual returned reviewer. This applies to PASS, approved,
   needs-rework, PATCH_REQUIRED, REPLAN_REQUIRED, MISSING_EVIDENCE and BLOCKED
   wherever role-compatible; missing/same-author proof stops before routing.
   Bind the task, returned evidence/artifact version and actual author; role or
   verdict labels do not prove independence. Other-role PASS keeps its actual
   correlation; the Implementer-to-Tester-to-Reviewer successor gate below still
   applies before any route.
2. Confirm the result role is permitted (normalize only Code-Implementer and
   Code-Reviewer aliases) and the verdict is role-compatible. approved and
   needs-rework belong only to Plan-Reviewer; Plan-Reviewer returns native
   JSON rather than PASS. PATCH_REQUIRED and REPLAN_REQUIRED belong only to
   independent Reviewer (including normalized Code-Reviewer). Other non-plan-
   review roles use PASS, MISSING_EVIDENCE or BLOCKED; their PATCH_REQUIRED or
   REPLAN_REQUIRED is incompatible and stops. Unknown/incompatible results
   stop; do not infer or normalize verdict spelling.
3. If the result reveals runtime semantics, registry behavior, workflow binding,
   or another out-of-scope expansion, stop.
4. Route by verdict without inventing a broader workflow model:
   - `approved`: route only when the declared next role is explicitly
     `Implementer` (normalize Code-Implementer); every other or missing next
     role stops. Before returning Implementer, verify the genuinely returned
     native/reviewer proof and authorized owner-recorded reviewer-in-progress
     to approved transition. Bind the reviewed snapshot/version to actual review,
     current whole source to owner-approved snapshot, and identical bytes outside
     the exact authorized Status metadata to the reviewed body. Legitimate
     Status-only changes may change whole hashes. Native approval alone, current
     reviewer-in-progress, absent/stale owner evidence or mismatched body stops
     awaiting owner proof; routing never writes status or invents approval.
     Keep the native verdict; never convert it to PASS
   - `needs-rework`: route to `Plan-Creator`
   - `PASS`: Implementer (including Code-Implementer) routes only to explicitly
     declared Tester; Tester routes only to explicitly declared Reviewer
     (normalize Code-Reviewer). Missing/wrong successor stops, even if permitted
     for other tasks. This preserves Implementer -> Tester -> independent
     Reviewer. Independent Reviewer and other compatible nonimplementation PASS
     retain their explicit bounded permitted-role route or stop.
   - `PATCH_REQUIRED`: only independent Reviewer routes to `Implementer`
   - `REPLAN_REQUIRED`: only a genuinely correlated independent Reviewer may
     route to Plan-Creator, and only after checking an eligible destination:
     known authorized Plan-Creator ownership of a current canonical planned or
     needs-rework source with a valid authoring edge/action, OR an explicitly
     distinct new canonical topic/plan path and complete frozen initial planned
     authoring inputs under exact existing mode/selected-root/path authority.
     Bind the actual verdict/task/author, old source body/version and destination
     baseline/version; new intent must identify outcome, scope, locked decisions,
     artifact paths, contracts and optional-analysis disposition without guessing.
     A new planned intent is not a created phase or approval. The old approved
     source/body/approval/step remains immutable with no outgoing planning edge.
     Missing/ambiguous owner, authority, destination or baseline stops; REPLAN
     itself grants no write authority or approved-to-creator transition.
   - `MISSING_EVIDENCE`: route only to the bounded role that can supply the
     missing evidence; if that owner is unknown, stop
   - `BLOCKED`: stop
5. Emit exactly one next role or `stop`, with a short factual reason.

# Examples

- **Positive**: An independent `Reviewer` returns `PATCH_REQUIRED` with concrete bounded
  evidence, and the skill routes to `Implementer`.
- **Negative**: A result says "probably approved" with no explicit verdict, and
  the skill refuses to invent one.

# Outputs

- `next_role`: `Planner` | `Plan-Creator` | `Plan-Reviewer` | `Implementer` | `Reviewer` | `Tester` | `Explorer` |
  `stop`
- `reason`: short factual reason
- `stop_condition`: `none` or exact blocker

# Validation

## Required Checks

- `PASS`: the result came from real dispatch, the Observer is in `ROUTING`, the
  verdict is exactly one frozen allowed value, and the skill returns exactly
  one allowed `next_role` or `stop` consistent with the stated verdict.
- BLOCKED: stop when actual dispatch/result correlation or actor identity is
  missing, or any review-role verdict lacks actual distinct reviewer/author proof;
  stop when the verdict is unknown, unstructured, or unsupported;
  when the evidence owner for `MISSING_EVIDENCE` is unknown; or when proceeding
  would require invented workflow state, registry behavior, runtime semantics,
  or a broader routing model than this skill allows.

## Quality Checks (best effort)

- `SOFT FAIL`: mark status as `INCOMPLETE` when the allowed verdict is clear
  enough to route or stop, but the bounded evidence summary or blocker detail is
  incomplete. Identity/correlation/required independence are hard preflight
  inputs and never eligible for this soft-fail route. Required owner-approved
  source binding, REPLAN destination/owner/authority/frozen-input eligibility
  and implementation-chain successors are also hard gates.
- Under `SOFT FAIL`, keep the routing decision within the frozen verdict set,
  state the missing evidence explicitly, and avoid inventing additional workflow
  state.

# Failure Handling

## Missing Context

- Missing actual linkage, actor identity or required Reviewer independence
  is BLOCKED and stops; no best-effort route.
- Only after hard preflight may partial non-routing supporting detail allow a
  bounded route or stop with the limitation stated explicitly.
- If missing context could reasonably change the next allowed role, mark the
  result `BLOCKED` and stop.

## Ambiguous Requirement

- If the returned result does not contain one frozen verdict value, do not infer
  or normalize it into the allowed set.
- If `MISSING_EVIDENCE` lacks a known bounded owner, stop instead of inventing
  one.

## Execution Limitation

- If the request depends on hidden workflow state, file-path ownership, registry
  identifiers, launcher-specific targets, or runtime orchestration details,
  return `stop` or `BLOCKED` with the limitation stated explicitly.
- Do not fabricate broader workflow progression beyond the single returned
  subAgent result.

# Boundaries

- Do not choose the initial dispatch role.
- Do not build the context package.
- Do not reconstruct the full existing workflow from a step artifact.
- Do not invent verdict values outside the frozen set.
- Do not emit registry identifiers, file paths, or launcher-specific targets.

# Local references

- `examples.md`: verdict-driven routing examples, including stop conditions for
  missing evidence and out-of-scope expansion

## Mode and evidence-owner boundary

MISSING_EVIDENCE routes only to its known, permitted bounded evidence owner;
unknown or incompatible owners stop. Real dispatch and result identifiers
must exist. All routes obey current mode: Plan Mode permits no writes for any
role. Code role aliases do not create new verdicts or extra roles.
