## Pico Wireless RGB KeyPad Device

### About

Using a Raspberry Pi Pico W to make a 'secure door access system' for a uni coursework project.
Project is using code from [pimoroni's RGB KeyPad example](https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_rgb_keypad/demo.py), and [raspberrypi's wireless example in pico-micropython-examples](https://github.com/raspberrypi/pico-micropython-examples/blob/master/wireless/webserver.py).

### Project definition

- Pico W will handle user input and send entered code over a wifi connection to a second device
- Second device will handle the request from pico and validate code
- Second device will send either authorised, unauthorised, or invalid request response to Pico W
- Pico W will illuminate keys in a pattern to signal the received response

### Current progress

- Pico W can establish a wifi connection
- Pico W can handle an HTTP request from a client
- Pico W can perform an action based on the nature of that request

### Current issues

- When multiple requests are received processes on the pico don't appear to be starting and finishing correctly

