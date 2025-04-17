from battle import is_in_battle, exit_battle
from controls import move_direction
from identifier import check_for_shiny
from os import _exit
from util import sleep_with_speed

def roam_grass(emulator_executable_path, rom_file_path):
    while True:
        move_direction('left')
        sleep_with_speed(8)
        is_battle = is_in_battle()
        if is_battle:
            is_shiny, pokemon_name = check_for_shiny()
            if (is_shiny):
               _exit(0)
            exit_battle(pokemon_name)
        move_direction('right')