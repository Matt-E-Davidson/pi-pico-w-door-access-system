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

NUM_PADS = kp.get_num_pads()
VALID_KEYS = KEYS.keys()


def init_kp():
    kp.init()
    kp.set_brightness(1.0)


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
        illum_key_with_colour(key, COLOURS[0])


def flash_all_keys(colour, times):
    for _ in range(times):
        illum_keys_with_colour(range(16), colour)
        kp.update()
        time.sleep(0.5)
        reset_key_colours(range(16))
        kp.update()
        time.sleep(0.5)


def loading_pattern():
    for _ in range(2):
        for i in [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4]:
            illum_key_with_colour(i, COLOURS[4])
            kp.update()
            time.sleep(0.2)
            reset_key_colour(i)
            kp.update()
            time.sleep(0.1)
        reset_key_colours(range(16))
        kp.update()
    reset_key_colours(range(16))
    kp.update()


def kp_actions(action):
    if action == 0:
        loading_pattern()
    if action == 1:
        flash_all_keys(COLOURS[1], 3)
    if action == 2:
        flash_all_keys(COLOURS[2], 3)
