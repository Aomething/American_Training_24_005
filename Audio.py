#!/user/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT) # LSB
GPIO.setup(24, GPIO.OUT) # MSB
GPIO.setup(26, GPIO.OUT) # Enable

GPIO.output(26, GPIO.LOW)

time.sleep(2)

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

text = input("PIN 0")

time.sleep(1)

GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.LOW)

text = input("PIN 1")

time.sleep(1)

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)

text = input("PIN 2")

time.sleep(1)

GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

text = input("PIN 3")

time.sleep(2)

GPIO.output(26, GPIO.HIGH)

#GPIO.output(26, GPIO.HIGH)

#GPIO.output(23, GPIO.LOW)
#GPIO.output(24, GPIO.LOW)

#######################

#time.sleep(3)

#print("MUX 0")

#GPIO.output(26, GPIO.HIGH)

#GPIO.output(23, GPIO.LOW)
#GPIO.output(24, GPIO.LOW)

#GPIO.output(26, GPIO.LOW)

######################

#time.sleep(3)

#print("MUX 1")

#GPIO.output(26, GPIO.HIGH)

#GPIO.output(23, GPIO.HIGH)
#GPIO.output(24, GPIO.LOW)

#GPIO.output(26, GPIO.LOW)

######################

#time.sleep(3)

#print("MUX 2")

#GPIO.output(26, GPIO.HIGH)

#GPIO.output(23, GPIO.LOW)
#GPIO.output(24, GPIO.HIGH)

#GPIO.output(26, GPIO.LOW)

######################

#time.sleep(3)

#print("MUX 3")

#GPIO.output(26, GPIO.HIGH)

#GPIO.output(23, GPIO.HIGH)
#GPIO.output(24, GPIO.HIGH)

#GPIO.output(26, GPIO.LOW)

######################
#time.sleep(3)

#GPIO.output(26, GPIO.HIGH)
