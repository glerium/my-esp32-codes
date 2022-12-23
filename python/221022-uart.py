''' 使用UART实现两个单片机之间使用杜邦线进行通信
    接线方法：单片机分别为A、B；A与B的GND相接；A的tx脚接B的rx脚，A的rx脚接B的tx脚；
    注意两个单片机的baudrate应设置成相同
'''

from machine import UART
import time
uart1 = UART(1, baudrate=1220, tx=32, rx=33)
while True:
    uart1.write('123456789')
    print(uart1.read(9))
    time.sleep(0.1)