# 舵机的使用
from machine import Pin,PWM
import time
key = Pin(35,Pin.IN)
pwm = PWM(Pin(15,Pin.OUT))
pwm.freq(50)
pwm.duty(67)
# while True:
#     pwm.duty(20)
#     time.sleep(1)
#     pwm.duty(128)
#     time.sleep(1)
