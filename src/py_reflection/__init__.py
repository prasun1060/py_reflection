# PyReflection 1.0

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
}

import py_reflection.views



