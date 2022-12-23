''' 让蜂鸣器发声，手动控制蜂鸣器的振动频率（手动模拟PWM） '''

from machine import Pin
import time

def Buzz(BUZZ,freq):   # 使蜂鸣器震动，接受两个参数：BUZZ是蜂鸣器，freq是振动频率
    for i in range(200):
        BUZZ.value(0)
        time.sleep_us(int(1.0/freq*1000000))
        BUZZ.value(1)
        time.sleep_us(int(1.0/freq*1000000))

LEDG = Pin(32,Pin.OUT)
LEDR = Pin(33,Pin.OUT)
KEY1 = Pin(35,Pin.IN)
BOOT = Pin(0,Pin.IN)
BUZZ = Pin(25,Pin.OUT)
freq=[0,1046,1175,1318,1397,1568,1760,1976]  # 每个音符对应的频率
song_freq=[1,1,5,5,6,6,5,5,4,4,3,3,2,2,1]        # 歌曲
for i in song_freq:
    if i:
        Buzz(BUZZ,freq[i])
    time.sleep_ms(100)