from time import localtime, strftime

def print_with_time(msg):
    current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    print(f"[{current_time}]: {msg}")

def print_encounter_data(total_encounters, last_shiny):
    print("===============================================================================")
    print_with_time(f"Total encounters: {total_encounters}")
    print_with_time(f"Encounters since last shiny: {total_encounters - last_shiny}")
    print("===============================================================================")

def print_pokemon_name(pokemon_name, max_val_percent, is_found):
    print_with_time(f"{pokemon_name} found! Confidence: {max_val_percent}")

def print_is_in_picture(max_val_percent, is_found):
    print_with_time(f"Template found in image! Confidence: {max_val_percent}")

def print_is_in_battle(max_val_percent, is_found):
    if is_found:
        print_with_time(f"In Battle! Confidence: {max_val_percent}")
    else:
        print_with_time(f"Not in Battle. Confidence in battle: {max_val_percent}")