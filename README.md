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

Clone repository, enter your wifi ssid & password in [example_secrets.py](/example_secrets.py) then rename to 'secrets.py'.

Connect Pico W and upload project to the device.

Run with the Pico (W) Console and the wifi connection will be attempted. If successful the pico ip address will be displayed in the console and you will be able to send requests to it in the format `http://xxx.xxx.xxx.xxx/parameter` using the ip address and a parameter from the list below.

#### Valid parameters
|Parameter | Action |
|----------|--------|
| /light/on | Turns on the board led |
| /light/off | Turns off the board led |
| /keypad/action/0 | Illuminates keys on the keypad in a pattern |
| /keypad/action/1 | Flashes all keys on keypad red 3 times |
| /keypad/action/2 | Flashes all keys on keypad green 3 times |
| /keypad/action/3 | Illuminates keys on the keypad in a wave pattern |

#### Adding more parameters
- Add the parameter as a key in `REQUESTS` dict in [api_handler.py](/app/api_handler.py)
- Add the function to be performed as a value to that key in the format `[function, function_params]`
- Implement the function in the appropriate file. For example for a request that does something with the keypad add it to [keypad_functions.py](/app/keypad_functions.py)

## Current progress

- Pico W can establish a wifi connection
- Pico W can handle an HTTP request from a client
- Pico W can perform an action based on the nature of that request

## Future improvements

- Need to handle sending entered key combinations from keypad
- Implement validation of sent combination
- Better handling of request & response params
