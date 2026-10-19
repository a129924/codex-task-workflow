# idea-core-acceptance

本 plan 由 Plan-Creator `/root/plan_creator_core_acceptance` 依使用者接受的完整對話計畫，在指定 feature worktree 落盤。Base：`47166176192adfb8c0e5920e25ab7b8ce8bc1807`。尚未進行獨立 planning review、核心驗收或輔助工具執行；Reviewer Handoff 僅為 schema。

**Semantic warning — optional analysis INCOMPLETE**：`analysis/idea-core-acceptance/requirements.md` 與 `analysis/idea-core-acceptance/technical-spec.md` 均不存在；依已鎖定需求與產品 authorities 起草，不新增 analysis／step。

## Goal / Outcome

**Goal**：驗收現有 0.2.0 的保存、跨 Session 恢復及授權更新，交付自足 testcase、去敏結果與獨立審查。

推薦先做此 topic：現有安裝包及 bounded create/read/update 已有紀錄，但核心「換 Session 仍能理解工作」的 TC02 仍 partial。相較先擴充結案或跨專案搜尋，此 topic 可先補核心留存能力的可查證基礎。這是順序選擇，不是其他功能的既有 gate；本 topic 通過不等完整 v1。

**Non-Goal**：新增 runtime 能力、完成所有生命週期驗收，或以圖表代替測試證據。

## Scope

**In-Scope**：在目前日常 Codex host、既有安裝與連線，以使用者指定或明確授權代理選定、且 preflight 通過的 project 新建一張專用測試 Task，完成 A–F；加入 Archify 流程圖、PR Lens bounded diff 輔助圖及 Graphify 既有 graph 導航。

**Out-Of-Scope**：runtime fixes、結案／跨專案搜尋、README cleanup；調整安裝、config、OAuth、帳號、ACL 或方案；建立 Graphify graph。輔助工具不擴張產品 acceptance。

## Locked Decisions

- 真正新 Session 由人員於 host 開啟，或由可驗證 host API 建立；forked subagent／清空原對話不算。
- 恢復 Session 僅取得 ID、必要連線授權及已安裝 skill/resources；不給原對話、預期正文、原 repo 或其他 workflow skill。Tester／Reviewer 另持 baseline。
- 沿用 skill 的 private/license/schema 規則及仍有效 audit，不放寬或一律重做。
- 更新只限明確授權的 summary／description，保留未知及重要變更歷史，不改 State、權限等非 scope 欄位；測試票保留，不自動 close/delete。
- 新 testcase 不抹除 TC02 歷史 partial。Stable-library intent absent；stable publishing 缺獨立 publishing contract 時 BLOCKED。
- **git-branch-name**：`docs/a129924/idea-core-acceptance`。主體為 plan、testcase 與結果文件，故採 `docs`；沿用既有 `a129924` namespace。指定 feature worktree 已建立於此 branch、base 如上；dev 不作實現。這不代表 remote freshness 已驗證。

## Boundaries / Exclusions

Plan-Creator 擁有 plan；獨立 Plan-Reviewer 審 planning。Approved 後 Implementer 擁有文件與輔助產物、Tester 提供具 provenance 的驗證、獨立 Reviewer 判定驗收；Observer 僅派遣與彙整。

Implementer 錄入觀察，不代判 gate。Runtime 缺陷或路徑漂移須停止修改，由 Reviewer 分類後另作 bounded fix／契約修訂。不得在 dev worktree 實作。

## Status / Allowed Transitions

- **Current**：`approved`
- **Execution model**：Plan-Creator → independent Plan-Reviewer；approved 後 Implementer → Tester → independent Reviewer → 已授權 bounded delivery。
- **Next actor**：Implementer
- **Stage-local action**：依本 plan 準備自足 test definitions 與限定的外部輔助工具產物，維持 exact write set、preflight 與核心 A–F 邊界。
- **Allowed transitions**：[]（planning 終態）
- **Plan owner／author**：`/root/plan_creator_core_acceptance`

Owner 僅在真正獨立 Plan-Reviewer start acknowledgement 後記錄 `reviewer-in-progress`，僅依其 native verdict 記錄 `approved` 或 `needs-rework`；不得捏造 acknowledgement 或 approval。`approved` 為 planning 終態，allowed planning transitions `[]`、next actor Implementer、action 為準備本 plan 的自足測試定義。實作與驗收尚未執行。

## Artifact Paths

| 標記 | Exact path | Owner | 用途 |
| --- | --- | --- | --- |
| Written：New | `plan/idea-core-acceptance/idea-core-acceptance.plan.md` | Plan-Creator | 本 topic 執行契約及 owner phase |
| Written：New | `docs/testcases/TC-YOUTRACK-IDEA-ACCEPTANCE-001.md` | Implementer | 自足測試定義與具 provenance 的去敏觀察 |
| Modify | `docs/testcases/idea-save-recall-validation-summary.md` | Implementer | Bounded 結果與保留限制 |

**Modify** 另允許原 owner 修訂上述本 topic 新建產物；不覆寫 ReadOnly。**Deleted**：無。公開 repo write set 僅上述三個 exact paths；本次 materialization 僅寫 plan。`README.md`、`VERSION`、`.github/copilot-instructions.md` 均不修改。

**ReadOnly**：`GOAL.md`、`docs/task-workflow.baseline.md`、`docs/task-content-format.md`、`docs/task-workflow-contract.md`、`plan/topic-plan-contract.md`、`plan/agent-handoff-workflow.md`；`plugins/youtrack-idea/` 全部內容；既有 `docs/testcases/TC-YOUTRACK-IDEA-UPDATE-001.md`。

外部 **Written** 的固定 run root 為 `/private/tmp/idea-core-acceptance-20261019/run-001`；以下每列是預定產物或明列的有限工具中間產物，不表示已生成或驗收。每個 path 均由指定 owner 寫入，缺工具／未執行情境記錄狀態，不製作虛假產物。

| 外部產物 | Exact path／有限確定性公式 | Owner | 用途 |
| --- | --- | --- | --- |
| Evidence index | `/private/tmp/idea-core-acceptance-20261019/run-001/manifest.json` | Implementer | 彙整實際 path／SHA-256、版本、Session provenance 及受限 target mapping |
| Observations | `/private/tmp/idea-core-acceptance-20261019/run-001/observations.md` | Tester | 實際觀察、證據類型及未執行限制 |
| Baseline comparison | `/private/tmp/idea-core-acceptance-20261019/run-001/comparisons.json` | Tester | 依獨立 baseline 比較 A–F；不代判 acceptance gate |
| Archify candidate | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.json` | Implementer | 固定 workflow basename 的 synthetic 規格 |
| Archify validation receipt | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/validation.json` | Implementer | validate JSON stdout |
| Archify delivery receipt | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/delivery.json` | Implementer | deliver JSON stdout及凍結 bytes binding |
| Archify HTML | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.html` | Implementer | 受驗證的 workflow |
| Archify visual receipt | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.json` | Tester | 四尺寸 containment／capture receipt |
| Archify contact sheet | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.html` | Tester | 人工檢視入口 |
| Archify capture | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.1440x900.light.png` | Tester | 最小 light |
| Archify capture | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.1440x900.dark.png` | Tester | 最小 dark |
| Archify capture | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.2048x1320.light.png` | Tester | 最大 light |
| Archify capture | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/workflow.visual-check.2048x1320.dark.png` | Tester | 最大 dark |
| Archify perceptual record | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/archify/visual-review.json` | Tester | 真實人工檢視結果，與自動 receipt 分開 |
| PR Lens bounded diff | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/diff.patch` | Implementer | 真實 base SHA 與工作樹 snapshot 對應差異 |
| PR Lens graph | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/graph.json` | Implementer | 固定單一 architecture view 的 graph |
| PR Lens staging manifest | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/staging/manifest.json` | Implementer | CLI 原生有限 render manifest，驗證後移至 rendered |
| PR Lens staging graph | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/staging/drawn.graph.json` | Implementer | CLI 實際繪製 graph，驗證後移至 rendered |
| PR Lens staging SVG | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/staging/core-acceptance-review-light-<h>.svg` | Implementer | 僅一個原生 content-addressed SVG；h 定義如下 |
| PR Lens final manifest | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/rendered/manifest.json` | Implementer | 保留原生 manifest 與實際 asset path |
| PR Lens final graph | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/rendered/drawn.graph.json` | Implementer | 與 staging bytes 相同的 graph |
| PR Lens final SVG | `/private/tmp/idea-core-acceptance-20261019/run-001/artifacts/pr-lens/rendered/core-acceptance-review-light-<h>.svg` | Implementer | 與 staging bytes 相同的唯一 SVG |

PR Lens 命名契約：CLI 固定 0.11.0、其 pinned runtime renderer 固定 `@coldtea/pr-lens-renderer` 0.3.1；graph 固定 `lenses=["architecture"]`、`flows=[]`，恰一個無 children 的 view，ID=`core-acceptance-review`、lens=`architecture`；render 固定 `--theme light`。唯一 asset ID=`core-acceptance-review-light`，`h=SHA256(該 SVG 原始 UTF-8 bytes)` 的小寫十六進位前 32 字元。上表兩個 `<h>` 指同一實際 digest，是單一資產的完整有限路徑公式，並非 wildcard；不授權額外 view/theme/asset 或任意 future files。版本、資產數量、命名或路徑不符即停止工具交付，依 bounded revision 處理，不臨時擴表。

執行前逐一解析固定 root、每個 destination 與既存 parent/symlink chain，確認 checkout 外 containment、無其他 run 覆寫及必要權限；每次 mkdir/write/promotion 前重查。PR Lens 先僅向上述 staging 位置 local render；其原生 manifest 在記憶體建立的單一 asset path 必須符合上述有限公式及 containment 才可寫入。若當前執行方式不能安全核對，不改 runtime，以 tool limitation／direct diff fallback 停止。生成後 Implementer 解析原生 manifest，核對唯一實際檔名、SVG hash／bytes、固定 graph及零額外資產，再對已解析的 exact destinations 重查權限，將三個 staging 產物原樣移至對應 rendered paths；不得重寫或偽造原生 manifest。固定 run manifest 記錄生成後實際完整 paths／hashes與移動 provenance，Tester 核對。

Staging 僅限表列三個 PR Lens 中間產物，成功移動後不作額外交付。Archify deliver 所需 private same-directory snapshot 僅屬該命令內部短暫 staging，不是新增持久產物，也不授權手動任意檔；殘留或非預期輸出如實記錄並停止，不隱藏。不得將其他目錄、額外 tool outputs 或新的 run root 當自動授權；路徑變更須 bounded plan revision。

公開內容只用 synthetic／去敏資料；不公開 tenant、Task/project、帳號、ACL/license 或私人正文，任何證據均不存 credentials。完整私人正文只在操作上下文處理。不假定 repo 內目錄已被忽略；此 fixed root 不取代必要寫入權限 preflight。

## Implementation Steps

1. Approved 後，Implementer 編寫自足 **TestCase**、synthetic 初始／更新 baseline、預期結果與證據記錄方式；準備 preflight、新 Session 人員交接及評估者資訊隔離。
2. **Graphify**：僅 bounded 導航既有 graph，檢查 freshness／sources 並回源確認。使用 pinned `/Users/andrew/.local/bin/graphify`（graphifyy 0.9.73），每次 CLI 含 help/version 均設 `GRAPHIFY_NO_AUTO_REFRESH=1`，query budget 1500。無可用 graph／runtime 或版本不符即 `rg`＋targeted source fallback；不 build、refresh、install、改 hooks/config 或開 visualization。
3. **Archify**：實作時依 skill 選 workflow schema/example 後立即寫候選，呈現「save → 新 Session recall → 授權 update → 另一新 Session recall」及 test/check/stop 交接，不畫成完整 v1 或虛構成功。繁體中文 authored content；fixed Viewer UI／`html lang` 英文 fallback。全部產物放外部 `artifacts/archify/`。
4. **PR Lens**：針對實際 base/head 或 bounded diff，記錄真 SHA 及必要工作樹 snapshot；不虛構 PR/commit provenance。只用 pinned CLI 0.11.0：`/Users/andrew/.local/share/pr-lens-runtime/bin/pr-lens` local validate/render；圖包含本 topic 差異及未變相鄰契約／skill。既有 overlay 唯讀沿用，沒有則 `--no-config`。不為產圖新增 commit/PR，不寫 repo config、不 upload/API/auth/publish/install。Draft PR 建立屬下方獨立交付動作，使用 `gh`，不是 PR Lens publication。
5. Implementer 依 Tester provenance 錄入去敏實際觀察、工具結果與限制；保留歷史 partial／FAIL／未執行項，不代替 Reviewer 判定。

## Validation / Acceptance Checks

| TestCase | 最低核心證據 |
| --- | --- |
| **A：來源與環境** | 綁定 source/version/host 及 installed bytes；真正新 Session 能載入 skill、讀取 references，取得必要工具及當次 schema。 |
| **B：保存** | 本人、project、private/license/schema preflight 通過後單次 create，立即同 ID 完整 readback，比對正文與 metadata。 |
| **C：跨 Session 恢復** | 新 Session 僅依 ID 恢復目的、背景、方向或未知、階段、下一步／阻礙及參考限制；Tester／Reviewer 另持 baseline 比對。 |
| **D：授權更新** | 同 ID 更新 snapshot、保留歷史及理由；寫前重讀、單次 update、完整 readback，核對可得非 scope 欄位無意外變更。 |
| **E：更新後恢復** | 再一次真正獨立新 Session，在相同資訊限制下恢復更新後脈絡及未解事項。 |
| **F：唯讀與停止** | 唯讀請求無寫入；重要停止規則採適當 static／model-only 證據，未 live 分支保留限制，不要求全部故障注入。 |

Live、static、model-only 分列；安裝成功不等行為通過。缺工具、有效 private/license 證據、target、完整讀回或真正新 Session，受影響項記 `NOT_EXECUTED`／`INCOMPLETE` 並停止。Formal output schema 不可得及競態限制如實保留；一般他人未實測不可改記 PASS／N/A。

輔助工具另驗：Archify 每次候選修改後 validate，showcase 9/9、零 warnings/errors，通過後凍結並 deliver；對同份 HTML 做 visual-check，四個 desktop sizes（1440×900、1600×1000、1920×1080、2048×1320）無 overflow，最小／最大 light/dark 四張人工檢視。外部產物不使用要求 repo containment 的 `--repo-root`。PR Lens 核對 manifest/SVG 與實際 diff，誤述或不適合即 direct diff fallback。

工具 pending／不可用如實記錄，不冒充核心 PASS，也不自動成為核心產品 blocker。獨立 Reviewer 分別核對核心與工具證據、paths、去敏及 provenance，回傳 `PASS`、`PATCH_REQUIRED`、`REPLAN_REQUIRED`、`MISSING_EVIDENCE` 或 `BLOCKED`；證據收集完不等驗收通過。

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

使用者已明確授權：在指定 feature worktree 完成本 topic，通過獨立 review 且無未解重大問題後，由 Implementer 作 bounded topic commit → push → 以 `gh` 建立 Draft PR → 停於 human review。不增加公開 write set，不把此授權交給 PR Lens 的 publication 流程；缺必要驗收證據時如實回報並依 gate 停止，不能為交付而宣稱 PASS。

無自動 merge、release、publish、tag 或 cleanup；保留 feature worktree 與測試票供 human review。Stable publishing 仍需獨立契約。

## Open Questions / Unresolved Items

無未決產品或架構問題。使用者已授權代理推薦並選擇合適 project，優先核對既有專用測試 project；不要求新建 project 或更改 ACL。實際 project、Task ID、新 Session、audit 適用證據及外部 evidence 權限仍是執行 preflight inputs，不在公開文件填入真實 target。Private/license 證據尚未提供不代表 gate 通過；缺少時停止受影響 live 操作、記 INCOMPLETE，不阻塞文件準備或冒稱驗收通過。
