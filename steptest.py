"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())

for i in range(200):
    kit.stepper2.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE)
    time.sleep(0.01)
kit.stepper2.release()