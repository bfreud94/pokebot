from controls import press_button, press_n_times, quick_press

from time import sleep

def get_magikarp():
    press_n_times('z', 4)
    press_button('x')

def go_to_magikarp_screen():
    sleep(0.1)
    press_button('enter')
    press_button('down')
    press_button('z')
    press_n_times('up', 2, quick_press)
    press_n_times('z', 2)