import subprocess
import socket
import datetime
import csv
import os

TRUSTED_FILE = "trusted_devices.txt"
LOG_FILE = "device_log.csv"


def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"


def load_trusted_devices():
    if not os.path.exists(TRUSTED_FILE):
        return []
    with open(TRUSTED_FILE, "r", encoding="utf-8") as file:
        return [
            line.strip().lower()
            for line in file
            if line.strip() and not line.startswith("#")
        ]


def add_trusted_device(mac):
    mac = mac.lower().strip()
    trusted = load_trusted_devices()

    if mac in trusted:
        print("This device is already trusted.")
        return

    with open(TRUSTED_FILE, "a", encoding="utf-8") as file:
        file.write(mac + "\n")

    print("Trusted device added successfully.")


def log_device(entry):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "Timestamp", "IP Address", "MAC Address", "Hostname", "Status"
            ])
        writer.writerow(entry)


def scan_network():
    print("\nScanning local network...\n")

    trusted_devices = load_trusted_devices()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        output = subprocess.check_output(["arp", "-a"], text=True)
    except Exception as e:
        print("Error running arp command:", e)
        return

    print("-" * 90)
    print(f"{'IP ADDRESS':<18}{'MAC ADDRESS':<22}{'HOSTNAME':<30}STATUS")
    print("-" * 90)

    for line in output.splitlines():

        # Ignore headers and empty lines
        if not line.strip():
            continue
        if line.startswith("Interface:"):
            continue
        if "Internet Address" in line:
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        ip = parts[0]
        mac = parts[1].lower()

        if "-" not in mac:
            continue

        hostname = get_hostname(ip)
        status = "TRUSTED" if mac in trusted_devices else "UNKNOWN"

        print(f"{ip:<18}{mac:<22}{hostname:<30}{status}")

        log_device([timestamp, ip, mac, hostname, status])

    print("\nScan completed.")


def show_trusted_devices():
    trusted = load_trusted_devices()
    print("\nTrusted Devices:")

    if not trusted:
        print("No trusted devices found.")
        return

    for mac in trusted:
        print("-", mac)


def menu():
    print("\nOWN NETWORK SECURITY MONITOR")
    print("1. Scan network")
    print("2. Add trusted device (manual input)")
    print("3. View trusted devices")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            scan_network()
        elif choice == "2":
            mac = input("Enter MAC address to trust: ").strip()
            add_trusted_device(mac)
        elif choice == "3":
            show_trusted_devices()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
