# YouTrack Idea

版本 0.2.0 的 portable skill-only Codex plugin，支援主動保存目的已知的私人 Idea、經明確授權更新指定 Task 的摘要／正文及寫後讀回確認，以及新 Session 依同一 Task ID 恢復工作概要。不結案、跨專案總覽或背景同步；使用不需要原對話、planning 文件、PR、原 repo 或其他 workflow skill。

## 安裝與外部啟用

在支援 portable plugins 的 Codex host 加入含 `.agents/plugins/marketplace.json` 的本地 repo marketplace，選擇 `idea-save-recall-local`／「私人 Idea 留存」中的 `youtrack-idea`，由使用者 install 並 enable。`source.path=./plugins/youtrack-idea` 相對 marketplace root（本 repo root），不是 `.agents/plugins/`。host 操作依其正式安裝介面；catalog parse 或 CLI help 不代表載入成功。安裝啟用後開新 Session，確認 skill 真正載入且 packaged references 可讀。

Plugin 不 bundle MCP、transport 或 credentials。catalog 的 AVAILABLE／ON_INSTALL／Productivity 是本地 entry metadata；ON_INSTALL 不會替本方案自動註冊或登入 user-managed MCP。人員須在明確授權下管理官方 YouTrack MCP、client config 與 OAuth。

若尚無連線，由本人先確認實際 HTTPS tenant `/mcp`、帳號、project 與授權。下列是非 active 說明，placeholder 必須換成本人確認值，不要直接執行：

```sh
codex mcp add youtrack_idea --url '<使用者確認HTTPS tenant /mcp>'
codex mcp login youtrack_idea --oauth-client-registration cimd
```

已配置且仍有效的連線／OAuth可沿用，不因工具暫未暴露重做登入。CIMD 須由 tenant 支援並啟用；未開停在人員／管理員邊界，不改走 token／REST。`~/.codex/config.toml` 與 credential store 由 client／人員管理，不存 repo，不由 skill 自動修改。

人員在 user-client 設定 `enabled_tools`：保存／讀回保留以下七個官方工具，使用更新功能時僅額外加入官方 `update_issue`：

- `get_current_user`
- `find_projects`
- `get_project`
- `get_issue_fields_schema`
- `create_issue`
- `get_issue`
- `search_issues`

allowlist 不代替 ACL。新 Session 確認所需工具可見、當次 schema 可用（更新另需 `update_issue`），`get_current_user` 為本人預期身分。缺工具／必要參數或欄位，停止受影響操作並提出 Integration Scope Gap，不自建 payload adapter。

## 建立前的 gates

依 [skill](skills/youtrack-idea/SKILL.md) 每次 create 前檢查 schema／private／license：project 與必要 custom fields 合法，summary/description 可持久化，read 可回 ID/project/summary/完整 description；visibility arguments 的身分表示按當前 schema。正式輸出 schema 未暴露不能假稱完整 shape 驗證；可得 schema／真實唯讀回應不足以確認必要條件就停，不試建票補證。

私人存取須有真實 project ACL、global roles／override、Guest、All Users、team／groups audit，及本人正向、一般他人／匿名負向證據；只有 skill 明列且經 human 明確授權的限定單一使用者例外可替代一般他人實測。預期可讀者為本人與日後明確授權至多一 bot；管理員例外揭露，無 bot 不新建。AI visibility 只額外縮窄，不能替代 ACL；讀不到不證明票不存在。

核對 tenant License Details、實際 subscription、retention／inactivity 條款，確認私人 project 與本人加至多一 bot 的規模；bot 算 User，不承諾永久保存或永久免費。來源衝突保留並以實際 tenant 證據查明。缺證標 pending，停止受影響 live create 與產品通過聲明。需付費、改 ACL／帳號／方案或僅允 public，由人員決定，不自動變更。

### 限定單一使用者替代路徑

只在本次 human 明授權、完整 Users 僅本人管理員＋banned Guest 且無其他一般帳號／bot，完整 users/groups/team/project/global roles/override audit 符合 [skill 的全部條件](skills/youtrack-idea/SKILL.md)，並有本人正向與匿名對同既有票 sign-in 拒絕的證據時，才可交獨立 Reviewer 判定一般他人實測的替代證據。Guest 無角色／Read Issue、All Users 無角色、Registered Users project 無權限且 global Observer 無 Read Issue／override、其他角色無一般讀票 grant，皆必核對。一般實測記 NOT_EXECUTED，不能標 PASS／N/A。新增一般人／bot／其他帳號或 roles/ACL/groups/team/Guest/global override 組態變更即失效，回常規實測；不新增帳號、不改權限。這不放寬新 Session load、schema、license/private entitlement／官方 retention 適用與其他缺證，不保證永久免費或保存。

此段是 single-user-privacy-v1 契約修訂；原 0.1.0 package identity 不變，原 approval/hash 只對舊 bytes 有效，修訂須獨立審查並讓安裝副本同步後才執行。

## 保存、讀回與停止

可說「把這個目的已知的想法存到我指定的 project」，或在新 Session 提供同一 Task ID 請求讀回。目的／project／對象不明先釐清；方向或下一步未知可保留待釐清。既有同事情沿用 ID，不另建；唯讀請求不寫入，明確授權更新依下方流程。summary、metadata／description 映射、完整正文及參考限制依 packaged rules；正文 Idea 不推定系統 State，不新建 tag。

只單次 create，可信 ID 回傳後立即同 ID get，核對 project、summary、完整 snapshot 一致才「已證實保存」。寫後不符或不可讀回報驗證未完成。提交中斷無可信 ID 時，只在本次 project 查摘要候選、完成分頁、逐張 get 核對同次建立證據；0 結果、碰撞、多候選、隱藏、缺欄位或分頁未完均保持結果不明並停，不能 retry create。沒有 marker、idempotency 或 exactly-once 保證。

停用 plugin 只停用 skill，保留遠端 Task。外部 MCP 停用由人員管理，不自動刪 Task、清 credentials、遷移資料或 rollback delete。

## 驗證範圍

公開驗證摘要見 `docs/testcases/idea-save-recall-validation-summary.md`。只發布去敏結果；tenant、Task、帳號／方案及權限稽核的詳細證據留在本機，不由此包提供或保證其他環境可用。

正式輸出 schema 未暴露時不能假稱完整 shape 驗證。使用時仍須檢查當次必要欄位與前置條件；未知或不足就停止受影響操作。驗證不輸出私人正文、個資或憑證。

## Packaged references provenance

三份 references 為唯讀契約逐 byte 副本，內容與相對連結未改寫。來源 repo commit（三檔最近一次共同變更）：`98f81ddcb90c0c9d23fd3729302892aa457db2e8`；copy basis HEAD：`e01b8d1147620498fde0c28581e75c7ac9fef810`。來源路徑僅作開發 provenance；執行時只讀包內相對 references，不需要來源 repo。更新副本需另有 bounded contract revision。

| 來源 | 包內副本 | SHA-256 |
| --- | --- | --- |
| `docs/task-content-format.md` | [內容規則](skills/youtrack-idea/references/task-content-format.md) | `cc7565dd088089984a3d2d4bbb75b4d02ed0526a449e612be8b9bad8f015a6d9` |
| `docs/task-content-format.template.md` | [模板](skills/youtrack-idea/references/task-content-format.template.md) | `f6bee25993f2e35bcacc6ffe525697b5c80994f5286600b9b9e16ed419699c48` |
| `docs/task-content-format.examples.md` | [示例](skills/youtrack-idea/references/task-content-format.examples.md) | `2503c1ed4bc5835510c097e70a58684a303251ff26bbcb2887be455a770135f8` |

三份同目錄相對連結形成閉包；示例的 `example://` 為原文虛構位置，不是可存取依賴、真人證據或驗收結果。

## 0.2.0：經授權更新

明確提供 Task ID 與更新內容，例如「更新既有 Task 的最新進展，保留歷史及未完成限制」。依 skill 的更新流程，先讀原 snapshot、整理目前 snapshot 與重要變更、寫前重讀檢查衝突、單次 update、同 ID 完整讀回。只更新 summary／description，不移動 project、不改 State／權限，不重建票。唯讀請求永遠不會因內容過期而自動更新。

目前 host 若只暴露七工具，更新功能停於 Integration Scope Gap；需人員將官方 `update_issue` 加入 allowlist 並重新載入，不改 token／REST 或 UI 寫入。以當次實際 schema 為準，不在包內硬編未觀察的 wire arguments。沒有 conditional revision 時，寫前重讀不能消除讀寫競態；逾時後不重送，僅同 ID 查證，仍不明就停。

0.2.0 的更新情境見 `docs/testcases/TC-YOUTRACK-IDEA-UPDATE-001.md`（開發驗證用途，執行 skill 不依賴 repo）。三份 packaged references 不變。已有一次明確授權的既有 Task 正文更新與完整同 ID 讀回觀察；不代表所有逾時、衝突或跨 Session 情境已通過。TC02 部分驗證、TC13 fallback、正式輸出 schema 與 model-only 等限制保留。
