from adafruit_circuitplayground.express import cpx
from time import sleep

while True:
    if cpx.button_a:
        print("You pressed button A")
        # make the first 5 leds red and the rest green
        for i in range(0,5):
            cpx.pixels[i] = (100,0,0)
        for i in range(5,10):
            cpx.pixels[i] = (0,100,0)
    if cpx.button_b:
        print("You pressed button B")
        # make the first 5 leds green and the rest red
        for i in range(0,5):
            cpx.pixels[i] = (0,100,0)
        for i in range(5,10):
            cpx.pixels[i] = (100,0,0)