import time
import subprocess

def open_emulator(emulator_path):
    """Attempts to open the emulator."""
    try:
        print(f"Attempting to open emulator: {emulator_path}")
        subprocess.Popen(['open', emulator_path])
        time.sleep(5)  # Give the emulator some time to open
        print("Emulator should be open now.")
        return True
    except FileNotFoundError:
        print(f"Error: Emulator file not found at {emulator_path}")
        return False
    except Exception as e:
        print(f"An error occurred while trying to open the emulator: {e}")
        return False

def open_rom_in_emulator(emulator_path, rom_path):
    """Attempts to open the ROM within the already running emulator
       using command-line arguments (emulator-dependent)."""
    try:
        print(f"Attempting to open ROM '{rom_path}' in emulator '{emulator_path}'")
        # This command structure is highly emulator-specific.
        # Consult your emulator's documentation for the correct syntax.
        subprocess.Popen(['open', '-a', emulator_path, rom_path])
        time.sleep(5)  # Give the emulator time to load the ROM
        print("ROM should be loaded in the emulator.")
        return True
    except FileNotFoundError:
        print(f"Error: Emulator or ROM file not found.")
        return False
    except Exception as e:
        print(f"An error occurred while trying to open the ROM: {e}")
        return False