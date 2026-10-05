# Codex Task Workflow

這個 repo 保存 Task 工作流的需求 baseline、產品目標與導讀文件，作為後續 Codex plugin 設計與實作的起點。產品方向是先支援 Codex，搭配 YouTrack 保存私人、跨專案且可長期查詢的 Task 紀錄；其他 Agent 留待後續。

正式 repo 位置：`/Users/andrew/code/plugins/codex-task-workflow`。

## 目前狀態

目前只有 baseline 與 repo 骨架，尚無可安裝或執行的 plugin。本輪交付限於以下三份文件：

- [GOAL.md](GOAL.md)：產品目的、工作邊界、第一版能力，以及產品與本輪文件各自的完成條件。
- [Task Workflow 需求 Baseline](docs/task-workflow.baseline.md)：逐字保存 `/Users/andrew/Downloads/task-workflow.baseline.md` 的需求基準，來源原檔保留不動。
- 本 README：目前階段、文件入口與下一階段方向。

建議先讀 GOAL.md 確認目標與邊界，再閱讀 baseline 的完整需求與驗收情境。

## 下一階段

依 GOAL.md 與 baseline 的需求，確認 Codex plugin 與 YouTrack 的整合方式、私人存取、跨專案查詢，以及本人加至多一個 bot 的免費方案限制，再提出可實作與驗證的設計。

runtime、transport、plugin manifest、Skill 結構及 YouTrack schema 尚未定案，本輪文件不鎖定這些介面，也未建立占位整合元件、實際 Task 資料或憑證。後續 Task 工作流須能獨立使用，不以本 repo 的文件、特定檔名或其他工作流 Skill 作為必要依賴。
