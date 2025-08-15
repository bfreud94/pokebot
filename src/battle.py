from controls import move_direction, press_button, press_n_times
from mss import mss
from PIL import Image
from screen import capture_image_and_compare, get_monitor_to_capture

from constants.pokemon import get_pokemon_to_wait_for
from util.misc import get_battle_template_path, sleep_with_speed
from util.print_fns import print_with_time

def is_in_battle(confidence_threshold=0.9, is_fighting=False):
    monitor_to_capture = get_monitor_to_capture()
    if not monitor_to_capture:
        print_with_time("Error: Could not determine capture monitor.")
        return False

    pil_img_path = "images/current/battle_screen.png"
    template_path = get_battle_template_path(is_fighting)
    return capture_image_and_compare(monitor_to_capture, pil_img_path, template_path)

def is_battle_over():
    monitor_to_capture = get_monitor_to_capture()
    if not monitor_to_capture:
        print_with_time("Error: Could not determine capture monitor.")
        return False

    pil_img_path = "images/current/battle_complete.png"
    template_path = "images/templates/battle_complete.png"
    return capture_image_and_compare(monitor_to_capture, pil_img_path, template_path)

def fight_pokemon():
    press_n_times('z', 2)

def exit_battle(pokemon_name):
    before_delay = 0.5
    after_delay = 0.5
    should_wait_battle_intro = get_pokemon_to_wait_for(pokemon_name)
    if should_wait_battle_intro:
        press_button('z', 3, 3)
        sleep_with_speed(10)
    print_with_time("Exiting battle...")
    if not should_wait_battle_intro:
       press_button('z', 5, after_delay)
    press_button('down')
    press_button('right')
    press_n_times('z', 2)