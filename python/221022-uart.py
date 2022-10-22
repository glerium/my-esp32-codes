from machine import UART
import time
uart1 = UART(1, baudrate=1220, tx=32, rx=33)
while True:
    uart1.write('123456789')
    print(uart1.read(9))
    time.sleep(0.1)