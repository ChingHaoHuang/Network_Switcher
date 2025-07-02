import pytest
import logging
import os

# Define a temporary log file path for testing
TEST_LOG_FILE = "app.log" # 這裡應該是 main.py 中實際使用的日誌檔案名稱

@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Fixture to ensure the log file is clean before and after each test."""
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)
    yield
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)

def test_logging_message_capture(caplog):
    """測試日誌訊息是否能被 caplog 正確捕獲。"""
    logger = logging.getLogger(__name__)
    caplog.set_level(logging.INFO)
    
    test_message = "This is a test log message."
    logger.info(test_message)

    assert test_message in caplog.text
    assert "INFO" in caplog.text
