from app.keypad_functions import kp_actions
from app.pin_handler import set_led

REQUESTS = {'/light/on': [set_led, 1],
            '/light/off': [set_led, 0],
            '/keypad/action/0': [kp_actions, 0],
            '/keypad/action/1': [kp_actions, 1],
            '/keypad/action/2': [kp_actions, 2]}

html = """<!DOCTYPE html>
        <html>
            <head>
                <title>Pico W</title>
            </head>
            <body>
                <h1>Pico W</h1>
                <p>%s</p>
            </body>
        </html>
"""


def process_request(request):
    for request_param, action in REQUESTS.items():
        if request.find(request_param) != -1:
            action[0](action[1])

