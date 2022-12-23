''' 使用面包板外接按钮，对应22号GPIO引脚 '''
from machine import Pin
import time
BUZZ = Pin(25,Pin.OUT)
BTN = Pin(22,Pin.IN,Pin.PULL_UP)
while True:
    if BTN.value() == 0:
        for i in range(5):
            BUZZ.value(0)
            time.sleep_us(800)
            BUZZ.value(1)
            time.sleep_us(800)