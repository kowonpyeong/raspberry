import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *
from time import sleep, strftime
from datetime import datetime


from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
def main():
    mylcd = LCD.lcd()
    light=40
    tough=38
    flame=36
    Switch= 10
    led= 11
    led2=15
    
    GPIO.setup(flame, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(light, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(tough, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)
    
    while True:
        if GPIO.input(tough) == GPIO.HIGH:
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'T', fill="white", font=proportional(CP437_FONT))
            sleep(1)
                
                
        
            for i in range (10):
                GPIO.output(led, GPIO.HIGH)
                sleep(0.3)
                GPIO.output(led, GPIO.LOW)
                sleep(0.3)
            break
            
                
                
        elif GPIO.input(flame) == GPIO.HIGH:
            for i in range (10):
                GPIO.output(led, GPIO.HIGH)
                sleep(0.3)
                GPIO.output(led, GPIO.LOW)
                sleep(0.3)
            break
            
        
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'F', fill="white", font=proportional(CP437_FONT))
            sleep(1)
            
            
        elif GPIO.input(light) == GPIO.HIGH:
            
            mylcd.lcd_clear()
            mylcd.lcd_display_string("Room Light ON",1)
            
        
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'L', fill="white", font=proportional(CP437_FONT))
            sleep(1)
            
            

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
