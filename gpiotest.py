import RPi.GPIO as GPIO
import time
#setup GPIO as BCM Numbering

#GPIO.setmode(GPIO.BCM)

#setup GPIO using Board Numbering

GPIO.setmode(GPIO.BOARD)

GPIO.setup(23,GPIO.IN,pull_up_down =GPIO.PUD_DOWN)

GPIO.setup(24,GPIO.IN,pull_up_down = GPIO.PUD_UP)
	
	while True:
		try:
			if(GPIO.input(23) ==1):
				print("Button 1 pressed")
				time.sleep(0.2)
			if(GPIO.input(24) == 0):
				print("Button 2 pressed")
				time.sleep(0.2)
		except KeyboardInterrupt:
			print("Program Terminated")
		finally:
			GPIO.cleanup()