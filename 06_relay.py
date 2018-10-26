#!/usr/bin/env python

#-----------------------------------------------------------
# File name   : 06_relay.py
# Description : Toggle a relay.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import RPi.GPIO as GPIO
import time

RELAY_PIN = 12    # pin12

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
	GPIO.setup(RELAY_PIN, GPIO.OUT)   # Set pin mode as output
	GPIO.output(RELAY_PIN, GPIO.HIGH)

def loop():
	while True:
		print ('...clsoe')
		GPIO.output(RELAY_PIN, GPIO.LOW)
		time.sleep(1)
		print ('open...')
		GPIO.output(RELAY_PIN, GPIO.HIGH)
		time.sleep(1)

def destroy():
	GPIO.output(RELAY_PIN, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

