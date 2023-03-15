import json
import app.api_handler as api
import time
import urequests as requests

from secrets import SSID, PASSWORD, SERVER


def connect_to_wifi(wlan):
    wlan.active(False)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    connection_attempts = 10
    while connection_attempts > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        connection_attempts -= 1
        print('waiting for connection...')
        time.sleep(1)
    if wlan.status() != 3:
        return False
    else:
        print("Connected to WiFi, pico ip address: ", wlan.ifconfig()[0])
        return True


def send_request(body):
    try:
        response = requests.get(SERVER, json=body)
        api.process_request(json.loads(response.text))
        response.close()
    except OSError as e:
        print("Request failed: ", e)

