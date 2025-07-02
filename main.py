from colorama import Fore, Style, init
from src.config_manager import load_config
from src.admin_checker import is_admin
from src.network_info import get_ip_address, get_windows_proxy_settings
from src.route_manager import add_route, delete_route
from src.proxy_manager import set_proxy
from src.hosts_manager import sync_hosts_file
from src.logger import setup_logging

def display_menu_and_get_choice():
    """顯示主選單並獲取使用者選擇。"""
    print(Style.BRIGHT + Fore.CYAN + "\n--- 網路切換工具 ---")
    print(Fore.YELLOW + "請選擇要執行的操作：")
    print(Fore.GREEN + "1. 新增網路路由")
    print(Fore.GREEN + "2. 刪除網路路由")
    print(Fore.GREEN + "3. 設定系統 Proxy")
    print(Fore.GREEN + "4. 同步 hosts 檔案")
    print(Fore.GREEN + "5. 顯示網路狀態")
    print(Fore.RED + "0. 結束程式")

    while True:
        choice = input(Fore.YELLOW + "請輸入選項 (0-5)：" + Style.RESET_ALL)
        if choice in [str(i) for i in range(6)]:
            return choice
        print(Fore.RED + "無效的選項，請重新輸入。")

def handle_add_route(config):
    """處理新增路由的操作。"""
    gateway = config.get('Routes', {}).get('gateway')
    target_hosts_str = config.get('Routes', {}).get('target_hosts', '')
    if not gateway or not target_hosts_str:
        print(Fore.RED + "錯誤：設定檔中缺少路由設定。")
        return
    target_hosts = [host.strip() for host in target_hosts_str.split(',') if host.strip()]
    for host in target_hosts:
        add_route(host, gateway)

def handle_delete_route(config):
    """處理刪除路由的操作。"""
    target_hosts_str = config.get('Routes', {}).get('target_hosts', '')
    if not target_hosts_str:
        print(Fore.RED + "錯誤：設定檔中缺少路由設定。")
        return
    target_hosts = [host.strip() for host in target_hosts_str.split(',') if host.strip()]
    for host in target_hosts:
        delete_route(host)

def handle_set_proxy(config):
    """處理設定 Proxy 的操作。"""
    proxy_server = config.get('Proxy', {}).get('server')
    if not proxy_server:
        print(Fore.RED + "錯誤：設定檔中缺少 Proxy 伺服器設定。")
        return
    set_proxy(proxy_server)

def handle_sync_hosts(config):
    """處理同步 hosts 檔案的操作。"""
    source_hosts_path = "network reference/hosts"
    system_hosts_path = config.get('HostsFile', {}).get('path')
    if not system_hosts_path:
        print(Fore.RED + "錯誤：設定檔中缺少 hosts 檔案路徑設定。")
        return
    sync_hosts_file(source_hosts_path, system_hosts_path)

def handle_show_status():
    """處理顯示網路狀態的操作。"""
    print(Fore.CYAN + "\n--- 網路狀態 ---")
    ip_address = get_ip_address()
    print(f"本機 IP 位址: {Fore.GREEN}{ip_address}{Style.RESET_ALL}")

    proxy_settings = get_windows_proxy_settings()
    if proxy_settings.get("ProxyEnable") == 1:
        print(Fore.YELLOW + "系統代理已啟用。")
        print(f"  代理伺服器: {Fore.GREEN}{proxy_settings.get('ProxyServer', 'N/A')}{Style.RESET_ALL}")
        print(f"  代理例外: {Fore.GREEN}{proxy_settings.get('ProxyOverride', 'N/A')}{Style.RESET_ALL}")
    elif proxy_settings.get("ProxyEnable") == 0:
        print(Fore.YELLOW + "系統代理已禁用。")
    else:
        print(Fore.YELLOW + "無法確定系統代理狀態或未找到明確的代理設定。")
    print(Fore.CYAN + "--- 網路狀態結束 ---\n")


def main():
    """主函數，運行工具。"""
    init(autoreset=True)
    setup_logging()

    if not is_admin():
        print(Fore.RED + "錯誤：請以系統管理員身分重新執行此指令碼。")
        return

    config = load_config()

    actions = {
        '1': lambda: handle_add_route(config),
        '2': lambda: handle_delete_route(config),
        '3': lambda: handle_set_proxy(config),
        '4': lambda: handle_sync_hosts(config),
        '5': handle_show_status,
    }

    while True:
        choice = display_menu_and_get_choice()
        if choice == '0':
            print(Fore.CYAN + "正在結束程式...")
            break
        
        action = actions.get(choice)
        if action:
            action()
        else:
            # This case should not be reached due to the validation in display_menu_and_get_choice
            print(Fore.RED + "無效的選項，請重新輸入。")

if __name__ == "__main__":
    main()
