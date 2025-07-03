# 如何為本專案貢獻 (How to Contribute)

首先，非常感謝您考慮為 `Network Switcher` 專案做出貢獻！您的每一份努力都對我們至關重要。

本文件旨在提供一份清晰的指南，幫助您順利地參與專案的開發。

## 行為準則 (Code of Conduct)

為了營造一個友善、互相尊重的協作環境，我們期望所有參與者都能遵守社群的行為準則。在您開始貢獻之前，請花時間閱讀我們的 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) (待建立)。

## 如何回報問題或建議功能

我們使用 **GitHub Issues** 來追蹤所有的錯誤回報 (Bugs) 和功能請求 (Feature Requests)。

在建立 Issue 之前，請先搜尋現有的 Issues，確保您的問題或建議尚未被提出。

### 回報錯誤 (Reporting Bugs)

如果您發現了程式中的錯誤，請建立一個 Issue 並盡可能提供以下資訊：

*   **清晰的標題**: 簡要描述問題。
*   **重現步驟**: 詳細說明如何觸發這個錯誤。
*   **預期行為**: 描述在正常情況下應該發生什麼。
*   **實際行為**: 描述實際發生了什麼，並附上**完整的錯誤訊息或堆疊追蹤 (stack trace)**。
*   **您的環境**: 您的作業系統、Python 版本等。

### 建議新功能 (Suggesting Enhancements)

如果您有關於新功能或改進的建議，也歡迎建立一個 Issue。請在內容中詳細說明：

*   **問題描述**: 這個功能主要解決了什麼問題？
*   **解決方案建議**: 您認為應該如何實現這個功能？
*   **替代方案** (可選): 您是否考慮過其他實現方式？

## 您的第一個程式碼貢獻

準備好開始貢獻程式碼了嗎？太棒了！

### 開發流程

我們的開發流程、程式碼風格、測試標準和版本控制規範，都詳細記錄在以下文件中。在開始撰寫程式碼前，請務必閱讀它們：

1.  **[開發工作流程 (WORKFLOW.md)](WORKFLOW.md)**: 了解從規劃到提交的完整開發週期。
2.  **[專案標準 (PROJECT_STANDARDS.md)](PROJECT_STANDARDS.md)**: 遵循我們的程式碼風格、文件和測試規範。

### 提交 Pull Request (PR) 的步驟

1.  **Fork 本倉庫**: 將本專案 Fork 到您自己的 GitHub 帳號下。
2.  **Clone 您的 Fork**: `git clone https://github.com/YOUR_USERNAME/Network_Switcher.git`
3.  **建立新分支**: `git checkout -b feature/your-feature-name` 或 `fix/your-bug-fix-name`
4.  **進行修改**: 撰寫您的程式碼和測試。
5.  **執行測試**: 確保所有測試都能通過 (`pytest`)。
6.  **提交變更**: `git commit -m "feat: 新增了不起的功能"` (請遵循 Conventional Commits 規範)。
7.  **Push 到您的 Fork**: `git push origin feature/your-feature-name`
8.  **建立 Pull Request**: 在 GitHub 上，從您的分支向本專案的 `master` 分支發起一個 Pull Request。

請在 PR 的描述中清晰地說明您的變更內容。我們會盡快審核您的貢獻！

再次感謝您的參與！
