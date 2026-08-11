from platform import system
from pynput.keyboard import Key, Controller

os = system()

def get_movement_fns():
    if os == "Windows":
        keyboard = Controller()
        return {
            "keyDown": lambda key: keyboard.press(key),
            "keyUp": lambda key: keyboard.release(key),
            "press": lambda key: (keyboard.press(key), keyboard.release(key))
        }
    else:
        from pyautogui import press, keyDown, keyUp
        return {
            "keyDown": lambda key: keyDown(key),
            "keyUp": lambda key: keyUp(key),
            "press": lambda key: press(key)
        }

def get_movement_inputs():
    if os == "Windows":
        return {
            "left": Key.left,
            "right": Key.right,
            "up": Key.up,
            "down": Key.down,
            "space": Key.space,
            "x": 'x',
            "z": 'z'
        }
    else:
        return {
            "left": 'left',
            "right": 'right',
            "up": 'up',
            "down": 'down',
            "space": 'space',
            "x": 'x',
            "z": 'z'
        }

def get_template_path():
    return "images\\templates\\windows" if os == "Windows" else "images/templates/"

def get_path_from_os(path):
    return path.replace("/", "\\") if os == "Windows" else path

def get_pokemon_name_from_template(name_template_path):
    print(f"Name template path: {name_template_path}")
    delimiter = "\\" if os == "Windows" else "/"
    index = 3 if os == "Windows" else 2
    return name_template_path.split(delimiter)[index].capitalize()

def get_pokemon_screenshot_dir():
    screenshot_dir = "images\\pokemon\\windows" if os == "Windows" else "images/pokemon"
    return screenshot_dir
