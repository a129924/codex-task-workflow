# TC-YOUTRACK-IDEA-ACCEPTANCE-001 — 核心保存、恢復與授權更新

## 範圍與證據狀態

驗收既有 YouTrack Idea 0.2.0：一次保存、真正新 Session 依 ID 恢復、同 ID 明確授權更新、另一真正新 Session 恢復及唯讀／停止邊界。不新增 runtime、結案或跨專案能力。此文件為可執行定義，2026-10-19 準備時 A–F live 均為 **NOT_EXECUTED**；不是產品 PASS。歷史 TC02 partial 及舊 FAIL／輸出 schema／競態限制保留，不被本 testcase 覆蓋。

Source：`plugins/youtrack-idea/skills/youtrack-idea/SKILL.md` 與三份 packaged references；base `47166176192adfb8c0e5920e25ab7b8ce8bc1807`。核准 plan `plan/idea-core-acceptance/idea-core-acceptance.plan.md` SHA-256 `730b68bdad68c9cc8b8aebc8f2d35ad189a3af7b6acf54c6bba443081789d058`。外部證據索引 `/private/tmp/idea-core-acceptance-20261019/run-001/manifest.json`；其存在不代表驗收完成。

## Preflight 與角色隔離

1. Tester 綁定 host/client、安裝版本、source/installed manifest、skill 及三 references 的實際 bytes/hash。版本號相同不足以證明相符。確認新 Session 真正載入 skill、可讀 references、認證與工具有效；沿用仍有效本人證據，身分不明／連線變動才重新 `get_current_user`。
2. 使用者已授權代理選擇合適 project，優先既有專用測試 project。依當次 `find_projects`／`get_project` 唯讀結果確認單一目標；無安全候選則停，不新建 project、不改 ACL。此授權優先於 skill 的一般不自行選擇規則。
3. 逐項檢查正式 runtime input schema：`get_current_user`、`find_projects`、`get_project`、`get_issue_fields_schema`、`create_issue`、`get_issue`、`search_issues`；更新另需 `update_issue` 安全部分更新語意。正式 output schema 不可得保留限制；以真實唯讀回應確認 ID/project/summary/完整 description、reporter、created/time 及可得 metadata，不用 prose 猜 wire shape。
4. 沿用仍適用的 private/license audit，核對 project ACL、global roles/override、Guest、All Users、team/groups、本人正向、合法一般他人與匿名負向、實際 License Details/subscription 與 retention/inactivity。不得用 private 名稱或本人可讀替代。單一使用者例外僅在明確授權、完整組態 audit 及匿名負向證據皆有效時由獨立 Reviewer 核對；一般他人 live 仍記 NOT_EXECUTED，替代結論另欄。組態變更即失效。缺證停止 create，不改安裝/config/OAuth/帳號/ACL/方案。
5. create 前讀取指定 project 當次 required fields/合法值；不得猜 Type、State、Assignee。若需 visibility，核對合法 permittedUsers/permittedGroups，於單次 create 原子表達，不事後改權限。測試票保留，不自動 close/delete。
6. Tester 與 Reviewer 持有下列 baseline；恢復執行者完全不取得本文件、manifest、baseline、原對話、原 repo、planning 文件或其他 workflow skill。恢復者只收到可信 Task ID、必要連線授權、已安裝 skill/resources，以及「請依此 ID 唯讀恢復工作概要」指令。
7. Session R1、R2 均須由人於 host 開啟或可驗證 host API 建立的真正新 Session；forked subagent、清空原對話均不算。記錄建立方式、時間、獨立 session/thread ID、實際 cwd、載入資源、完整初始輸入種類及隔離證據，私人 ID 僅留受限 mapping。API 若繼承原 repo cwd 或上下文而無法證明隔離，標 INCOMPLETE 並停受影響恢復；不得以新 thread ID 單獨宣稱獨立。

## Synthetic baseline S0（僅供保存者與評估者）

所有內容虛構。summary：`展場清單：減少漏帶展示用品`。description 使用以下完整模板；真實 ID/project 以 authoritative metadata 補足，準備時的待取得標記不觸發補 ID update。required custom fields/visibility 另依 preflight，不從正文推定 YouTrack State。

```markdown
# 展場清單：減少漏帶展示用品

- Task 識別：待釐清：尚未取得識別
- 專案：待釐清：由已授權測試專案 metadata 確認
- 標籤：待釐清：尚未確認標籤

## 目的與背景
- 目的：減少展場出發前漏帶展示用品。
- 已知背景：虛構團隊上次漏帶轉接頭，現有口頭提醒難以複查。

## 目前方向
- 方向：待釐清：紙本或共用清單尚未決定。
- 主要理由：不適用：尚未形成方向
- 待釐清：清單維護者與存放位置尚未確認。

## 工作狀態
- 階段：Idea
- 下一步：待釐清：先確認誰能維護清單。
- 阻礙：待釐清：尚未確認是否可取得過往用品清單。

## 參考資料
- 位置：example://expo/checklist｜用途：過往用品項目線索｜存取狀態：虛構位置，未讀原件，缺少可讀清單。

## 重要變更
- 1｜早期口頭提醒方案 → 待釐清清單方向｜理由：口頭提醒曾漏帶用品，尚無驗證完成的替代方案。

## 結案
- 結案類型：不適用：尚未結案
- 結果或停止原因：不適用：尚未結案
```

## Synthetic baseline S1（明確授權更新的唯一差異）

在可信同一 Task ID 上，明確授權僅改 description，summary 保持 S0。指令為：「更新此 ID 的目前方向為先試用紙本清單，理由是現場離線仍可複查；下一步為用一份虛構用品項目試填一次。保留維護者、存放位置與過往清單可得性未知、Idea 階段、參考限制、既有重要變更與未結案狀態，追加這次變更與理由。不要改其他欄位。」

S1 是完整 S0 description 套用下列三行替換及一行追加；其他 bytes 保持，若產品規則需要無害格式正規化，先記錄並由 Tester 比較，不事後改 baseline 配合輸出：

| 欄位 | S1 預期 |
| --- | --- |
| 方向 | 先試用紙本清單。 |
| 主要理由 | 現場離線仍可複查。 |
| 下一步 | 用一份虛構用品項目試填一次。 |
| 待釐清 | 清單維護者與存放位置尚未確認。（保留） |
| 追加重要變更 | `2｜清單方向待釐清 → 先試用紙本清單｜理由：現場離線仍可複查；尚未完成試填驗證。` |

保留第一筆變更且順序不變，保留過去漏帶事實及「尚無驗證完成的替代方案」的歷史語意。方向決定不是試填完成；不得補造 PASS、維護者、tag 或結案。

## 九欄位比較矩陣

Tester 分別比較 R1 對 S0、R2 對 S1；逐列記 match/mismatch/missing、來源證據及差異，不能只評「大致相符」。允許概要轉述；目的、未知、歷史與參考限制不得改義。完整存取 snapshot 的 B/D 另做 exact 比較。

| # | 欄位 | R1 預期 | R2 預期 |
| --- | --- | --- | --- |
| 1 | Task ID／project | 同一可信 metadata；不把待取得當真 ID | 同 ID/project |
| 2 | 目的與背景 | 減少漏帶；上次漏轉接頭；口頭提醒難複查 | 保留 |
| 3 | 目前方向與理由 | 方向未知；尚未形成方向 | 試用紙本；離線可複查 |
| 4 | 階段 | 正文 Idea；不推定系統 State | Idea，不轉階 |
| 5 | 下一步 | 先確認維護者，仍待釐清 | 虛構用品項目試填一次，未完成 |
| 6 | 阻礙與待釐清 | 過往清單可得性、維護者、存放位置未知 | 全部保留未知 |
| 7 | 參考及存取限制 | example:// 為虛構未讀，缺可讀清單 | 保留；不可聲稱已讀 |
| 8 | 重要變更／歷史 | 口頭提醒 → 待釐清方向及理由 | 保留 1，再追加 2 與理由及未驗證 |
| 9 | 標籤／結案 | 標籤待釐清；兩結案欄尚未結案 | 保留；無新 tag／結案 |

## A–F 操作、比較與停止

| 案例 | 執行方式及最低證據 | 準備時 live 狀態 |
| --- | --- | --- |
| A 來源與環境 | 完成上述 preflight，綁定 source/installed bytes、host、schema 與兩次新 Session provenance；任一必要條件缺失停受影響項。 | NOT_EXECUTED |
| B 保存 | 保留 exact S0、本人、project、開始時間；單次 create，可信 ID 立即同 ID 完整 readback，逐 byte/metadata 比對。成功回應但讀回不符不算保存證實。 | NOT_EXECUTED |
| C 跨 Session 恢復 | 真正 R1 僅依 ID 唯讀恢復；Tester 在獨立上下文對九欄位比 S0，核對無寫工具呼叫。 | NOT_EXECUTED |
| D 授權更新 | 原 ID 完整讀取並保留 preparation snapshot；明確授權 S1；寫前再讀 ID/project/完整 summary/description/可得 updated/visibility。基線不同停 stale payload；候選已一致則不寫。單次安全 partial update 後立即完整 readback，比 S1 並核對可得 State/Type/Assignee/tags/visibility/reporter/resolution 等非 scope 欄位。 | NOT_EXECUTED |
| E 更新後恢復 | 真正 R2，同隔離限制，九欄位比 S1；須保留未知、歷史、未驗證，不把進展當完成。 | NOT_EXECUTED |
| F 唯讀與停止 | R1/R2 唯讀 request 無 mutation；另以 static/model-only 核對缺工具/schema/private/license/完整讀回/真新 Session、目的或 ID 不明均停止；不強求所有 live 故障注入。各分支證據類型獨立，不用 static 充當 live。 | NOT_EXECUTED |

create 提交結果不明：可信 ID 已知先讀；無 ID 僅在本次 project 依正式 schema 與官方 safely quoted query 做 bounded candidates/pagination，再逐票核對 exact summary/snapshot、reporter/time 與操作關聯。無法安全 quoting、0/多候選、pagination 不完整或歧義均保留「結果不明」並停；不 retry、重建、擴專案搜尋、無限輪詢。找不到不證明未建。

update 逾時仍讀可信原 ID，不 retry/rollback/create。讀回相符只證明目前內容相符，不證明此次因果；完整讀回缺失、不符或非 scope 欄位意外變更均停並標 INCOMPLETE／結果不明。無 conditional revision 時寫前重讀仍有競態，不能聲稱無 lost update。明確拒絕且無提交疑慮才記明確失敗，內容未知與操作失敗分開。

## 結果記錄與交接

Tester 僅寫外部 `observations.md`、`comparisons.json` 與 plan 所列 visual receipts/captures；記錄實際執行時間、session provenance、工具名/schema 綁定、呼叫次數、同 ID 比較結果、受限原證據定位及每個未執行理由。私人 target mapping 僅在操作上下文／受限證據處理，不將 tenant、Task/project、帳號、ACL/license 詳情、正文或 credentials 貼入公開文件。

Implementer 依 Tester 真實證據錄入去敏結果；初次準備時尚無 observations/comparisons；後續真實觀察列於下方，未填造成功記錄。恢復者不得讀這些評估產物。Reviewer 獨立判定核心與輔助工具；完成收集不等 gate PASS。

Archify 的固定 Viewer UI 與 html lang 使用英文 fallback，authored content 為繁體中文。圖示只呈現預定流程；visual-check 四尺寸與最小／最大 light/dark 人工檢視由 Tester 負責。PR Lens 僅輔助實際 bounded diff，缺工具可 direct diff fallback；Graphify 無既有 graph 時採 rg/source fallback，不 build。工具成敗不代替 A–F。

## 第一輪 Tester 觀察與視覺回修 — 2026-10-19

此節更新初次準備狀態，保留上方作為初始定義／歷史。依獨立 Tester 的 `observations.md`／`comparisons.json`：A 為 INCOMPLETE；六份 installed/source 檔案 bytes 相符，當次八項正式 input declarations 可用，formal output schema 未暴露。真正 host API 新 thread 載入 skill 與三 references，但 host 自動注入原 repo instructions/context，因此隔離 INCOMPLETE，不能充當 C/E。可得回傳僅 actor 最終報告且截斷，未取得完整工具呼叫 trace；不據此聲稱已獨立證明無 mutation。

B–E 均 NOT_EXECUTED，未 create/update。當次 private/license 適用證據與授權仍不足，停止 create；舊單次授權已消耗，不自動延伸。F 僅完成 bounded static 停止規則核對，live recall、model-only 與 fault injection 未執行，整項仍 INCOMPLETE。九欄位 R1/S0、R2/S1 均無 live snapshot 可比。歷史 TC02 partial 及其他限制仍保留，無產品 PASS。

原 Archify HTML SHA-256 `170d5e80fa9780acf0c25f2f77f787e04995598bd6f9b08b967eaacd11e7f36d` 曾 deterministic 9/9，但 Tester 真正 visual-check exit 1、人工檢視 FAIL：四尺寸 scrollHeight 依序為 1520/1611/1611/1644，大於 viewport 高度 900/1000/1080/1320；最小畫面裁切最後審查節點。此 FAIL 不被新 revision 抹除。既有 visual receipts/captures 仍綁定原 HTML，不能用於新圖。

依獨立 Reviewer PATCH_REQUIRED 回修 authored 垂直配置，改為兩條流程帶，保留全節點文字、字級與語意，合併重複限制卡及移除多餘 viewBox 空間；未手改 HTML、隱藏 overflow 或加入捲動。蛇形流程以既有 main-role arrows 表達，省略只接受欄位遞增的 mainPath lint 欄位；一次正式授權跨帶連線指定 bottom→top，確保方向。新 specification SHA-256 `f65f4108696412327a7342b6c6c7c24189fe808c6356e0788c0048405196c51b`，新 HTML SHA-256 `a873039ad747c2a32946a109e0da1504bdd7ed5a626cc53f6cf65b3ba2dc6ece`。兩輪 focused correction 後 validate/deliver exit 0，showcase 9/9、零 errors/warnings。**新 revision visual-check／人工視覺重驗 pending Tester**，並非已通過。原 FAIL、舊 hashes、修訂與受測版本 binding 保留於 manifest。

後續狀態：使用者已授權本輪沿用同 project 的單一使用者 audit 並確認組態未變，獨立 Reviewer 已作 preflight-only 通過判定，Tester 正恢復獨立測試。上述 A–F 是第一輪已收證據的歷史狀態；本次圖修不預判恢復後結果，待 Tester 新證據與獨立審查再錄入。

## 最終實測證據同步 — 2026-10-19

本節取代上方「恢復測試進行中／visual pending」的當時狀態，保留全部第一輪 FAIL／PARTIAL／INCOMPLETE。依 Tester 最終 `comparisons.json` SHA-256 `22ff479973d978a54b630d84546274bbe92343c145f6fbc22009010b4c3c25df`、observations 及 visual receipts 錄入；獨立 Reviewer `/root/reviewer_core_acceptance` 經實際 parent handoff 判定 E 的 bounded multi-turn recovery PASS，範圍不含 single-turn PASS 或最終 artifact gate。以下 PASS 均限本次 synthetic S0/S1 與使用者選定 CLI 環境。

| 案例 | 實際結果與範圍 |
| --- | --- |
| A | 六份 installed/source bytes 相符、八項當次 input declarations 可用。使用者選現有 CLI 0.163.0，在 repo 外 `/private/tmp` fresh exec、read-only，未改安裝/config/model。先前觀察 0.162.1 不是 pinned 版本；實際 probe 與 C/E 為 0.163.0。原 host API 注入 repo context 的隔離 INCOMPLETE 永久保留，不改記成功。CLI probe 與兩次 recall 為不同 native fresh threads，實際讀到 skill bytes 相同；未把 probe 當 C/E。 |
| B | 本次 audit 沿用經使用者明授權及 unchanged 確認，獨立 Reviewer preflight-only 通過後，fresh 本人比對符合。單次 create，立即同 ID 完整 get_issue，S0 summary/description exact、project/reporter/createdAt 與 self-only visibility 核對一致。 |
| C | 真正 repo 外 fresh CLI Session，只給可信 ID、唯讀意圖與隔離限制；未給 baseline/原 repo/其他 Session。完整 native trace 僅 packaged skill read 與一次同 ID get_issue，S0 exact，恢復概要九欄位全 MATCH，零 mutation。 |
| D | 原 Tester 上下文完整 preparation read、獨立 prewrite reread 確認 unchanged；單次 update 僅指定 ID＋description，summary 未改。立即同 ID 完整 readback exact S1，兩筆歷史順序保留，19 項可得非 scope 欄位無意外變更。 |
| E | 另一真正 repo 外 fresh CLI Session，同 only-ID／唯讀／隔離限制；一次 get_issue 得 exact S1，零 mutation。首答仍是 8 MATCH＋歷史欄 PARTIAL：省略中間待釐清方向及兩次各別理由，不將 source 完整偷換為概要完整。 |
| E 追問 | 經獨立 Reviewer 授權，在同一 R2 唯一一次一般追問「請僅依同一 Task 記錄，列出重要變更的先後與各次理由；保持唯讀。」未給 baseline／評分／預期答案，沒有新 thread、command、MCP call 或 write。回覆完整兩筆先後、各別理由及未完成試填，未補造日期。Reviewer 判 combined bounded multi-turn PASS；首答歷史 PARTIAL 與非 single-turn 限制保留。 |
| F | C/E 完整 native traces 均僅唯讀，前述 static stop rules 核對及缺當次授權時先停 create 的歷史保留。不是全部 adverse branches 通過：model-only、unknown create/update recovery 與 live fault injection 未執行。 |

九欄位最終比較：C 對 S0 九列 MATCH；E 首答對 S1 第 1–7、9 列 MATCH，第 8 歷史列 PARTIAL；同 R2 的上述唯一追問另有第 8 列 MATCH 證據，不重寫首答。合計恰一 create、一 description update；無 close/delete、State/Type/tag/ACL/account/config/visibility 改動。真實 target/account/URL、Task 正文 mapping 與 native thread IDs 不公開，也不複製至 run manifest。

修正版 HTML `a873039ad747c2a32946a109e0da1504bdd7ed5a626cc53f6cf65b3ba2dc6ece` 已由 Tester visual-check exit 0：四尺寸 scrollWidth/Height 均不超過 viewport；最小／最大 light/dark 四張實際 view_image 人工檢視 PASS，完整流程、stop、審查、legend／限制皆可見，無可見裁切或重疊。原 HTML `170d5e80…` 四尺寸 FAIL 的 1520/1611/1611/1644 與修復關聯仍保留。PR Lens 依本次文件同步重建真實 bounded diff；新產物仍須 Tester 重新核對，沒有新 commit/PR。Graphify 保持無既有 graph 的 source fallback。

限制：歷史 TC02 partial 不被本次 bounded testcase 改寫；普通他人 live negative 仍 NOT_EXECUTED，單一使用者 substitute 只限本次經獨立核對的組態／授權，不作永久私密或保存承諾，license/retention 來源衝突保留。Formal output schema 未暴露；沒有 conditional revision，prewrite reread 不消除競態、不能保證無 lost update／exactly-once。逾時／衝突／未知寫入與所有停止分支未 fully live 驗收。CLI trace 支持本次可見行為，不證明所有 hidden host injection 不存在或日常 host 普遍相容。此為證據同步，尚待 Tester final artifact rebinding 與獨立 Reviewer 最終 gate。
