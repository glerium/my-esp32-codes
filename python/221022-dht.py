''' 使用dht模块操纵温度湿度传感器 '''
from machine import Pin
import dht
import time
sensor = dht.DHT11(Pin(5))
while True:
    try:
        sensor.measure()            # 调用温湿度传感器进行测量
        temp = sensor.temperature() # 温度
        hum = sensor.humidity()     # 湿度
        print('Temperature = {:3.1f}C\nHumidity = {:3.1f}%\n'.format(temp,hum))
        time.sleep(0.3)
    except OSError:      # 错误处理
        print('Failed to read sensor.')