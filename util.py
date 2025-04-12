import time

def sleep_with_speed(duration, is_sped_up=True, speed_up_factor=10):
    adjusted_duration = duration if not is_sped_up else duration / speed_up_factor
    print(f"Sleeping for {adjusted_duration} seconds (game sped up).")
    time.sleep(adjusted_duration)

def get_percentage(number):
    return f"{round(number * 100, 2)}%"

def print_encounters(total_encounters):
    print("=====================================")
    print(f"Total encounters: {total_encounters}")
    print("=====================================")