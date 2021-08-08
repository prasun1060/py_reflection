# PyReflection 1.0

from flask import Flask, json, jsonify, request
import win32com.client as wc
from pywinauto.application import Application as pw
import os


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

def connect_refection(view_idx:int=1) -> object:
    try:
        wgs = wc.GetObject('Reflection Workspace')
        wgs_screen = wgs.GetObject('Frame').view(view_idx).Control.Screen
    except:
        print('Unexpected error occured!, Please check if reflection desktop is open.')
    else:
        return wgs_screen

@app.route('/connect')
def connect():
    import time
    while True:
        try:
            print('Connecting to Reflection Workspace Desktop')
            app = pw(backend='win32').connect(title_re='.*Reflection*', found_index=0)
            dlg = app.window()[0]
            dlg.set_focus()
        except:
            print('Unable to connect to Reflection Workspace Desktop. retrying...')
            time.sleep(0.1)
        else:
            return jsonify({
                'response': 'Reflection Workspace successfully connected.',
                'error': False
            })

@app.route('/send_keys', methods=['GET', 'POST'])
def send_keys():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    text = request.args.get('text')
    if text is None:
        return jsonify({
            'response': 'Unexpected error occured; Text input cannot be None.',
            'error': True
        })
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return jsonify({
            'response': 'Unexpected error occured; Values of x and y should be numeric.',
            'error': True
        })
    else:
        try:
            reflection_obj.PutText2(text, x, y)
        except:
            print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
            return jsonify({
                'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
                'error': True
            })
        else:
            return jsonify({
                'response': 'Success',
                'error': False
            })

@app.route('/press_enter', methods=['GET', 'POST'])
def press_enter():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    try:
        reflection_obj.SendControlKey(1)
    except:
        print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
        return jsonify({
            'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
            'error': True
        })
    else:
        return jsonify({
            'response': 'Enter pressed successfully',
            'error': False
        })

@app.route('/press_key', methods=['GET', 'POST'])
def press_key():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    control_key = request.args.get('control_key')
    try:
        reflection_obj.SendControlKey(CONTROL_KEYS[control_key])
    except:
        print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
        return jsonify({
            'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
            'error': True
        })
    else:
        return jsonify({
            'response': 'Key pressed successfully',
            'error': False
        })

@app.route('/press_control_keys', methods=['GET', 'POST'])
def press_control_keys():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    control_key = int(request.args.get('control_key'))
    try:
        reflection_obj.SendControlKey(control_key)
    except:
        print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
        return jsonify({
            'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
            'error': True
        })
    else:
        return jsonify({
            'response': 'Key pressed successfully',
            'error': False
        })

@app.route('/get_text', methods=['GET', 'POST'])
def get_text():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        length = int(request.args.get('length'))
    except:
        return jsonify({
            'response': 'Unexpected error occured; Values of x and y should be numeric.',
            'error': True
        })
    else:
        try:
            output = reflection_obj.GetText(x, y, length)
        except:
            print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
            return jsonify({
                'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
                'error': True
            })
        else:
            return jsonify({
                'response': output,
                'error': False
            })

@app.route('/get_text_coordinates', methods=['GET', 'POST'])
def get_text_coordinates():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    text = request.args.get('text')
    total_row_count = int(request.args.get('total_row_count'))
    total_column_count = int(request.args.get('total_column_count'))
    if total_row_count is None or total_column_count is None:
        total_row_count = 24
        total_column_count = 80
    for row_no in range(1, total_row_count + 1):
        line = reflection_obj.GetText(row_no, 1, total_column_count)
        if line.find(text) != -1:
            return jsonify({
                'error': False,
                'response': {'x': row_no, 'y': line.find(text)+1}
            })
    return jsonify({
        'error': False,
        'response': {'x': 0, 'y': 0}
    })

@app.route('/check_text_present', methods=['GET', 'POST'])
def check_text_present():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    text = request.args.get('text')
    total_row_count = int(request.args.get('total_row_count'))
    total_column_count = int(request.args.get('total_column_count'))
    if total_row_count is None or total_column_count is None:
        total_row_count = 24
        total_column_count = 80
    for row_no in range(1, total_row_count + 1):
        line = reflection_obj.GetText(row_no, 1, total_column_count)
        if line.find(text) != -1:
            return jsonify({
                'error': False,
                'response': True
            })
    return jsonify({
        'error': False,
        'response': False
    })

@app.route('/move_cursor', methods=['GET', 'POST'])
def move_cursor():
    view_idx = request.args.get('view_idx')
    if view_idx is None:
        view_idx = 1
    else:
        view_idx = int(view_idx)
    reflection_obj = connect_refection(view_idx=view_idx)
    if reflection_obj is None:
        return jsonify({
            'response': 'Unexpected error occured; Please check if refection desktop is open.',
            'error': True
        })
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return jsonify({
            'response': 'Unexpected error occured; Values of x and y should be numeric.',
            'error': True
        })
    else:
        try:
            output = reflection_obj.MoveCursorTo1(x, y)
        except:
            print('Unexpected error occured!, Please reconnect to the reflection tool and try again.')
            return jsonify({
                'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
                'error': True
            })
        else:
            return jsonify({
                'response': 'Cursor moved successfully.',
                'error': False
            })

@app.route('/get_view_count', methods=['GET', 'POST'])
def get_view_count():
    try:
        wgs = wc.GetObject('Reflection Workspace')
        output = wgs.GetObject('Frame').viewCount
    except:
        print('Unexpected error occured!, Please check if reflection desktop is open.')
        return jsonify({
            'response': 'Unexpected error occured; Please reconnect to the reflection tool and try again.',
            'error': True
        })
    else:
        return jsonify({
            'response': output,
            'error': False
        })

if __name__ == '__main__':

    if os.path.exists('LICENSE.txt'):
        with open('LICENSE.txt') as f:
            license_txt = f.read()
        if license_txt.find('Copyright (c) 2021 Prasun Bhattacharyya') != -1:
            app.run(port=4200, debug=False)
        else:
            print('LICENSE.txt file missing! Please get the original License Key.')
    else:
        print('LICENSE.txt file missing! Please get the original License Key.')