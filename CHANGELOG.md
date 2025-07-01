# 變更日誌

本專案的所有顯著變更都將記錄在此檔案中。

本檔案的格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
且本專案遵循[語意化版本](https://semver.org/lang/zh-TW/) (Semantic Versioning)。

## [0.3.0] - 2025-07-01

### 新增 (Added)
- 實作了設定系統 Proxy 的功能。
- 新增 `network reference/` 資料夾，包含舊版手動切換網路設定的參考檔案。

## [02.0] - 2025-07-01

### 新增 (Added)
- 實作了程式啟動時的系統管理員權限檢查。

### 變更 (Changed)
- **重大重構**: 將整個專案從批次檔 (Batch Script) 遷移至 Python。
- 採用了使用 `pytest` 框架的測試驅動開發 (TDD) 流程。
- 使用結構更清晰的 `config.ini` 檔案取代了原有的 `config.bat`。

## [0.1.0] - 2025-06-30

### 新增 (Added)
- 使用批次檔架構進行專案初始化。
