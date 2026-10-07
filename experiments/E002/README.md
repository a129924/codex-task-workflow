# E002：目前 Codex 的 YouTrack MCP OAuth 與 Ticket 操作驗證

## 驗證什麼

- 編號：E002。E001 依使用者提供的 PR #1 占用資訊保留；2026-10-07 已查本地全部可得 Git 歷史與遠端 branch/PR，未見 E002 占用。PR #1 的 files 不含實驗目錄，不能據此否定使用者的 E001 占用資訊。
- 設計日期：2026-10-07，本輪前置探測日期：2026-10-07；OAuth 登入與認證後 MCP 呼叫尚未執行。
- 主要問題：目前 Codex、指定 tenant、OAuth/CIMD 與專用測試專案能否只經官方 MCP 完成同一張票的完整操作？
- 假設：登入身分正確，真實 MCP 可建立、讀取、更新、resolved 並重新查得同一張票。

## 為什麼

此結果決定官方 MCP 能否作為後續 Task 整合的候選；不包含正式 plugin 實作或採用核准。文件只能證明能力設計，不能證明此帳號、tenant、專案權限與 workflow 的實際行為。

2026-10-07 查閱官方資料：

- [YouTrack Cloud 2026.2 MCP](https://www.jetbrains.com/help/youtrack/cloud/model-context-protocol-server.html)：官方 issue/schema/user tools、AI visibility、endpoint。
- [YouTrack OAuth Clients](https://www.jetbrains.com/help/youtrack/cloud/oauth-clients.html)：CIMD 預設關閉、須管理員啟用、不支援 DCR。
- [Resolve Issues](https://www.jetbrains.com/help/youtrack/cloud/resolve-issues.html)：多個 State 欄位均 resolved 才算整票結案。
- [官方 Codex MCP 文件](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)：trusted project 的 `.codex/config.toml`、HTTP、OAuth 與 CIMD。
- 本機 `codex-cli 0.160.1` 的 `mcp add/login --help` 已查，login 支援 `--oauth-client-registration cimd`。

假設成立可支持這一組條件繼續評估 MCP；假設不成立則將具體限制交回原整合決策，不偷偷切 token／REST。文件版本不代表 tenant 版本。

## 成功與失敗判準

- 成功：TC01–TC05 真實 MCP 全部成立，同一 ID，中文與換行內容持久化，resolved 與結案回查有證據。
- 失敗：確認必要前置條件滿足後，仍可重現地違反假設。
- 無法判定：已嘗試但缺版本、CIMD、權限、client 工具載入、schema、網路或回查證據。
- 未執行：尚未開始 OAuth/MCP 實際操作。
- 判準設定於 2026-10-07、實驗前；不以圖表或設定解析成功替代。
- MCP 上限 30 分鐘、一張票；每個受阻步驟最多一次診斷後有限修正重試。需要管理員設定、client 重啟、改變 OAuth 路徑或到達上限時停止。

## 環境與前置條件

- 真實目標：`https://a129924-tasks.youtrack.cloud/mcp`；tenant 版本、權限與 AI visibility 尚未驗證；本輪公開 OAuth metadata 回傳 CIMD 支援為 false。
- Client：目前 Codex；CLI 0.160.1；feature branch `chore/a129924/youtrack-mcp-validation`，基底 `994b509b645755744836d0a8e2baf0056e353799`。
- 專用測試專案：使用者已建立，Project ID 為 `MCPTEST`；仍待認證後 MCP 回傳確認，不把使用者提供資訊冒充 server 驗證。
- `.codex/config.toml` 僅在此 feature worktree 設定 HTTP/OAuth，不含 credentials；須由 Codex 信任該 project 才載入。
- 使用者在瀏覽器完成自己的 OAuth 登入／同意；遇管理員設定停在人工邊界。新增設定不代表当前 session 已載入工具。
- 本地圖為預期流程，沒有模擬 MCP 或偽造 Ticket。全局 Codex 設定未改。

## 重現步驟

在此 feature worktree 開啟／信任 Codex，先確認 user-provided project 已存在及 CIMD 前置條件，再由使用者執行：

```sh
codex mcp login youtrack_feasibility --oauth-client-registration cimd
```

此命令尚未執行；可能啟動瀏覽器並保存 OAuth credentials，不把授權 URL、code、state、token、callback 或私人回傳貼進本紀錄。不要用 `codex mcp add` 另改全局設定。必要時重開 client，確認當前 session 可見且可呼叫工具。

| TestCase | 操作／輸入 | 觀察 |
| --- | --- | --- |
| TC01 | OAuth 後呼叫 `get_current_user`，由使用者確認回傳是預期帳號 | endpoint、呼叫時間、身分比對結果；不保存 email／姓名等非公開資料 |
| TC02 | `find_projects/get_project` 確認 user-provided project，`get_issue_fields_schema` 查欄位 | project ID、必要欄位、合法 resolved 值的依據；缺資料向管理員求證 |
| TC03 | marker 為 `E002-YT-MCP-<UTC timestamp>-<random suffix>`；`create_issue` 標題含 marker，描述為 `YouTrack MCP 測試第一版` | 保存回傳 ID／URL；`get_issue` 讀回核對同一 ID、project、summary、description |
| TC04 | `update_issue` 更新 summary 為 `<marker> 已更新`，description 為兩行 `YouTrack MCP 測試第二版`、`中文與換行留存驗證` | `get_issue` 比對完整文字與換行，保留同一 ID |
| TC05 | 描述增加 `測試結果：本票用於 MCP 可行性驗證。`，所有 State 欄位改為已確認合法的 resolved 值 | `get_issue` 核對內容；`search_issues` 以同一 ID 查 resolved，再以 `issue id: <ID> #Resolved` 查得同一票 |
| TC06 | 若建立操作逾時或不明，以 marker 及指定 project 查詢 | 發現已建立則沿用 ID；查詢仍不明則停止，不重建第二張票 |

實際參數採當前 MCP `tools/list` 揭露的 schema，本文不虛構 wire arguments。`get_issue` 只驗內容，不假設它或 fields schema 暴露 resolved metadata。
若發現額外必填欄位／workflow，不為通過驗證而改規則。每次觀察先去敏，再記錄工具名、輸入概要、同 ID 比對值、錯誤與判準。

實際停止位置：2026-10-07 已透過 CLI 讀取 feature project 設定、探測公開 OAuth metadata 與 MCP endpoint。metadata 回傳 `client_id_metadata_document_supported: false`，MCP 回應 401 並要求認證；依管理員邊界停止。沒有啟動 OAuth、沒有認證後 MCP 呼叫、沒有 Ticket。請管理員在 Administration → Access Management → OAuth Clients 啟用 Allow automatic OAuth client registration via CIMD；確認 metadata 後才啟動既定登入。

## 是否成功

- 本輪前置探測日期：2026-10-07；OAuth 與 Ticket 步驟尚未執行。
- 實驗狀態：**無法判定**；已開始真實站台前置探測，但 CIMD 未開啟，不能判定 OAuth／Ticket 操作能力。TC01–TC06 仍未執行。
- 本輪驗證任務完成：**否**；缺少管理員 CIMD 設定、OAuth 及 TC01–TC06 證據。
- 驗證準備可交付 human review，不表示假設已成立、Task 整合完成或 blocker 已解除。

## 結果與證據

已觀察：feature worktree 已建立；CLI 功能說明已查；global Codex 設定未見 YouTrack server；本 topic 無既有 Graphify graph／runtime source，使用限定搜尋 fallback，沒有 graph build 或 provider 呼叫。

- [topic plan](../../plan/youtrack-mcp-validation/youtrack-mcp-validation.plan.md)：九欄邊界、有限實驗與使用者追加的 commit／push／Draft PR 授權。
- [預期驗證流程](diagram/workflow.html)：先前準備階段的 Archify 設計示意；其中「測試專案未建立」停點現已解除，當前停點為 CIMD。固定 Viewer UI／HTML language fallback English。
- [產物交付 receipt](diagram/delivery.json) 與 [桌面視覺 receipt](diagram/workflow.visual-check.json)：只證明本地圖表，不能作為 MCP 證據。
- `evidence/preflight.json`：先前準備階段的歷史 snapshot。
- `evidence/oauth-preflight.json`：本輪公開 metadata／MCP endpoint 探測及設定載入觀察；不含 credentials、帳號或服務 scope ID。
- `evidence/visual-review.md`：真實閱圖狀態與限制。

尚未取得 OAuth、`get_current_user`、project schema、Ticket ID、任何 MCP 寫入／讀取／resolved 證據。
PR Lens 已對先前真實 topic commits 製作本地 change map；本輪變更提交後更新至最新 head，不上傳圖表。未提交 diff 只直接審閱。

## 結論與限制

`MCPTEST` 已由使用者建立，先前專案資訊缺口已解除；尚不能判定此帳號能否登入與操作 Ticket。本輪前置探測因 CIMD 未開啟受阻，實驗為無法判定，並非假設失敗。
下一步需管理員啟用 CIMD，再確認 metadata、完成 OAuth；目前 session 尚無 YouTrack 工具，必要時在 feature project 重啟 client。登入後以 MCP 確認 `MCPTEST`、執行 TC01–TC06。
條件不足時保留部分證據，不切換 token／REST、不刪測試票、不建立正式 plugin。
正式採用仍交回原整合決策與 review；Draft PR 的 human review 先評估這份驗證準備及未滿足前置條件。
