from pyautogui import press, keyDown, keyUp

from util.misc import sleep_with_speed
from util.print_fns import print_with_time

def move_direction(direction, duration=2):
    print_with_time(f"Moving {direction} for {duration} seconds...")
    if direction == 'left':
        keyDown('left')
        sleep_with_speed(duration=duration)
        keyUp('left')
    elif direction == 'right':
        keyDown('right')
        sleep_with_speed(duration=duration)
        keyUp('right')
    elif direction == 'up':
        keyDown('up')
        sleep_with_speed(duration=duration)
        keyUp('up')
    elif direction == 'down':
        keyDown('down')
        sleep_with_speed(duration=duration)
        keyUp('down')
    print_with_time(f"Finished moving {direction}.")

def press_button(button, duration=0.5, before_delay=0.5, after_delay=0.5):
    sleep_with_speed(before_delay)
    print_with_time(f"Pressing {button} for {duration} seconds...")
    keyDown(button)
    sleep_with_speed(duration=duration)
    keyUp(button)
    print_with_time(f"Finished pressing {button}.")
    sleep_with_speed(after_delay)

def speed_up_game(indefinitely=False, duration=0.5):
    print_with_time("Speeding up the game...")
    keyDown('space')
    if indefinitely:
       sleep_with_speed(duration=duration)
       keyUp('space')
    print_with_time("Game speed increased.")

def quick_press(button):
    print_with_time(f"Pressing {button} quickly")
    press(button)

def press_n_times(button, times, press_fn=press_button):
    for _ in range(times):
        press_fn(button)