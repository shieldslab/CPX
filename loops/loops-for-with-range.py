from adafruit_circuitplayground.express import cpx
import time

while True:
    # notice that ranges in python don't include the last number
    # this will go 0, 1, 2, 3, 4
    for pixel in range(0, 5):
        cpx.pixels[pixel] = (10,0,0)
    # this will go 5, 6, 7, 8, 9
    for pixel in range(5, 10):
        cpx.pixels[pixel] = (0,10,0)

    time.sleep(1)

    # you can include your step in a range
    # this will go 0, 2, 4, 6, 8
    for pixel in range(0, 10, 2):
        cpx.pixels[pixel] = (0,0,10)

    time.sleep(1)