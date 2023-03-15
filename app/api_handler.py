import json
import app.wireless_functions as wf
from app.keypad_functions import kp_actions


def process_request(request):
    if request:
        kp_actions(0)
    else:
        kp_actions(1)


def send_code(code):
    wf.send_request(json.dumps(code))
