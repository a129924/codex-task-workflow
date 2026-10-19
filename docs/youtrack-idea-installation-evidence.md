# YouTrack Idea：安裝與啟用證據

2026-10-19 的單一 CLI 觀察未能完成 inventory：命令 exit 1，stdout 為空，stderr 指出 configured marketplace snapshot 的 root 缺少支援的 manifest。因此目前 **installed＝UNKNOWN、effective-enabled＝UNKNOWN、安裝事件時間＝UNKNOWN**。使用者設定的 `enabled = true` 只是一項宣告；本文件沒有修復安裝或設定。

## 目的與範圍

| 欄位 | 本題內容 |
| --- | --- |
| Goal | 讓安裝、有效啟用、設定宣告與歷史證據分開，結論可追溯。 |
| Non-Goal | 不新增產品功能，不要求所有狀態為正向，不宣稱完整產品驗收。 |
| In-Scope | 單一主機、既有 CLI、固定 OBS cwd 的唯讀觀察；重用固定歷史來源；本報告與私人審閱輔助。 |
| Out-Of-Scope | desktop／host matrix、neutral-directory 比較、安裝／重裝／註冊／登入／啟停／設定或 PATH 修復、live Task、新 Session、bytes 重驗、core summary 修改及新測試套件。 |
| ReadOnly | OBS／CORE 的指定 commit 來源、必要 CLI help／host context、限定非秘密設定鍵、既有 graph／overlay 是否存在。 |
| Written | Plan-Creator 新建 `plan/plugin-installation-evidence/plugin-installation-evidence.plan.md`；Implementer 新建本報告。私人 RUN 只含 approved plan allowlist 的 index、原始查詢與 review aids；Tester 的 `verification.json` 尚待其本人執行。 |
| Modify | 既有 tracked files 無修改；上述兩份是新增檔，不列為修改。 |
| Deleted | 無。 |
| TestCase | 本文件末尾的人工表格；未遇分支維持 method-only，沒有 fault injection。 |

OBS 是原始 main worktree，僅作觀察；FEATURE 是分離的文件 worktree，base 為 `0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a`。RUN 是本次私人 evidence root。公開只使用 aliases；exact roots、binary locator、原始私有路徑、命令、exit、完整 SHA-256 與檔案清單留在 RUN 的 `manifest.json`、`context.json`、`provenance-observations.json`、`aids.json`，不進 Git。

## 本次 context 與原始結果

觀察時間為 **2026-10-19T03:51:42Z**（查詢完成記錄 `03:51:42.859429+00:00`），CLI `0.163.0`，macOS `26.5.2`（build `25F84`）。實際 OBS branch 是 `dev`、HEAD 是 `0c6d81aa1b8381573d599cc6bb31bbf02af5b954`，查詢前工作樹乾淨。這是 runtime context；下節歷史文件仍從凍結的 OBS@`0d3ca3d` Git objects 讀取，未將來源悄悄換成較新的 dev。FEATURE HEAD 仍為 base，沒有建立實作 commit。

從 OBS 執行一次原命令，沒有 `--available`、profile 或 config overrides：

```sh
codex plugin list --marketplace idea-save-recall-local --json
```

實際 exit `1`；`plugin-list.stdout.json` 是 **0 bytes**，不是成功 JSON 或空陣列。`plugin-list.stderr.txt` 原樣保留 warning 與錯誤，公開去識別摘錄為：

```text
WARNING: proceeding, even though we could not create PATH aliases: Operation not permitted (os error 1)
Error: failed to load configured marketplace snapshot(s):
- `idea-save-recall-local` at <CONFIGURED_SNAPSHOT>: marketplace root does not contain a supported manifest
```

版本及 help 命令 exit 0，也有相同 PATH aliases warning。沒有改 PATH／權限或重新查詢 inventory。CLI help 說明 `--available` 會把未安裝項目加入 JSON；本次未使用該選項，但查詢失敗，所以不能利用「無項目」推導未安裝，也沒有成功結果 schema 可解析或 runtime `enabled` 欄位可解讀。錯誤只支持本次 configured snapshot 載入失敗；不證明本 repo 的 root `plugin.json` 格式錯誤、不證明 plugin 已卸載。

限定設定讀取發現 user config 的 `[plugins."youtrack-idea@idea-save-recall-local"] enabled = true`，及 OBS project 的 `trust_level = "trusted"`；沒有預設 profile 或 `CODEX_HOME`／`CODEX_PROFILE` 環境值。OBS 與已檢查的直接父目錄沒有 project `.codex/config.toml`，已檢查的 system config／requirements 位置亦不存在。這是限定檔案與鍵值觀察，不是所有 cloud／ancestor／managed 層的有效設定 dump，未證實完整 precedence。

[OpenAI 官方 packaging 文件](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo) 說明 repo plugin enabled 設定、trusted project 載入與 precedence；[官方 CLI plugin browser 說明](https://learn.chatgpt.com/docs/plugins#plugin-browser-in-codex-cli) 提供 installed／enabled 的使用介面背景。這些是設定語意來源，不能替代本次有效設定或載入證據。單獨宣告 `true`、同版本號或歷史安裝成功，都不足以補成目前有效啟用。

## 固定來源與可支持範圍

以下連結綁定 commit，沒有把目前分支的相對連結冒稱歷史 bytes。完整逐檔 digest 留在私人 index；短 digest 供交叉識別。來源文件內的結論仍是既有記錄，本題沒有重跑。

| ID／來源 | 固定版本 | SHA-256 前 12 碼 | 證據界線 |
| --- | --- | --- | --- |
| [R：plugin README](https://github.com/a129924/codex-task-workflow/blob/0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a/plugins/youtrack-idea/README.md) | OBS@`0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a` | `9b69fb9d37cf` | 安裝方法與 packaged references provenance；不是本機狀態。 |
| [P：plugin manifest](https://github.com/a129924/codex-task-workflow/blob/0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a/plugins/youtrack-idea/plugin.json) | OBS@`0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a` | `cd7145df21d5` | 宣告 youtrack-idea 0.2.0；不是 installed inventory。 |
| [M：marketplace catalog](https://github.com/a129924/codex-task-workflow/blob/0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a/.agents/plugins/marketplace.json) | OBS@`0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a` | `dd7c0acd3865` | 宣告 marketplace 名稱與 ./plugins/youtrack-idea；不證明實際註冊位置。 |
| [H：歷史公開摘要](https://github.com/a129924/codex-task-workflow/blob/0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a/docs/testcases/idea-save-recall-validation-summary.md) | OBS@`0d3ca3d9dd764d15b22932a3fcc88c7feb52bb1a` | `168cad4e5b9e` | 2026-10-16 次級 discovery／安裝記錄；當時 installed manifest、skill 與三份 references byte-match；CLI／OS／確切事件時間未知。 |
| [CP：core plan](https://github.com/a129924/codex-task-workflow/blob/655cbf36eec4e8065b8d54c41aa638d394c452bf/plan/idea-core-acceptance/idea-core-acceptance.plan.md) | CORE@`655cbf36eec4e8065b8d54c41aa638d394c452bf` | `730b68bdad68` | 凍結 core 範圍與私人記錄 locator；不是目前 checkout bytes。 |
| [CT：core testcase](https://github.com/a129924/codex-task-workflow/blob/655cbf36eec4e8065b8d54c41aa638d394c452bf/docs/testcases/TC-YOUTRACK-IDEA-ACCEPTANCE-001.md) | CORE@`655cbf36eec4e8065b8d54c41aa638d394c452bf` | `146aac07151f` | 固定 core 六檔比對、八項 input declarations 及 fresh recall 記錄；不重驗。 |
| [CS：core 公開摘要](https://github.com/a129924/codex-task-workflow/blob/655cbf36eec4e8065b8d54c41aa638d394c452bf/docs/testcases/idea-save-recall-validation-summary.md) | CORE@`655cbf36eec4e8065b8d54c41aa638d394c452bf` | `b356b38c7f06` | CLI 0.163.0 bounded multi-turn recall 等既有觀察與限制；不是目前安裝或 blanket PASS。 |

H 的文件日期、當時成功安裝敘述、這次查詢時間與真實安裝事件時間分開。本題未取得可綁定目前安裝的 event receipt，沒有從 cache 或 filesystem mtime 推算安裝時間，也沒有重裝補歷史。

CORE 固定為 `655cbf36eec4e8065b8d54c41aa638d394c452bf`，由 Git objects 讀取 CP／CT／CS；已知 core worktree 後來前進，沒有 checkout 或讀其目前文件冒充固定來源。CT／CS 記錄六個 installed/source 檔案 byte-match、八項 input declarations、CLI 0.163.0 的兩個 repo 外 fresh recall：C 九欄 MATCH，E 首答歷史 PARTIAL，唯一一般追問後的 bounded multi-turn 證據完整。這不是 single-turn PASS；先前 API context injection INCOMPLETE、TC02 PARTIAL、formal output schema 不可得、adverse／timeout／unknown-write 未完整驗收等限制保留。這些歷史結果不建立目前 bytes 或新產品驗收；沒有複製私人 Task 內容、重跑 live 或開新 Session。

## 證據矩陣

| 步驟／前提 | 文件來源 | 既有／目前證據 | 環境／時間 | 未知或限制 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| catalog 與 package identity | R／P／M | 宣告 youtrack-idea 0.2.0，source.path 相對 marketplace root | OBS@0d3ca3d | catalog 不等於已註冊或已安裝 | 需要時由人員另行核對實際 snapshot；本題不修。 |
| CLI／cwd | context、CLI help | 0.163.0；從 OBS 執行，HEAD 0c6d81a | macOS 26.5.2，2026-10-19T03:51:42Z | 不推廣其他 client／cwd | 後續重觀察須另留新 context。 |
| installed inventory | 原始 stdout／stderr／exit | exit 1、空 stdout、snapshot load error | 同上 | installed UNKNOWN；沒有成功 schema，非「零 installed」 | 保留失敗；不重試／註冊／安裝。 |
| declarative config | allowlisted user／project keys | user enabled=true，OBS trusted | 本次限定讀取 | 完整 precedence／effective load 未證實 | 維持 declarative 與 effective 分列。 |
| effective-enabled | inventory＋官方語意 | 無 runtime 結果 | 同上 | UNKNOWN，沒有可分類的 enabled 欄位 | 不由 true 宣告補推啟用。 |
| 安裝事件時間 | H 與 receipt 調查界線 | H 日期 2026-10-16；本次未取得 event receipt | H CLI／OS／確切時間未知 | UNKNOWN；mtime 不算安裝時間 | 不回填日期、不重裝。 |
| 固定 core reuse | CP／CT／CS | 六檔、input declarations、fresh recall 的歷史記錄 | CORE@655cbf3，記錄 CLI 0.163.0／2026-10-19 | 當前 bytes、其他 host、所有 adverse branch 未證實 | 引用固定來源與限制，不重跑。 |
| 工具輔助 | RUN aids／receipts | 見下節；獨立於上述證據 | 本次 local-only | 不能替代 Tester／Reviewer | 將實際檔案交 Tester。 |

方法判準：成功 inventory 若明確 installed 且 effective disabled，應分列 installed／DISABLED；缺 `enabled` 或語意、scope 不明時 effective 為 UNKNOWN；來源同一維度衝突時保留 CONFLICT 及各版本，不任選有利結果。本次未遇這些成功 schema 分支，僅查核方法，未注入假資料。

## 審閱輔助與限制

Archify 以繁體中文繪製「核准唯讀方法」與「本次失敗觀察」兩個 lane，無動畫；省略 `meta.locale`，固定 Viewer UI／HTML language 使用 English fallback。初稿布局診斷經三次 focused layout corrections 後，最終 validate／deliver exit 0、showcase **9 checks、0 errors、0 warnings**。錯誤數從 13 降至 1、1、0，未達連續兩輪不改善停點。沙箱 Chrome 首次 SIGABRT，保留失敗紀錄；相同 HTML 的授權本機 visual-check 重跑 exit 0，1440×900、1600×1000、1920×1080、2048×1320 均無 X/Y overflow。Implementer 實際檢視最小／最大 light／dark 四張截圖：方法／結果分明、節點／legend／限制卡片完整，沒有可見遮擋或裁切。自動 receipt 的 `visualReview: pending` 沒有被改寫為人工結果；人工觀察另記 aids index。未驗證互動、匯出或無障礙認證。

Graphify pinned 0.9.73 的 version command 使用 `GRAPHIFY_NO_AUTO_REFRESH=1`。只在 OBS／FEATURE 的已宣告 graph 路徑查找，未找到既有 graph；未做 graph query／build／refresh，改以固定 Git objects／targeted source reads。這不證明全主機沒有 graph。

PR Lens pinned 0.11.0 的 pre-commit working-tree map 嘗試以實際兩份新增文件及未變 plugin／catalog／公開摘要為基礎。兩份未追蹤檔透過真實 `git diff --no-index /dev/null <file>` 納入，完整 patch 與 digest 留私人 index；base／HEAD 均仍是 0d3ca3d，沒有偽造 head commit。第一次 validate exit 1：graph document 要求 `provenance`；核對 pinned schema 後確認必填 repo／base.sha／head.sha，沒有 working-tree snapshot 欄位。未以 base SHA 冒充新文件 bytes，因此此 candidate 保留為無效，render 未執行、沒有 rendered manifest 或 SVG；目前採 direct-diff fallback。這是此 pre-commit 表示方式的限制，不宣稱 PR Lens 普遍失效。獲授權且實際建立 topic commit 後，才可另以真實 head 製作 map。工具只作 change comprehension，不能判定證據正確性。沒有 hosted canvas、provider、upload、server 或工具安裝。

## TestCase

下表是 Implementer 的實際人工檢查，不是獨立 Tester／Reviewer gate；其後續結論仍待各本人執行。`OBSERVED` 表示真實觀察已記錄，`METHOD_ONLY` 表示只核對未遇分支判準。

| input | preconditions | steps | expected | actual | evidence | status |
| --- | --- | --- | --- | --- | --- | --- |
| CLI／cwd context | 指定 OBS，無 overrides | 核對 realpath、HEAD、版本、OS、UTC | context 與歷史來源分開 | OBS HEAD 0c6d81a；CLI 0.163.0／OS 26.5.2；FEATURE base0d | context.json | OBSERVED |
| inventory schema | 原命令一次、無 --available | 保留 stdout／stderr／exit，再嘗試分類 | 失敗或非 JSON 不當成功空結果 | exit1、stdout 0 bytes、snapshot error、PATH warning；無成功 schema | plugin-list.*、provenance-observations.json | OBSERVED |
| 設定與有效狀態 | 僅 allowlist 非秘密鍵 | 分列 true、trusted 與 runtime | 不足即 UNKNOWN | declarative true；installed／effective UNKNOWN | context、原始結果、官方文件 | OBSERVED |
| disabled／缺 enabled／衝突分支 | 僅成功 schema 有足夠 scope 時適用 | 查核分列規則，禁止注入假資料 | 不混用 installed／disabled，缺語意 UNKNOWN，衝突保留 | 本次未遇成功 schema；判準如上，未執行 branch | 方法判準 | METHOD_ONLY |
| 安裝歷史 receipt | H 為次級來源 | 分開文件日期／事件／查詢／mtime | 無 receipt 不填事件時間 | 事件時間 UNKNOWN，H CLI／OS／確切時間未知 | H、provenance index | OBSERVED |
| Core reuse | 固定 CORE Git objects | 讀 CP／CT／CS、核對 hash | 不混目前 worktree，不重跑 | 三份固定物件可讀；記錄原結果及限制；無新 live | source table、manifest | OBSERVED |
| 九欄／diff／去識別 | 只兩個 public outputs | 核對 owner、路徑、private index、原 plan hash | 既有修改／刪除為無，原 plan 不改 | 本報告新增；plan 由另一 owner 新增；exact paths 私人保留 | diff／manifest，交 Tester 再驗 | OBSERVED |
| Tools | 依 pinned/local-only 契約 | 讀 receipts、四張截圖及實際 diff | 各工具 used／fallback／failed 如實 | Archify 實際結果如上；Graphify source fallback；PR Lens pre-commit validate 失敗／render 未執行，direct-diff fallback | aids.json、tool receipts | OBSERVED（保留工具失敗） |

本題的交付目的是證據清晰。查詢失敗、未知或停用均可如實交付；後續是否變更 marketplace／安裝／設定，需另定範圍。本文件不宣稱獨立測試、review 或產品驗收已通過。
