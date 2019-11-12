from adafruit_circuitplayground.express import cpx
from time import sleep

# the easy way to do touch with a CPX is just to call cpx.touch_A1, cpx.touch_A2, etc.
# you can also use the board and touchio modules
from touchio import TouchIn
import board

pinArray = [TouchIn(board.A1), TouchIn(board.A2), TouchIn(board.A3), TouchIn(board.A4), TouchIn(board.A5), TouchIn(board.A6), TouchIn(board.A7)]
# these are the NeoPixels closest to teach touch pin
pixArray = [6,8,9,1,2,3,4]

while True:
    noTouch = True
    for num, pin in enumerate(pinArray):
        if pin.value:
            # if a pin is touched, num will be the index in the pinArray
            print(num)
            cpx.start_tone(220*num)
            noTouch = False # a pin was touched
            cpx.pixels[pixArray[num]] = (100,0,0)
    if noTouch:
        # if no pin is touched, no sound and no light
        cpx.pixels.fill((0,0,0))
        cpx.stop_tone()
    sleep(.1)