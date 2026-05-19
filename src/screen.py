from identifier import are_images_equal

from PIL import Image, ImageGrab
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from time import sleep

from util.print_fns import print_is_in_battle, print_with_time

def get_primary_monitor_geometry():
    screen = ImageGrab.grab()
    return {"top": 0, "left": 0, "width": screen.width, "height": screen.height}

def get_window_geometry():
    window_title = "mGBA"
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in windows:
        owner = window.get('kCGWindowOwnerName', '')
        title = window.get('kCGWindowName', '')
        if title is not None and window_title in title:
            bounds = window.get('kCGWindowBounds')
            if bounds:
                return {"top": int(bounds['Y']), "left": int(bounds['X']), "width": int(bounds['Width']), "height": int(bounds['Height'])}
    return None

def get_monitor_to_capture():
    game_window_geometry = get_window_geometry()

    if game_window_geometry:
        monitor_to_capture = game_window_geometry
        print_with_time(f"Capturing mGBA window: {monitor_to_capture}")
        return monitor_to_capture
    else:
        primary_monitor = get_primary_monitor_geometry()
        if primary_monitor:
            monitor_to_capture = primary_monitor
            print_with_time(f"mGBA window not found. Capturing primary monitor: {monitor_to_capture}")
        else:
            print_with_time("Error: Could not determine capture monitor.")
            return False

def capture_screen(monitor_to_capture, screen_path):
    m = monitor_to_capture
    bbox = (m["left"], m["top"], m["left"] + m["width"], m["top"] + m["height"])
    img = ImageGrab.grab(bbox=bbox)
    img.save(screen_path)

def capture_image_and_compare(monitor_to_capture, pil_img_path, template_path, confidence_threshold=0.9):
    m = monitor_to_capture
    bbox = (m["left"], m["top"], m["left"] + m["width"], m["top"] + m["height"])
    pil_img = ImageGrab.grab(bbox=bbox)
    pil_img.save(pil_img_path)
    return are_images_equal(template_path, pil_img_path, confidence_threshold, print_is_in_battle, {})