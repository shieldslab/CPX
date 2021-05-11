import time
import board
import pulseio
from adafruit_motor import servo

# I got the adafruit_motor library here: https://github.com/adafruit/Adafruit_CircuitPython_Motor/releases/

# CPX has PWM on the following pins: A1, A2, A3, A6, A8, A9
# There is NO PWM on: A0, A4, A5, A7

# create two PWMOut objects on pins A2 and A3
pwm1 = pulseio.PWMOut(board.A2, duty_cycle=0, frequency=50)
pwm2 = pulseio.PWMOut(board.A3, duty_cycle=0, frequency=50)

# Create two servo objects, servo1 and servo2
servo180 = servo.Servo(pwm1)
servoCont = servo.ContinuousServo(pwm2)

while True:
    for angle in range(0, 180):  # 0 - 180 degrees, 5 degrees at a time.
        servo180.angle = angle
        time.sleep(0.01)
    for angle in range(180, 0, -1): # 180 - 0 degrees, 5 degrees at a time.
        servo180.angle = angle
        time.sleep(0.01)
    for throttle in range(-100, 100, 2):
        servoCont.throttle = throttle/100
        time.sleep(0.05)
    for throttle in range(100, -100, -2):
        servoCont.throttle = throttle/100
        time.sleep(0.05)