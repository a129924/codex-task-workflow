---
name: youtrack-idea
description: 將目的已知的 Idea 保存為私人 YouTrack Task，或經明確授權更新指定既有 Task 並寫後讀回確認；亦可僅依 Task ID 恢復概要。不處理結案或跨專案總覽。
---

# 私人 Idea 保存與讀回

使用官方 user-client MCP `youtrack_idea`。保存／讀回基礎七工具：`get_current_user`、`find_projects`、`get_project`、`get_issue_fields_schema`、`create_issue`、`get_issue`、`search_issues`。更新僅額外使用官方 `update_issue`，且必須當次已暴露並可核對實際 schema；不使用 delete/close，不自建 adapter、proxy、重試服務或背景同步。不因已讀到過期資訊而自動寫入。Task 使用不依賴原對話、planning 文件、PR、原 repo 或其他 workflow skill。

## 啟用與當次 schema preflight

確認 skill 已在安裝後的新 Session 真正載入，官方 MCP 已啟用且認證有效。沿用仍有效的本人確認與連線證據；身分不明或連線狀態有變時用 `get_current_user` 比對使用者確認的本人，不從歷史實驗猜身分。CIMD 未開、登入或啟用需要人員處理時停下，不改走 token／REST，不改 client config／credential store。

檢查當次需要的工具 runtime schema（保存／讀回基礎七項；更新另需 `update_issue`），依正式宣告構造參數；缺工具、必要 argument 或欄位不符時提出 Integration Scope Gap，停止受影響操作。不憑文件、歷史宣告或範例猜 wire shape。正式輸出 schema 未暴露不等於欄位不存在，也不代表已驗證輸出；依可得 schema 與真實唯讀回應核對必要欄位，不把工具 prose 當真實輸出證據。無法核對就保留未驗證並停止受影響操作，不為取得 create 輸出而試建票。

每次 create 前用 `get_issue_fields_schema` 核對指定 project 的必要 custom fields 及合法值；確認 project、summary、description 可持久化，`get_issue` 可讀回真實 ID/project/summary/完整 description。恢復查證還需 reporter、created/time 與可得操作關聯。需要建立時 visibility arguments，確認當前 `permittedUsers`／`permittedGroups` schema 與合法身分表示；缺必要資料先問／停，不調整 project workflow。

`find_projects` 只在辨識使用者指定目標 project 時限定查詢，以 `get_project` 核對可得資訊；多候選先讀可得資訊再請使用者選定，不自行選擇，不提供跨專案 Task 搜尋入口。

## 每次建立前的 private／license gate

沿用可適用且仍有效的真實 tenant 證據，不以「private」名稱或工具 allowlist 代替權限驗證：

- audit 指定 project ACL、global roles／override、Guest、All Users、team、groups；預期可讀者為本人與日後明確授權至多一 bot。揭露管理員特殊權限，無 bot 不新建。
- 常規路徑本人正向可讀；使用既有合法一般他人身分及匿名途徑取得不可讀的負向證據（只有下方限定單一使用者例外可替代一般他人實測）；已有授權 bot 才驗 bot。AI-specific visibility 只能額外縮窄，不能取代 ACL；讀不到不能證明票不存在。
- 核對實際 tenant License Details、subscription、retention／inactivity 條款，確認私人 project 與本人加至多一 bot 的規模可用；bot 算 User。來源衝突保留，不能挑選有利文件消除衝突，不承諾永久保存。

缺證標 pending，停止受影響 live create 與產品通過聲明。需要外部身分操作、付費、改帳號／ACL／方案，或僅允 public，交由 human 決定 Integration Scope Gap，不自行修改。

### 限定單一使用者 tenant 的負向取證例外

僅針對使用者明確授權的本次單一使用者 tenant／指定專案，普通他人實測可由完整帳號／角色 audit 加匿名負向驗證替代；這不是一般 tenant 的預設政策。必須同時滿足：

1. 完整 Users 清單只有本人管理員及被 banned 的 Guest，沒有其他一般使用者、bot 或未知帳號；完整核對所有 users、groups、team、project roles、global roles 及 Override Visibility Restrictions，揭露管理員 override。
2. Guest banned 且無角色／Read Issue；All Users 無任何指派角色；Registered Users 在目標 project 無權限，其 global Observer 不含 Read Issue 或 visibility override；沒有其他群組、直接角色、全域角色或 override 對一般他人授予讀票權。
3. 本人已正向讀取該專案既有票；匿名環境對同一既有票讀取被 sign-in gate 拒絕，未取得票內容。不能把登入後畫面、UI 導航失敗或讀不到候選票當匿名負向證據，也不能推論票不存在。
4. 保留 human 對本次替代方式的明確授權及可追溯證據，由獨立 Reviewer 核對適用性與完整性；缺任一條件即 pending，停止 create。一般他人實測仍記 NOT_EXECUTED，不得改為 PASS 或 N/A；替代路徑結論與實測狀態分欄記錄。
5. 只適用本次已 audit 的 tenant／project／帳號與角色組態。出現一般使用者、bot、其他帳號／角色，或 ACL、group、team、global role／override、Guest 狀態變動，例外即失效；重新 audit 並回到常規合法一般他人與匿名負向實測，不沿用本次豁免。不得新增帳號或修改權限來湊條件。

此例外只替代一般他人負向實測，不放寬 private entitlement、License Details／subscription、官方 retention／inactivity 適用判讀與來源衝突處理，不作永久免費／私人／保存保證。也不放寬安裝更新後獨立新 Session 的 skill 真正載入、本人／七工具與必要 schema gate；TC02 建立後同 ID 新 Session 讀回仍是獨立驗收。保留未執行實測、輸出 schema 未暴露及其他既有驗證限制；採用替代路徑不將產品驗收或其他 runtime gate 自動標 PASS。

## 整理候選內容

保存時讀 packaged [內容規則](references/task-content-format.md) 與 [模板](references/task-content-format.template.md)；需對照未知／矛盾／參考情境時再讀 [示例](references/task-content-format.examples.md)。示例與 `example://` 均為虛構，不作真人或存取證據。副本含完整生命週期格式，本 skill 執行 Idea 新建、經授權的指定 ID 內容更新與既有 ID 唯讀；不執行結案或系統階段轉換。

確認使用者主動要求保存、希望解決的目的、明確已授權的 project，以及是否指向既有同一事情。目的不明先釐清；方向、理由、下一步或阻礙未知可保存，依規則標 `待釐清：…`。`無` 必須已確認，`不適用：…` 要有原因。來源矛盾保留差異，不把較新訊息或候選方案當成決策。對象不明停止受影響 create，不以新建規避。

- summary 採 `工作對象：目的或期望結果`，以已知目的命名。
- authoritative metadata 表達 Task ID/project；description 保存完整其餘自足正文、標籤語意及模板所有區段與順序：目的與背景、目前方向、工作狀態、參考資料、重要變更、結案。可保留同名標題，不以虛構 ID/project 取代 metadata。準備時識別待取得；讀回 snapshot 用真實 metadata 補齊 ID/project 語意，不為補 ID 再 update。
- 正文階段寫 Idea，不推定 YouTrack State=Idea；標籤未知如實待釐清，不建立 tag。尚未結案兩欄寫 `不適用：尚未結案`；重要變更只依已知來源，不虛構歷史。
- 參考依 `位置：…｜用途：…｜存取狀態：…`，不可存取說明缺少什麼，轉述不能當已讀原件。本文能恢復目的、背景、方向或未知、階段、下一步或缺口、阻礙，不以「詳見參考」代替；不匯入全文或完整對話。
- required custom fields 只填已知、已授權意圖且 schema 合法的值；不足問／停，不默認 Type、State、Assignee 或改 workflow。

## Save 與寫後確認

指向既有同事情時，沿既有 ID `get_issue`，不另建；唯讀請求僅回報，只有明確授權更新才進入下方流程。多候選先釐清，無法判定就停。

新建必須目的、project、對象與授權明確，啟用/schema、private/license gate 均滿足。提交前在本次上下文保留 project、exact summary、完整 snapshot、reporter 身分及操作開始時間。依當前合法 schema **單次** `create_issue`；可用 visibility arguments 時，在此次 create 原子表達本人及已明確授權至多一 bot，不以事後 ACL update 補救，也不取代 private project gate。不加 marker、不假定 idempotency key，不承諾 exactly-once。

create 明確回可信 ID，立即 `get_issue` 同 ID，核對 ID/project/summary/完整 description 與 metadata 語意。一致才回報「已證實保存」、真實 ID 與已保存摘要；readback 不符或失敗則說明驗證未完成／結果不明，不更新、不另建。

## 結果不明的 bounded recovery

提交後斷線、逾時或是否接受無法確定，不能說成未建立，不 retry create。可信 ID 已知先 `get_issue`；無 ID 時，只在本次指定 project 用摘要字串作 safely quoted candidate `search_issues`。依當前 runtime schema 與官方 YouTrack query quoting 表達；單引號 arbitrary string 是全文搜尋，不是 summary equality。無法安全表達時停，不猜 escaping。

完成 pagination 後逐候選 `get_issue`，比對 project、exact summary、完整 snapshot、reporter、created/time 與可得操作關聯。僅充分證據支持同次建立才沿用 ID 並做寫後核對；單一內容相符不普遍證明同一事情。這是本次不明寫入的限定查證，不是跨專案搜尋能力。

0 候選、分頁不完整、AI visibility 隱藏、碰撞／多候選、metadata 不足或任何歧義均維持結果不明，停止並請人員安全查證。無法在本次有限查證中完成分頁或同票核對就停，不持續輪詢或放寬 project。找不到不證明未建立，不以重建作默認 fallback。不承諾跨 Session 自動保留重試紀錄。

## 經授權更新既有 Task

只有使用者明確要求更新指定 Task ID、且已知變更目的／內容時才寫入。保存或讀回的授權不包含更新；目的或目標不明先釐清，不建立替代票。使用 packaged 內容規則與模板，修正目前 snapshot 並追加重要變更；保留原有變更順序、理由、參考及未完成驗證，不把過去 FAIL 刪成從未發生，也不把有限 PASS 擴張成完整產品 PASS。

1. 確認 `update_issue` 當次正式輸入宣告，是否能僅更新指定 ID 的 summary／description。缺工具或無法確認安全部分更新語意就停止寫入；交人員以官方 client 設定啟用，不自改 allowlist、config、OAuth，不走 token／REST 或 UI 替代。正式 output schema 未暴露仍保留限制，以實際同 ID 讀回核對。
2. `get_issue` 讀取真實 ID、project、完整 summary／description 及可得 updated／visibility metadata；確認仍為已授權 project／對象，本人及私人存取條件仍適用，不因可讀就推定可寫或可公開。無法取得完整正文就停。沿用仍有效的 private/license 證據，不更動權限。
3. 在本次上下文保留原始完整 snapshot 及擬寫 snapshot，只更動明確授權的 summary／description。本模式不移動 project、不改 State／Type／Assignee／tags／visibility，也不結案。由實際來源確認最新進展，票內歷史與新事實有差異時記錄「原狀態 → 新狀態」與理由；未知保留。僅在目前上下文保留私人原文，不在輸出或 repo 證據重貼全文、個資或憑證。
4. 寫前再讀同 ID，對照完整 summary／description、project 及可得 updated／visibility；若相對準備基線有變，停止舊 payload，展示必要的去敏衝突後重新整理，不靜默覆蓋。若工具提供正式 conditional revision，使用它；沒有就揭露仍有讀寫競態，不能承諾原子合併／無 lost update。候選與當前已相同時回報「內容已一致，未寫入」。
5. 依當次 schema 單次 `update_issue`，只送已授權且實際需改的 summary／description 與指定 ID。不猜 wire names、不送未修改欄位、不把 create 結果不符當作更新授權，不宣稱 exactly-once。
6. 無論 update 回應成功或結果不明，立即以可信原 ID `get_issue`。完整比較 ID／project／summary／description 與擬寫 snapshot，並核對可得 visibility 及可得未授權欄位沒有意外變更。一致且無異常才回報「已確認目前內容與授權更新一致」；工具成功且讀回一致可報「已證實更新」。逾時後讀回相符僅證明目前內容相符，不證明本次寫入因果。讀回不符、不可達或有非預期變更時回報驗證未完成／結果不明並停；不自動 retry update、不回滾覆寫、不 create。只在獨立明確的新授權與新基線下再次處理。

輸出去敏摘要、真實 Task ID、更新範圍與確認結果，並明記仍未通過的驗證。此為使用者主動更新，不承諾背景同步或跨 Session 自動追蹤。本地／model-only 驗證與一次 live 更新各自記錄，不互相冒充。

## 依 ID 讀回與結果表達

新 Session 只需同一 Task ID 與既有 client 啟用／OAuth 狀態。`get_issue` 後以 Task 記錄回報目的、背景、方向或未知、階段、下一步或缺口、阻礙、參考存取限制及既有歷史／結案資訊。未知下一步如實未知，不補造待辦、同步進度、轉階或寫入。缺必要欄位時揭露缺口，不編造完整 snapshot。

操作結果分別表達：候選／準備中、已證實保存、明確失敗、結果不明（含驗證未完成）。內容未知與操作失敗分開。只有認證／權限明確拒絕且無提交疑慮才報明確失敗；有提交疑慮沿不明流程，讀回不可達不當未建。停用 skill 保留已存 Task，不清資料或 credentials。結案、其他生命週期能力或替代平台需求交後續 Mission；不自動同步本地工作進度。
