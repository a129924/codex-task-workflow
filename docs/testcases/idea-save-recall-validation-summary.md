# YouTrack Idea 0.2.0 — Public validation summary

This release provides a portable skill-only plugin for private Idea creation, ID-based recall and explicitly authorized existing-Task content updates. It does not synchronize progress automatically, change permissions, close tasks or create duplicates to recover ambiguous writes.

## Results

- Actual skill-creator quick_validate passed for the released skill. JSON parsing and packaged reference-link checks passed. Structural validation does not prove runtime behavior.
- Static checks and model-only scenarios completed within their recorded scope; they do not establish full host behavior.
- A bounded live create/same-ID readback and one authorized description-only update/full readback were observed. Readback matched the expected content; available unrelated fields remained unchanged. Private identifiers, content and environment details are not published.
- TC12 passed for the frozen create/recall diagram: deterministic showcase validation/delivery 9/9, no warnings/errors; four desktop sizes (1440×900, 1600×1000, 1920×1080, 2048×1320) had no overflow. Four smallest/largest light/dark captures were manually inspected. Prior failures remain in local history. This excludes interaction, export and accessibility certification.
- Diagram HTML SHA-256: `145ab8deddab6370d861698749f1b52dad48854b0e730a80d395fe1016ec58a5`. The diagram depicts the earlier create/recall workflow, not the later authorized-update extension.

## Limits

- TC02 remains partial; historical session/snapshot/provenance gaps and a prior private-output handling finding are retained locally. No full TC02 PASS is claimed.
- TC13 uses the approved direct-source/inventory fallback. Graph validation/render/manifest acceptance was not completed and is not claimed.
- Formal output schemas were unavailable. Some client/server version details were not established.
- Ordinary-other-user negative testing was not executed; any accepted privacy substitute is configuration-specific and must not be assumed for another installation. Detailed account, license and ACL observations remain private.
- Update timeout, conflict and cross-session adverse paths are not fully accepted. A prewrite reread cannot eliminate concurrent-write races without conditional revision support.
- There is no blanket product/runtime acceptance claim.

## Publication boundary

Detailed planning, live tenant/Task evidence, license/ACL audits and local operation records are excluded from public Git history. The public summary reports bounded outcomes without tenant URLs, Task/project IDs, account identities, private text or credentials. Full local evidence is retained separately.

## Portable manifest review clarification — 2026-10-16

The review concern that Codex discovery always requires `.codex-plugin/plugin.json` does not apply to the portable package format used here. [Official packaging documentation](https://developers.openai.com/plugins/build/plugins) supports root `plugin.json` with Agent Plugins schemas; the Codex layout is an optional compatibility fallback. Directory-submission metadata requirements are distinct from this local/repository marketplace installation.

The official `codex plugin add youtrack-idea@idea-save-recall-local --json` command was rerun successfully for version 0.2.0. Installed manifest, skill and all three references byte-match the source. Skill quick_validate also passed again. This proves current-client discovery/installation and copied skill files, not universal client compatibility, directory ingestion validation or a new-session behavioral acceptance run. No separate plugin-validator command was available in the installed CLI; it is not claimed as executed. The existing runtime and acceptance limits above remain.

## Core acceptance preparation — 2026-10-19

A new self-contained [core acceptance testcase](TC-YOUTRACK-IDEA-ACCEPTANCE-001.md) defines synthetic save/update baselines, nine-field recovery comparison, A–F preflight and checks, genuine new-session isolation, and bounded stop behavior. This is preparation only: A–F live are NOT_EXECUTED; no new-session recovery or product PASS is claimed. Tester observations and independent Reviewer acceptance remain pending. Historical TC02 partial and all earlier limitations above remain.

Auxiliary diagrams and their actual receipts are retained outside the repository under the approved run evidence index. Graph navigation uses source fallback when no existing graph is available. Diagram validation, diff rendering and visual review are separate evidence classes and cannot establish live acceptance. No installation, account, ACL or runtime changes are part of this preparation.

Actual non-live preparation results: Archify showcase validation and delivery exited 0 with 9/9 checks, zero errors and warnings; the delivered specification and HTML hashes are bound by the external receipt. At initial preparation, its four-size visual-check and manual capture review were NOT_EXECUTED; the actual subsequent FAIL and correction are recorded below. Pinned PR Lens CLI 0.11.0 / renderer 0.3.1 validated and locally rendered one light architecture view from a real three-file working-tree diff, including untracked plan/testcase, with one native content-addressed SVG. No new commit or PR is implied. No existing Graphify graph was found in the bounded checkout inventory, so navigation used current source directly; no graph build/refresh was run. These results do not change A–F live status.

## Core acceptance observations and visual correction — 2026-10-19

Independent Tester evidence supersedes the initial preparation status: A is INCOMPLETE despite all six installed/source files byte-matching and eight input declarations being available. A genuine host API thread loaded the packaged skill/references, but inherited original repository instructions/context, so recovery isolation remains unproven. Formal output schema and complete tool-call trace remain unavailable. B–E are NOT_EXECUTED; no create/update occurred. At that first test phase, private/license applicability and authorization were missing. F had bounded static stop-rule evidence only, with live recovery, model-only and adverse paths unexecuted; no complete core acceptance PASS is claimed.

The original HTML `170d5e80fa9780acf0c25f2f77f787e04995598bd6f9b08b967eaacd11e7f36d` genuinely failed Tester containment and visual review: scrollHeight 1520/1611/1611/1644 exceeded the four viewport heights, and smallest captures clipped the final review node. That FAIL is retained. Following independent Reviewer PATCH_REQUIRED, Implementer compacted the authored layout into two lanes without shrinking text, clipping content or hiding overflow. New HTML `a873039ad747c2a32946a109e0da1504bdd7ed5a626cc53f6cf65b3ba2dc6ece` again passed deterministic validation/delivery 9/9 with no errors/warnings. Its visual-check and manual review await Tester rerun; old visual receipts apply only to the failed original bytes. External manifest preserves the revision and failure binding. Historical TC02 partial and earlier limitations remain.

Subsequent coordination update: the user authorized reuse of the same-project single-user audit and confirmed unchanged configuration; independent Reviewer approved preflight only, and Tester is resuming verification. The observations above preserve the first evidence round. Resumed core results remain pending and will be recorded from Tester evidence; the visual correction does not assign a core verdict.

## Final bounded core evidence synchronization — 2026-10-19

The following supersedes earlier pending statuses while retaining their historical FAIL/PARTIAL/INCOMPLETE evidence. After explicit current-run audit reuse authorization, unchanged-configuration confirmation and independent preflight-only approval, one synthetic S0 Task was created and immediately read back exactly. One authorized description-only update produced exact S1 readback; summary and all 19 available non-scope fields were unchanged. Totals are exactly one create and one update, with no close/delete or permission/configuration changes.

The user selected existing CLI 0.163.0 for two distinct fresh recall Sessions outside the repository, with only the trusted ID, read intent and isolation constraints. Complete native traces show packaged skill reads and one same-ID get_issue per recall, with zero mutation calls. C recovered all nine S0 fields. E read exact S1, but its first summary remains 8 MATCH plus history PARTIAL. One independently authorized generic history follow-up in the same R2 recovered both ordered changes, their reasons and uncompleted validation, with no new tool calls, writes, baseline or evaluator feedback. Independent Reviewer classified this combined evidence as bounded multi-turn PASS; it is not single-turn PASS or final artifact approval. Six installed/source files byte-match and eight input declarations were available. The earlier API repo-context injection remains INCOMPLETE; an earlier 0.162.1 observation was superseded by actual 0.163.0 probe/recall evidence without installation or config changes.

Repaired HTML `a873039ad747c2a32946a109e0da1504bdd7ed5a626cc53f6cf65b3ba2dc6ece` passed Tester visual-check at all four desktop sizes with no X/Y overflow; all four minimum/maximum light/dark captures were actually inspected and passed. The original HTML’s four-size FAIL and clipping remain in history. PR Lens is refreshed against the final real working-tree snapshot without inventing a commit/PR; final artifact rebinding and independent review remain pending. Graphify remains source fallback.

The evidence covers only the recorded synthetic save/recall/update and multi-turn history recovery in the selected CLI environment. Historical TC02 partial remains unchanged. Ordinary-other-user negative testing, model-only and live fault/timeout/unknown-write branches remain NOT_EXECUTED. The reviewed single-user privacy substitute is configuration-specific; license/retention source conflicts and no permanent guarantee remain. Formal output schema is unavailable and no conditional revision eliminates the read/write race. Static stop-rule and live readonly evidence do not establish blanket runtime acceptance, hidden host behavior or universal client compatibility. No private identifiers, URLs, accounts, raw records or thread IDs are published.
