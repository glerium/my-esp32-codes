''' 借助PWM模块驱动电机
    效果：电机先从快到慢再从慢到快，不断循环
    原理：占空比的不同可以改变电机旋转的速度，不断改变pwm.duty即可达到效果
'''
from machine import Pin,PWM
import time
pwm1 = PWM(Pin(26,Pin.OUT))
pwm2 = PWM(Pin(27,Pin.OUT))
pwm1.freq(50)
pwm2.freq(50)
for cnt in range(10):
    for i in range(0,1024,128):
        pwm1.duty(i)
        pwm2.duty(1023-i)
        time.sleep(0.3)
    for i in range(1023,-1,128):
        pwm1.duty(i)
        pwm2.duty(1023-i)
        time.sleep(0.3)