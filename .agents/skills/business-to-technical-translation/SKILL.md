---
name: business-to-technical-translation
description: "Translate a frozen business baseline into a technical specification; surface feasibility conflicts."
complexity: medium
risk_profile:
  - ambiguity_sensitive
use_when:
  - "a readable frozen requirements file, or an explicitly identified complete frozen conversation draft in actual Plan Mode, is available for technical translation"
  - the workflow needs explicit technical tasks, artifacts, constraints, and dependency mapping before execution planning starts
  - architecture fit, delivery cost, or operational burden must be tested against the business baseline
  - the request needs a pessimistic implementer view instead of optimistic solution selling
do_not_use_when:
  - the business baseline is missing, contradictory, or still vague; route back to `business-intent-alignment`
  - the task is direct implementation, coding, or runtime debugging
  - the main work is architecture invention without a frozen baseline to translate
inputs:
  - topic name and intended `analysis/<topic>/technical-spec.md` path
  - "readable frozen requirements file, or complete identified frozen conversation requirements draft in actual Plan Mode"
  - current repository, platform, or system constraints that the design must obey
  - available architecture rules, dependency boundaries, and compliance obligations
  - staffing, timeline, integration, operational, and cost constraints
  - known failure tolerances, rollback expectations, and non-negotiable business priorities
outputs:
  - "technical baseline: conversation draft with intended path in Plan Mode; authorized feature file in Default"
  - requirement-to-technical mapping with tasks, artifacts, and dependency notes
  - cost-of-realization and feasibility constraints for each major workstream
  - architecture-compliance results, conflicts, and rollback-to-alignment triggers
---

# Purpose
Turn a frozen business baseline into a technical specification that names the required engineering work, feasibility constraints, and rollback triggers.

# Trigger / When to use
Use this skill when:
- a readable frozen requirements file, or an explicitly identified complete frozen
  conversation draft in actual Plan Mode, is available for technical translation
- the workflow needs explicit technical tasks, artifacts, constraints, and dependency mapping before execution planning starts
- architecture fit, delivery cost, or operational burden must be tested against the business baseline
- the request needs a pessimistic implementer view instead of optimistic solution selling

Do not use this skill when:
- the business baseline is missing, contradictory, or still vague; route back to `business-intent-alignment`
- the task is direct implementation, coding, or runtime debugging
- the main work is architecture invention without a frozen baseline to translate

# Inputs
- verified actual active engine mode; for Default output, selected feature worktree
  and exact authorized output path
- topic name and intended `analysis/<topic>/technical-spec.md` path
- readable frozen `analysis/<topic>/requirements.md`, or in actual Plan Mode an
  explicitly identified complete frozen conversation requirements draft with
  intended path and content identity; no fabricated file or disk-read claim
- current repository, platform, or system constraints that the design must obey
- available architecture rules, dependency boundaries, and compliance obligations
- staffing, timeline, integration, operational, and cost constraints
- known failure tolerances, rollback expectations, and non-negotiable business priorities

# Process
0. Verify actual active mode before artifact output. In Plan Mode return only a
   conversation technical-spec draft with intended path and frozen-input identity;
   never write files or delegate around the no-write boundary. Default file output
   requires selected feature worktree and exact authorized path. Unknown/unverified
   mode blocks file output. Controlled mode labels are not actual engine evidence.
1. Confirm the task is technical translation, not business discovery or implementation. If the baseline is missing, vague, or contradictory, stop spec authoring and route back to `business-intent-alignment` with the exact gap.
2. Adopt a pessimistic implementer posture. Assume hidden coupling, operational cost, migration effort, and failure handling all count until proven otherwise.
3. Map each requirement to the minimum technical realization: components, interfaces, data changes, operational dependencies, validation artifacts, and owner-facing tasks.
4. Estimate the cost of realization for each major workstream in concrete terms: complexity, sequencing, staffing pressure, integration burden, and ongoing operational overhead.
5. Run an architecture-compliance self-check against existing standards, boundaries, and supported patterns. Name every fit, mismatch, waiver need, and missing prerequisite explicitly.
6. Detect conflicts between technical reality and business intent, including schedule impossibility, platform limitations, security/compliance gaps, data constraints, and rollback-risk surfaces.
7. When conflicts are material, trigger rollback to alignment instead of forcing a false technical plan. State which business assumption failed, what must be renegotiated, and which work remains blocked.
8. Produce the technical baseline with traceability, tasks/artifacts, feasibility,
   architecture-compliance results, conflicts and rollback triggers. Actual Plan
   Mode returns a complete conversation draft with intended
   `analysis/<topic>/technical-spec.md` path; Default writes only the exactly
   authorized feature path. Do not turn conversation input/output into file claims.

# Examples
- **Positive**: Translate a frozen offline-order baseline into a technical spec that names local-storage needs, sync tasks, architecture fit checks, staffing pressure, and a rollback trigger if secure offline storage is unavailable on the approved platform.
- **Negative**: Invent a technical plan from a vague request, ignore platform mismatch because the feature is `strategic`, or skip cost and rollback analysis because the team can `figure it out during implementation`.

# Outputs
- mode-appropriate implementation-facing technical baseline: conversation draft
  with intended path in Plan Mode, or exactly authorized feature file in Default
- requirement-to-technical mapping with tasks, artifacts, and dependency notes
- cost-of-realization and feasibility constraints for each major workstream
- architecture-compliance results, conflicts, and rollback-to-alignment triggers

# Verification
- confirm every business requirement maps to concrete technical work or an explicit blocker
- confirm cost, sequencing, and operational burden are stated instead of implied
- confirm architecture-compliance self-check results are explicit
- confirm material conflicts trigger rollback guidance instead of optimistic hand-waving

# Red Flags
- the spec proceeds even though the business baseline is missing or contradictory
- the plan assumes architecture exceptions without naming them
- feasibility risk is hidden behind generic words such as `straightforward` or `minor`
- the document promises delivery without naming integration, migration, or operational cost

# Common Rationalizations
- `We can estimate after implementation starts.`
- `Architecture exceptions are just details.`
- `If the requirements and platform disagree, we can build around it later.`
- `The business baseline is close enough even though success still is not technically testable.`

# Boundaries
- Do not silently rewrite business intent to make implementation easier.
- Do not continue when the baseline is too vague to translate honestly.
- Do not start coding, scaffolding, or runtime execution.
- Do not hide impossible scope behind optimism or omit rollback triggers.

# Validation

## Required Checks
- PASS: before decomposition, actual mode is verified and the frozen input is
  readable requirements file content, or in actual Plan Mode a complete explicitly
  identified frozen conversation draft; its intended path is not a disk existence claim
- Default file output requires exact authorized selected-feature path; Plan Mode
  never writes, and unknown/unverified mode blocks writes
- BLOCKED: if the business baseline is missing, vague, or internally contradictory — stop spec authoring and route back to `business-intent-alignment` with the exact gap named

## Quality Checks
- every business requirement maps to concrete technical work or an explicit blocker
- cost, sequencing, and operational burden are stated rather than implied
- architecture-compliance self-check results are explicit
- material conflicts trigger rollback guidance rather than optimistic hand-waving

## On Soft Fail
- mark output as INCOMPLETE if partial technical tasks can be mapped but one or more requirements remain untranslatable without further clarification
- list each untranslatable requirement explicitly rather than silently omitting it

# Failure Handling

## Missing Context
- BLOCKED — if no readable frozen requirements file or permitted complete frozen
  conversation baseline is supplied, stop and route back to business-intent-alignment.
  Missing, vague or unfrozen conversation input also blocks; never invent a file.

## Ambiguous Requirement
- if a requirement is present but too vague to translate honestly, surface the specific ambiguity and stop rather than proceeding with guesswork
- if platform constraints or architecture rules are missing and their absence would change the feasibility result, name them as required inputs before continuing

## Execution Limitation
- if architecture-compliance rules are unavailable, mark the compliance section as INCOMPLETE and flag that a full architecture check could not be performed; do not omit rollback triggers because rules are missing
- do not force a technical plan when the baseline is too vague; return the vague requirements as explicit gaps

# Local references
- `reference.md`: stable rules for frozen-baseline gating, technical-spec shape, cost framing, architecture self-checks, and rollback behavior
- `examples.md`: detailed pessimistic-implementer scenarios, including conflict detection and rollback-to-alignment cases
- `checklist.md`: repeatable medium-risk misuse-prevention checks before declaring the technical spec review-ready
