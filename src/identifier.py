from cv2 import imread, IMREAD_GRAYSCALE, matchTemplate, minMaxLoc, TM_CCOEFF_NORMED
from db import add_shiny_entry, get_db_config, update_database_value
from log import log_encounter
from mss import mss
from os import path
from PIL import Image
from screen import get_monitor_to_capture

from util.math import get_percentage
from util.misc import get_time
from util.pokemon import get_pokemon_data
from util.print_fns import print_encounter_data, print_is_in_picture, print_pokemon_name

def are_images_equal(image_path_one, image_path_two, confidence_threshold, print_fn, print_fn_args):
    try:
        img_1 = imread(image_path_one, IMREAD_GRAYSCALE)
        img_2 = imread(image_path_two, IMREAD_GRAYSCALE)
        
        if img_1 is None or img_2 is None:
            print(f"Error: Could not read one of the images for name matching.")
            return False, None
		
        res = matchTemplate(img_1, img_2, TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(res)

        max_val_percent = get_percentage(max_val)
        
        if max_val >= confidence_threshold:
            print_fn(**print_fn_args, max_val_percent=max_val_percent, is_found=True)
            return True
        else:
            print_fn(**print_fn_args, max_val_percent=max_val_percent, is_found=False)
            return False
    except Exception as e:
        print(f"Error during name matching: {e}")
        return False


def find_name_in_battle(battle_screen_path, name_template_path, confidence_threshold=0.99):
    pokemon_name = name_template_path.split("/")[1].capitalize()
    if "Latios" in name_template_path or "Latias" in name_template_path:
        confidence_threshold = 0.999
    return are_images_equal(battle_screen_path, name_template_path, confidence_threshold, print_pokemon_name, { "pokemon_name": pokemon_name })

def is_in_picture(template_path, image_path, confidence_threshold=0.99):
    return are_images_equal(template_path, image_path, confidence_threshold, print_is_in_picture, {})

def check_for_shiny():
    monitor_to_capture = get_monitor_to_capture()
    if not monitor_to_capture:
       print("Error: Could not determine capture monitor.")
       return False

    with mss() as sct:
       sct_img = sct.grab(monitor_to_capture)
       screen_path = "images/tmp/battle_screen.png"  # Save for comparison
       img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
       img.save(screen_path)

    db_data = get_db_config()
    if db_data is None:
        print("Error: Could not retrieve database configuration.")
        return False

    total_encounters = db_data["total_encounters"]
    last_shiny = db_data["last_shiny"]

    pokemon_data = get_pokemon_data()
    for pokemon_name, data in pokemon_data.items():
        regular_path = data["image_path"]
        name_found = find_name_in_battle(screen_path, data["text_image_path"])

        if name_found:
            if not is_in_picture(screen_path, regular_path):
                print("Shiny form present! Stopping program.")
                total_encounters += 1
                update_database_value(f"total_encounters={total_encounters - 1}", f"total_encounters={total_encounters}")
                update_database_value(f"last_shiny={last_shiny}", f"last_shiny={total_encounters}")
                add_shiny_entry(format_entry(pokemon_name, total_encounters, last_shiny))
                print_encounter_data(total_encounters, last_shiny)
                log_encounter(pokemon_name.capitalize(), True, total_encounters, last_shiny)
                return True, pokemon_name
            else:
                print("Regular form present. Continuing.")
                total_encounters += 1
                update_database_value(f"total_encounters={total_encounters - 1}", f"total_encounters={total_encounters}")
                print_encounter_data(total_encounters, last_shiny)
                log_encounter(pokemon_name.capitalize(), False, total_encounters, last_shiny)
                return False, pokemon_name
    print(f"No match found")
    return False

def format_entry(pokemon_name, total_encounters, last_shiny):
    return {
        "pokemon": pokemon_name,
        "time_found": get_time(),
		"img_path": f"images/shinies/{pokemon_name}_{total_encounters}.png",
		"last_shiny": last_shiny,
		"total_encounters": total_encounters
	}