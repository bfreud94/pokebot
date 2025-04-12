import cv2
import numpy as np
import mss
import pyautogui

from PIL import Image

from controls import move_direction, press_button
from screen import get_monitor_to_capture, get_primary_monitor_geometry, get_window_geometry
from util import get_percentage

def is_in_battle(template_path, confidence_threshold=0.6, save_screenshot=False, screenshot_filename="images/tmp/captured_screen.png"):
    monitor_to_capture = get_monitor_to_capture()
    if monitor_to_capture is False:
        print("Error: Could not determine capture monitor.")
        return False
    with mss.mss() as sct:
        sct_img = sct.grab(monitor_to_capture)
        screen = np.array(sct_img)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

        if save_screenshot:
            pil_img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
            pil_img.save(screenshot_filename)
            print(f"Screenshot saved to: {screenshot_filename}")

        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Error: Template image not found at {template_path}")
            return False

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        max_val_percent = get_percentage(max_val)	

        if max_val >= confidence_threshold:
            print(f"In Battle! Confidence: {max_val_percent}")
            return True
        else:
            print(f"Not in Battle. Confidence in battle: {max_val_percent}")
            return False

def exit_battle(pokemon_name):
    before_delay = 0.5
    after_delay = 0.5
    if pokemon_name == 'groudon' or pokemon_name == 'kyogre':
        press_button('z', 3, 3)
    print("Exiting battle...")
    press_button('z', before_delay, after_delay)
    press_button('down')
    press_button('right')
    press_button('z')
    press_button('z')