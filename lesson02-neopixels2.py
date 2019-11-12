from adafruit_circuitplayground.express import cpx
from time import sleep

delay = 0.5

red = (255,0,0)
grn = (0,255,0)
blu = (0,0,255)
wht = (255,255,255)
yel = (255,255,0)
cyn = (0,255,255)
mag = (255,0,255)
off = (0,0,0)

while True:
    print("red")
    cpx.pixels.fill(red)
    sleep(delay)
    print("green")
    cpx.pixels.fill(grn)
    sleep(delay)
    print("blue")
    cpx.pixels.fill(blu)
    sleep(delay)
    print("white")
    cpx.pixels.fill(wht)
    sleep(delay)
    print("yellow")
    cpx.pixels.fill(yel)
    sleep(delay)
    print("cyan")
    cpx.pixels.fill(cyn)
    sleep(delay)
    print("magenta")
    cpx.pixels.fill(mag)
    sleep(delay)
    print("off")
    cpx.pixels.fill(off)
    sleep(delay)