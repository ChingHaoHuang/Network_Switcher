import ctypes
import os
import configparser
import subprocess

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

def main():
    """Main function to run the tool."""
    if not is_admin():
        print("Error: Please re-run this script as an Administrator.")
        return

    print("Welcome, Administrator!")
    # More logic will be added here following TDD.

if __name__ == "__main__":
    main()
