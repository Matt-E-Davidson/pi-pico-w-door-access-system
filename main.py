import network
import app.wireless_functions as wf
from app.keypad_functions import init_kp, flash_all_keys, take_user_input, COLOURS


def main():
    init_kp()
    if wf.connect_to_wifi(network.WLAN(network.STA_IF)):
        flash_all_keys(COLOURS[4], 2)
        while True:
            take_user_input()
    else:
        flash_all_keys(COLOURS[1], 2)
        print("WiFi connection failed")


main()
