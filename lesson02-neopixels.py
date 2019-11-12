from adafruit_circuitplayground.express import cpx
from time import sleep

delay = 0.5

while True:
    print("red")
    cpx.pixels.fill((255,0,0))
    sleep(delay)
    print("green")
    cpx.pixels.fill((0,255,0))
    sleep(delay)
    print("blue")
    cpx.pixels.fill((0,0,255))
    sleep(delay)
    print("white")
    cpx.pixels.fill((255,255,255))
    sleep(delay)
    print("yellow")
    cpx.pixels.fill((255,255,0))
    sleep(delay)
    print("cyan")
    cpx.pixels.fill((0,255,255))
    sleep(delay)
    print("magenta")
    cpx.pixels.fill((255,0,255))
    sleep(delay)
    print("off")
    cpx.pixels.fill((0,0,0))
    sleep(delay)