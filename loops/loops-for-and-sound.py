from adafruit_circuitplayground.express import cpx
import time

while True:
    # this is pretty much the range of human hearing
    for tone in range(20, 20000, 100):
        cpx.start_tone(tone)
        print(tone)
        time.sleep(.1)
        cpx.stop_tone()
