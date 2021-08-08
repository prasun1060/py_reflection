# py_reflection

```

██████╗░██╗░░░██╗██████╗░███████╗███████╗██╗░░░░░███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░██████╔╝█████╗░░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░██║░░██║███████╗██║░░░░░███████╗███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
```

Developed by - Prasun Bhattacharyya
Email - bhattacharyyaprasun47@gmail.com

 Rest API endpoint to automate Microfocus Reflection Desktop Workspace
 
 **All requests in this library should be GET only.
 
 How to start:
 
 1. Install the package via pip:
    ```
    py -m pip install py_reflection
    ```
    
 2. Run the package (Run the commands below in terminal):
    ```
    set FLASK_APP=py_reflection
    set FLASK_ENV=development
    pip install -e .
    flask run
    ```
 
 Api Endpoint and their description:
 ** All of the endpoints have a common parameter view_idx(integer, optional). Use this parameter to toggle between session in emulator.
 
 1. /send_keys: Use this endpoint to press keys in the emulator.
                   Parameters to pass: text(string), x(integer), y(integer)
 
 2. /get_text: Use this endpoint to get text from a specific coordinate.
                   Parameters to pass: x(integer), y(integer)
 
 3. /press_key: Use this endpoint to press special control keys:
                   Parameters to pass: control_key(string all in caps).
                   Available control keys:
                    'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','TAB','DELETE','LEFT','DOWN','UP','RIGHT','PAGEUP','PAGEDOWN','CLEAR','END','ENTER'
 
 4. /get_text_coordinates: Use this endpoint to get coordinates of text present in emulator screen.
                            Parameters to pass: text(string), total_row_count(integer, optional), total_column_count(integer, optional)
 
 5. /check_text_present: Use this endpoint to check if given text present in emulator screen.
                            Parameters to pass: text(string), total_row_count(integer, optional), total_column_count(integer, optional)
 
 6. /move_cursor: Use this endpoint to move cursor to specified coordinate.
                        Parameters to pass: x(integer), y(integer)
                        
 7. /get_view_count: Use this endpoint to get number of sessions opened in emulator.

Link to GitHub: https://github.com/prasun1060/py_reflection