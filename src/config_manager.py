import configparser

def load_config(file_path="config.ini"):
    """讀取設定檔並回傳一個字典。
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}