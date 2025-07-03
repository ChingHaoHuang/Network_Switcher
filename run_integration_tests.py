
import sys
import pytest
from src.admin_checker import is_admin

def run_integration_tests():
    """
    Runs integration tests that require administrator privileges.
    """
    if not is_admin():
        print("錯誤：整合測試需要系統管理員權限。")
        print("請以系統管理員身分執行此腳本。")
        sys.exit(1)

    print("以系統管理員權限執行整合測試...")
    # -m integration: 只執行標記為 'integration' 的測試
    # -v: 詳細輸出
    result = pytest.main(['-v', '-m', 'integration'])

    if result == 0:
        print("整合測試成功通過。")
    else:
        print("整合測試失敗。")
        sys.exit(1)

if __name__ == "__main__":
    run_integration_tests()
