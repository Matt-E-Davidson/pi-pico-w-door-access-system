import network
import app.wireless_functions as wf
from app.keypad_functions import init_kp, flash_keys


CONNECT_TO_INTERNET = True


def main():
    init_kp()
    if CONNECT_TO_INTERNET:
        wlan = network.WLAN(network.STA_IF)
        if wf.connect_to_wifi(wlan):
            flash_keys(4, 2)
            socket = wf.bind_socket()
            while True:
                wf.accept_requests(socket)
        else:
            flash_keys(1, 2)
            print("WiFi connection failed")


main()
