import ctypes
import os
import configparser
import subprocess
from colorama import Fore, Style, init

def load_config(file_path="config.ini"):
    """Reads the configuration file and returns a dictionary."""
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def add_route(target_host, gateway):
    """Adds a new network route to the system's routing table.
    Returns True on success, False on failure.
    """
    try:
        command = ["route", "ADD", target_host, "MASK", "255.255.255.255", gateway]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully added route: {target_host} via {gateway}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error adding route: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def delete_route(target_host):
    """Deletes a network route from the system's routing table.
    Returns True on success, False on failure.
    """
    try:
        command = ["route", "DELETE", target_host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully deleted route: {target_host}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error deleting route: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def set_proxy(proxy_server):
    """Configures the system-wide proxy settings.
    Returns True on success, False on failure.
    """
    try:
        command = ["netsh", "winhttp", "set", "proxy", proxy_server]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully set proxy to: {proxy_server}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error setting proxy: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def sync_hosts_file(source_path, dest_path):
    """Copies the content of the source hosts file to the destination.
    Returns True on success, False on failure.
    """
    try:
        with open(source_path, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(dest_path, 'w', encoding='utf-8') as dest:
            dest.write(content)
        print(f"Successfully synced hosts file from {source_path} to {dest_path}")
        return True
    except Exception as e:
        print(f"Error syncing hosts file: {e}")
        return False

def main():
    """Main function to run the tool."""
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
        elif choice == '0':
            print(Fore.CYAN + "正在結束程式...")
            break
        else:
            print(Fore.RED + "無效的選項，請重新輸入。")

if __name__ == "__main__":
    main()
