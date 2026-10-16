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
