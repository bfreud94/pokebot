from os import getenv, path
from util.os import os, get_pokemon_screenshot_dir

def get_pokemon_data():
    pokemon_names = getenv("WILD_POKEMON").split(",")
    screenshot_dir = get_pokemon_screenshot_dir() if os == "Windows" else "images/pokemon"
    pokemon_data = {
        name: {
            "image_path": path.join(screenshot_dir, f"{name}/{name}.png"),
            "text_image_path": path.join(screenshot_dir, f"{name}/{name}_text.png")
        }
        for name in pokemon_names
	}
    return pokemon_data