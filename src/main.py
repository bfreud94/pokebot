from actions import roam_grass, loop_roam_grass, magikarp_static_encounter
from controls import speed_up_game
from db import read_database
from dotenv import load_dotenv
from processes.game_start import open_game, open_mgba, quit_game, start_game_after_open
from os import getenv
from time import sleep, time

from util.misc import get_time
from util.print_fns import print_with_time

load_dotenv()

def get_program_args():
    emulator_executable_path = getenv('EMULATOR_EXECUTABLE_PATH')
    rom_file_path = getenv('ROM_FILE_PATH')
    
    return {
        "emulator_executable_path": emulator_executable_path,
        "rom_file_path": rom_file_path
    }

def main():
    print("Welcome to the Pokémon emulator automation script!")
    input("Press Enter once the game is loaded and focused...")

    print_with_time(f"Starting game at current time: {get_time()}")

    start_time = time()
    program_args = get_program_args()
    sleep(3)
    speed_up_game()
    loop_roam_grass()

main()