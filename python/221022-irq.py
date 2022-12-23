''' esp32的irq中断 '''
from machine import Pin
import time
LED = Pin(32,Pin.OUT)
KEY = Pin(5,Pin.IN)
LED.value(1)
cnt = 0

def fallback(KEY):  # 回调函数
    global cnt
    LED.value(0)
    cnt += 1
    print('fallback %d' % cnt)

KEY.irq(trigger=Pin.IRQ_RISING, handler=fallback)   # 添加中断，当KEY按钮抬起时触发中断并执行fallback回调函数
# KEY.irq(trigger=Pin.IRQ_RISING, handler=rising)