import usb_hid
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

while True:
    if cpx.button_a:
        kbd.send(Keycode.ALT, Keycode.A)
        while cpx.button_a: # Wait for button to be released
            pass

    if cpx.button_b:
        kbd.send(Keycode.ALT, Keycode.V)
        while cpx.button_b: # Wait for button to be released
            pass