# 手势检测（光感+红外线感应联动检测）
from machine import Pin,ADC,PWM,Timer
import time
sensor1 = Pin(18,Pin.IN)    # default: 0
sensor2 = Pin(14,Pin.IN)    # default: 1
LED1 = Pin(32,Pin.OUT)
LED2 = Pin(33,Pin.OUT)
covered1 = covered2 = False
time1 = time2 = time.ticks_ms()
LED1.value(1)
LED2.value(1)

def led1_off(tim):
    global LED1
    LED1.value(1)
def led2_off(tim):
    global LED2
    LED2.value(1)

while True:
    val1 = sensor1.value()
    val2 = sensor2.value()
#     print('{:d} {:d}'.format(val1,val2))
    if val1 != 1:
        if covered2:
            LED2.value(0)
            covered1 = covered2 = False
            print('left')
            tim0 = Timer(0)
            tim0.init(period=300, mode=Timer.ONE_SHOT, callback=led2_off)
        else:
            covered1 = True
            time1 = time.ticks_ms()
    if val2 != 0:
        if covered1:
            LED1.value(0)
            covered1 = covered2 = False
            print('right')
            tim1 = Timer(1)
            tim1.init(period=300, mode=Timer.ONE_SHOT, callback=led1_off)
        else:
            covered2 = True
            time2 = time.ticks_ms()
    if time.ticks_diff(time.ticks_ms(),time1) >= 300:
        covered1 = False
    if time.ticks_diff(time.ticks_ms(),time2) >= 300:
        covered2 = False
    time.sleep_ms(10)