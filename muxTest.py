#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(22, GPIO.OUT) # LSB
GPIO.setup(27, GPIO.OUT) # MSB

text = input("Next MUX Address (0)")

# 0
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

text = input("Next MUX Address (1)")

# 1
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)

text = input("Next MUX Address (2)")

# 2
GPIO.output(22, GPIO.HIGH)
GPIO.output(27, GPIO.LOW)

text = input("Next MUX Address (3)")

# 3
GPIO.output(22, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)

text = input("Next MUX Address (END)")

# 0
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
