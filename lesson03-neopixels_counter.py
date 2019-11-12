from adafruit_circuitplayground.express import cpx
from time import sleep

count = 0

while True:
    # only detect the CHANGE from false to true
    if cpx.button_a and not btnA:
        print("You pressed button A")
        cpx.pixels.fill((0,0,0))
        # turn them all off then only light up to count
        if count < 10:
            count += 1
        for i in range(0,count):
            cpx.pixels[i] = (0,100,0)
    # only detect the CHANGE from false to true
    if cpx.button_b and not btnB:
        print("You pressed button B")
        cpx.pixels.fill((0,0,0))
        # turn them all off then only light up to count
        if count > 0:
            count -= 1
        for i in range(0,count):
            cpx.pixels[i] = (0,100,0)
    btnA = cpx.button_a
    btnB = cpx.button_b
    # don't go too fast
    sleep(.01)