import picokeypad as kp
import time


KEYS = {0x0001: {"key": 0,  "colour": 0}, 0x0002: {"key": 1,  "colour": 0},
        0x0004: {"key": 2,  "colour": 0}, 0x0008: {"key": 3,  "colour": 0},
        0x0010: {"key": 4,  "colour": 0}, 0x0020: {"key": 5,  "colour": 0},
        0x0040: {"key": 6,  "colour": 0}, 0x0080: {"key": 7,  "colour": 0},
        0x0100: {"key": 8,  "colour": 0}, 0x0200: {"key": 9,  "colour": 0},
        0x0400: {"key": 10, "colour": 0}, 0x0800: {"key": 11, "colour": 0},
        0x1000: {"key": 12, "colour": 0}, 0x2000: {"key": 13, "colour": 0},
        0x4000: {"key": 14, "colour": 0}, 0x8000: {"key": 15, "colour": 0}}

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


def get_key_colour(key):
    return KEYS[key]["colour"]


def set_key_colour(key, colour):
    KEYS[key]["colour"] = colour


def update_key_colour(key, colour):
    r, g, b = COLOURS[colour]
    kp.illuminate(key, r, g, b)
    kp.update()


def update_key_colours():
    for key in range(NUM_PADS):
        update_key_colour(key, KEYS[key_to_hex(key)]["colour"])


def reset_key_colours():
    for key in range(NUM_PADS):
        KEYS[key_to_hex(key)]["colour"] = 0
    return update_key_colours()


def get_key_combination(pressed_key):
    for key in range(NUM_PADS):
        if (pressed_key >> key) & 0x01:
            if get_key_colour(key_to_hex(key)) == max(COLOURS.keys()):
                KEYS[key_to_hex(key)]["colour"] = 0
            else:
                KEYS[key_to_hex(key)]["colour"] = get_key_colour(key_to_hex(key)) + 1


def correct_combination():
    for _ in range(3):
        for key in range(NUM_PADS):
            KEYS[key_to_hex(key)]["colour"] = 4
        update_key_colours()
        time.sleep(0.2)
        reset_key_colours()
        time.sleep(0.2)


def start_pattern():
    pattern_keys = [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10, 9]
    for key in pattern_keys:
        update_key_colour(key, 1)
        time.sleep(0.1)
        update_key_colour(key, 0)
    for colour in range(1, len(COLOURS)):
        r, g, b = COLOURS[colour]
        for key in range(NUM_PADS):
            kp.illuminate(key, r, g, b)
        kp.update()
        time.sleep(0.2)
    for x in range(9, -1, -1):
        kp.set_brightness(x/10)
        kp.update()
        time.sleep(0.05)


def wave_pattern():
    diagonals = {"outer": [0, 1, 2, 3, 4, 7, 8, 11, 12, 13, 14, 15],
                 "inner": [5, 6, 9, 10]}
    for _ in range(3):
        for colour in range(2, len(COLOURS)):
            for key in diagonals["inner"]:
                update_key_colour(key, colour)
            time.sleep(0.1)
            for key in diagonals["outer"]:
                update_key_colour(key, colour - 1)
            time.sleep(0.1)


def wave_brightness():
    for x in range(10, -1, -1):
        kp.set_brightness(x/10)
        time.sleep(0.1)


def flash_keys(colour, times):
    for _ in range(times):
        for key in range(NUM_PADS):
            update_key_colour(key, colour)
        time.sleep(0.5)
        reset_key_colours()


def adjust_brightness(brightness, brightness_direction):
    if brightness == 0 or brightness == 10:
        brightness_direction *= -1
    brightness += (1 * brightness_direction)
    kp.set_brightness(brightness/10)
    kp.update()
    return brightness, brightness_direction


def set_passcode():
    print("On the keypad, enter a 4-key combination passcode: ")
    last_key = 0
    iteration = 0
    passcode = [0, 0, 0, 0]
    while iteration < 4:
        current_key = kp.get_button_states()
        if last_key != current_key:
            last_key = current_key
            if current_key > 0:
                passcode[iteration] = current_key
                iteration += 1
    reset_key_colours()
    return passcode


def take_input(last_pressed_key, combination, passcode):
    iteration = 0
    while True:
        # Get button states
        pressed_key = kp.get_button_states()
        # If any button is pressed
        if pressed_key > 0 and (pressed_key != last_pressed_key):
            last_pressed_key = pressed_key
            if iteration == 4:
                iteration = 0
                combination = [0, 0, 0, 0]  # type: ignore
            combination[iteration] = pressed_key  # type: ignore
            iteration += 1
            if pressed_key == 32769:
                reset_key_colours()
                combination = [0, 0, 0, 0]
                iteration = 0
                continue
            get_key_combination(pressed_key)
            update_key_colours()
            if combination == passcode:
                correct_combination()
        # brightness, brightness_direction = adjust_brightness(brightness, brightness_direction)
        time.sleep(0.1)


def kp_actions(action):
    if action == 0:
        wave_pattern()
        reset_key_colours()
    if action == 1:
        start_pattern()
        reset_key_colours()
    if action == 2:
        pass
