from controls import press_button, press_n_times, quick_press

from pyautogui import hotkey, keyUp
from time import sleep
from util.misc import sleep_with_speed

def reset_and_start_game():
    hotkey('command', 'r')
    for _ in range(4):
        press_button('z')
    quick_press('z')
    quick_press('x')
    quick_press('z')
    quick_press('x')

def quit_game():
    keyUp('space')
    sleep_with_speed(10)
    hotkey('command', 'q')
    sleep_with_speed(10)
    press_button('enter')

def open_mgba():
    sleep_with_speed(10)
    hotkey('command', 'space')
    press_button('m')
    press_button('g')
    press_button('b')
    press_button('a')
    press_button('enter')
    sleep_with_speed(10)

def open_game():
    sleep_with_speed(10)
    hotkey('command', '0')

def start_game_after_open():
    sleep_with_speed(10)
    press_button('z')
    press_button('x')
    for _ in range(7):
        press_button('z')
    press_button('x')