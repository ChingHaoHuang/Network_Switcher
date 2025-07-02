import ctypes
import os

def is_admin():
    """檢查腳本是否以系統管理員權限運行。
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0