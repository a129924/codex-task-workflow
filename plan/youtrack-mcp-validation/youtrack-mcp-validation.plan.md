# YouTrack MCP OAuth 可行性驗證 topic plan

核准設計日期：2026-10-07。目標 endpoint：`https://a129924-tasks.youtrack.cloud/mcp`。
分支：`chore/a129924/youtrack-mcp-validation`，從 `dev` 的 `994b509b645755744836d0a8e2baf0056e353799` 建立獨立 feature worktree；所有實作在 feature worktree。

## Goal 與工作邊界

| 欄位 | 預計允許行為與限制 |
| --- | --- |
| Goal | 確認目前 Codex 能否經原生 HTTP＋OAuth/CIMD 呼叫官方 MCP，完成同一張 Ticket 的建立、讀取、更新、結案與回查。 |
| Non-Goal | 正式 plugin、多使用者、跨專案驗收、長期認證更新、效能或正式採用保證。 |
| In-Scope | OAuth、真實身分與 MCP 呼叫、schema、一張測試票、寫後讀取、結案後回查、去敏紀錄與本地圖表。 |
| Out-Of-Scope | 替代 client／token／REST、代建專案、修改專案權限／workflow、安裝升級工具、正式資料與發布／merge。 |
| ReadOnly | 文件、Git 與編號查證，授權後的身分、專案、schema、Ticket 讀取與搜尋。 |
| Written | 一張測試票、E002 紀錄、去敏證據、Archify specification／HTML／驗證與視覺證據；PR Lens 產物置於 repo 外。 |
| Modify | 本 worktree 的 MCP 設定、同一張測試票、本次新增產物的必要修正。OAuth credentials 僅由 client 保存，秘密不進 repo。 |
| Deleted | 無；保留測試票、歷史與證據。 |
| TestCase | TC01–TC06，詳見 E002；圖表驗證不替代 MCP 實驗。 |

## 操作與判準

1. 確認專用測試專案、tenant 版本、CIMD 與權限；管理員設定或 client 重啟停在人工邊界。
2. 原生 OAuth/CIMD 登入後，由目前 Codex 呼叫 `get_current_user`，核對預期帳號。
3. 查專案 schema 與合法 resolved 值；metadata 不足向管理員求證，不猜值或改規則。
4. 唯一 marker 建立一張票；讀取比對 ID、專案、標題、描述。
5. 更新標題與中文、換行描述；讀回比對。
6. 所有 State 類型欄位達到 resolved；讀回內容，以 `search_issues` 的同 ID、resolved 值及 `#Resolved` 搜尋確認整票結案。

成功須有真實 OAuth、當前 client MCP 呼叫、同一 ID 的完整操作及持久化／結案回查證據。
前置條件成立而可重現地不符假設才判失敗；已嘗試但缺權限、設定或證據為無法判定；未嘗試為未執行。
MCP 實驗限 30 分鐘、一張票，每個受阻步驟最多一次診斷後有限修正重試；建立回應不明先搜尋 marker，不能盲目重建。

## 輔助技能

- Archify：一張靜態 workflow，區分預期與觀察；繁中內容，固定 Viewer UI fallback English。依 showcase、deliver、visual-check 與實際閱圖驗證。
- Graphify：本 topic 無既有 graph、無相關 runtime code，採 targeted search/source reads fallback；不新建 graph。若呼叫 CLI，必設 `GRAPHIFY_NO_AUTO_REFRESH=1`。
- PR Lens：本 topic 有真實不同的 base/head commits 後才製圖，不借 PR #1、不偽造 SHA。只用 pinned 0.11.0 validate/render，產物置於 `/private/tmp/youtrack-mcp-validation/pr-lens/`，不發布圖表或改 repo config。

## Dispatch 與停止條件

Plan-Reviewer 已在對話中審查設計與 bounded 修訂；沒有宣稱 runtime gate 通過。
模式與授權允許後，由 Implementer 處理設定／產物、Tester 執行、Reviewer 判讀。
目前專用測試專案尚未建立，MCP 實驗停在 human-check；不代建專案、不改管理員設定。
實驗四態與本輪任務完成否分開，結論僅適用實際驗證條件。

## 本輪交付授權

使用者於核准計畫後追加授權：先建 feature worktree，在其中實現，按 topic commit → push → Draft PR → human review。
此授權允許本 topic 的正常提交與 Draft PR，未授權 merge、正式發布、上傳本地圖表或解除上述 MCP 前置條件。
