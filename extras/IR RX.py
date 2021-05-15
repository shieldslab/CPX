# receiver

import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx
import time
import math

pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

cpx.pixels.fill((10,10,0))

# this is the ideal array for 255.  one header pair, 8 ones, then a trailing zero.
p = [9500, 4500, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 550, 0]

while True:
    # read the pulses
    pulses = decoder.read_pulses(pulsein)
    print(pulses)
    s = 0
    # if the read series of pulses is kinda close (the sum of the differenes is less than 9000),
    # then it's probably a A button.  else, it's an B button
    for i,val in enumerate(pulses):
        if i < len(p):
            s += abs(val-p[i])
    if s < 9000:
        print("received A")
        cpx.pixels.fill((10,0,0))
    else:
        print("received B")
        cpx.pixels.fill((0,10,0))
    time.sleep(.05)