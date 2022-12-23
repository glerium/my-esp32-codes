''' LED灯和按钮的综合应用——模拟抢答器
    KEY1(35)、KEY2(34)：两位选手；BOOT(0)：清空状态
'''
from machine import Pin
import time

def Buzz(BUZZ):   # 选手按下按钮后调用蜂鸣器(BUZZ)
    for i in range(500):
        BUZZ.value(0)
        time.sleep_us(631)
        BUZZ.value(1)

LEDG = Pin(32,Pin.OUT)
LEDR = Pin(33,Pin.OUT)
KEY2  = Pin(34,Pin.IN)
KEY1  = Pin(35,Pin.IN)
BOOT  = Pin(0,Pin.IN)
BUZZ  = Pin(25,Pin.OUT)
LEDG.value(1)
LEDR.value(1)
light = False
while True:
    if KEY1.value()==0:
        if light == True:
            continue
        cnt=0
        for i in range(1000):    #防断触
            if KEY1.value()==0:
                cnt+=1
        if cnt>=800:
            LEDR.value(0)
            light = True
            Buzz(BUZZ)
    if KEY2.value()==0:
        if light == True:
            continue
        cnt=0
        for i in range(1000):    #防断触
            if KEY2.value()==0:
                cnt+=1
        if cnt>=800:
            LEDG.value(0)
            light = True
            Buzz(BUZZ)
    if BOOT.value()==0:
        cnt=0
        for i in range(1000):    #防断触
            if BOOT.value()==0:
                cnt+=1
        if cnt>=800:
            LEDR.value(1)
            LEDG.value(1)
            light = False