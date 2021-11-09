import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

GPIO.setmode(GPIO.BOARD)

def main():
    green = 10
    blue = 12
    GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(blue, GPIO.LOW)
        with canvas(virtual) as draw:
            text(draw, (0, 1), '2', fill="white", font=proportional(CP437_FONT))
           

            sleep(2)
            
        GPIO.output(blue, GPIO.HIGH)

        with canvas(virtual) as draw:
            text(draw, (0, 1), '1', fill="white", font=proportional(CP437_FONT))
            
            
            sleep(2)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
