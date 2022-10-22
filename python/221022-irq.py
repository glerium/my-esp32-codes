from machine import Pin
import time
LED = Pin(32,Pin.OUT)
KEY = Pin(5,Pin.IN)
LED.value(1)
cnt = 0

def fallback(KEY):
    global cnt
    LED.value(0)
    cnt += 1
    print('fallback %d' % cnt)

KEY.irq(trigger=Pin.IRQ_RISING, handler=fallback)
# KEY.irq(trigger=Pin.IRQ_RISING, handler=rising)