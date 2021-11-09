import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
green = 10
blue = 12
red = 16


GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
while 1:
        GPIO.output(green, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(green, GPIO.LOW)
        time.sleep(1)
        GPIO.output(blue, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(blue, GPIO.LOW)
        time.sleep(1)
        GPIO.output(red, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(red, GPIO.LOW) 
        time.sleep(1)

if __name__=='__main__':
    main()

