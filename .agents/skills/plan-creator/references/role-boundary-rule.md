# Role boundary rule

- Plan-Creator authors and revises topic plans.
- Plan-Reviewer independently reviews planning contracts and returns native JSON.
- Implementer implements bounded code and fixes; Implementation Steps belong to it.
- Tester runs assigned verification; Reviewer independently reviews code/evidence.
- Planner checks readiness; Explorer reads bounded facts.
- Observer dispatches, aggregates evidence and stops at boundaries. It does not
  implement, test, author verdicts or execute Git publication/cleanup itself.
- Code-Implementer / Code-Reviewer are aliases, not extra roles.
- Keep independent verdict/logging and routing outside Implementation Steps.
- A plan's Reviewer Handoff declares the schema, never an author-made approval.
- All roles respect Plan Mode no-write restrictions and authorized write sets.
