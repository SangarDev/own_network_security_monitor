# OWN NETWORK SECURITY MONITOR

## Description:
A Python console-based application for ethically monitoring devices
connected to the user's own Wi-Fi network. The tool performs read-only
network scans and identifies trusted and unknown devices based strictly
on user-defined input.

## Features:
- Scans the local network using ARP
- Displays IP address, MAC address, and hostname
- User-controlled trusted device list
- Identifies unknown devices on the network
- Logs scan history to a CSV file
- Read-only, non-intrusive, and ethical operation

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
1. Open Command Prompt or PowerShell
2. Navigate to the project directory
3. Run the command:
   python monitor.py

## Ethical Use:
This project is intended only for monitoring networks that you own or
have explicit permission to manage. It does not perform hacking,
password extraction, spying, or unauthorized access of any kind.

## Author:
Sangar Khan

