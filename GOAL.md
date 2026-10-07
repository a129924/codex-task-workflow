# Codex Task Workflow：產品目標

## 目的

建立可長期留存、供本人與 Codex 查詢的 Task 紀錄。隔一段時間或換一個 Session 回來，仍能知道一件事為什麼做、目前選擇什麼方向、做到哪裡，以及接下來做什麼。

本 repo 的正式位置是 `/Users/andrew/code/plugins/codex-task-workflow`。需求基準保存於 `docs/task-workflow.baseline.md`；本文件整理產品目的、邊界與完成條件，不取代需求基準。

## 使用者與產品方向

服務獨立開發者，使用規模以本人加至多一個 bot 評估。Task 需要私人存取、跨專案收集，並能依專案、標籤與狀態篩選；不必與 public code repo 的外部 Issue 混在一起。

第一版優先支援 Codex，以 Codex plugin 搭配 YouTrack 為方向。評估免費方案時，須確認適合持續累積 Task，避免張數限制成為日常負擔；具體額度與限制仍須在整合階段查證。

整合優先採官方支援或社群廣泛採用的工具；缺少合適選項時，再評估自行補足。其他 Agent 留待後續，不在第一版承諾支援。

## Task 應保存的工作脈絡

同一件事情從發想到結束沿用同一個 Task 識別，隨工作成熟逐步補充：

- 名稱、目的、已知背景、所屬專案與標籤。
- 目前方向、主要理由與仍待釐清的問題。
- 目前階段、下一步與阻礙。
- 可選的參考位置，以及理解用途所需的簡短說明。
- 重要方向變更的先後與理由，以及結案結果或停止原因。

Idea 可以只有目的、已知背景、待釐清問題與下一步，不要求所有欄位完整。Agent 不得把尚未確認的內容補成已定案的決策。

更新目前方向時，保留重要變更的簡短脈絡；不要求保存所有對話或每個技術步驟。

## 第一版能力

使用者在需要時請 Codex 執行四類操作：

1. 建立 Task：將已討論的發想整理成可留存的高層摘要。
2. 查詢 Task：跨專案尋找工作，依專案、標籤與狀態篩選，讀取單張 Task，並能包含已關閉項目。
3. 更新 Task：記錄方向、階段、下一步、阻礙與參考資料；重要方向變更附上理由。
4. 關閉 Task：保存完成結果、取消或停止原因，保留日後查詢能力。

留存能力以實際寫入 Task 的內容為準，不承諾每個 Session 自動更新。新的 Codex Session 應能透過 Task 紀錄理解工作概要，再按需要查看參考資料。

## 獨立性與生命週期

沒有 `plan.md`、`step.md`、PR 或其他 Skill，仍可建立、查詢、更新與關閉 Task。不以特定檔名、目錄或檔案是否存在作為建立或轉換階段的條件。

參考資料可以有零份、一份或多份，包含任意名稱的文件、設計圖、討論連結與 PR。附加參考不表示 plugin 接管其產生、維護或同步。參考暫時無法存取時，Task 本身的目的、方向、狀態與下一步仍應可讀，Agent 應說明缺少的資料。

主要生命週期為：

Idea → Draft plan → Implementation plan／實作 → PR → Close

階段描述進展，不要求搭配文件或執行特定 Skill；可以跳過階段、返回前一階段，或在決定不繼續時結案。Close 必須留下結果或原因。PR 可關聯同一張 Task，建立或合併 PR 不自動關閉 Task。實際狀態名稱與系統映射留待整合設計。

## 範圍外

第一版不包含：

- 強制更新狀態的 Hook、阻擋機制、背景同步或主動通知。
- Ghostty 視窗辨識、Session 命名、Session 自動恢復或多 Agent 協調。
- 執行或接管既有規劃、實作、Review 與 step-tracker 工作流。
- 自動掃描所有 repo、匯入歷史文件或同步文件全文。
- 自動追蹤 GitHub PR 事件、建立 PR 或自動結案。
- 自建任務管理平台、專屬 Dashboard 或完整對話記憶系統。

原始 baseline 階段只交付需求文件與 repo 骨架，當時不實作 YouTrack 串接、可執行 plugin、安裝流程或其他 Agent 支援，也不鎖定 runtime、transport、manifest、Skill 結構或 YouTrack schema。這是歷史交付範圍；目前階段見下方與 README。

## 產品完成條件

第一版產品需證明：

1. 沒有任何規劃文件或其他工作流 Skill，也能建立 Idea，查詢、更新，並以停止原因結案。
2. 同一張 Task 可後續附加任意名稱的文件或 PR，不要求調整原本檔案結構，也不接管參考資料維護。
3. 連假後可從專案 Task 清單找到工作，理解目的、方向、階段與下一步。
4. 新的 Codex Session 不依賴原始對話，也能理解概要並辨識待釐清內容。
5. 結案後仍可查詢重要選擇、方向變更理由、最終結果與參考資料。
6. 四類操作適用於私人、跨專案的 Task 管理，符合本人加至多一個 bot 的使用規模。

## 原始 baseline 階段文件完成條件（歷史）

該階段的正式 repo 包含本文件、README.md 及與來源逐字一致的需求 baseline；文件清楚區分目前階段與產品目標，路徑一致，且未建立占位整合元件或存放實際 Task 資料與憑證。

文件與骨架驗收通過，只代表該 baseline 階段交付完成，不代表 Codex plugin 或 YouTrack 整合已完成。

## 目前驗證階段

後續 [E002](experiments/E002/README.md) 已透過官方 YouTrack MCP，在指定 Codex client、OAuth/CIMD、帳號及 MCPTEST 專案下完成一張測試票的建立、讀取、更新、結案與回查。Repo 保存去敏測試內容、結果與重現範例；沒有交付正式 plugin，也沒有預設啟用的 project MCP 設定。Credentials 仍由 client 保存，不進 repo。

E002 的完成條件與證據記錄於 [topic plan](plan/youtrack-mcp-validation/youtrack-mcp-validation.plan.md) 與實驗 README；本次有限驗證不代表上列第一版產品完成條件已成立。正式整合與採用仍待獨立決策及 human review。
