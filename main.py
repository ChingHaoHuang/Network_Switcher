import ctypes
import os
import configparser
import subprocess
import socket
import winreg
from colorama import Fore, Style, init

def load_config(file_path="config.ini"):
    """讀取設定檔並回傳一個字典。
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}

def is_admin():
    """檢查腳本是否以系統管理員權限運行。
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

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
        print(f"標準輸出: {e.stdout}")
        print(f"標準錯誤: {e.stderr}")
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
        print(f"標準輸出: {e.stdout}")
        print(f"標準錯誤: {e.stderr}")
        return False
    except Exception as e:
        print(f"發生意外錯誤: {e}")
        return False

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
        print(f"標準輸出: {e.stdout}")
        print(f"標準錯誤: {e.stderr}")
        return False
    except Exception as e:
        print(f"發生意外錯誤: {e}")
        return False

def sync_hosts_file(source_path, dest_path):
    """將來源 hosts 檔案的內容複製到目標位置。
    成功時回傳 True，失敗時回傳 False。
    """
    try:
        with open(source_path, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(dest_path, 'w', encoding='utf-8') as dest:
            dest.write(content)
        print(f"成功同步 hosts 檔案從 {source_path} 到 {dest_path}")
        return True
    except Exception as e:
        print(f"同步 hosts 檔案錯誤: {e}")
        return False

def main():
    """主函數，運行工具。"""
    init(autoreset=True) # Initialize Colorama

    if not is_admin():
        print(Fore.RED + "錯誤：請以系統管理員身分重新執行此指令碼。")
        return

    config = load_config()
    
    while True:
        print(Style.BRIGHT + Fore.CYAN + "\n歡迎，系統管理員！")
        print(Fore.YELLOW + "請選擇要執行的操作：")
        print(Fore.GREEN + "1. 新增網路路由")
        print(Fore.GREEN + "2. 刪除網路路由")
        print(Fore.GREEN + "3. 設定系統 Proxy")
        print(Fore.GREEN + "4. 同步 hosts 檔案")
        print(Fore.GREEN + "5. 顯示網路狀態")
        print(Fore.RED + "0. 結束程式")

        choice = input(Fore.YELLOW + "請輸入選項：" + Style.RESET_ALL)

        if choice == '1':
            gateway = config.get('Routes', {}).get('gateway')
            target_hosts = config.get('Routes', {}).get('target_hosts', '').split(',')
            if not gateway or not target_hosts:
                print(Fore.RED + "錯誤：設定檔中缺少路由設定。")
                continue
            for host in target_hosts:
                add_route(host.strip(), gateway)
        elif choice == '2':
            target_hosts = config.get('Routes', {}).get('target_hosts', '').split(',')
            if not target_hosts:
                print(Fore.RED + "錯誤：設定檔中缺少路由設定。")
                continue
            for host in target_hosts:
                delete_route(host.strip())
        elif choice == '3':
            proxy_server = config.get('Proxy', {}).get('server')
            if not proxy_server:
                print(Fore.RED + "錯誤：設定檔中缺少 Proxy 伺服器設定。")
                continue
            set_proxy(proxy_server)
        elif choice == '4':
            source_hosts_path = "network reference/hosts" 
            system_hosts_path = config.get('HostsFile', {}).get('path')
            if not system_hosts_path:
                print(Fore.RED + "錯誤：設定檔中缺少 hosts 檔案路徑設定。")
                continue
            sync_hosts_file(source_hosts_path, system_hosts_path)
        elif choice == '5':
            print(Fore.CYAN + "\n--- 網路狀態 ---")
            ip_address = get_ip_address()
            print(f"本機 IP 位址: {Fore.GREEN}{ip_address}{Style.RESET_ALL}")

            proxy_settings = get_windows_proxy_settings()
            if proxy_settings["ProxyEnable"] == 1:
                print(Fore.YELLOW + "系統代理已啟用。")
                print(f"  代理伺服器: {Fore.GREEN}{proxy_settings['ProxyServer']}{Style.RESET_ALL}")
                print(f"  代理例外: {Fore.GREEN}{proxy_settings['ProxyOverride']}{Style.RESET_ALL}")
            elif proxy_settings["ProxyEnable"] == 0:
                print(Fore.YELLOW + "系統代理已禁用。")
            else:
                print(Fore.YELLOW + "無法確定系統代理狀態或未找到明確的代理設定。")
                
            print(Fore.CYAN + "--- 網路狀態結束 ---\n")

        elif choice == '0':
            print(Fore.CYAN + "正在結束程式...")
            break
        else:
            print(Fore.RED + "無效的選項，請重新輸入。")

if __name__ == "__main__":
    main()
