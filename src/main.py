from actions import roam_grass
from controls import speed_up_game
from db import read_database
from dotenv import load_dotenv
from os import getenv
from time import sleep

load_dotenv()

def get_program_args():
    emulator_executable_path = getenv('EMULATOR_EXECUTABLE_PATH')
    rom_file_path = getenv('ROM_FILE_PATH')
    
    sleep(3)
    speed_up_game()
    return {
        "emulator_executable_path": emulator_executable_path,
        "rom_file_path": rom_file_path
    }

def main():
    print("Welcome to the Pokémon emulator automation script!")
    input("Press Enter once the game is loaded and focused...")
    
    program_args = get_program_args()
    roam_grass(**program_args)

main()