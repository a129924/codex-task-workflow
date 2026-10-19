# Codex Task Workflow

這個 repo 保存 Task 工作流的需求 baseline、產品目標、導讀文件與現有的 YouTrack Idea plugin。完整產品方向是先支援 Codex，搭配 YouTrack 保存私人、跨專案且可長期查詢的 Task 紀錄；其他 Agent 留待後續。

正式 repo 位置：`/Users/andrew/code/plugins/codex-task-workflow`。

## 目前狀態

Repo 已提供 [youtrack-idea 0.2.0](plugins/youtrack-idea/plugin.json)，是 portable skill-only Codex plugin。它支援保存目的已知的私人 Idea、依同一 Task ID 讀回概要，以及經明確授權更新指定 Task 的摘要／正文並寫後讀回確認。不提供結案、跨專案總覽或背景同步；使用不依賴原對話、planning 文件、原 repo 或其他工作流 Skill。

安裝與使用請由 [YouTrack Idea 說明](plugins/youtrack-idea/README.md) 開始。Plugin 不內含 MCP 或 credentials；使用時仍須由人員管理官方 YouTrack MCP、認證及當次必要工具，並滿足文件列出的 schema、私人存取與方案前置條件。

[公開驗證摘要](docs/testcases/idea-save-recall-validation-summary.md) 記錄有限 live 建立／同 ID 讀回，以及一次明確授權的正文更新／完整讀回。亦有當時 client 的 0.2.0 安裝成功與安裝副本 byte-match 紀錄；這些不代表通用 client 相容或新 Session 行為驗收通過。TC02 仍為部分驗證、TC13 使用 fallback，正式輸出 schema 未暴露，一般他人不可讀實測未執行；跨 Session、更新逾時及衝突情境尚未完整驗收，不能據此宣稱完整產品或 v1 通過。

歷史 E002 則是在指定 Codex client、OAuth/CIMD、帳號及 MCPTEST 專案下，透過官方 MCP 完成同一張測試 Ticket 的建立、讀取、更新、結案與回查。它只支持該組條件下的 MCP 可行性，不是現有 plugin 的完整驗收，也不表示 Idea plugin 提供結案功能。

文件入口：

- [YouTrack Idea：安裝與使用](plugins/youtrack-idea/README.md)：現有 plugin 的安裝／外部 MCP 啟用說明、保存、讀回與授權更新的使用方式及停止條件。
- [YouTrack Idea 公開驗證摘要](docs/testcases/idea-save-recall-validation-summary.md)：已記錄的有限結果、安裝觀察與尚未完成的驗收。
- [GOAL.md](GOAL.md)：完整產品目的、工作邊界與第一版完成條件；其「目前驗證階段」仍保留較早描述，現有套件狀態請對照本 README 與公開驗證摘要。
- [Task Workflow 需求 Baseline](docs/task-workflow.baseline.md)：逐字保存 `/Users/andrew/Downloads/task-workflow.baseline.md` 的需求基準，來源原檔保留不動。
- [YouTrack MCP 驗證計畫](plan/youtrack-mcp-validation/youtrack-mcp-validation.plan.md)：E002 的範圍、事前判準與停止條件。
- [E002 驗證結果](experiments/E002/README.md)：成功判讀、同一張 MCPTEST-1 的完整操作與去敏證據；版本 metadata 於 review 階段補查，圖表保留準備階段 snapshot。
- 本 README：目前階段、文件入口與下一階段方向。

使用現有 plugin，先讀 YouTrack Idea 的安裝與使用說明，再對照公開驗證摘要。了解完整產品方向，則讀 GOAL.md 與 baseline 的需求及驗收情境。

## 下一階段

現有 Idea plugin 已有 manifest、Skill 與安裝說明；後續驗收應以公開摘要列出的缺口為起點，分別確認新 Session 載入與同 ID 讀回、更新逾時／衝突等情境，不以歷史安裝或 E002 成功代替。

完整 Task 產品仍須依 GOAL.md 與 baseline，另行設計及驗證跨專案查詢、結案等能力，以及私人存取、本人加至多一個 bot 的方案限制。使用時仍須核對當次工具與 schema；OAuth credentials 由 client 保存，不進 repo。Task 工作流維持獨立使用，不以本 repo 的文件、特定檔名或其他工作流 Skill 作為必要依賴。

## Repo 開發工具

本 repo 另有 repo-local Agent Skills，供需求分析、規劃、step 查詢、
分離 agent 交接及 worktree 開發使用。這些開發工具與上述 Idea plugin 及
Task 產品獨立；Task 不依賴這些 skills 或規劃文件。

- [Skills 安裝、支援範圍與驗證狀態](docs/agent-skills-installation.md)
- [agent-skill-implementation Topic Plan](plan/agent-skill-implementation/agent-skill-implementation.plan.md)
- [TC-AGENT-SKILLS-001](docs/testcases/TC-AGENT-SKILLS-001.md)

Step 目前僅支援明確選定的 base-plan；全部正常用途需以 TestCase 的實際
執行及獨立 review 證據確認，不能由檔案存在推定通過。
