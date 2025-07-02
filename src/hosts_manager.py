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