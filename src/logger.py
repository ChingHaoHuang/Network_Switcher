import logging
from src.config_manager import load_config

def setup_logging():
    """根據 config.ini 中的設定初始化日誌系統。"""
    config = load_config()
    log_level_str = config.get('Settings', {}).get('log_level', 'INFO').upper()
    log_level = getattr(logging, log_level_str, logging.INFO)

    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("app.log")])