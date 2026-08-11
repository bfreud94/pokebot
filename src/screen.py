from identifier import are_images_equal

from cv2 import COLOR_RGBA2RGB, cvtColor, imwrite
import numpy as np
from mss import mss
from util.os import os
from time import sleep

from util.print_fns import print_is_in_battle, print_with_time

def get_primary_monitor_geometry():
    with mss() as sct:
        monitor = sct.monitors[1]  # Primary monitor
        return {"top": monitor["top"], "left": monitor["left"], "width": monitor["width"], "height": monitor["height"]}

def get_window_geometry_windows():
    import win32gui
    window_title = "mGBA"
    result = {}

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if window_title in title:
                rect = win32gui.GetWindowRect(hwnd)
                result["left"] = rect[0]
                result["top"] = rect[1]
                result["width"] = rect[2] - rect[0]
                result["height"] = rect[3] - rect[1]

    win32gui.EnumWindows(enum_handler, None)
    return result if result else None

def get_window_geometry_mac():
    from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
    window_title = "mGBA"
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in windows:
        title = window.get('kCGWindowName', '')
        if title is not None and window_title in title:
            bounds = window.get('kCGWindowBounds')
            if bounds:
                return {"top": int(bounds['Y']), "left": int(bounds['X']), "width": int(bounds['Width']), "height": int(bounds['Height'])}
    return None

def get_window_geometry():
    if os == "Windows":
        return get_window_geometry_windows()
    else:
        return get_window_geometry_mac()

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
    sleep(0.05)
    with mss() as sct:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cvtColor(frame, COLOR_RGBA2RGB)
        imwrite(screen_path, frame)

def capture_image_and_compare(monitor_to_capture, pil_img_path, template_path, confidence_threshold=0.9):
    m = monitor_to_capture
    monitor = {
        "top": m["top"],
        "left": m["left"],
        "width": m["width"],
        "height": m["height"]
    }
    sleep(0.05)
    with mss() as sct:
        screenshot = sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cvtColor(frame, COLOR_RGBA2RGB)
        imwrite(pil_img_path, frame)
    return are_images_equal(template_path, pil_img_path, confidence_threshold, print_is_in_battle, {})