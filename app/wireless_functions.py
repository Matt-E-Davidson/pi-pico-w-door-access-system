import app.api_handler as api
import json
import urequests as requests

from app.keypad_functions import kp_actions
from secrets import SSID, PASSWORD, SERVER


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


def send_request(body):
    try:
        response = requests.get(SERVER, json=body)
        api.process_request(json.loads(response.text))
        response.close()
    except OSError as e:
        print("Request failed: ", e)
