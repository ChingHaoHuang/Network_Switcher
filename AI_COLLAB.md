# AI 協作上下文 (AI Collaboration Context)

本文件為與大型語言模型 (LLM) 協作提供分層的上下文，旨在優化不同能力 LLM 的互動效率。

---

## 第一層：核心摘要 (Core Summary)

*   **專案目標**: 開發一個名為 "Network Switcher" 的 Windows 命令列工具，用於快速切換網路設定。
*   **技術棧**: Python 3.x, pytest
*   **關鍵文件索引**:
    *   [開發路線圖 (ROADMAP.md)](ROADMAP.md)
    *   [開發工作流程 (WORKFLOW.md)](WORKFLOW.md)
    *   [專案標準 (PROJECT_STANDARDS.md)](PROJECT_STANDARDS.md)
    *   [變更日誌 (CHANGELOG.md)](CHANGELOG.md)
*   **當前任務**: 請查閱 `ROADMAP.md` 的「未來規劃 (Backlog)」部分以確定下一個任務。

---

## 第二層：擴展上下文 (Expanded Context)

### 工作流程摘要
我們的開發流程遵循 `WORKFLOW.md` 中定義的五個步驟：1. 規劃 -> 2. 開發與測試 -> 3. 執行測試與報告 -> 4. 文件更新 -> 5. 提交。

### 核心標準
*   **命名約定**: 遵循 PEP 8。
*   **提交訊息**: 遵循 Conventional Commits 規範 (例如 `feat:`, `fix:`, `docs:`)。
*   **語言**: 所有程式碼註解、文件和提交訊息均使用「台灣繁體中文」。

### 最近變更
請查閱 `CHANGELOG.md` 的最新版本條目以了解最近的程式碼變更。

---

## 第三層：動態上下文獲取指南 (Dynamic Context Guide)

**這部分是給予 LLM 的指令，而非靜態資訊。**

*   **獲取即時任務**: 在開始新任務前，請務必**重新讀取 `ROADMAP.md`** 以確認最新的開發目標。
*   **了解特定功能**: 若要了解特定功能的實現細節，請**閱讀 `src/` 目錄下對應的模組**。
*   **除錯**: 當遇到錯誤時，請要求提供**完整的錯誤堆疊追蹤 (stack trace)** 和相關日誌。
*   **修改程式碼**: 在修改任何檔案之前，請務必**先使用 `read_file` 讀取其最新內容**，以避免版本衝突。
*   **執行指令**: 在提出需要執行指令時，請**明確說明指令的目的**並等待使用者確認。

---

## 開發注意事項與潛在陷阱 (Legacy Notes)

*本區塊保留了舊版 `GEMINI.md` 中的部分內容作為參考，新開發應優先遵循上述指南。*

### 1. 批次檔 (Batch Script) 的陷阱
*   `errorlevel` 的不穩定性：應立即將其值儲存到一個臨時變數中。
*   變數作用域與延遲擴展：需啟用 `setlocal enabledelayedexpansion` 並使用 `!variable!` 語法。

### 2. Python 開發環境管理
*   **虛擬環境的重要性**：務必使用 `venv` 或 `conda` 建立虛擬環境。
*   **`requirements.txt` 的維護**：新增或移除套件後，應及時更新 `requirements.txt`。

### 3. 測試驅動開發 (TDD) 實踐
*   **紅燈 -> 綠燈 -> 重構**：遵循 TDD 的核心循環。
*   **提交前驗證**：在提交前，務必執行 `pytest` 並更新所有相關文件。

### 4. Shell 指令的跨平台相容性
*   在執行檔案系統操作（如 `del` vs `rm`）時，需注意當前作業系統環境。
