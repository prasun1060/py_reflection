# PyReflection 1.0
# Author - Prasun Bhattacharyya

print("""

██████╗░██╗░░░██╗██████╗░███████╗███████╗██╗░░░░░███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░██████╔╝█████╗░░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░██║░░██║███████╗██║░░░░░███████╗███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

Developed by - Prasun Bhattacharyya
Email - bhattacharyyaprasun47@gmail.com
""")

from flask import Flask


app = Flask(__name__)

CONTROL_KEYS = {
    'F1': 10,
    'F2': 11,
    'F3': 12,
    'F4': 13,
    'F5': 14,
    'F6': 15,
    'F7': 16,
    'F8': 17,
    'F9': 18,
    'F10': 19,
    'F11': 20,
    'F12': 21,
    'F13': 22,
    'F14': 23,
    'F15': 24,
    'F16': 25,
    'F17': 26,
    'F18': 27,
    'F19': 28,
    'TAB': 3,
    'DELETE': 41,
    'LEFT': 8,
    'DOWN': 5,
    'UP': 6,
    'RIGHT': 7,
    'PAGEUP': 34,
    'PAGEDOWN': 35,
    'CLEAR': 38,
    'END': 2,
    'ENTER': 1,
}

import py_reflection.views



