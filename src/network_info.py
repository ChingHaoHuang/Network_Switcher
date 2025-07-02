import socket
import winreg

def get_ip_address():
    """獲取本機的 IP 位址。
    此方法通常對於尋找活躍的網路介面更可靠。
    """
    s = None
    try:
        # 建立一個 UDP socket (SOCK_DGRAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 連接到一個公共 DNS 伺服器 (不發送任何數據)
        # 這會強制作業系統選擇正確的介面
        s.connect(("8.8.8.8", 80))
        # 獲取 socket 自身的位址
        ip_address = s.getsockname()[0]
        return ip_address
    except Exception:
        # 如果連接失敗，則回退到 gethostname
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        except socket.gaierror:
            return "127.0.0.1" # 無法解析主機名，回傳迴路位址
    finally:
        if s:
            s.close()

def get_windows_proxy_settings():
    """從 Windows 註冊表獲取系統 Proxy 設定。

    回傳:
        dict: 包含 'ProxyEnable'、'ProxyServer' 和 'ProxyOverride' 的字典。
              如果找不到鍵或發生錯誤，則該值為 None。
    """
    proxy_settings = {
        "ProxyEnable": None,
        "ProxyServer": None,
        "ProxyOverride": None,
    }
    
    try:
        # 開啟 Internet Settings 註冊表鍵
        # KEY_READ 足以用於讀取
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                             0,
                             winreg.KEY_READ)
        
        # 讀取 ProxyEnable
        try:
            proxy_enable, _ = winreg.QueryValueEx(key, "ProxyEnable")
            proxy_settings["ProxyEnable"] = proxy_enable
        except FileNotFoundError:
            # 如果未明確啟用/禁用代理，則該鍵可能不存在
            pass
        
        # 讀取 ProxyServer
        try:
            proxy_server, _ = winreg.QueryValueEx(key, "ProxyServer")
            proxy_settings["ProxyServer"] = proxy_server
        except FileNotFoundError:
            # 如果未設定代理伺服器，則該鍵可能不存在
            pass

        # 讀取 ProxyOverride
        try:
            proxy_override, _ = winreg.QueryValueEx(key, "ProxyOverride")
            proxy_settings["ProxyOverride"] = proxy_override
        except FileNotFoundError:
            # 如果未設定代理例外，則該鍵可能不存在
            pass
            
        winreg.CloseKey(key)
        
    except Exception as e:
        print(f"錯誤：存取註冊表時發生錯誤: {e}")
        
    return proxy_settings