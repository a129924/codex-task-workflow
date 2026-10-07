# Development agent handoff workflow

This contract applies only to repo-local development tools. It does not govern
Task product records or require the Task product to use planning artifacts.

## Roles and mode

Observer only inspects, dispatches one bounded task, aggregates evidence and
stops at boundaries. Allowed dispatched roles: Planner, Plan-Creator,
Plan-Reviewer, Implementer, Tester, Reviewer, Explorer. Code-Implementer and
Code-Reviewer are aliases for Implementer and Reviewer. Independent review
must use a different agent from the author. Planner checks planning sufficiency
and readiness; Plan-Creator authors plans; Plan-Reviewer reviews planning
contracts; Implementer writes bounded implementations/fixes; Tester executes
assigned verification; Reviewer reviews code and evidence; Explorer reads.

Plan Mode prohibits writes, commits, pushes and PR creation for all roles;
Plan-Creator drafts only in conversation. No subagent bypasses this boundary.
In execution mode writes require an authorized exact write set and selected
feature worktree. Never implement in the dev worktree.

## Planning states and handoff

Canonical transitions are:

- planned -> creator-in-progress (Plan-Creator drafts or revises the topic plan)
- creator-in-progress -> review-ready (complete plan and explicit review inputs)
- review-ready -> reviewer-in-progress (independent Plan-Reviewer starts)
- reviewer-in-progress -> approved (native JSON verdict approved)
- reviewer-in-progress -> needs-rework (native JSON verdict needs-rework)
- needs-rework -> creator-in-progress (Plan-Creator applies bounded plan fixes)

Every plan declares one current status, its valid next transition(s), one next
actor and one stage-local action. No unverified gate can be declared passed.
The author may provide the reviewer JSON schema but never author a real verdict.
At approved the planning state is terminal: allowed next planning transitions
is explicitly [] or none. The next actor is Implementer with the source-declared
bounded implementation action. This is an execution handoff, not a new planning
transition or state-machine. An approved source with these fields is eligible
for Base step creation; no outgoing approved planning edge is required.

## Implementation and local delivery

Only an approved plan may be handed to Implementer. The implementation handoff
contains exact plan/spec paths, write/read-only sets, locked decisions, selected
feature worktree and required acceptance evidence. Implementer returns changed
paths, limitations and verification evidence. Observer sends the bounded test
request and actual artifacts to Tester, then sends the diff, plan and test
results to an independent Reviewer. Reviewer returns PASS, PATCH_REQUIRED,
REPLAN_REQUIRED, MISSING_EVIDENCE or BLOCKED with evidence. PATCH_REQUIRED goes
to Implementer; REPLAN_REQUIRED goes to Plan-Creator; MISSING_EVIDENCE goes to
its known owner, otherwise stops. PASS permits the explicitly declared next
handoff or stops at local reviewable delivery. It does not imply publication.

Publication, human merge, release, branch deletion and worktree cleanup are
not automatic phases of this development contract. Separately authorized
commit/push/Draft PR work is dispatched to Implementer and stops for human
review; never silently add merge, release or cleanup. Retain the feature
worktree for that review. A separately requested publishing lifecycle requires
its own explicit topic contract; this contract defines no publish-state model.

## Real dispatch and routing

A real handoff requires separated role instructions, bounded context, explicit
handoff and result payloads. Keep a dispatch/result identifier as evidence.
No simulation or a text-only role label counts as actual dispatch. Select one
allowed role or stop; no registry, hidden launcher binding or fabricated state.
Native approved/needs-rework are allowed only from Plan-Reviewer. approved
routes to an explicitly declared next role or stop; needs-rework to Plan-Creator.
Unknown, role-incompatible or BLOCKED results stop. All artifacts and tests
remain evidence-pending until actual execution and independent review.
