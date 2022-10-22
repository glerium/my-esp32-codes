import network,time

def WIFI_Connect():
    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断
    if not wlan.isconnected():
        print('connecting...')
        wlan.connect('玛珈山职业技术学院', 'Wenzelin2004') #输入WIFI账号密码
        while not wlan.isconnected():
            time.sleep_ms(300)
            if time.time()-start_time > 10:
                print('timeout')
                break
    if wlan.isconnected():
        print('network information:', wlan.ifconfig())
WIFI_Connect()