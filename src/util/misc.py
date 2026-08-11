from os import getenv
from time import localtime, sleep, strftime

from util.print_fns import print_with_time

def sleep_with_speed(duration, is_sped_up=True, speed_up_factor=10):
    adjusted_duration = duration if not is_sped_up else duration / speed_up_factor
    print_with_time(f"Sleeping for {adjusted_duration} seconds (game sped up).")
    sleep(adjusted_duration)

def get_time():
   return strftime("%Y-%m-%d %H:%M:%S", localtime())

def get_battle_template_path(is_fighting=False):
    from util.os import get_template_path
    template_dir = get_template_path()
    battle_template_path = f"{template_dir}/trainer_profile_battle.png"
    return battle_template_path

def is_vowel(char):
    return char.lower() in 'aeiou'

def get_location():
	return getenv("CURRENT_LOCATION")