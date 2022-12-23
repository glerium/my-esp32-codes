''' 效果类似221016-button-number-led.py这份代码，但这次外接了两个LED数码管，范围变为00-99循环 '''
from machine import Pin
import time

gpio    = [19,5,12,16,23,17,21,22]
numbers = [[1,2,3,5,6,7],[3,7],[2,3,4,5,6],[2,3,4,6,7],[1,3,4,7],[1,2,4,6,7],[1,2,4,5,6,7],[2,3,7],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]
power   = [14,18]
LED = list()
POWER = list()

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

def show2(n:int, tim:int) -> None:
    ''' 循环显示两个数字
        参数含义：n：需要显示的数字（范围0-99）
                 tim：需要显示的时间（以毫秒为单位）
    '''
    cycle = 5
    x,y = n//10, n%10
    for i in range(tim//cycle):
        show(x)
        POWER[0].value(1)
        hide(x)
        POWER[0].value(0)
        show(y)
        POWER[1].value(1)
        hide(y)
        POWER[1].value(0)
        time.sleep_ms(cycle)

init()
ima = 0
show2(ima,1000)
while True:
    ima = (ima + 1) % 100
    show2(ima, 1000)