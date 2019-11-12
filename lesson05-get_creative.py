from adafruit_circuitplayground.express import cpx
from time import sleep

while True:
    if cpx.switch:
        print("switch on")

    cpx.detect_taps = 2
    if cpx.tapped:
        print("double tap")

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

