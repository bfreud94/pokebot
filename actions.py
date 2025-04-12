import os

from battle import is_in_battle, exit_battle
from controls import move_direction
from identifier import check_for_shiny
from util import sleep_with_speed

def roam_grass():
    while True:
        move_direction('up')
        sleep_with_speed(1)
        is_battle = is_in_battle('images/tmp/battle_start_template.png', save_screenshot=True)
        if is_battle:
            is_shiny, pokemon_name = check_for_shiny()
            if (is_shiny):
               os._exit(0)
            exit_battle(pokemon_name)
        move_direction('down')
        sleep_with_speed(1)