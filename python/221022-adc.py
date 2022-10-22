from machine import Pin,ADC
import time
LED = Pin(32,Pin.OUT)
LED.value(1)

adc = ADC(Pin(14))
adc.atten(ADC.ATTN_11DB)

while True:
    print(adc.read())
    time.sleep(1)
