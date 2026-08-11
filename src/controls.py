from util.os import get_movement_fns, get_movement_inputs
from util.misc import sleep_with_speed
from util.print_fns import print_with_time

_fns = get_movement_fns()
_inputs = get_movement_inputs()
_keyDown = _fns["keyDown"]
_keyUp = _fns["keyUp"]
_press = _fns["press"]

def _key(name):
    return _inputs.get(name, name)

def move_direction(direction, duration=2):
    print_with_time(f"Moving {direction} for {duration} seconds...")
    key = _key(direction)
    _keyDown(key)
    sleep_with_speed(duration=duration)
    _keyUp(key)
    print_with_time(f"Finished moving {direction}.")

def press_button(button, duration=0.5, before_delay=0.5, after_delay=0.5):
    sleep_with_speed(before_delay)
    print_with_time(f"Pressing {button} for {duration} seconds...")
    key = _key(button)
    _keyDown(key)
    sleep_with_speed(duration=duration)
    _keyUp(key)
    print_with_time(f"Finished pressing {button}.")
    sleep_with_speed(after_delay)

def speed_up_game(indefinitely=False, duration=0.5):
    print_with_time("Speeding up the game...")
    _keyDown(_key('space'))
    if indefinitely:
        sleep_with_speed(duration=duration)
        _keyUp(_key('space'))
    print_with_time("Game speed increased.")

def quick_press(button):
    print_with_time(f"Pressing {button} quickly")
    _press(_key(button))

def press_n_times(button, times, press_fn=press_button):
    for _ in range(times):
        press_fn(button)