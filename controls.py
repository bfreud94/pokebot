import pyautogui

from util import sleep_with_speed

def move_direction(direction, duration=2):
    print(f"Moving {direction} for {duration} seconds...")
    if direction == 'left':
        pyautogui.keyDown('left')
        sleep_with_speed(duration=duration)
        pyautogui.keyUp('left')
    elif direction == 'right':
        pyautogui.keyDown('right')
        sleep_with_speed(duration=duration)
        pyautogui.keyUp('right')
    elif direction == 'up':
        pyautogui.keyDown('up')
        sleep_with_speed(duration=duration)
        pyautogui.keyUp('up')
    elif direction == 'down':
        pyautogui.keyDown('down')
        sleep_with_speed(duration=duration)
        pyautogui.keyUp('down')
    print(f"Finished moving {direction}.")

def press_button(button, duration=0.5, before_delay=0.5, after_delay=0.5):
    sleep_with_speed(before_delay)
    print(f"Pressing {button} for {duration} seconds...")
    pyautogui.keyDown(button)
    sleep_with_speed(duration=duration)
    pyautogui.keyUp(button)
    print(f"Finished pressing {button}.")
    sleep_with_speed(after_delay)

def speed_up_game(indefinitely=False, duration=0.5):
    print("Speeding up the game...")
    pyautogui.keyDown('space')
    if indefinitely:
       sleep_with_speed(duration=duration)
       pyautogui.keyUp('space')
    print("Game speed increased.")