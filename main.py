import network

from app.keypad_functions import init_kp, take_user_input, kp_actions
from app.wireless_functions import connect_to_wifi


def main():
    init_kp()
    if connect_to_wifi(network.WLAN(network.STA_IF)):
        kp_actions(0)
        while True:
            take_user_input()
    else:
        kp_actions(1)
        print("WiFi connection failed")


main()
