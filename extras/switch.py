import time
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.switch:
        for i in range(0,5):
            cpx.pixels[i]=(0,10,0)
        for i in range(5,10):
            cpx.pixels[i]=(0,0,0)
    else:
        for i in range(0,5):
            cpx.pixels[i]=(0,0,0)
        for i in range(5,10):
            cpx.pixels[i]=(10,0,0)