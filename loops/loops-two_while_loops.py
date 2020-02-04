from time import sleep
from adafruit_circuitplayground.express import cpx

# this main while loop will run forever
while True:
    print("starting")
    count = 0
    # this while loop will loop while count is less than 10
    while count < 10:
        sleep(.5)
        cpx.pixels[count] = (100,0,0)
        count += 1
    cpx.pixels.fill((0,0,0))