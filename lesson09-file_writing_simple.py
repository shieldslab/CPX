import time
from adafruit_circuitplayground.express import cpx

cpx.red_led = True
# remember, switch to the LEFT for coding; RIGHT for saving data

try:
    with open("myfile.txt", "w") as myfile:
        while True:
            temp = cpx.temperature
            myfile.write(str(temp))
            myfile.flush()
            cpx.red_led = not cpx.red_led
            time.sleep(1)
            # slow blinking means it's collecting data
except:
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(.1)
        # fast blinking means there is an error