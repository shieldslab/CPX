from time import sleep
from adafruit_circuitplayground.express import cpx

# while True runs forever

while True:
    cpx.pixels.fill((100,0,0))
    while cpx.button_a or cpx.button_b:
        # the program gets stuck in this loop
        # while a button is pressed
        cpx.pixels.fill((0,100,0))