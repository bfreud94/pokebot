from actions import roam_grass
from controls import speed_up_game

if __name__ == "__main__":
    print("Welcome to the Pokémon emulator automation script!")

    emulator_executable_path = '/Applications/mGBA.app'
    rom_file_path = '/Users/Freud/Games/Roms/Game Boy Advanced/Pokemon FireRed/Pokemon FireRed.gba'

    # if open_emulator(emulator_executable_path):
    if True:
        # Give the emulator a moment to fully launch before trying to open the ROM
        # time.sleep(3)

        # Try opening the ROM using command-line arguments.
        # This might not work for all emulators. Some require the emulator to be
        # running first and then you might need to send keyboard/mouse inputs
        # to the emulator window to open the ROM (more complex).
        # if open_rom_in_emulator(emulator_executable_path, rom_file_path):
            input("Press Enter once the game is loaded and focused...")
            speed_up_game()
            roam_grass()
        #else:
            #print("Failed to open the ROM within the emulator (command-line attempt).")
            #print("You might need a more emulator-specific approach.")
    else:
        print("Failed to open the emulator. Exiting.")