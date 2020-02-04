from time import sleep
from adafruit_circuitplayground.express import cpx

running = True

# the while loop will loop while whatever comes after the
# while keyword is true

while running:
    cpx.pixels.fill((100,0,0))
    if cpx.button_a or cpx.button_b:
        # this will make the while loop stop
        running = False