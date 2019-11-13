from adafruit_circuitplayground.express import cpx
from time import sleep

# this code reads from 4 different sensors on the CPX:
# 1) switch - True or False
# 2) accelerometer - returns a tuple of three values
# 3) light sensor - returns a value, typically between 0 and 300
# 4) temperature sensor - in Celsius
# it also calls the shake() function and reads the tapped property,
# both of which really just use the accelerometer
# shake() returns True or False, but it's a function because it accepts a a property, shake_threshold

while True:
    if cpx.switch:
        cpx.detect_taps = 2
        cpx.pixels[0] = (100,0,0)
        cpx.pixels[1] = (100,0,0)
    else
        cpx.detect_taps = 1
        cpx.pixels[0] = (100,0,0)
        cpx.pixels[1] = (0,0,0)

    if cpx.tapped:
        print("tapped")

    if cpx.shake():
        print("shake")

    if cpx.shake(shake_threshold=20):
    # default is 30; mininum is 10; over 40 is hard to detect
        print("small shake")

    # typical range is 0 to 300ish
    print(cpx.light)

    x, y, z = cpx.acceleration
    print(x)
    print(y)
    print(z)

    print(cpx.temperature)

    sleep(0.05)
