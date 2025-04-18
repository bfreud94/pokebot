from pyautogui import press, keyDown, keyUp
from util.misc import sleep_with_speed

def move_direction(direction, duration=2):
    print(f"Moving {direction} for {duration} seconds...")
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
    print(f"Finished moving {direction}.")

def press_button(button, duration=0.5, before_delay=0.5, after_delay=0.5):
    sleep_with_speed(before_delay)
    print(f"Pressing {button} for {duration} seconds...")
    keyDown(button)
    sleep_with_speed(duration=duration)
    keyUp(button)
    print(f"Finished pressing {button}.")
    sleep_with_speed(after_delay)

def speed_up_game(indefinitely=False, duration=0.5):
    print("Speeding up the game...")
    keyDown('space')
    if indefinitely:
       sleep_with_speed(duration=duration)
       keyUp('space')
    print("Game speed increased.")