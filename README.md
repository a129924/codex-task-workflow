# Codex Task Workflow

這個 repo 保存 Task 工作流的需求 baseline、產品目標與導讀文件，作為後續 Codex plugin 設計與實作的起點。產品方向是先支援 Codex，搭配 YouTrack 保存私人、跨專案且可長期查詢的 Task 紀錄；其他 Agent 留待後續。

正式 repo 位置：`/Users/andrew/code/plugins/codex-task-workflow`。

## 目前狀態

目前已保存 baseline，並完成 E002 的 YouTrack MCP 可行性驗證；尚無可安裝或執行的正式 plugin。E002 在指定 Codex client、OAuth/CIMD、帳號及 MCPTEST 專案下，透過官方 MCP 完成同一張測試 Ticket 的建立、讀取、更新、結案與回查。此結果只支持已驗證條件，正式整合與採用仍待獨立決策及 human review。

文件入口：

- [GOAL.md](GOAL.md)：產品目的、工作邊界、第一版能力，以及產品、歷史 baseline 與目前驗證階段的完成條件。
- [Task Workflow 需求 Baseline](docs/task-workflow.baseline.md)：逐字保存 `/Users/andrew/Downloads/task-workflow.baseline.md` 的需求基準，來源原檔保留不動。
- [YouTrack MCP 驗證計畫](plan/youtrack-mcp-validation/youtrack-mcp-validation.plan.md)：E002 的範圍、事前判準與停止條件。
- [E002 驗證結果](experiments/E002/README.md)：成功判讀、同一張 MCPTEST-1 的完整操作與去敏證據；版本 metadata 於 review 階段補查，圖表保留準備階段 snapshot。
- 本 README：目前階段、文件入口與下一階段方向。

建議先讀 GOAL.md 確認目標與邊界，再閱讀 baseline 的完整需求與驗收情境。

## 下一階段

依 GOAL.md、baseline 與 E002 的有限驗證結果，繼續確認正式 Codex plugin 的整合方式、私人存取、跨專案查詢，以及本人加至多一個 bot 的免費方案限制，再提出可實作與驗證的設計。E002 未驗證這些後續產品需求。

正式 plugin 的 runtime、transport、manifest、Skill 結構及產品 YouTrack schema 尚未定案。E002 僅增加需手動啟用的 MCP 重現範例、實驗紀錄與一張已結案測試票；OAuth credentials 由 client 保存，不進 repo。後續 Task 工作流須能獨立使用，不以本 repo 的文件、特定檔名或其他工作流 Skill 作為必要依賴。
