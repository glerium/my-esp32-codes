''' LED呼吸灯，手动模拟PWM调节亮度 '''
from machine import Pin
import time
LEDR = Pin(33,Pin.OUT)
LEDG = Pin(32,Pin.OUT)
LEDR.value(1)
LEDG.value(1)
while True:
    for i in range(500):
        LEDR.value(0)
        time.sleep_us(i)
        LEDR.value(1)
        time.sleep_us(1000-i)
    for i in range(501,0,-1):
        LEDR.value(0)
        time.sleep_us(i)
        LEDR.value(1)
        time.sleep_us(1000-i)