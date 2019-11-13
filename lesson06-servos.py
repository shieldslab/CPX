import time
import board
import pulseio
from adafruit_motor import servo

# I got the adafruit_motor library here: https://github.com/adafruit/Adafruit_CircuitPython_Motor/releases/

# CPX has PWM on the following pins: A1, A2, A3, A6, A8, A9
# There is NO PWM on: A0, A4, A5, A7

# create a PWMOut object on pins A2 and A3
pwm1 = pulseio.PWMOut(board.A2, duty_cycle=0, frequency=50)
pwm2 = pulseio.PWMOut(board.A3, duty_cycle=0, frequency=50)

# Create a servo object, my_servo.
servo1 = servo.Servo(pwm1)
servo2 = servo.Servo(pwm2)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo1.angle = angle
        servo2.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo1.angle = angle
        servo2.angle = angle
        time.sleep(0.05)