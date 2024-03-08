import math
from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(545, 2550)
kit.servo[0].angle = 0
kit.servo[1].set_pulse_width_range(475, 2220)
kit.servo[1].angle = 0

while True:
    sleep(2)
    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    sleep(2)
    kit.servo[0].angle = 180
    kit.servo[1].angle = 180

#while True:
    #for i in range(360):
        #kit.servo[0].angle = 180*(abs(math.sin(math.radians(i))))
        #print(180*(abs(math.sin(math.radians(i)/2))))
        #sleep(0.01)
        #kit.servo[1].angle = 180*(abs(math.sin(math.radians(i))))
        #print(180*(abs(math.sin(math.radians(i)/2))))
        #sleep(0.01)