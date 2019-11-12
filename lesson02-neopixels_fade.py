from adafruit_circuitplayground.express import cpx
from time import sleep

delay = 0.005

while True:
    # fade the red in
    for i in range(0,255):
        cpx.pixels.fill((i,0,0))
        sleep(delay)
    # fade the green in
    for i in range(0,255):
        cpx.pixels.fill((255,i,0))
        sleep(delay)
    # fade the blue in while the red fades out
    for i in range(0,255):
        cpx.pixels.fill((255-i,255,i))
        sleep(delay)
    # fade the blue and green out
    for i in range(0,255):
        cpx.pixels.fill((0,255-i,255-i))
        sleep(delay)