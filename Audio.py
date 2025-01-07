#!/user/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT) # LSB
GPIO.setup(24, GPIO.OUT) # MSB
GPIO.setup(26, GPIO.OUT) # Enable

GPIO.output(26, GPIO.LOW)

time.sleep(1)

GPIO.output(25, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
print("WRONG COLOR")
#text = input("PIN 0")
time.sleep(2)

GPIO.output(25, GPIO.HIGH)
GPIO.output(24, GPIO.LOW)

#text = input("PIN 1")
print("WRONG SHAPE")
time.sleep(2)

GPIO.output(25, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)

#text = input("PIN 2")
print("PULL OUT THE DRAWER")
time.sleep(2)

GPIO.output(25, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

#text = input("PIN 3")
print("CORRECT")

time.sleep(2)

print("DONE!")

GPIO.output(26, GPIO.HIGH)
