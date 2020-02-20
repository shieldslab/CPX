from adafruit_circuitplayground.express import cpx
import time

myList = [0, 1, 4, 5, 8, 9]

while True:
    # a for loop can loop through a list
    for pixel in myList:
        cpx.pixels[pixel] = (10,0,0)
