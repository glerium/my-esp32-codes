from machine import Pin
import time

gpio    = [19,5,12,16,23,17,21,22]
numbers = [[1,2,3,5,6,7],[3,7],[2,3,4,5,6],[2,3,4,6,7],[1,3,4,7],[1,2,4,6,7],[1,2,4,5,6,7],[2,3,7],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]
power   = [14,18]
LED = list()
POWER = list()
KEY1 = Pin(35,Pin.IN)
KEY2 = Pin(34,Pin.IN)
KEYB = Pin(0,Pin.IN)

def init() -> None:
    for i in gpio: LED.append(Pin(i,Pin.OUT))
    for i in power: POWER.append(Pin(i,Pin.OUT))
    for i in POWER: i.value(1)
    for i in LED: i.value(1)

def show(n:int) -> None:
    for i in numbers[n]:
        LED[i-1].value(0)
        
def hide(n:int) -> None:
    for i in numbers[n]:
        LED[i-1].value(1)

def show2_core(x:int, y:int, ans:bool) -> None:
    show(x)
    POWER[0].value(1)
    hide(x)
    POWER[0].value(0)
    if ans: LED[7].value(0)
    show(y)
    POWER[1].value(1)
    hide(y)
    POWER[1].value(0)
    if ans: LED[7].value(1)

def show2(x:int, y:int) -> None:
    show2_core(x,y,False)

def show2_ans(x:int, y:int) -> None:
    show2_core(x,y,True)
    
def read() -> int:
    x,y = 0,0
    show2(x,y)
    done = False
    while done == False:
        show2(x,y)
        if KEY1.value() == 0:
            while KEY1.value() == 0:
                show2(x,y)
            x=(x+1)%10
        if KEY2.value() == 0:
            while KEY2.value() == 0:
                show2(x,y)
            y=(y+1)%10
        if KEYB.value() == 0:
            while KEYB.value() == 0:
                show2(x,y)
            done = True
    return x*10+y

init()
while True:
    x,y = read(),read()
    ans = (x+y)%100
    LED[7].value(0)
    while KEYB.value() == 1:
        show2_ans(ans//10,ans%10)
    while KEYB.value() == 0:
        show2_ans(ans//10,ans%10)