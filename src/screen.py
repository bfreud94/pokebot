from identifier import are_images_equal
# from Image import fromBytes

from cv2 import COLOR_RGB2GRAY, cvtColor
from mss import mss
from numpy import array
from PIL import Image
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

from util.print_fns import print_is_in_battle, print_with_time

def get_primary_monitor_geometry():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
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
    with mss() as sct:
       sct_img = sct.grab(monitor_to_capture)
       img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
       img.save(screen_path)

def capture_image_and_compare(monitor_to_capture, pil_img_path, template_path, confidence_threshold=0.9):
    with mss() as sct:
        sct_img = sct.grab(monitor_to_capture)
        screen = array(sct_img)
        screen_gray = cvtColor(screen, COLOR_RGB2GRAY)

        pil_img = Image.frombytes("RGB", (sct_img.width, sct_img.height), sct_img.rgb, "raw", "RGB")
        pil_img.save(pil_img_path)
        return are_images_equal(template_path, pil_img_path, confidence_threshold, print_is_in_battle, {})
    return False