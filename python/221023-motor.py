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