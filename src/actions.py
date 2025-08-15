from battle import is_in_battle, is_battle_over, exit_battle, fight_pokemon
from controls import move_direction, press_button, press_n_times
from db import add_shiny_entry, get_db_data, format_entry, update_database_value
from identifier import check_for_shiny, check_for_shiny_magikarp
from log import log_encounter
from os import _exit
from screen import capture_screen, get_monitor_to_capture

from processes.magikarp_static import get_magikarp, go_to_magikarp_screen
from processes.game_start import reset_and_start_game
from util.misc import sleep_with_speed
from util.print_fns import print_encounter_data, print_with_time

from time import sleep

def loop_roam_grass():
    while True:
        roam_grass()

def roam_grass_with_reset(time):
    while True:
        if time() - start_time > 10:
            print_with_time("Resetting the game...")
            quit_game()
            open_mgba()
            open_game()
            speed_up_game()
            start_game_after_open()
            start_time = time()
            print_with_time("Resetting the game...")

def roam_grass():
    move_direction('up')
    sleep_with_speed(8)

    monitor_to_capture = get_monitor_to_capture()
    if not monitor_to_capture:
        print_with_time("Error: Could not determine capture monitor.")
        return False

    is_battle = is_in_battle()
    if is_battle:
        is_shiny, pokemon_name = check_for_shiny(capture_screen, monitor_to_capture)
        if (is_shiny):
            _exit(0)
        exit_battle(pokemon_name)
    move_direction('down')

def magikarp_static_encounter():
    while True:
        sleep(1)
        get_magikarp()
        go_to_magikarp_screen()

        is_shiny = check_for_shiny_magikarp(capture_screen, monitor_to_capture)

        db_data = get_db_data()
        total_encounters = db_data["total_encounters"]
        last_shiny = db_data["last_shiny"]

        total_encounters += 1

        if is_shiny:
            update_database_value(f"total_encounters={total_encounters - 1}", f"total_encounters={total_encounters}")
            update_database_value(f"last_shiny={last_shiny}", f"last_shiny={total_encounters}")
            add_shiny_entry(format_entry("magikarp", total_encounters, last_shiny))
            print_encounter_data(total_encounters, last_shiny)
            log_encounter("Magikarp", True, total_encounters, last_shiny)
            break
        else:
            update_database_value(f"total_encounters={total_encounters - 1}", f"total_encounters={total_encounters}")
            print_encounter_data(total_encounters, last_shiny)
            log_encounter("Magikarp", False, total_encounters, last_shiny)
            reset_and_start_game()

def roam_grass_and_fight():
    while True:
        move_direction('up')
        sleep_with_speed(8)
        is_battle = is_in_battle(True)
        if is_battle:
            monitor_to_capture = get_monitor_to_capture()
            if not monitor_to_capture:
                print_with_time("Error: Could not determine capture monitor.")
                return False

            is_shiny, pokemon_name = check_for_shiny(capture_screen, monitor_to_capture)
            if is_shiny:
                _exit(0)
            while is_battle:
                fight_pokemon()
                is_battle = is_in_battle(True)
                battle_over = is_battle_over()
                if battle_over:
                    press_n_times('z', 3)
                    break
        move_direction('down')