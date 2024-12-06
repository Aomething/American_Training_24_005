#!/usr/bin/env python

import RPi.GPIO as GPIO
import threading

from mfrc522 import MFRC522
from mfrc522 import BasicMFRC522
import time

GPIO.setwarnings(False)

#GPIO SETUP

GPIO.setmode(GPIO.BCM)

#GPIO.setup(5, GPIO.OUT) # RFID RESET
GPIO.setup(27, GPIO.OUT) # DEMUX RFID MSB
GPIO.setup(22, GPIO.OUT) # DEMUX RFID LSB

#GPIO.setup(23, GPIO.OUT) # DEMUX AUDIO MSB
#GPIO.setup(24, GPIO.OUT) # DEMUX AUDIO LSB
#GPIO.setup(25, GPIO.OUT) # DEMUX AUDIO ENABLE

#example
# GPIO.output(pin, GPIO.HIGH)
# GPIO.output(pin, GPIO.LOW)

#INITIALIZATION

GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
#GPIO.output(5, GPIO.LOW)

#GPIO.output(23, GPIO.LOW)
#GPIO.output(24, GPIO.LOW)
#GPIO.output(25, GPIO.HIGH)

reader = BasicMFRC522()
#reader = MFRC522()

starSlot = None
circleSlot = None
squareSlot = None
triangleSlot = None

def scanRFID_daemon(slot):
	global starSlot
	global circleSlot
	global squareSlot
	global triangleSlot


	while True:
		try:
			id = reader.read_id_no_block()
			if id:
				print("ID: ",id)
				if (slot == 0):
					starSlot = id
				elif (slot == 1):
					circleSlot = id
				elif (slot == 2):
					triangleSlot = id
				elif (slot == 3):
					squareSlot = id
				else:
					print("Error: Invalid Slot Number")

				return
		except Exception as e:
			print("Error scanning")
		time.sleep(0.1)

def mainProgram():
	print("---Main program")
	try:
		while True:
			print("simulate busy work")
			time.sleep(1)
	except KeyboardInterrupt:
		print("exiting main program")

try:
	GPIO.output(22, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	time.sleep(2)

	rfid_thread1 = threading.Thread(target=scanRFID_daemon, daemon=True, args=[0])
	print("Reading from Scanner 1")
	rfid_thread1.start()
#	print("Filler 1")
	rfid_thread1.join(timeout=5)
	print("Thread1 Returned")

	GPIO.output(22, GPIO.HIGH)
	GPIO.output(27, GPIO.LOW)
	print("changing mux...")
	time.sleep(6)

	rfid_thread2 = threading.Thread(target=scanRFID_daemon, daemon=True, args=[1])
	print("Reading from Scanner 2")
	rfid_thread2.start()
	rfid_thread2.join(timeout=5)
	print("Thread2 Returned")

	time.sleep(3)

	GPIO.output(22, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)

	print("Ending Program")

	print("Star Slot: ", starSlot)
	print("Circle Slot: ", circleSlot)
	print("Triangle Slot: ", triangleSlot)
	print("Square Slot: ", squareSlot)

finally:
	GPIO.cleanup()

