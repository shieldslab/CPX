from adafruit_circuitplayground.express import cpx
from time import sleep

# This program uses five of the CPX sensors
# 1) cpx.switch - True or False
# 2) cpx.button_b - True or False
# 3) light sensor - returns a number, typically between 0 and 300ish
# 4) accelerometer - returns tuple of three values, (x, y, z)
# 5) temperature sensor - returns Celsius
# cpx.tapped uses the accelerometer, is true or false, and uses single or double taps, based on cpx.detect_taps
# cpx.shake() uses the accelerometer to detect shaking and returns true or false
# cpx.shake() is a function because it can accept a parameter, shake_threshold

# Pixels key
# [0] - temperature (blue, yellow, or red)
# [2] - green if tapped
# [3-4] - yellow, indicating light intensity
# [5] - purple if x-acceleration is high
# [7] - btnBToggle, indicating shake threshold
# [8-9] - switch position, indicating single vs. double tap

btnBToggle = True

while True:
    # the switch determines if tap takes one or two taps, as indicated by the number of LEDs lit
    if cpx.switch:
        cpx.detect_taps = 2
        cpx.pixels[8] = (100,0,0)
        cpx.pixels[9] = (100,0,0)
    else:
        cpx.detect_taps = 1
        cpx.pixels[8] = (100,0,0)
        cpx.pixels[9] = (0,0,0)

    # tapping lights pixels[2]
    if cpx.tapped:
        cpx.pixels[2] = (0,100,0)

    # this captures just the button press, when button_b goes from false to true
    if cpx.button_b and not lastBtnB:
        btnBToggle = not btnBToggle
    lastBtnB = cpx.button_b

    # shaking turns off pixels[2]
    # btnBToggle determines how hard you need to shake
    if btnBToggle:
        cpx.pixels[7] = (0,0,100) # bright light indicates high shake threshold
        if cpx.shake():
            cpx.pixels[2] = (0,0,0)
    else:
        cpx.pixels[7] = (0,0,10) # dim light indicates low shake threshold
        if cpx.shake(shake_threshold=10):
            cpx.pixels[2] = (0,0,0)

    # light between 0 and 2 lights, based on brightness
    lights = int(cpx.light/10)
    if lights == 0:
        cpx.pixels[3] = (0,0,0)
        cpx.pixels[4] = (0,0,0)
    if lights ==1:
        cpx.pixels[3] = (0,0,0)
        cpx.pixels[4] = (10,10,0)
    if lights == 2:
        cpx.pixels[3] = (10,10,0)
        cpx.pixels[4] = (10,10,0)

    x, y, z = cpx.acceleration
    if abs(x) > 8:
        cpx.pixels[5] = (10,0,10)
    else:
        cpx.pixels[5] = (0,0,00)

    # pixels[0] is a temperature guage
    if(cpx.temperature > 25):
        cpx.pixels[0] = (10,0,0)
    elif(cpx.temperature > 24):
        cpx.pixels[0] = (10,10,0)
    else:
        cpx.pixels[0] = (0,0,10)

    sleep(0.01)
