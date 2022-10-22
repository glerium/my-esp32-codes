# 通过光感控制LED亮度
from machine import Pin,ADC,PWM
import time
adc = ADC(Pin(14))
pwm = PWM(Pin(32,Pin.OUT))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)
pwm.freq(100000)
while True:
    val = adc.read()
    print('{:.1f}'.format(val*1.4))
    pwm.duty(int(min(val*1.4,1023)))
    time.sleep_ms(10)