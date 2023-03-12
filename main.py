import network
import app.wireless_functions as wf
from app.keypad_functions import init_kp, flash_all_keys, COLOURS


def main():
    init_kp()
    if wf.connect_to_wifi(network.WLAN(network.STA_IF)):
        flash_all_keys(COLOURS[4], 2)
        socket = wf.bind_socket()
        while True:
            wf.accept_requests(socket)
    else:
        flash_all_keys(COLOURS[1], 2)
        print("WiFi connection failed")


main()
