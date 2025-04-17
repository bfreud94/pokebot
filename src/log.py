from util import get_time, is_vowel

def log_encounter_with_date(data, file):
    current_time = get_time()
    write_string = f"[{current_time}]: "
    file.write(write_string + data + "\n")

def log_encounter(pokemon_name, is_shiny, total_encounters, last_shiny):
    write_string = ""
    with open("encounters.txt", "a") as file:
        if is_shiny:
            writeString += f"Encountered a Shiny {pokemon_name}!"
        else:
            first_letter = pokemon_name[0].lower()
            a_or_an = "a" if is_vowel(first_letter) else "an"
            write_string += f"Encountered {a_or_an} {pokemon_name}"
        log_encounter_with_date(write_string, file)
        log_encounter_with_date(f"Total Encounters: {total_encounters}", file)
        log_encounter_with_date(f"Encounters since Shiny: {last_shiny}", file)
    print("Data written to encounters.txt")