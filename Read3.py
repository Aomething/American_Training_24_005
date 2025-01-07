#!/usr/bin/env python

import RPi.GPIO as GPIO
import threading
import func_timeout
from func_timeout import func_timeout, FunctionTimedOut

from mfrc522 import BasicMFRC522
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

STAR_PIN = 27
CIRCLE_PIN = 22
TRIANGLE_PIN = 13
SQUARE_PIN = 12

GPIO.setup(STAR_PIN, GPIO.OUT) # STAR RESET 
GPIO.setup(CIRCLE_PIN, GPIO.OUT) # CIRCLE RESET 
GPIO.setup(TRIANGLE_PIN, GPIO.OUT) # TRIANGLE RESET
GPIO.setup(SQUARE_PIN, GPIO.OUT) # SQUARE RESET

GPIO.output(STAR_PIN, GPIO.LOW)
GPIO.output(CIRCLE_PIN, GPIO.LOW)
GPIO.output(TRIANGLE_PIN, GPIO.LOW)
GPIO.output(SQUARE_PIN, GPIO.LOW)

starSlot = 0
circleSlot = 0
squareSlot = 0
triangleSlot = 0

def scan_star():
	global starSlot
	id = 0
	for i in range(0,5):
		GPIO.output(STAR_PIN, GPIO.HIGH)
		GPIO.output(CIRCLE_PIN, GPIO.LOW)
		GPIO.output(TRIANGLE_PIN, GPIO.LOW)
		GPIO.output(SQUARE_PIN, GPIO.LOW)
		time.sleep(0.1)
		reader1 = BasicMFRC522()
		print("Thread 1 running")
		try:
			id = reader1.read_id_no_block()
			if id:
				print("STAR ID: ",id)
				starSlot = id
				GPIO.output(STAR_PIN, GPIO.LOW)
				return
		except Exception as e:
			print("Error scanning star")
			return
		#time.sleep(0.1)
	starSlot = 0
	GPIO.output(STAR_PIN, GPIO.LOW)
	return

def scan_circle():
	global circleSlot
	id = 0
	for i in range(0,5):
		GPIO.output(STAR_PIN, GPIO.LOW)
		GPIO.output(CIRCLE_PIN, GPIO.HIGH)
		GPIO.output(TRIANGLE_PIN, GPIO.LOW)
		GPIO.output(SQUARE_PIN, GPIO.LOW)
		time.sleep(0.1)
		reader1 = BasicMFRC522()
		print("Thread 2 running")
		try:
			id = reader1.read_id_no_block()
			if id:
				print("CIRCLE ID: ",id)
				circleSlot = id
				GPIO.output(CIRCLE_PIN, GPIO.LOW)
				return
		except Exception as e:
			print("Error scanning circle")
			return
		#time.sleep(0.1)
	circleSlot = 0
	GPIO.output(CIRCLE_PIN, GPIO.LOW)
	return

def scan_triangle():
	global triangleSlot
	id = 0
	for i in range(0,5):
		GPIO.output(STAR_PIN, GPIO.LOW)
		GPIO.output(CIRCLE_PIN, GPIO.LOW)
		GPIO.output(TRIANGLE_PIN, GPIO.HIGH)
		GPIO.output(SQUARE_PIN, GPIO.LOW)
		time.sleep(0.1)
		reader1 = BasicMFRC522()
		print("Thread 3 running")
		try:
			id = reader1.read_id_no_block()
			if id:
				print("TRIANGLE ID: ",id)
				triangleSlot = id
				GPIO.output(TRIANGLE_PIN, GPIO.LOW)
				return
		except Exception as e:
			print("Error scanning triangle")
			return
		#time.sleep(0.1)
	triangleSlot = 0
	GPIO.output(TRIANGLE_PIN, GPIO.LOW)
	return

def scan_square():
	global squareSlot
	id = 0
	time.sleep(0.1)
	for i in range(0,5):
		GPIO.output(STAR_PIN, GPIO.LOW)
		GPIO.output(CIRCLE_PIN, GPIO.LOW)
		GPIO.output(TRIANGLE_PIN, GPIO.LOW)
		GPIO.output(SQUARE_PIN, GPIO.HIGH)
		time.sleep(0.1)
		reader1 = BasicMFRC522()
		print("Thread 4 running")
		try:
			id = reader1.read_id_no_block()
			if id:
				print("SQUARE ID: ",id)
				squareSlot = id
				GPIO.output(SQUARE_PIN, GPIO.LOW)
				return
		except Exception as e:
			print("Error scanning square")
			return
		time.sleep(0.1)
	squareSlot = 0
	GPIO.output(SQUARE_PIN, GPIO.LOW)
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

	#text = input("Activate Scanner 1")

	try:
		returnVal1 = func_timeout(1, scan_star)
	except FunctionTimedOut:
		print("scan_star() terminated\n")

	#text = input("Activate Scanner 2")
	time.sleep(0.25)
	try:
		returnVal2 = func_timeout(1, scan_circle)
	except FunctionTimedOut:
		print("scan_circle() terminated\n")

	#text = input("Activate Scanner 3")
	time.sleep(0.25)
	try:
		returnVal3 = func_timeout(1, scan_triangle)
	except FunctionTimedOut:
		print("scan_triangle() terminated\n")

	#text = input("Activate Scanner 4")
	time.sleep(0.25)
	try:
		returnVal4 = func_timeout(1, scan_square)
	except FunctionTimedOut:
		print("scan_square() terminated\n")

	print("SLOT CONTAINERS: ")
	print("STAR: \t\t ", starSlot)
	print("CIRCLE: \t ", circleSlot)
	print("TRIANGLE: \t ", triangleSlot)
	print("SQUARE: \t ", squareSlot)
	
	GPIO.output(STAR_PIN, GPIO.LOW)
	GPIO.output(CIRCLE_PIN, GPIO.LOW)
	GPIO.output(TRIANGLE_PIN, GPIO.LOW)
	GPIO.output(SQUARE_PIN, GPIO.LOW)
#################################################
# MAIN

starSlot = 0
circleSlot = 0
triangleSlot = 0
squareSlot = 0

try:
	for i in range(0,2):
		full_scan()
		print("\n----------- Full Scan Complete", i+1, "-----------\n")
finally:
	GPIO.cleanup()

