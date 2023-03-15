from app.keypad_functions import kp_actions
from secrets import SSID, PASSWORD


def connect_to_wifi(wlan):
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while True:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        kp_actions(2)
    if wlan.status() != 3:
        return False
    else:
        return True
