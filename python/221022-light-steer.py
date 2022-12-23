''' 通过光线感应器控制LED亮度 '''
from machine import Pin,ADC,PWM
import time
adc = ADC(Pin(14))          # adc模块，用于测量光线感应器传来的电压数据
pwm = PWM(Pin(32,Pin.OUT))  # pwm模块，用来调节LED电压以控制亮度
adc.atten(ADC.ATTN_11DB)    # 设定adc模块的最大测量值（ADC.ATTN_11DB约为3.6V）
adc.width(ADC.WIDTH_10BIT)  # 设定输出时的位宽（ADC.WIDTH_10BIT指输出值在0~1023间）
pwm.freq(100000)
while True:
    val = adc.read()
    print('{:.1f}'.format(val*1.4))     # 调试语句，打印测量值
    pwm.duty(int(min(val*1.4,1023)))    # 计算得到应设定的pwm.duty值
    time.sleep_ms(10)