import subprocess

def set_proxy(proxy_server):
    """配置系統範圍的代理設定。
    成功時回傳 True，失敗時回傳 False。
    """
    try:
        command = ["netsh", "winhttp", "set", "proxy", proxy_server]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"成功設定代理為: {proxy_server}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"設定代理錯誤: {e}")
        print(f"標準輸出: {e.stdout}\n標準錯誤: {e.stderr}")
        return False
    except Exception as e:
        print(f"發生意外錯誤: {e}")
        return False