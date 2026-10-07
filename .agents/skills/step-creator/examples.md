# step-creator examples

## Positive: explicit Base

Caller selects base-plan for a complete local 11-section plan with canonical
planned -> creator-in-progress transition, next actor Plan-Creator, stage-local
action and one selector tuple. Destination absent. Render the Base wire,
verbatim implementation items and local-delivery shell with pending markers
when evidence is absent. Do not execute any actions.

## Blocked: unsupported or inferred profile

agent-skill-plan and python-implementation-plan both return BLOCKED before any
write. "Pick the right profile" also stops; never infer from plan content.

## Blocked: source or destination failure

Missing contract, duplicate/nested-only Implementation Steps, competing branch
selectors, an existing destination or source state/action conflict stops before
writing. Never repair/overwrite an existing output or manufacture evidence.
