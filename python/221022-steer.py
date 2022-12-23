''' 借助PWM模块操纵舵机
    效果：舵机在两个角度之间来回旋转
    原理：当电压频率为50Hz时，占空比（平均电压）的不同可以改变舵机旋转的角度
'''
from machine import Pin,PWM
import time
key = Pin(35,Pin.IN)
pwm = PWM(Pin(15,Pin.OUT))
pwm.freq(50)    # 设定pwm模块的频率（舵机必须采用50Hz）
# pwm.duty(67)
while True:
    pwm.duty(20)  # 控制15号引脚的占空比以控制舵机旋转的角度
    time.sleep(1)
    pwm.duty(128)
    time.sleep(1)