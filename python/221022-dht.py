from machine import Pin
import dht
import time
sensor = dht.DHT11(Pin(5))
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('Temperature = {:3.1f}C\nHumidity = {:3.1f}%\n'.format(temp,hum))
        time.sleep(0.3)
    except OSError:
        print('Failed to read sensor.')