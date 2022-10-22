from machine import Pin
import time

KEY1 = Pin(35,Pin.IN)
gpio = [12,14,18,5,23,22,21,19]
LED = list()
for i in gpio:
    LED.append(Pin(i,Pin.OUT))
for i in LED:
    i.value(1)
numbers = [[1,2,3,5,6,7],[3,7],[2,3,4,5,6],[2,3,4,6,7],[1,3,4,7],[1,2,4,6,7],[1,2,4,5,6,7],[2,3,7],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]

def show(num:int) -> None:
    for i in numbers[num]:
        LED[i-1].value(0)

def hide(num:int) -> None:
    for i in numbers[num]:
        LED[i-1].value(1)

ima = 0
show(ima)
while True:
    if KEY1.value() == 0:
        while KEY1.value() == 0:
            pass
        hide(ima)
        ima = (ima + 1) % 10
        show(ima)