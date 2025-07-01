# 網路切換工具 (Network Switcher)

## 專案交接總覽 (Project Handover Overview)

#### **1. 專案目標**
本專案旨在開發一個名為 "Network Switcher" 的命令列工具，用於快速切換 Windows 作業系統的網路設定，例如網路路由、系統 Proxy 等。

#### **2. 技術棧**
*   **語言**: Python 3.x
*   **測試框架**: `pytest`
*   **相依性管理**: 使用 Python 內建的 `venv` 模組建立虛擬環境，並透過 `pip` 管理專案所需的套件。

#### **3. 專案架構圖**
```mermaid
graph TD
    subgraph "專案根目錄 (MyQQ)"
        A["main.py (主程式)"]
        B["config.ini (設定檔)"]
        C["tests/ (測試目錄)"]
        D["README.md (說明書)"]
        E["CHANGELOG.md (變更日誌)"]
        F["ROADMAP.md (開發路線圖)"]
        H["GEMINI.md (專案總結與注意事項)"]
        I[".venv/ (虛擬環境)"]
    end

    A -- "讀取設定" --> B
    C -- "測試" --> A

    style G fill:#f9f,stroke:#333,stroke-width:2px
```

#### **4. 開發流程：測試驅動開發 (TDD)**
本專案嚴格遵循「紅燈 -> 綠燈 -> 重構」的 TDD 循環，以確保程式碼的穩定與可靠性。

```mermaid
sequenceDiagram
    participant 開發者
    participant 程式碼
    participant 測試

    開發者->>測試: 1. 撰寫失敗的測試 (紅燈)
    Note right of 測試: `pytest` -> 顯示測試失敗
    測試-->>開發者: 回報失敗 (ImportError, AssertionError)

    開發者->>程式碼: 2. 撰寫最精簡的程式碼
    開發者->>測試: 執行測試
    Note right of 測試: `pytest` -> 顯示測試通過
    測試-->>開發者: 回報成功 (綠燈)

    開發者->>程式碼: 3. 重構程式碼
    Note left of 程式碼: 優化結構、提升可讀性
    開發者->>測試: 再次執行測試
    Note right of 測試: `pytest` -> 確認測試依然通過
    測試-->>開發者: 回報成功

    loop 開發下一個功能
        開發者->>測試: 重複 TDD 循環...
    end
```

---

## 快速上手

### 環境需求
- Python 3.x

### 安裝與設定

1.  **複製專案庫：**
    ```sh
    git clone <your-repo-url>
    cd MyQQ
    ```

2.  **建立並啟用虛擬環境：**
    本專案使用虛擬環境來管理相依套件。
    ```sh
    # 建立虛擬環境
    py -m venv .venv

    # 啟用虛擬環境
    .venv\Scripts\activate
    ```
    *啟用後，您的命令提示字元前端會出現 `(.venv)` 字樣。*

3.  **安裝相依套件：**
    在虛擬環境啟用後，安裝所有必要的套件。
    ```sh
    pip install pytest pytest-html
    ```

## 使用方法

在專案根目錄下，執行以下指令來啟動主程式：
```sh
python main.py
```
*請注意：您必須在具有「系統管理員」權限的終端機中執行此指令，工具才能正常運作。*

## 開發相關

### 執行測試

本專案使用 `pytest` 進行測試。在啟用虛擬環境後，於專案根目錄執行以下指令即可運行所有測試：
```sh
pytest
```

### 產生測試報告

若要產生詳細的 HTML 格式測試報告，請執行：
```sh
pytest --html=test_report.html
```
此指令會在專案根目錄下建立一個名為 `test_report.html` 的檔案。
