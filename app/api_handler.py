import json
import urequests as requests

from secrets import SERVER


def process_response(response):
    from app.keypad_functions import kp_actions
    if response:
        kp_actions(0)
    else:
        kp_actions(1)


def get_code_length():
    return send_request(uri="/code-length")


def send_code(code):
    process_response(send_request(uri="/validate-code", body=json.dumps(code)))


def send_request(uri='', body=None):
    try:
        return json.loads(requests.get(SERVER + uri, json=body).text)
    except OSError as e:
        print("Request failed: ", e)
