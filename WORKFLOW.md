# 開發工作流程 (Development Workflow)

本文件定義了 `Network Switcher` 專案的標準開發工作流程，旨在確保程式碼品質、可追蹤性及團隊協作的一致性。

## 首次開發環境設定 (First-Time Setup)

在開始開發之前，請遵循以下步驟設定您的開發環境。

1.  **安裝 uv**:
    *   我們強烈建議使用 `uv` 來管理 Python 虛擬環境和依賴。請參考 [uv 官方文件](https://github.com/astral-sh/uv) 進行安裝。
    *   通常，您可以使用 `pip` 或 `pipx` 來安裝：
        ```bash
        # 使用 pip
        python -m pip install uv
        # 或使用 pipx (推薦)
        pipx install uv
        ```

2.  **建立虛擬環境**:
    *   在專案的根目錄下，執行以下指令來建立一個名為 `.venv` 的虛擬環境：
        ```bash
        python -m uv venv
        ```

3.  **安裝依賴**:
    *   建立環境後，使用以下指令將 `requirements.txt` 中定義的所有依賴安裝到您的虛擬環境中：
        ```bash
        python -m uv pip sync requirements.txt
        ```

4.  **執行指令 (兩種方式)**:

    *   **方式一：啟動虛擬環境 (傳統方式)**
        *   在終端機中執行多個指令前，可以先啟動虛擬環境：
        *   **Windows (PowerShell)**:
            ```powershell
            . .\.venv\Scripts\Activate.ps1
            ```
        *   **Windows (CMD)**:
            ```cmd
            .venv\Scripts\activate.bat
            ```
        *   **Linux / macOS**:
            ```bash
            source .venv/bin/activate
            ```
        *   啟動後，您的終端機提示字元前應該會出現 `(.venv)` 字樣。

    *   **方式二：使用 `uv run` (推薦)**
        *   `uv` 提供了一個更便捷的方式來執行指令，無需手動啟動/停用環境。
        *   您可以在任何指令前加上 `python -m uv run`，`uv` 會自動在 `.venv` 環境中執行它。
        *   例如：
            ```bash
            python -m uv run pytest --version
            ```
        *   **在後續的工作流程中，我們將優先使用此方式。**

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

    *   **依賴管理 (Dependency Management)**
        *   **目標**: 維護專案依賴的一致性與可追蹤性。
        *   **工具**: `uv`, `requirements.in`, `requirements.txt`
        *   **流程**:
            *   若要新增或移除專案的**直接依賴**，請修改 `requirements.in` 檔案。
            *   修改後，執行 `python -m uv pip compile requirements.in --output-file requirements.txt` 來重新生成 `requirements.txt`。
            *   `requirements.txt` 檔案**不應手動修改**，它是由 `uv` 自動生成的。

3.  **執行測試與產出報告 (Test Execution & Reporting)**
    *   **目標**：驗證所有功能是否正常運作並存檔記錄。
    *   **工具**：`uv`, `pytest`, `get_report_filename.py`
    *   **流程**：
        *   使用 `uv run` 來執行所有測試：
            ```bash
            python -m uv run pytest
            ```
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
