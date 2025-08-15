def get_pokemon_to_wait_for(pokemon_name):
    weather_pokemon = ["groudon", "kyogre"]
    intimidate_pokemon = ["ekans"]
    return pokemon_name in weather_pokemon or pokemon_name in intimidate_pokemon