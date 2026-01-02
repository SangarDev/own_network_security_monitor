# OWN NETWORK SECURITY MONITOR

## Description:
A Python console-based tool for ethically monitoring devices connected
to the user's own Wi-Fi network. Trusted devices are defined strictly
through manual user input, and the tool performs read-only network scans
to identify unknown connections.

## Features:
- Lists connected devices on the local network
- Displays IP address, MAC address, and hostname
- User-controlled trusted device list
- Flags unknown devices on the network
- Logs scan history to a CSV file
- Read-only and non-intrusive operation

## Technologies:
- Python 3
- subprocess module
- socket module
- CSV file handling

## Project Structure:
- monitor.py              Main application script
- trusted_devices.txt     User-defined trusted devices
- device_log.csv          Scan log file (auto-generated)
- README.txt              Project documentation

## How to Run:
1. Open Terminal or PowerShell
2. Navigate to the project directory
3. Run the command:
   python monitor.py

## Ethical Use:
This tool is intended only for monitoring networks that you own or have
explicit permission to manage. It does not perform hacking, password
extraction, spying, or any form of unauthorized access.

