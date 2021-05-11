import time
import math
from adafruit_circuitplayground.express import cpx

while True:
    x,y,z = cpx.acceleration
    if x != 0:
        # yay trig!
        angle = math.atan(y/x)
    # get the quadrant right
    if x > 0:
        angle = math.degrees(angle)+90
    elif x < 0:
        angle = math.degrees(angle)+270
    print(angle)
    led = int(angle/36)
    cpx.pixels.fill((0,0,0))
    cpx.pixels[led] = (0,10,0)
    time.sleep(.1)