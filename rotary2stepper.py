# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# ignore the terrible code formatting ill fix it later

"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from adafruit_seesaw import seesaw, rotaryio, digitalio

kit = MotorKit(i2c=board.I2C())

seesaw = seesaw.Seesaw(board.I2C(), addr=0x36)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)

button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = 0
run = True

while run:
    position = -encoder.position

    if position != last_position:
        stepDirection = stepper.FORWARD if (position - last_position) > 0 else stepper.BACKWARD
        print(abs(last_position - position))
        if -13 < position < 13 and last_position < 24:
            for i in range(8*int(abs(last_position - position))):
                kit.stepper2.onestep(direction=stepDirection, style=stepper.DOUBLE)
        last_position = position

         
    if not button.value and not button_held:
        button_held = True
        print("Button pressed")

    if button.value and button_held:
        button_held = False
        kit.stepper2.release()
        run = False

