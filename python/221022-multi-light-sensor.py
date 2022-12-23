''' 手势检测（光感+红外线感应联动检测）
    程序效果：光感放在左侧，红外放在右侧，手指遮挡传感器时会发出信号，并被程序读取
             若手掌从左往右划过，则输出right并亮起LED1灯；反之则输出left，亮起LED2灯；
    基本原理：sensor1为光线感应器，sensor2为红外感应器，程序不断检测sensor1.value和sensor2.value
             当sensor1.value==0时代表光感被遮挡，sensor2.value==1时红外被遮挡
             同时会有两个变量time1和time2来记录各个传感器上次被遮挡的时间
             若两个传感器在300ms内都有被遮挡记录，则输出left/right，并亮起对应的LED灯
'''
from machine import Pin,Timer
import time
sensor1 = Pin(18,Pin.IN)    # default: 0
sensor2 = Pin(14,Pin.IN)    # default: 1
LED1 = Pin(32,Pin.OUT)
LED2 = Pin(33,Pin.OUT)
covered1 = covered2 = False     # bool类型：表示各个传感器是否在近300ms内被遮挡过
time1 = time2 = time.ticks_ms()
LED1.value(1)
LED2.value(1)

def led1_off(tim):  # 回调函数
    global LED1
    LED1.value(1)
def led2_off(tim):  # 回调函数
    global LED2
    LED2.value(1)

while True:
    val1 = sensor1.value()  # 读取传感器1
    val2 = sensor2.value()  # 读取传感器2
#     print('{:d} {:d}'.format(val1,val2))
    if val1 != 1:       # 当光线感应器被遮挡时
        if covered2:    # 若近300ms内红外传感器也被遮挡过
            LED2.value(0)
            covered1 = covered2 = False   # 本次手势检测已经结束，防止重复输出
            print('left')
            tim0 = Timer(0)       # esp32的内部计时器
            tim0.init(period=300, mode=Timer.ONE_SHOT, callback=led2_off)   # 设置时间中断：300ms后熄灭LED2灯
        else:
            covered1 = True         # 记录本次被遮挡的状态
            time1 = time.ticks_ms() # 记录本次被遮挡的时间
    if val2 != 0:
        if covered1:
            LED1.value(0)
            covered1 = covered2 = False
            print('right')
            tim1 = Timer(1)
            tim1.init(period=300, mode=Timer.ONE_SHOT, callback=led1_off)   # 设置时间中断：300ms后熄灭LED1灯
        else:
            covered2 = True
            time2 = time.ticks_ms()
    if time.ticks_diff(time.ticks_ms(),time1) >= 300:   # 更新covered1状态：若上次被遮挡时间与当前时间相差300ms以上
        covered1 = False
    if time.ticks_diff(time.ticks_ms(),time2) >= 300:
        covered2 = False
    time.sleep_ms(10)