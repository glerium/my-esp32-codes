from machine import Pin
import time
LED_G = Pin(32,Pin.OUT)
LED_R = Pin(33,Pin.OUT)
KEY1  = Pin(34,Pin.IN)
KEY2  = Pin(35,Pin.IN)
LED_R.value(1)
LED_G.value(1)
red   = 1
green = 1
while True:
    if KEY1.value() == 0:
        while KEY1.value() == 0:
            pass
        if red:
            LED_G.value(0)
        else:
            LED_G.value(1)
        red = 1 - red
    if KEY2.value() == 0:
        while KEY2.value() == 0:
            pass
        if green:
            LED_R.value(0)
        else:
            LED_R.value(1)
        green = 1 - green