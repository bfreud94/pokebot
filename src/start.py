from time import sleep
from rocess import Popen

from util.print_fns import print_with_time

def open_emulator(emulator_path):
    """Attempts to open the emulator."""
    try:
        print_with_time(f"Attempting to open emulator: {emulator_path}")
        Popen(['open', emulator_path])
        sleep(5)  # Give the emulator some time to open
        print_with_time("Emulator should be open now.")
        return True
    except FileNotFoundError:
        print_with_time(f"Error: Emulator file not found at {emulator_path}")
        return False
    except Exception as e:
        print_with_time(f"An error occurred while trying to open the emulator: {e}")
        return False

def open_rom_in_emulator(emulator_path, rom_path):
    """Attempts to open the ROM within the already running emulator
       using command-line arguments (emulator-dependent)."""
    try:
        print_with_time(f"Attempting to open ROM '{rom_path}' in emulator '{emulator_path}'")
        # This command structure is highly emulator-specific.
        # Consult your emulator's documentation for the correct syntax.
        Popen(['open', '-a', emulator_path, rom_path])
        sleep(5)  # Give the emulator time to load the ROM
        print_with_time("ROM should be loaded in the emulator.")
        return True
    except FileNotFoundError:
        print_with_time(f"Error: Emulator or ROM file not found.")
        return False
    except Exception as e:
        print_with_time(f"An error occurred while trying to open the ROM: {e}")
        return False