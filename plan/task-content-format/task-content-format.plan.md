# task-content-format Topic Plan

Plan path：`plan/task-content-format/task-content-format.plan.md`
Plan owner：Plan-Creator `/root/plan_creator`
Selected feature：`/Users/andrew/code/plugins/codex-task-workflow.worktrees/agent-20261008-task-content-format`
Branch：`docs/a129924/task-content-format`
Base：`71c3c3bc068a172e579c46f77c0d0a67242c73ae`

Analysis routing：`INCOMPLETE`。缺少 optional `analysis/task-content-format/requirements.md` 與 `analysis/task-content-format/technical-spec.md`。本計畫依使用者確認的 frozen scope，以及唯讀產品權威 `GOAL.md`、`docs/task-workflow.baseline.md` 起草；不新增 analysis outputs。此 warning 本身不構成 scope blocker。

## Goal / Outcome

交付可直接使用的 Task／Ticket 內容規則、Markdown 模板與示例，使本人手寫及 Agent 整理的紀錄，都能在不依賴原對話或參考資料的情況下，理解目的、目前方向、階段、下一步及待釐清事項，並回查重要變更與結案原因。

交付完成代表文件情境驗收成立，不代表 YouTrack 操作、MCP、正式 plugin 或產品 Agent 支援已驗證。

## Scope

In scope：

- 一份正式 topic plan。
- 三份分離文件：內容規則、可複製 Markdown 模板、完整情境示例。
- 共用格式、未知值語意、更新方式、階段最小內容，以及本人手寫／Agent 整理兩種使用路徑的文件驗收。
- 使用者已授權 feature delivery：通過必要審查且無重大問題後，由 Implementer 依 topic commit、push、建立 Draft PR，停在 human review。

Out of scope：

- 程式碼、plugin runtime、manifest、Skill、transport、YouTrack schema、整合操作及產品發布。
- README／navigation、產品基準及既有 topics 的修改。
- 實際 Task 寫入、文件同步、產品 PR 操作、背景更新或自動結案。

## Locked Decisions

**內容與獨立性**

- 同一件事沿用同一 Task 識別；改名、換方向、切換階段或結案不建立替代識別。
- 已知目的即可留存 Idea；方向或下一步未知時明記待釐清，不補造方案、決策或行動。
- 目的尚不清楚時，先釐清目的；不得把猜測寫成有效目的。
- Task 不依賴 repo 開發 skills、planning artifacts、特定檔名、文件存在或 PR。
- 本 topic 是本地文件開發；stable-library intent absent。

**共用 Markdown interface**

Task 名稱採單行 `<工作對象>：<目的或期望結果>`。依已知目的命名，不宣稱尚未成立的方案；標題變更不改 Task 識別。

模板固定採以下區段與欄位順序；本人及 Agent 使用相同內容契約：

```markdown
# <工作對象>：<目的或期望結果>

- Task 識別：<既有識別；建立前為「待釐清：尚未取得識別」>
- 專案：<已知專案，或明確語意標記>
- 標籤：<已知標籤，或明確語意標記>

## 目的與背景
- 目的：
- 已知背景：

## 目前方向
- 方向：
- 主要理由：
- 待釐清：

## 工作狀態
- 階段：
- 下一步：
- 阻礙：

## 參考資料
- <參考條目，或明確語意標記>

## 重要變更
- <重要變更條目，或「無」>

## 結案
- 結案類型：
- 結果或停止原因：
```

這是 Markdown 與抽象 Task metadata 的內容契約，不指定任何 YouTrack 實體欄位。名稱、識別、專案、標籤、階段如由既有系統 metadata 表達，必須保持相同語意；本 topic 不設計其映射。文件模板及示例仍呈現完整結構，以便獨立閱讀。

**值的語意**

| 表達 | 固定語意 |
| --- | --- |
| `待釐清：<缺少或尚未決定的內容>` | 未知、未確認或尚未決定；不是不存在 |
| `無` | 已確認目前沒有；不得代替未知 |
| `不適用：<原因>` | 此項在目前情境不適用；不得用於逃避未確認內容 |

模板不使用空白暗示有效答案。Idea 可以大量使用上述標記，不要求先補齊所有資訊。尚未結案的結案欄位使用 `不適用：尚未結案`；沒有目前方向時，主要理由可使用 `不適用：尚未形成方向`。

**Snapshot 與重要變更**

- 名稱、metadata、目的背景、目前方向、工作狀態、參考與結案內容，呈現目前 snapshot；更新時直接修正相應欄位。
- 重要方向或目的調整、影響恢復理解的階段退回／跳轉，另追加重要變更，不覆寫既有順序與理由。
- 變更條目固定包含：`<先後序號>｜<變更前> → <變更後>｜理由：<已確認理由或待釐清標記>`。已知日期可附記，不補造日期或理由。
- 不保存全部對話或每個技術步驟。普通措辭修正不要求新增歷史。
- Agent 僅整理可得來源；矛盾或資料不足明記待釐清，不默認較新的文字已形成決策。

**參考與結案**

- 參考可為零、一或多份；每筆保留位置、用途與存取狀態。未知存取狀態不表示已讀；不可存取時說明缺少的資料。
- Task 的恢復摘要必須留在 snapshot，不以「詳見參考」取代核心內容。
- 結案類型使用 `完成`、`取消` 或 `停止`，並記錄完成結果或取消／停止原因。Close 的下一步可為 `不適用：此 Task 已結案`；未解決問題仍如實保留。
- PR 建立或合併不自動代表 Task 結案。

**階段最小內容**

所有階段保留名稱、目的、專案／標籤、方向與理由、階段、下一步／阻礙、參考、重要變更及結案區段；未知資訊依上述語意標記。以下是內容要求，不是系統轉換 gate：

| 階段 | 最小內容要求 |
| --- | --- |
| Idea | 已知目的；可得背景；待釐清事項；下一步或其待釐清標記。方向可尚未形成 |
| Draft plan | Snapshot 說明正在整理的初步方向、可得理由及尚未確定事項 |
| Implementation plan／實作 | Snapshot 說明目前實作方向、已知進展、下一步與阻礙；不要求複製詳細步驟 |
| PR | Snapshot 說明目前交付／審查情況、下一步與阻礙；PR 參考仍是可選 |
| Close | 結案類型及實際結果或停止原因；保留既有方向、重要變更及參考 |

允許跳階段及返回前階段，不以欄位完整度、文件存在或 Skill 執行作為通用轉換條件。階段反映實際工作情況；缺失資訊明示，不捏造進展。

## Boundaries / Exclusions

Plan-Creator 擁有 plan 及其 phase 記錄；獨立 Plan-Reviewer 判斷 planning contract。Implementer 建立三份文件及處理已授權的 bounded commit／push／Draft PR；Tester 提供文件演練證據；獨立 Reviewer 判斷實作與驗收；Observer 負責派遣與停點。

只有 selected feature 可寫；primary dev worktree 唯讀。除 Artifact Paths 所列四個 repo outputs，其餘 repo 檔案全部唯讀。不得建立 step、review-log、requirements、technical-spec 或額外 tracked 文件。需要新增路徑或改變凍結格式時停止，交回 bounded plan revision。

交付檢查使用已授權的 PRLens local external 工作區 `/private/tmp/task-content-format/pr-lens/`，CLI pinned `0.11.0`；無 `.github/pr-lens.yml` 時不建立，不上傳 PRLens。Graphify 無 usable graph，採其 explicit fallback 的 targeted sources；不建 graph，不修改 AGENTS、config 或 hooks。這些工具的 bounded 使用不改變 Task 產品 scope。

## Status / Allowed Transitions

- **Current**：`approved`。
- **Next actor**：Implementer。
- **Stage-local action**：依已批准計畫，在 selected feature 實作三份 declared docs，提供文件驗收證據；不修改 plan 或其他 tracked paths。
- **Allowed next planning transitions**：`[]`；approved 是 terminal planning state，後續為 execution handoff。

Actual mode：Default。使用者已授權本 feature delivery；本輪 Plan-Creator owner 的 exact write set 僅為本 plan，以及必要 topic parent directory，不實作三份文件或 commit。

Previous review 的 genuine independent start acknowledgment：

- Review actor：Plan-Reviewer `/root/plan_reviewer`。
- Start ID：`task-content-format-/root/plan_reviewer-start-1`。
- Start source SHA256：`8a40779cdb43697da510bc18f6d4adb5633bd1adb8ee8f0a9daae6713aff2e7b`。
- Start outside-Status SHA256：`f47109195376fb86bbf7648c157f5f56ecd935e81f802996dcb816a0d4955f1d`。
- Owner：Plan-Creator `/root/plan_creator`，依此真實 start 記錄 `reviewer-in-progress`。

Owner 依獨立 Plan-Reviewer 的真實 native verdict 記錄 phase，不得補造 verdict 或 phase history。


已收到真實 native review result：

- Reviewer：Plan-Reviewer `/root/plan_reviewer`。
- Review start ID：`task-content-format-/root/plan_reviewer-start-1`。
- Reviewed whole SHA256：`482d8270edcc0c328b03f9635662bf1a454ddb8513a58b723d0a12f8ae100743`。
- Reviewed outside-Status SHA256：`f47109195376fb86bbf7648c157f5f56ecd935e81f802996dcb816a0d4955f1d`。
- Native verdict：`needs-rework`。
- Blocking issue：Open Questions / Unresolved Items 仍将review start与owner phase eligibility列為尚待建立，與Status已記genuine start/current reviewer-in-progress矛盾。
- Bounded fix：只修正 Open Questions 的 stale 行政句，使其按 Status 及實際 review／驗收證據查證。

上述 first start 與 verdict 僅為 previous review proof，不構成修正版的新 start 或批准；下一輪須取得新的真實獨立 review start。

`needs-rework` 的下一角色為 Plan-Creator，轉回 `creator-in-progress`。`approved` 的 allowed next planning transitions 為 `[]`，下一角色為 Implementer，執行三份文件的 bounded implementation。

Execution model：正式批准後，Implementer → Tester → independent Reviewer → 已授權的 topic commit／push／Draft PR → human review。獨立 Reviewer 的 PASS 才允許依已授權交付繼續；重大問題依 repo contract 分流，不能當成通過。尚未執行的驗收一律 evidence-pending。

Reviewer Handoff JSON 僅為正式獨立 review 的 schema，不是本 plan 的 verdict；缺少 readable plan／contracts、真實 start acknowledgment 或 owner-recorded `reviewer-in-progress` 時，依共享契約返回 BLOCKED coordination，不產生 native approval。

Current review 的 genuine independent start acknowledgment：

- Review actor：Plan-Reviewer `/root/plan_reviewer`。
- Start ID：`task-content-format-/root/plan_reviewer-start-2`。
- Start source SHA256：`d396ba9b4b66a570eb4a3bf9deb1e3eb2e378e45147465d56da832a0e85579a4`。
- Start outside-Status SHA256：`bfc933c30dbd223415015a576ff2d9fe06c93dd517bbb0165d35dcfde52d18c1`。
- Owner：Plan-Creator `/root/plan_creator`，依此真實 start 記錄 `reviewer-in-progress`；此輪 native approved verdict 已收到，記錄如下。

Current review 的 genuine native verdict：

- Reviewer：Plan-Reviewer `/root/plan_reviewer`。
- Review start ID：`task-content-format-/root/plan_reviewer-start-2`。
- Reviewed whole SHA256：`baac8e93d82aa2304bcb0f14ae894c4bfc77f6cba38dfc126230509e8ed5e393`。
- Reviewed outside-Status SHA256：`bfc933c30dbd223415015a576ff2d9fe06c93dd517bbb0165d35dcfde52d18c1`。
- Native verdict：`approved`；blocking issues：`[]`；copilot feedback triage 的 ADDRESS／DISCUSS／SKIP 均為 `[]`。
- Owner：Plan-Creator `/root/plan_creator`，依此真實 native result 記錄 `approved`。

Approval 僅允許 bounded implementation handoff，不代表文件實作、驗收或交付已完成。

## Artifact Paths

| Artifact | Exact path | Owner | 用途 |
| --- | --- | --- | --- |
| Topic plan | `plan/task-content-format/task-content-format.plan.md` | Plan-Creator | 格式、範圍、驗收與角色契約 |
| 內容規則 | `docs/task-content-format.md` | Implementer | 使用與更新規則 |
| Markdown 模板 | `docs/task-content-format.template.md` | Implementer | 完整可複製格式 |
| 情境示例 | `docs/task-content-format.examples.md` | Implementer | 手寫與 Agent 整理驗收示例 |

四個路徑預期為新建；之後修改僅限各 owner 的對應 artifact。Deleted：無。

`README.md`、`VERSION`、`.github/copilot-instructions.md`、`GOAL.md`、`docs/task-workflow.baseline.md`、既有 topics 與 workflow contracts 均不修改；不存在的唯讀路徑也不建立。每次實際寫入仍須驗證 Default mode、既有 exact authority，以及 target／parent 在 selected feature canonical root 內的 containment。Git delivery metadata 僅由後續獲授權角色操作，不因此增加 tracked output。

## Implementation Steps

正式批准後，由 Implementer：

1. 建立內容規則，完整呈現 Locked Decisions，並說明手寫／Agent 整理、建立／更新／結案的文件用法。
2. 建立可直接複製的 Markdown 模板；區段、欄位順序及語意標記與規則一致，附最少使用說明。
3. 建立以下五組示例；每組包含來源事實、本人手寫版本及 Agent 整理版本：
   - A：不完整 Idea，已知目的，方向與下一步待釐清，無參考。
   - B：同一 Task 改變方向，更新 snapshot，保留先後與理由；展示合理跳階段或退回。
   - C：參考不可存取，但 Task 本文仍足以恢復概要。
   - D：正常完成結案，保存結果；有 PR 時區分 PR 情況與 Task 結案。
   - E：Idea 決定停止，無 planning 文件或其他 Skill，保存停止原因。
4. 比對三份文件，修正格式或語意差異，回報 exact changed paths、來源對應、驗收結果及限制。
5. Tester 及獨立 Reviewer 的必要證據齊備且無重大問題後，依 Observer 的 bounded delivery handoff 執行 topic commit、push 與 Draft PR；附驗收證據及範圍限制，交付 human review，不自行 merge。

## Validation / Acceptance Checks

| Check | 所需證據與通過條件 |
| --- | --- |
| 來源一致 | 對照 GOAL 與 baseline：同一識別、Idea 可不完整、可跳轉／退回、可選參考、重要變更與結案均保留；無新增產品整合承諾 |
| 共用格式 | 規則、模板與五組示例的標題、欄位、區段順序及值語意一致；模板無未說明空白 |
| A：不完整 Idea | 手寫及 Agent 版本都只保留已知目的／背景，方向與下一步明記待釐清；未知阻礙不寫成「無」 |
| B：方向變更 | 兩版本都沿用識別；snapshot 是目前方向；歷史保留前後、順序及理由；階段變動不要求文件 |
| C：參考缺失 | 兩版本都保留參考位置、用途及不可存取狀態；不宣稱已讀；遮蔽參考及原對話後仍能讀懂概要 |
| D：完成結案 | 兩版本都記錄完成結果、保留變更及參考；不以 PR 建立／合併自動推導結案 |
| E：停止結案 | 兩版本都能從 Idea 直接停止，記錄原因；不要求 plan、step、PR 或 Skill |
| 不補造 | 提供目的未知或來源矛盾的反例，確認要求釐清／標記缺口，不生成定案目的、方向、理由或下一步 |
| 路徑與流程 | Tracked diff 僅包含四份 declared outputs，由相應 owner 管理；沒有額外檔案、code、schema 或 navigation 變更；delivery 停在 Draft PR human review |

Tester 對五組示例的兩種路徑分別演練，共十次，回報每次能否從紀錄回答「為何做、目前方向或未知處、在哪個階段、下一步或待釐清處、阻礙」，以及結案時的結果／原因。Evidence 使用對話回報與既有 diff，不新增 tracked 證據檔。

驗收限文件情境演練與來源比對，不操作 YouTrack／MCP，也不宣稱真實產品能力通過。獨立 Reviewer 收到 plan、三份 artifacts、diff 與 Tester 結果後才判定實作 verdict。PRLens／Graphify 的有限檢查與缺失限制應如實回報，不以缺少 graph 或未上傳作為已完成工具驗證。

## Reviewer Handoff

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

使用者已授權在無重大問題且必要 review／驗收完成後，由 Implementer 按 topic commit、push、建立 Draft PR；停止於 human review，保留 feature worktree。

無自動 merge、release、branch deletion 或 worktree cleanup，也不授權 PRLens 上傳。無 post-merge 動作；stable publishing 須另有批准的 publishing contract，本 topic 不授權。

## Open Questions / Unresolved Items

沒有阻止本 frozen-scope plan 進入獨立 planning review 的內容問題。

尚缺兩份 optional analysis artifacts，已列為 INCOMPLETE warning，不新增或推定其內容。Review start、owner phase、native verdict 與實作驗收進度依 Status 及獨立 review／Tester 的實際證據查證；本節不另行宣稱隨 phase 改變的條件是否成立。
