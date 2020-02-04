from time import sleep
from adafruit_circuitplayground.express import cpx

while True:
    # this main loop runs forever
    r = 0
    g = 0
    b = 0
    while r < 255:
        # every time a while loop runs, it checks to see if its condition
        # is still true.  this one will run 255 times
        cpx.pixels.fill((r,g,b))
        r += 1
        sleep(0.01)
    while g < 255:
        # when the above loop is done, this one will start
        cpx.pixels.fill((r,g,b))
        g += 1
        sleep(0.01)
    while b < 255:
        # then this one last
        cpx.pixels.fill((r,g,b))
        b += 1
        sleep(0.01)