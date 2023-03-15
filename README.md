# Pico Wireless RGB KeyPad Device

## About

Using a Raspberry Pi Pico W to make a 'secure door access system' for a uni coursework project.

Project is written in micropython, using code from [pimoroni's RGB KeyPad example](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_rgb_keypad/demo.py), and [raspberrypi's wireless example in pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples/blob/master/wireless/webserver.py).

## Project definition

- Pico W will handle user input and send entered code over a wifi connection to a second device
- Second device will handle the request from pico and validate code
- Second device will send either authorised, unauthorised, or invalid request response to Pico W
- Pico W will illuminate keys in a pattern to signal the received response

## Usage

### Hardware requirements

- Raspberry Pi Pico W
- Pimoroni RGB KeyPad

### Software requirements

- VS Code
- Pico-W-Go extension
- Pimoroni-picow-micropython uf2 file on pico

Connect pico to computer while holding the BOOTSEL button, drag and drop [uf2](/pimoroni-picow-v1.19.16-micropython.uf2) file onto board. (Note: I have included a version of this file in the project, but I will not be maintaining this so it would be better to check their [releases page](https://github.com/pimoroni/pimoroni-pico/releases))

Clone repository, enter your wifi ssid + password and server address in [example_secrets.py](/example_secrets.py) then rename to 'secrets.py'.

Connect Pico W and upload project to the device.

The Pico will load and if wifi connection is successful the keypad will flash green. If not the keypad will flash red and the program will not proceed. (Future work will create a way for user to re-try connection)

If the wifi connection was successful you will now be able to enter a 4 digit code on the keypad which will be sent to the server you specified. The server side will validate the code and if the code is correct the keypad will flash green, otherwise it will flash red.


## Current progress

- Pico W can establish a wifi connection
- Pico W can send an HTTP request to the server and handle response

## Future improvements

- Better handling of request & response params
