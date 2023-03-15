import app.api_handler as api
import picokeypad as kp
import time


KEYS = {0x0001: 0, 0x0002: 1,
        0x0004: 2, 0x0008: 3,
        0x0010: 4, 0x0020: 5,
        0x0040: 6, 0x0080: 7,
        0x0100: 8, 0x0200: 9,
        0x0400: 10, 0x0800: 11,
        0x1000: 12, 0x2000: 13,
        0x4000: 14, 0x8000: 15}

COLOURS = {0: [0x05, 0x05, 0x05], 1: [0xff, 0x00, 0x00], 2: [0xff, 0x7f, 0x00],
           3: [0xff, 0xff, 0x00], 4: [0x00, 0xff, 0x00], 5: [0x00, 0x00, 0xff],
           6: [0x4b, 0x00, 0x82], 7: [0x94, 0x00, 0xd3]}

OUTER_KEYS = [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4]
INNER_KEYS = [5, 6, 9, 10]

NUM_PADS = kp.get_num_pads()
VALID_KEYS = KEYS.keys()


def init_kp():
    kp.init()
    kp.set_brightness(1.0)
    reset_key_colours(range(16))
    kp.update()


def key_to_hex(key):
    return 2**key


def illum_key_with_colour(key, colour):
    kp.illuminate(key, colour[0], colour[1], colour[2])


def illum_keys_with_colour(keys, colour):
    for key in keys:
        illum_key_with_colour(key, colour)


def reset_key_colour(key):
    illum_key_with_colour(key, COLOURS[0])


def reset_key_colours(keys):
    for key in keys:
        reset_key_colour(key)


def flash_all_keys(colour, times):
    for _ in range(times):
        illum_keys_with_colour(range(16), colour)
        kp.update()
        time.sleep(0.5)
        reset_key_colours(range(16))
        kp.update()
        time.sleep(0.5)


def loading_pattern(times):
    for _ in range(times):
        for i in OUTER_KEYS:
            illum_key_with_colour(i, COLOURS[4])
            kp.update()
            time.sleep(0.1)
            reset_key_colour(i)
            kp.update()
            time.sleep(0.05)
        reset_key_colours(range(16))
        kp.update()
    reset_key_colours(range(16))
    kp.update()


def error_pattern():
    for _ in range(10):
        for colour in [1, 2]:
            illum_keys_with_colour(INNER_KEYS, COLOURS[colour])
            illum_keys_with_colour(OUTER_KEYS, COLOURS[colour - 1])
            kp.update()
            time.sleep(0.2)
    reset_key_colours(range(16))
    kp.update()


def take_user_input():
    pressed_keys = []
    key_colours = []
    while True:
        button_states = kp.get_button_states()
        if button_states > 0:
            if (len(pressed_keys) > 0) and (KEYS[button_states] == pressed_keys[-1]):
                illum_key_with_colour(KEYS[button_states],
                                      COLOURS[(key_colours[-1] + 1) % len(COLOURS)])
                key_colours.append((key_colours[-1] + 1) % len(COLOURS))
            else:
                illum_key_with_colour(KEYS[button_states], COLOURS[5])
                key_colours.append(5)
            kp.update()
            pressed_keys.append(KEYS[button_states])
            if len(pressed_keys) == 4:
                api.send_code(pressed_keys)
                for key in pressed_keys:
                    reset_key_colour(key)
                    kp.update()
                break
        time.sleep(0.2)


def kp_actions(action, times=1):
    if action == 0:
        flash_all_keys(COLOURS[4], 3)
    elif action == 1:
        flash_all_keys(COLOURS[1], 3)
    elif action == 2:
        loading_pattern(times)
    else:
        error_pattern()
