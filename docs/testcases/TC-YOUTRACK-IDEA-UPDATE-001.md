# TC-YOUTRACK-IDEA-UPDATE-001 — Authorized update

## Scope

Version 0.2.0 supports explicit-ID summary/description updates with same-ID full readback. Read-only requests do not authorize updates. Project, State, ACL, tags, subscription, votes, close and delete are outside this mode. No automatic synchronization or duplicate creation.

| Case | Condition | Expected behavior |
| --- | --- | --- |
| U01 | Explicit ID and authorized progress | Read original, revise snapshot, preserve history, single partial update, exact full readback. |
| U02 | Read-only request or unclear target/content | No mutation; clarify missing intent. |
| U03 | Tool/schema unavailable or unsafe partial-update semantics | Stop; no REST/UI/config workaround or new Task. |
| U04 | Prewrite reread differs from preparation baseline | Stop stale payload; report conflict. Disclose remaining race without conditional revision. |
| U05 | Candidate already matches current | No write; report consistent content. |
| U06 | Update transport ambiguity | Read original ID; no retry, rollback or duplicate creation. Matching content does not prove causation. |
| U07 | Readback mismatch/unavailable or unexpected metadata change | Report verification incomplete/unknown; stop. |
| U08 | New progress supersedes historical failure | Correct current snapshot, append changes, retain history and incomplete-validation limits. |

## Sanitized observations

Skill structural validation passed. One authorized description-only update was observed with matching prewrite baseline and exact same-ID/project/summary/full-description readback. Available custom fields, visibility, tags, reporter and resolution state remained unchanged. Original change history was retained. No duplicate creation or retry.

U01/U08 have bounded observations for one operation, not full-suite acceptance. U03 missing-tool stop was observed and later resolved through explicitly authorized client configuration and reload. U02/U04/U05/U06/U07 adverse branches were not executed as live acceptance. Formal output schemas remain unavailable; there is no conditional revision argument. No independent review of all 0.2.0 behavior is claimed. See the public validation summary for remaining limitations. Private tenant, account, Task and ACL evidence are intentionally omitted.
