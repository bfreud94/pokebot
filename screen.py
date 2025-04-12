import mss
import Quartz

def get_primary_monitor_geometry():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        return {"top": monitor["top"], "left": monitor["left"], "width": monitor["width"], "height": monitor["height"]}

def get_window_geometry():
    window_title = "mGBA"
    windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
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
        print(f"Capturing mGBA window: {monitor_to_capture}")
        return monitor_to_capture
    else:
        primary_monitor = get_primary_monitor_geometry()
        if primary_monitor:
            monitor_to_capture = primary_monitor
            print(f"mGBA window not found. Capturing primary monitor: {monitor_to_capture}")
        else:
            print("Error: Could not determine capture monitor.")
            return False