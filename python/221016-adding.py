''' 自制加法器，可以通过按键实现两位数以内加法
    需要外接八字LED数码管（引脚定义见gpio数组）
'''
from machine import Pin
import time

gpio    = [19,5,12,16,23,17,21,22]
numbers = [[1,2,3,5,6,7],[3,7],[2,3,4,5,6],[2,3,4,6,7],[1,3,4,7],[1,2,4,6,7],[1,2,4,5,6,7],[2,3,7],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]
power   = [14,18]
LED = list()      # 每个数码管对应引脚的Pin对象
POWER = list()    # 每个电源引脚的Pin对象
KEY1 = Pin(35,Pin.IN)
KEY2 = Pin(34,Pin.IN)
KEYB = Pin(0,Pin.IN)

def init() -> None:   # 内部变量的定义
    for i in gpio: LED.append(Pin(i,Pin.OUT))
    for i in power: POWER.append(Pin(i,Pin.OUT))
    for i in POWER: i.value(1)
    for i in LED: i.value(1)

def show(n:int) -> None:    # 让某数字对应的LED灯亮起
    for i in numbers[n]:
        LED[i-1].value(0)
        
def hide(n:int) -> None:    # 让某数字对应的LED灯熄灭
    for i in numbers[n]:
        LED[i-1].value(1)

def show2_core(x:int, y:int, ans:bool) -> None: 
# 交替显示两个数字一次，当切换频率足够快时看不出交替闪烁的现象
# 参数含义：x,y：交替显示的两个数字；ans: 是否让小数点位亮起（当输出答案时ans=True）
    show(x)
    POWER[0].value(1)   # 给第一个数字上电
    hide(x)
    POWER[0].value(0)
    if ans: LED[7].value(0)  # 小数点位
    show(y)
    POWER[1].value(1)   # 给第二个数字上电
    hide(y)
    POWER[1].value(0)
    if ans: LED[7].value(1)

def show2(x:int, y:int) -> None:      # 在显示答案前调用show2_core()函数的代码
    show2_core(x,y,False)

def show2_ans(x:int, y:int) -> None:  # 在显示答案时调用show2_core()函数的代码，和show2()函数的区别在于调用时的ans变量为True
    show2_core(x,y,True)
    
def read() -> int:     # 读取数字时的主要代码
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