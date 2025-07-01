import ctypes
import os
import configparser

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

def main():
    """Main function to run the tool."""
    if not is_admin():
        print("Error: Please re-run this script as an Administrator.")
        return

    print("Welcome, Administrator!")
    # More logic will be added here following TDD.

if __name__ == "__main__":
    main()
