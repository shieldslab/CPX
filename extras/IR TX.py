# transmitter

import time
from adafruit_circuitplayground.express import cpx
import adafruit_irremote
import pulseio
import pwmio
import board

pwm = pwmio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)

# the encoder defines how we will send bytes of data (1s and 0s)
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550], zero=[550, 1700], trail=0)

cpx.pixels.fill((0,0,10))

while True:
    if cpx.button_a:
        print("Button A pressed!")
        cpx.red_led = True
        encoder.transmit(pulseout, [255])
        cpx.red_led = False
        cpx.pixels.fill((10,0,0))
        time.sleep(0.2)
    if cpx.button_b:
        print("Button B pressed!")
        cpx.red_led = True
        encoder.transmit(pulseout, [1])
        cpx.red_led = False
        cpx.pixels.fill((0,10,0))
        time.sleep(0.2)