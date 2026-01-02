# OWN NETWORK SECURITY MONITOR

## Description:
A Python console-based tool for ethically monitoring devices connected
to the user's own Wi-Fi network. Trusted devices are defined strictly
through manual user input.

## Features:
- Lists connected devices on the local network
- Displays IP address, MAC address, and hostname
- User-controlled trusted device list
- Flags unknown devices
- Logs scan history to CSV
- Read-only and non-intrusive

## Technologies:
- Python 3
- subprocess
- socket
- CSV handling

## How to Run:
1. Open terminal / PowerShell
2. Navigate to project directory
3. Run:
   python monitor.py

Ethical Use:
This tool is intended only for monitoring networks you own or are
authorized to manage. It does not extract passwords, spy, or interfere
with other devices.


