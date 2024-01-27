# Basic validation system in python using variables
# This can be modified to support API such as keyauth

import os
import time
import subprocess

verified = False
verify = 'LICENSED2024'

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
input(color("        - PRESS [ENTER] TO CONTINUE        ", Colors.BLACK))
time.sleep(2)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

code = input(color("ENTER YOUR LICENSE CODE...", Colors.RED))
if code == verify:
    print(color("LICENSE VERIFIED!", Colors.GREEN))
    verified = True

else:
    print(color("INVALID LICENSE CODE!", Colors.RED))

if verified is True:
    print(color("Proceeding!", Colors.GREEN))
    time.sleep(2)
    clear()
    subprocess.run(['python', 'NetPy.py'])

