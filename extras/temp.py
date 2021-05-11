import time
from adafruit_circuitplayground.express import cpx

while True:
    # just so we know it's working
    cpx.pixels.fill((0,10,0))
    print("Temperature C:", cpx.temperature)
    # convert to Fahrenheit
    print("Temperature F:", cpx.temperature * 1.8 + 32)
    time.sleep(1)