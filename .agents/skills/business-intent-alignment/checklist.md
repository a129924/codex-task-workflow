# Business Intent Alignment Checklist

Use this checklist before treating the mode-appropriate requirements baseline as review-ready.

- [ ] The task is business-intent alignment, not technical design, implementation planning, or coding.
- [ ] Actual engine mode is verified; a controlled prompt mode label is not proof.
- [ ] Plan Mode returns a complete conversation draft with intended
  `analysis/<topic>/requirements.md` path, with no file writes/existence claims.
- [ ] Default output requires selected feature worktree and exact authorized path;
  unknown/unverified mode blocks writes and never delegates around the boundary.
- [ ] Every in-scope requirement names an actor, condition, observable result, and metric or decision rule.
- [ ] Soft adjectives such as `fast`, `simple`, `accurate`, or `better` were converted into measurable language.
- [ ] Contradictions were surfaced explicitly:
  - [ ] resolved with a clear decision, or
  - [ ] recorded as blockers instead of hidden in compromise wording.
- [ ] Extreme-boundary checks were applied for at least these cases:
  - [ ] no network or degraded dependency
  - [ ] wrong user role or missing approval
  - [ ] interrupted or partially completed flow
  - [ ] low-volume and peak-volume conditions
- [ ] Assumptions and non-goals are stated clearly enough that technical translation will not need to guess intent.
- [ ] The document does not contain architecture choices, task breakdowns, or implementation estimates.
- [ ] If blockers remain, the baseline says technical translation must roll back or wait; it does not pretend the baseline is fully frozen.
