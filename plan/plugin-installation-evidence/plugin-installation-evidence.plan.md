# plugin-installation-evidence

計畫作者與 phase owner：Plan-Creator `/root/plan_creator_provenance`。本文件只授權明列的 feature 寫入；規劃核准與實作驗證分開。

**Semantic warning — INCOMPLETE analysis layer：**選用的 `analysis/plugin-installation-evidence/requirements.md` 與 `analysis/plugin-installation-evidence/technical-spec.md` 均不存在。本計畫依凍結需求起草；此警告本身不阻擋規劃，不新增 analysis 檔案。

## Goal / Outcome

產出獨立、去識別且可自行閱讀的 `docs/youtrack-idea-installation-evidence.md`，區分目前 Codex CLI 的安裝觀察、有效啟用支持程度、宣告設定與歷史來源，每項結論均可追溯至來源及 context。

完整記錄未知、停用、缺 receipt、不可取得或來源衝突，均可構成有效交付；不要求所有觀察為正向。Archify、PR Lens、Graphify 僅輔助理解與審閱，不取代主要證據或 Tester／Reviewer 判定。

## Scope

實際報告必須包含以下九個具名欄位；放入報告既有結構，不另增九個 topic-plan 必要章節：

| 報告欄位 | 必要內容 |
| --- | --- |
| `Goal` | 本題證據清晰、可追溯的交付目的 |
| `Non-Goal` | 不建立產品功能、不保證全部狀態為正向 |
| `In-Scope` | 單一主機 CLI 限定觀察、既有證據重用、報告與私人 review aids |
| `Out-Of-Scope` | desktop／host matrix、neutral-directory 比較、安裝／註冊／登入／啟停／設定修復、live Task、新 session、bytes 重驗、core summary 修改及新 test suite |
| `ReadOnly` | 固定來源、限定設定／host context、可用既有 graph 與必要既有 overlay |
| `Written` | 新 plan（Plan-Creator）、新 report（Implementer）及明列的私人 outputs；區分 owner |
| `Modify` | 既有 tracked files 預期無；依最終 diff 如實記錄，新增檔不假列修改 |
| `Deleted` | 預期無，依最終 diff 核對 |
| `TestCase` | 同份報告內的人工驗證表，採下述欄位與案例，不另建測試檔 |

保留既有 README commit／push 成果及其他 topic。Plan owner 的 phase 更新不授予 Implementer 額外寫入權。

## Locked Decisions

1. `FEATURE` 是本計畫所在的已選定 feature worktree，branch 為 `docs/a129924/plugin-installation-evidence`，base 為 `0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a`；相對原始 repo 的位置為 `../codex-task-workflow.worktrees/agent-20261019-plugin-installation-evidence`。命名符合 `docs/<既有 namespace a129924>/<三字 kebab-case>`；不切換 dev branch，也不重建既有 FEATURE。
2. `OBS` 固定為 Git common-dir 所屬的原始 `dev` main worktree，亦即凍結交接的原始 repo；不是 FEATURE，也不另選 neutral directory。執行時須以凍結 locator 核對其 realpath，再於私人 `context.json` 綁定 OBS／FEATURE 的 exact roots、common-dir、branch／HEAD；public report 僅使用 aliases。禁止從 FEATURE cwd 查詢後宣稱 OBS 的有效狀態。Remote branch 衝突未新查，發布前另行驗證。
3. preflight 為 CLI `0.163.0`、macOS `26.5.2`；執行時重驗 binary／版本、OS、UTC、cwd／HEAD、profile／config context，不注入 overrides。版本漂移只記錄，不升降級或回填歷史。
4. catalog 名稱 `idea-save-recall-local` 不證明已註冊；plugin 宣告為 `youtrack-idea` `0.2.0`。首次 inventory 固定從 OBS 執行：

   ```sh
   codex plugin list --marketplace idea-save-recall-local --json
   ```

   不使用 `--available`，只檢查實際目標項目，保留 stdout、stderr、exit 與 warnings。
5. installed、runtime 有效啟用、宣告式 config／trust／profile 值及未知／衝突分開。只有欄位語意與 cwd／config scope 足夠明確，才能支持有效啟用；單獨 `enabled` 或設定值不足。
6. 查詢時間、安裝事件時間、文件日期與 filesystem metadata 分開；`mtime` 不作安裝時間。缺 receipt 維持未知，不重新安裝補歷史。
7. 本題為 local 文件工作，stable-library intent absent；穩定發布需另有核准 contract。本 session 已授權的 topic commits／push／Draft PR 依後述條件執行，不授予 merge／release／cleanup。

## Boundaries / Exclusions

Plan-Creator 作者、獨立 Plan-Reviewer 審規劃；Implementer 蒐集與撰文，Tester 查核，獨立 Reviewer 判定實作，Observer 協調路由。只有真正獨立 planning approval 後才能進行 implementation。

設定僅經官方 provenance 入口或限定相關鍵值 allowlist 讀取；不 dump 完整 config、不掃 home、不逆向私人 storage、不蒐集 credential。沒有可靠入口就記錄未知；查詢需要未授權寫入時停止該觀察，不修權限。

缺 marketplace、不支援、非 JSON、錯誤、warning、模糊項目或無匹配，均保留實際結果。無匹配只有在查詢 scope 與完整性成立時，才支持該限定範圍未安裝。

工具不得安裝／升級、修改 config／PATH／hooks、呼叫 provider、上傳或啟動 server。PR Lens 保持 local-only；另獲本 session 授權的 GitHub CLI／API Draft PR 動作，依 Post-merge / release actions 處理，不透過 PR Lens。工具失敗、跳過與 fallback 各自如實記錄，不預判通過。

## Status / Allowed Transitions

- **Current：**`approved`（planning terminal）。
- **Execution model：**Plan-Creator → independent Plan-Reviewer；真正核准後 Implementer → Tester → independent Reviewer → 已授權 topic commits／push／Draft PR → human review。
- **Next actor：**Implementer。
- **Stage-local action：**Implementer 僅在 FEATURE 依本 approved plan 蒐集限定唯讀證據、建立明列私人 evidence／review aids，並撰寫 `docs/youtrack-idea-installation-evidence.md`；不得修改本 terminal approved plan 或擴大 scope。
- **Allowed next planning transitions：**`[]`（none；approved 為 terminal，後續是 bounded implementation handoff）。
- **Phase owner：**Plan-Creator `/root/plan_creator_provenance`。

每次建立目錄、寫入或更新 phase 前，重驗實際 Default mode、既有 exact authority、FEATURE canonical root 及 target／parent symlink containment；模糊或越界即停止，不在 dev worktree 實作。只有收到實際獨立 start acknowledgement 後，owner 才能更新 reviewer-in-progress；只有收到該 reviewer 的 native verdict 才能記錄 approved／needs-rework。

作者實際 phase 記錄（UTC；僅記本次落盤後發生的動作）：
- `2026-10-19T03:47:59.191991+00:00`：建立 planned source。
- `2026-10-19T03:47:59.210505+00:00`：planned → creator-in-progress。
- `2026-10-19T03:47:59.230360+00:00`：creator-in-progress → review-ready。
- `2026-10-19T03:49:25.425866+00:00`：review-ready → reviewer-in-progress；owner 依 Observer `/root` 本次實際 handoff 轉交的獨立 start acknowledgement 記錄。Reviewer `/root/plan_reviewer_provenance` 已讀取實際 plan 與兩份 contracts，與作者為不同 agent，並確認 start 時 whole-file SHA-256 `bb91a3fda724dcc982850d2f38e1b654605910440bacba3e1d4aeabfe17fd306`、body-binding SHA-256 `dba6ea106c7a59c21524515b6f0db1a4d50ec826a1853bad302b8f6cfdc95f8c`。此記錄不是審查 verdict。
- `2026-10-19T03:50:21.884287+00:00`：reviewer-in-progress → approved；owner 依 Observer `/root` 本次實際 handoff 轉交並保留的獨立 Plan-Reviewer `/root/plan_reviewer_provenance` 原生 `approved` JSON 記錄。該 native verdict 的 `blocking_issues` 與 ADDRESS／DISCUSS／SKIP 均為空陣列；reviewed whole-file SHA-256 `d8ad5cab80b419cb335f6467a789b7648abe40da5877aa6577d620548b57521f`、body-binding SHA-256 `dba6ea106c7a59c21524515b6f0db1a4d50ec826a1853bad302b8f6cfdc95f8c`。本記錄來自真正獨立 review result，不是作者自評；不代表實作或測試已執行。

## Artifact Paths

| Repo output | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plugin-installation-evidence/plugin-installation-evidence.plan.md` | Plan-Creator | 規劃契約及 owner phase 記錄 |
| Report | `docs/youtrack-idea-installation-evidence.md` | Implementer | 去識別、自足的證據文件 |

僅以上兩個 FEATURE repo outputs；不改 README、VERSION、plugin、共享 summary，不新增 step、analysis、測試檔或 repo 圖檔。路徑漂移停止並回到 bounded plan revision。

私人根目錄採 `/private/tmp/plugin-installation-evidence-<UTC YYYYMMDDTHHMMSSZ>-<UUIDv4>/`；建立前凍結完整 literal realpath，確認 checkout 外、無既有目標／symlink，不覆寫。基本檔案維持：

- Implementer：`manifest.json`、`context.json`、`plugin-list.stdout.json`、`plugin-list.stderr.txt`、`provenance-observations.json`。
- Tester：`verification.json`。

本題明確擴充 Implementer 私人 allowlist：

- `aids.json`：工具版本、實際 executable locator、命令／結果／fallback、輔助檔 exact 路徑與 digest。
- `archify/workflow.json`、`archify/workflow.html`、`archify/validation.json`、`archify/delivery.json`、`archify/visual-check.stdout.json`；另僅允許工具在同目錄產生的 snapshot、四張截圖、contact sheet 與 receipt sidecars，逐項納入 manifest。
- `pr-lens/graph.json`、`pr-lens/validate.txt`、`pr-lens/render.txt`；`pr-lens/rendered/` 僅接受實際 render manifest 列出的檔案，逐項索引與 hash。
- Graphify query／fallback 記錄直接寫入 `aids.json`，不新增 graph／cache。

manifest 保存 exact locators、完整 hashes 與未產生原因；context 保存 binary／版本／OS／UTC／cwd／HEAD／profile／config provenance。非 JSON stdout 亦原樣保存並記 parse failure。私人內容不進 repo，不複製 raw core 證據。

唯讀來源綁定 `OBS@0d3ca3d`、固定 `CORE@655cbf3`，實際 realpaths、完整 commit IDs 與逐檔 hashes 留私人 index，重用時重驗：

- OBS：`plugins/youtrack-idea/README.md`、`plugins/youtrack-idea/plugin.json`、`.agents/plugins/marketplace.json`、`docs/testcases/idea-save-recall-validation-summary.md`（H）。
- CORE：`plan/idea-core-acceptance/idea-core-acceptance.plan.md`（CP）、`docs/testcases/TC-YOUTRACK-IDEA-ACCEPTANCE-001.md`（CT）、`docs/testcases/idea-save-recall-validation-summary.md`（CS）。
- 必要官方入口／allowlisted 設定、host context、fresh existing graph；若存在才讀 `.github/pr-lens.yml`。

CORE 固定來源完整 commit 為 `655cbf36eec4e8065b8d54c41aa638d394c452bf`。最新上游交接觀察該 worktree 已至 `9ad3322863e0ab96dd65f8b66c53b275dcf5b378`；不得直接把目前 worktree 檔案冒稱固定來源。優先以可讀 Git object 取得指定 commit 的必要來源，核對逐檔 hash；無法取得即記錄限制／衝突，不 checkout、不修改 core。CP 所指私人記錄只讀本題必要內容，且須綁定其實際版本；來源不符不冒稱 frozen bytes。

## Implementation Steps

1. **確認 context 與來源。**從 OBS 重驗版本、help、cwd／HEAD、realpaths、設定 scope 與時間，保留 stdout／stderr／exit，包括 PATH alias permission warning；建立私人 index。Graphify 僅用 skill 指定的 pinned `0.9.73` runtime，每次 CLI 呼叫均設 `GRAPHIFY_NO_AUTO_REFRESH=1`。只查 fresh existing graph、budget ≤1500，核對 revision／coverage／source paths，重要關係再讀來源；無 graph、過期或缺相關文件節點即以 targeted `rg`／source reads fallback，不 build／extract／refresh／寫 version stamp。既有 targeted search 未找到 graph 不等於證明全域不存在。
2. **蒐集與分類。**執行鎖定 inventory，讀必要既有 receipt，分開 installed／effective／config／history／unknown。H 為 `2026-10-16` 次級 client discovery／installation／six-bytes 記錄，CLI／OS／確切時間未知。CP／CT／CS 只支持其固定版本的 bytes、input schemas、CLI `0.163.0` fresh recall／native traces，不推廣為目前 all-refs 或目前 bytes；同版本號不證明 bytes 相同。不重跑 core／session／live。
3. **撰寫實際 report。**落實九欄、方法／scope、去識別 context aliases、來源版本／時間、claim matrix、限制與 TestCase；exact 私人 locators 留 index。
4. **製作限定 review aids。**
   - **Archify：**僅畫「唯讀蒐集 → 證據分類 → 報告」workflow，區分 planned method 與 observed results；繁體中文 authored labels、無動畫，省略 `meta.locale` 並揭露固定 Viewer UI／HTML language 的 English fallback。執行時才讀 workflow schema／example，先寫 candidate。每次修改後 validate；showcase 須 **9 checks、0 errors、0 warnings**，最終須 `deliver`。對外部 HTML 執行 `visual-check <external.html> --json`，**不傳 `--repo-root`**。檢查 1440×900、1600×1000、1920×1080、2048×1320 的完整 containment，並人工檢視實際 HTML／截圖；自動 receipt 的 `visualReview: pending` 不等於人工通過。持續進行針對診斷的 focused correction；只要最佳錯誤數仍改善即可繼續，連續兩輪未改善最佳錯誤數時停止，並如實記錄未解診斷或缺工具狀態。
   - **PR Lens：**只在實際 topic diff 存在後，使用 skill 指定 pinned `0.11.0` runtime validate／render。base 固定 `0d3ca3d`，比對實際 head／working tree 的兩個 public outputs；未追蹤新檔用真實 `--no-index`／source bytes 納入，不造 head commit。原 README 工作已在 base；新 plan 是本題 changed artifact。plugin／core 鄰居只有確實未變才標 unchanged。既有 overlay 若存在則讀取並傳 config，否則才用 `--no-config`。只產生外部 map，不提供 correctness findings；最終 diff 再核對，不準確或增加負擔即改 direct-diff fallback。

## Validation / Acceptance Checks

實際報告的 `TestCase` 必須是同份文件內的自足人工表格，欄位為 `input`、`preconditions`、`steps`、`expected`、`actual`、`evidence`、`status`，至少涵蓋：

| 案例 | 查核重點 |
| --- | --- |
| CLI／cwd context | 實際版本、時間及 OBS scope，避免 feature context 混用 |
| Inventory schema | 原始 stdout／stderr／exit、欄位真實語意、錯誤／warning／非 JSON／無匹配 |
| 狀態分類 | installed-but-disabled、缺 enabled、precedence／trust 未解、來源衝突 |
| 歷史 receipt | 缺 receipt／只有 mtime 不冒稱安裝時間，不回填歷史 |
| Core reuse | 固定來源／hash、Git object 與目前 worktree 分離，不重跑或過度推論 |
| 九欄／diff／私人證據 | 欄位落實、owner、Written／Modify／Deleted 真實、兩個 repo outputs、去識別與 exact private allowlist |
| Tools | 各工具 used／skipped／failed／fallback、版本、receipt、實際 diff timing 與人工視覺狀態 |

Tester 依實際 report、限定來源與 index 查核，不注入故障、不另建 suite、不重跑核心證據；未遇案例只核對方法判準，`actual/status` 不預填通過。正向 installed／effective-enabled 必須有足夠來源與 context；誠實 `UNKNOWN`／`DISABLED`／`CONFLICT` 可完成交付。

Tester 將 evidence binding、工具實況、去識別與 exact diff 查核寫入 `verification.json`。獨立 Reviewer 取得實際 plan、diff、私人 index 與 Tester 結果後自行判定；unsupported assertion、缺必要 provenance／分類、來源混淆、不安全蒐集或 scope drift 才要求補正／停止。

## Reviewer Handoff

以下僅為 eligibility 成立後使用的 native schema template，非作者 verdict。獨立 Plan-Reviewer 必須取得本計畫、`plan/agent-handoff-workflow.md`、`plan/topic-plan-contract.md`、真正獨立 start acknowledgement 與 owner 記錄的 `reviewer-in-progress`；缺項只回報 BLOCKED coordination，不得 native approve。

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

本 session 已明確授權：在實際 Tester 驗證與獨立 Reviewer 完成交付判定後，派遣 Implementer 對本題兩個 repo outputs 依 topic commits、push 至 `origin` 的 `docs/a129924/plugin-installation-evidence`，再以 GitHub CLI／API 開啟 target `dev` 的 **Draft PR**，最後停在人工 review。發布前核對實際 branch／base／diff、remote 狀態與 commit 內容；不納入私人 evidence 或原 README 工作，不使用 PR Lens 發布功能。

此授權不等於 planning approval 或未來測試／review 已通過，也不新增 publish planning state。沒有自動 merge、release、tag、branch 刪除或 worktree cleanup；保留 FEATURE。Stable publishing 在缺少另行核准 contract 時仍為 BLOCKED。

## Open Questions / Unresolved Items

沒有阻擋規劃的需求問題。Inventory schema、registration、receipt、有效啟用、歷史時間、工具可用性及固定 core 私人記錄的實際綁定待實作證據；缺漏保持未知，不強迫補齊。

FEATURE 與本計畫已具既有寫入授權；planning approval 尚未成立。作者在 review-ready 停止，等待真正獨立 reviewer start，再由 owner 記錄下一 phase；不得提前交付 Implementer。
