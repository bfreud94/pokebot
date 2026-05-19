from identifier import are_images_equal

import cv2
import numpy as np
from mss import mss
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from time import sleep

from util.print_fns import print_is_in_battle, print_with_time

def get_primary_monitor_geometry():
    with mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        return {"top": monitor["top"], "left": monitor["left"], "width": monitor["width"], "height": monitor["height"]}

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
    monitor = {
        "top": m["top"],
        "left": m["left"],
        "width": m["width"],
        "height": m["height"]
    }
    with mss() as sct:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        cv2.imwrite(screen_path, frame)

def capture_image_and_compare(monitor_to_capture, pil_img_path, template_path, confidence_threshold=0.9):
    m = monitor_to_capture
    monitor = {
        "top": m["top"],
        "left": m["left"],
        "width": m["width"],
        "height": m["height"]
    }
    with mss() as sct:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        cv2.imwrite(pil_img_path, frame)
    return are_images_equal(template_path, pil_img_path, confidence_threshold, print_is_in_battle, {})