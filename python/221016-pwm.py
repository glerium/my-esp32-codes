from machine import Pin,PWM
import time
import random
led = list()
pwm = list()
lights = [25]
random.seed(114514)
for i in lights:
    led.append(Pin(i,Pin.OUT))
    print(i)
    pwm.append(PWM(Pin(i,Pin.OUT)))
for i in pwm:
    i.freq(100000)
    i.duty(0)
while True:
    n=len(pwm)
    for i in range(n):
        for j in range(1024):
            pwm[i].duty(j)
            time.sleep_us(1000)
        for j in range(1023,-1,-1):
            pwm[i].duty(j)
            time.sleep_us(1000)