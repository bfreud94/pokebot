def print_encounter_data(total_encounters, last_shiny):
    print("=====================================")
    print(f"Total encounters: {total_encounters}")
    print(f"Encounters since last shiny: {total_encounters - last_shiny}")
    print("=====================================")

def print_pokemon_name(pokemon_name, max_val_percent, is_found):
    print(f"{pokemon_name} found! Confidence: {max_val_percent}")

def print_is_in_picture(max_val_percent, is_found):
    print(f"Template found in image! Confidence: {max_val_percent}")

def print_is_in_battle(max_val_percent, is_found):
    if is_found:
        print(f"In Battle! Confidence: {max_val_percent}")
    else:
        print(f"Not in Battle. Confidence in battle: {max_val_percent}")