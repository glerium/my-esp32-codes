from machine import Pin
import time
LED_G = Pin(32,Pin.OUT)
LED_R = Pin(33,Pin.OUT)
light = [0,0,0,1,1,1,0,0,0]
while True:
    for i in light:
        LED_R.value(0)
        LED_G.value(0)
        time.sleep(0.3 if not i else 0.7)
        LED_R.value(1)
        LED_G.value(1)
        time.sleep(0.5)
    time.sleep(1.5)
