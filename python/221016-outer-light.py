''' 外接4个LED灯 '''
from machine import Pin
import random
import time
LED1 = Pin(18,Pin.OUT)
LED2 = Pin(21,Pin.OUT)
LED3 = Pin(23,Pin.OUT)
LED4 = Pin(16,Pin.OUT)
LED  = [LED1, LED2, LED3, LED4]
KEY1 = Pin(35,Pin.IN)
KEY2 = Pin(34,Pin.IN)

for i in LED: i.value(1)
time.sleep(0.5)
for i in LED: i.value(0)

while True:
    if KEY1.value()==0:
        while KEY1.value()==0:
            pass
        last=0
        while KEY1.value()==1:
            LED[last].value(0)
            nxt = random.randint(0,3)
            LED[nxt].value(1)
            last=nxt
            time.sleep_ms(70)
        while KEY1.value()==0:
            pass
        for i in LED: i.value(0)
        LED[last].value(1)