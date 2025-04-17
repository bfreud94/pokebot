import argparse
import time
from os import getenv, path

def sleep_with_speed(duration, is_sped_up=True, speed_up_factor=10):
    adjusted_duration = duration if not is_sped_up else duration / speed_up_factor
    print(f"Sleeping for {adjusted_duration} seconds (game sped up).")
    time.sleep(adjusted_duration)

def get_percentage(number):
    return f"{round(number * 100, 2)}%"

def get_time():
   return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_has_extended_display():
    parser = argparse.ArgumentParser(description="Pokémon Emulator Automation Script")
    parser.add_argument(
        "--extended-display",
        action="store_true",
        help="Enable extended display mode (default: False)"
    )
    args = parser.parse_args()
    has_extended_display = args.extended_display
    return has_extended_display

def get_battle_template_path():
    has_extended_display = get_has_extended_display()
    battle_template_path = "images/tmp/battle_start_template.png"
    if has_extended_display:
        battle_template_path = "images/tmp/battle_start_template_ed.png"
    return battle_template_path

def get_image_paths(name, screenshot_dir):
    ending = ".png"
    has_extended_display = get_has_extended_display()
    if has_extended_display:
        ending = "_ed.png"
    image_path = path.join(screenshot_dir, f"{name}/{name}.png"),
    text_image_path = path.join(screenshot_dir, f"{name}/{name}_text.png")
    return { image_path, text_image_path }

def get_pokemon_data():
    pokemon_names = getenv("WILD_POKEMON").split(",")
    print(f"Pokemon names: {pokemon_names}")
    screenshot_dir = "images"
    pokemon_data = {
        name: {
            "image_path": path.join(screenshot_dir, f"{name}/{name}.png"),
            "text_image_path": path.join(screenshot_dir, f"{name}/{name}_text.png")
        }
        for name in pokemon_names
        for image_path, text_image_path in [get_image_paths(name, screenshot_dir)]
	}
    return pokemon_data

def is_vowel(char):
    return char.lower() in 'aeiou'