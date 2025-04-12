import time
import mss
import cv2
import numpy as np
from PIL import Image
import sys
import os

from screen import get_monitor_to_capture
from util import get_percentage, print_encounters

pokemon_names = ["celebi", "entei", "groudon", "kyogre", "latias", "latios", "lugia", "mew", "mewtwo", "rayquaza", "raikou", "suicune"]
# pokemon_names = ["pidgey", "rattata"]
screenshot_dir = "images"
pokemon_data = {
    name: {
        "regular": os.path.join(screenshot_dir, f"{name}/{name}.png"),
        "shiny": os.path.join(screenshot_dir, f"{name}/{name}_shiny.png"),
        "text": os.path.join(screenshot_dir, f"{name}/{name}_text.png")
    }
	for name in pokemon_names
}

total_encounters = 0

def find_name_in_battle(battle_screen_path, name_template_path, confidence_threshold=0.99):
    pokemon_name = name_template_path.split("/")[1].capitalize()
    if "Latios" in name_template_path or "Latias" in name_template_path:
        confidence_threshold = 0.999
    try:
        battle_screen = cv2.imread(battle_screen_path, cv2.IMREAD_GRAYSCALE)
        name_template = cv2.imread(name_template_path, cv2.IMREAD_GRAYSCALE)

        if battle_screen is None or name_template is None:
            print(f"Error: Could not read one of the images for name matching.")
            return False, None

        res = cv2.matchTemplate(battle_screen, name_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        max_val_percent = get_percentage(max_val)

        if max_val >= confidence_threshold:
            print(f"{pokemon_name} found! Confidence: {max_val_percent}")
            return True, pokemon_name
        else:
            return False, None
    except Exception as e:
        print(f"Error during name matching: {e}")
        return False, None, None

def compare_images(image_path1, image_path2, tolerance=10):
    try:
        img1 = cv2.imread(image_path1)
        img2 = cv2.imread(image_path2)
        if img1 is None or img2 is None:
            print(f"Error: Could not read one of the images for comparison.")
            return False

        img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0])) # Ensure same size
        difference = cv2.absdiff(img1, img2)
        average_difference = np.mean(difference)
        return average_difference < tolerance
    except Exception as e:
        print(f"Error during image comparison: {e}")
        return False

def is_in_picture(template_path, image_path, confidence_threshold=0.99):
    try:
        # Load the images in color (BGR format)
        template = cv2.imread(template_path)
        image = cv2.imread(image_path)

        if template is None or image is None:
            print(f"Error: Could not read one of the images.")
            return False

        # Perform template matching
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        # Check if the match exceeds the confidence threshold
        max_val_percent = get_percentage(max_val)
        if max_val >= confidence_threshold:
            print(f"Template found in image! Confidence: {max_val_percent}")
            return True
        else:
            print(f"Template not found. Max confidence: {max_val_percent}")
            return False
    except Exception as e:
        print(f"Error during template matching: {e}")
        return False

def check_for_shiny():
    global total_encounters
    monitor_to_capture = get_monitor_to_capture()
    if monitor_to_capture is False:
       print("Error: Could not determine capture monitor.")
       return False
    with mss.mss() as sct:
       sct_img = sct.grab(monitor_to_capture)
       screen_path = "images/tmp/battle_screen.png"  # Save for comparison
       img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
       img.save(screen_path)

    for pokemon_name, data in pokemon_data.items():
        name_found, name_template_path = find_name_in_battle(screen_path, data["text"])

        if name_found:
            regular_path = data["regular"]
            if not is_in_picture(screen_path, regular_path):
                print("Shiny form present! Stopping program.")
                print_encounters(total_encounters)
                return True, pokemon_name
            else:
                total_encounters += 1
                print("Regular form present. Continuing.")
                print_encounters(total_encounters)
                return False, pokemon_name
    print(f"No match found")
    return False