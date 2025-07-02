import subprocess

def add_route(target_host, gateway):
    """向系統路由表添加新的網路路由。
    成功時回傳 True，失敗時回傳 False。
    """
    try:
        command = ["route", "ADD", target_host, "MASK", "255.255.255.255", gateway]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"成功添加路由: {target_host} 透過 {gateway}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"添加路由錯誤: {e}")
        print(f"標準輸出: {e.stdout}\n標準錯誤: {e.stderr}")
        return False
    except Exception as e:
        print(f"發生意外錯誤: {e}")
        return False

def delete_route(target_host):
    """從系統路由表刪除網路路由。
    成功時回傳 True，失敗時回傳 False。
    """
    try:
        command = ["route", "DELETE", target_host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"成功刪除路由: {target_host}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"刪除路由錯誤: {e}")
        print(f"標準輸出: {e.stdout}\n標準錯誤: {e.stderr}")
        return False
    except Exception as e:
        print(f"發生意外錯誤: {e}")
        return False
