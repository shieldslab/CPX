from adafruit_circuitplayground.express import cpx
from time import sleep

while True:
    # calling touch_A1, touch_A2, etc. causes the CPX to check if it's touched
    # it will return True or False
    if cpx.touch_A1:
        cpx.start_tone(440)
        print("A1")
    # python uses elif as short for "else if"
    elif cpx.touch_A2:
        cpx.start_tone(880)
        print("A2")
    else:
        cpx.stop_tone()