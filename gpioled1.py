import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)
LED=11
GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LED,GPIO.low)
time.sleep(10)
