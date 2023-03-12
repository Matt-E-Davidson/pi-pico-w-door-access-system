from machine import Pin


def set_led(val):
    Pin('WL_GPIO0', Pin.OUT).value(val)
