import network
import app.wireless_functions as wf
from app.keypad_functions import init_kp, kp_actions, take_user_input, COLOURS


def main():
    init_kp()
    if wf.connect_to_wifi(network.WLAN(network.STA_IF)):
        kp_actions(0)
        while True:
            take_user_input()
    else:
        kp_actions(1)
        print("WiFi connection failed")


main()
