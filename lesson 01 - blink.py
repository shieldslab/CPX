from adafruit_circuitplayground.express import cpx
from time import sleep

delay = 0.2

while True:
    cpx.red_led = True
    sleep(delay)
    cpx.red_led = False
    sleep(delay)