"""
Created by: James Couse
Created on: nov 23 2023
Module uses an ultrasonic distance sensor to detect
whether a servo should be turned or not.
"""

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)
pwm = pwmio.PWMOut(board.A0, frequency=50)
ServoNumber1 = servo.Servo(pwm)

while True:
    try:
        if sonar.distance <= 20:
            print("on")
            ServoNumber1.angle = 90
        else:
            print("off")
            ServoNumber1.angle = 0
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
