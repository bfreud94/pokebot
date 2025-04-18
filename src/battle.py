from controls import move_direction, press_button
from cv2 import COLOR_RGB2GRAY, cvtColor
from identifier import are_images_equal
from mss import mss
from numpy import array
from PIL import Image
from screen import get_monitor_to_capture, get_primary_monitor_geometry, get_window_geometry

from util.misc import get_battle_template_path
from util.print_fns import print_is_in_battle

def is_in_battle(confidence_threshold=0.9):
    template_path = get_battle_template_path()
    monitor_to_capture = get_monitor_to_capture()
    if not monitor_to_capture:
        print("Error: Could not determine capture monitor.")
        return False
    with mss() as sct:
        sct_img = sct.grab(monitor_to_capture)
        screen = array(sct_img)
        screen_gray = cvtColor(screen, COLOR_RGB2GRAY)

        pil_img_path = "images/tmp/captured_screen.png"
        pil_img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
        pil_img.save(pil_img_path)
        return are_images_equal(template_path, pil_img_path, confidence_threshold, print_is_in_battle, {})
    return False

def exit_battle(pokemon_name):
    before_delay = 0.5
    after_delay = 0.5
    if pokemon_name == 'groudon' or pokemon_name == 'kyogre':
        press_button('z', 3, 3)
    print("Exiting battle...")
    press_button('z', 5, after_delay)
    press_button('down')
    press_button('right')
    press_button('z')
    press_button('z')