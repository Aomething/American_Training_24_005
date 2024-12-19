#!/usr/bin/env python

import RPi.GPIO as GPIO
import threading
import func_timeout
from func_timeout import func_timeout, FunctionTimedOut

#from mfrc522 import MFRC522
from mfrc522 import BasicMFRC522
import time

GPIO.setwarnings(False)

#GPIO SETUP

GPIO.setmode(GPIO.BCM)

#GPIO.setup(5, GPIO.OUT) # RFID RESET
GPIO.setup(27, GPIO.OUT) # DEMUX RFID MSB
GPIO.setup(22, GPIO.OUT) # DEMUX RFID LSB

# example format
# GPIO.setup(pin. GPIO.OUT | GPIO.IN)
# GPIO.output(pin, GPIO.HIGH | GPIO.LOW)

#INITIALIZATION

#GPIO.output(27, GPIO.LOW)
#GPIO.output(22, GPIO.LOW)

reader1 = BasicMFRC522()

starSlot = 0
circleSlot = 0
squareSlot = 0
triangleSlot = 0

def scan_star():
	global starSlot
	id = 0
	for i in range(0,10):
		GPIO.output(22, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		print("Thread 1 running")
		#try:
		id = reader1.read_id_no_block()
		if id:
			print("STAR ID: ",id)
			starSlot = id
			return
		#except Exception as e:
		#	print("Error scanning")
		#	return
		#time.sleep(0.1)
	starSlot = 0
	return

def scan_circle():
	global circleSlot
	id = 0
	for i in range(0,10):
		GPIO.output(22, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		print("Thread 2 running")
		#try:
		id = reader1.read_id_no_block()
		if id:
			print("CIRCLE ID: ",id)
			circleSlot = id
			return
		#except Exception as e:
		#	print("Error scanning")
		#	return
		#time.sleep(0.1)
	circleSlot = 0
	return

def scan_triangle():
	global triangleSlot
	id = 0
	for i in range(0,10):
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(27, GPIO.LOW)
		print("Thread 3 running")
		#try:
		id = reader1.read_id_no_block()
		if id:
			print("TRIANGLE ID: ",id)
			triangleSlot = id
			return
		#except Exception as e:
		#	print("Error scanning")
		#	return
		#time.sleep(0.1)
	triangleSlot = 0
	return

def scan_square():
	global squareSlot
	id = 0
	for i in range(0,10):
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		print("Thread 4 running")
		#try:
		id = reader1.read_id_no_block()
		if id:
			print("SQUARE ID: ",id)
			squareSlot = id
			return
		#except Exception as e:
		#	print("Error scanning")
		#	return
		time.sleep(0.1)
	squareSlot = 0
	return

#MAIN BODY

def full_scan():
	global starSlot
	global circleSlot
	global triangleSlot
	global squareSlot
	
	#starSlot = 0
	#circleSlot = 0
	#triangleSlot = 0
	#squareSlot = 0

	try:
		returnVal1 = func_timeout(0.75, scan_star)
	except FunctionTimedOut:
		print("scan_star() could terminated\n")
	
	try:
		returnVal2 = func_timeout(0.75, scan_circle)
	except FunctionTimedOut:
		print("scan_circle() terminated\n")
	
	try:
		returnVal3 = func_timeout(0.75, scan_triangle)
	except FunctionTimedOut:
		print("scan_triangle() terminated\n")
	
	try:
		returnVal4 = func_timeout(0.75, scan_square)
	except FunctionTimedOut:
		print("scan_square() terminated\n")


	print("SLOT CONTAINERS: ")
	print("STAR: \t\t ", starSlot)
	print("CIRCLE: \t ", circleSlot)
	print("TRIANGLE: \t ", triangleSlot)
	print("SQUARE: \t ", squareSlot)
#################################################
# MAIN

starSlot = 0
circleSlot = 0
triangleSlot = 0
squareSlot = 0

try:
	for i in range(0,3):
		full_scan()
		print("\n----------- Full Scan Complete", i+1, "-----------\n")
		time.sleep(0.1)
finally:
	GPIO.cleanup()

