from time import localtime, sleep, strftime

def sleep_with_speed(duration, is_sped_up=True, speed_up_factor=10):
    adjusted_duration = duration if not is_sped_up else duration / speed_up_factor
    print(f"Sleeping for {adjusted_duration} seconds (game sped up).")
    sleep(adjusted_duration)

def get_time():
   return strftime("%Y-%m-%d %H:%M:%S", localtime())

def get_battle_template_path():
    battle_template_path = "images/tmp/battle_start_template.png"
    return battle_template_path

def is_vowel(char):
    return char.lower() in 'aeiou'