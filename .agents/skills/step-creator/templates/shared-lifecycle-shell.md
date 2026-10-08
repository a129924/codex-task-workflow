# Shared lifecycle shell

Sole non-authoritative fixed renderer for the supported base-plan profile.
Resolve <resolved-checkbox> as [X] only with exact evidence, otherwise [ ].
Repeat a single complete tuple in selector-bearing rows and handoff notes:

```text
topic=<topic>; branch=<governed branch>; managed-path-intent=<managed path>; primary-worktree=false
```

## Fixed head

The profile wire owns the heading `### Observer — Fixed Head`. This shell
supplies only these rows:

```markdown
- <resolved-checkbox> **Actor:** Observer — **Action:** Dispatch authorized feature-worktree and branch preparation to Implementer — **Selector:** <complete selector tuple>
- <resolved-checkbox> **Actor:** Implementer — **Action:** Verify the selected feature worktree and attached topic branch before implementation — **Selector:** <complete selector tuple>
```

Planned selectors do not prove creation. A primary/dev worktree never qualifies
as the implementation target. Observer cannot create it directly.

## Fixed tail

Render after Implementation Steps under
`## Observer Actionable Steps — Fixed Tail`:

```markdown
- <resolved-checkbox> **Actor:** Observer — **Action:** Dispatch the declared acceptance checks to Tester with actual artifacts and bounded evidence.
- <resolved-checkbox> **Actor:** Tester — **Action:** Execute the declared checks and report results and limitations.
- <resolved-checkbox> **Actor:** Observer — **Action:** Dispatch the diff, approved plan and test evidence to an independent Reviewer.
- <resolved-checkbox> **Actor:** Reviewer — **Action:** Return a bounded implementation verdict with evidence.
- <resolved-checkbox> **Actor:** Observer — **Action:** Route rework or stop at local reviewable delivery; preserve the feature worktree for human review.
```

No fixed publishing, merge, release or cleanup actions are rendered. Any
separately authorized publishing handoff remains outside this fixed shell.
