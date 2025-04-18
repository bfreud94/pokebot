from os import getenv, path

def get_pokemon_data():
    pokemon_names = getenv("WILD_POKEMON").split(",")
    screenshot_dir = "images/pokemon"
    pokemon_data = {
        name: {
            "image_path": path.join(screenshot_dir, f"{name}/{name}.png"),
            "text_image_path": path.join(screenshot_dir, f"{name}/{name}_text.png")
        }
        for name in pokemon_names
	}
    return pokemon_data