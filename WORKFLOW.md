# 開發工作流程 (Development Workflow)

本文件定義了 `Network Switcher` 專案的標準開發工作流程，旨在確保程式碼品質、可追蹤性及團隊協作的一致性。

## 工作流程概覽

我們的開發流程遵循以下核心步驟：

1.  **規劃 (Planning)**
    *   **目標**：確定下一個開發任務。
    *   **工具**：`ROADMAP.md`
    *   **流程**：從路線圖中選取下一個未完成的任務作為本次開發的目標。

2.  **開發與測試 (Development & Testing)**
    *   **目標**：實現功能並確保其正確性。
    *   **工具**：`src/` (核心邏輯), `tests/` (測試案例), `pytest` (測試框架), `config.ini` (設定檔)
    *   **流程**：
        *   在 `src/` 目錄下對應的模組中撰寫或修改程式碼。
        *   在 `tests/` 目錄下為變更的功能撰寫或更新單元測試。
        *   遵循測試驅動開發 (TDD) 的精神，確保所有測試都能通過。

3.  **執行測試與產出報告 (Test Execution & Reporting)**
    *   **目標**：驗證所有功能是否正常運作並存檔記錄。
    *   **工具**：`pytest --html=...`, `get_report_filename.py`
    *   **流程**：
        *   執行 `pytest` 來運行所有測試。
        *   使用 `get_report_filename.py` 生成標準化的報告名稱。
        *   將 HTML 測試報告儲存於 `test_reports/` 目錄中。

4.  **文件更新 (Documentation)**
    *   **目標**：記錄本次開發的變更。
    *   **工具**：`CHANGELOG.md`, `ROADMAP.md`
    *   **流程**：
        *   在 `CHANGELOG.md` 中為新版本或變更添加條目。
        *   更新 `ROADMAP.md` 中對應任務的狀態為「已完成」。

5.  **提交 (Commit)**
    *   **目標**：將所有變更儲存到版本控制系統。
    *   **工具**：`git`
    *   **流程**：將所有修改過的程式碼、測試和文件提交到 Git 倉庫。

## 工作流程圖

```mermaid
graph TD
    A[1. 規劃<br>(ROADMAP.md)] --> B{2. 開發與測試};
    B --> C[核心邏輯<br>(src/)];
    B --> D[單元測試<br>(tests/)];
    C --> E{3. 執行測試};
    D --> E;
    E -- pytest --o F[4. 產出報告<br>(test_reports/)];
    F --> G[5. 更新文件<br>(CHANGELOG.md)];
    G --> H[6. 提交變更<br>(Git)];
    H --> A;

    subgraph "開發週期"
        B
        C
        D
        E
        F
        G
        H
    end

    subgraph "參考文件"
        I[設定檔<br>(config.ini)]
        J[專案標準<br>(PROJECT_STANDARDS.md)]
    end

    I -.-> C;
    J -.-> C;
    J -.-> D;
