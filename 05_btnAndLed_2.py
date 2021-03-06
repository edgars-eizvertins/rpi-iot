#/usr/bin/python3


#-----------------------------------------------------------
# File name   : 05_btnAndLed_2.py
# Description : Toggle an LED by button.
# Author      : Jason
# E-mail      : jason@adeept.com
# Website     : www.adeept.com
# Date        : 2015/06/12
#-----------------------------------------------------------

import time
import RPi.GPIO as GPIO

LedPin = 11    # pin11 --- led
BtnPin = 12    # pin12 --- button

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off

def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)	
	print('led off...' if Led_status else '...led on')	
	time.sleep(0.05)

def loop():
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed) # wait for falling
	while True:
		time.sleep(0.01)		

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()



