# NetPy v1 Currently only supports Port Scanning functionality.
# Other features will be explored in later updates

import os
import time
import subprocess
from portscan import PortScan

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def color(text, color_code):
    return color_code + text + Colors.RESET

print(color("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■", Colors.RED))
print(color("███    ██ ███████ ████████ ██████  ██    ██ ", Colors.WHITE))
print(color("████   ██ ██         ██    ██   ██  ██  ██  ", Colors.WHITE))
print(color("██ ██  ██ █████      ██    ██████    ████   ", Colors.WHITE))
print(color("██  ██ ██ ██         ██    ██         ██    ", Colors.WHITE))
print(color("██   ████ ███████    ██    ██         ██    ", Colors.WHITE))
print(color("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■", Colors.RED))
print(color("        +  CREATED BY @WiiZARDD            ", Colors.WHITE))
input(color("        - PRESS [ENTER] TO CONTINUE        ", Colors.BLACK))
time.sleep(2)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(color("1: PORT SCANNER    2: SOON               ", Colors.RED))
print(color("3: SOON            4: SOON               ", Colors.RED))
option = input("ENTER YOUR OPTION:")

if option == "1":
    ip = input("Enter IP: ")
    port = input("Enter Port: ")
    threads = int(input("How many threads?"))
    scanner = PortScan(ip, port, thread_num=threads, show_refused=False, wait_time=1, stop_after_count=True)
    print("SCANNING PORTS - THIS MIGHT TAKE A MINUTE")
    open_port_discovered = scanner.run()
    adb_port = int(open_port_discovered[0][1])
else:
    print("No Open Ports Discovered!")

menu = input("Press anything to return to menu")
clear()
print(color("1: PORT SCANNER    2: SOON               ", Colors.RED))
print(color("3: SOON            4: SOON               ", Colors.RED))
option = input("ENTER YOUR OPTION:")
