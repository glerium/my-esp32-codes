''' 调用network模块连接WiFi网络 '''
import network,time

def WIFI_Connect():
    wlan = network.WLAN(network.STA_IF)     # STA模式
    wlan.active(True)            # 激活接口
    start_time=time.time()       # 记录时间做超时判断
    if not wlan.isconnected():
        print('connecting...')
        wlan.connect('esp32', '12345678')   # WIFI账号密码
        while not wlan.isconnected():
            time.sleep_ms(300)
            if time.time() - start_time > 10:   # 连接超时
                print('timeout')
                break
    if wlan.isconnected():    # 成功连接后输出WiFi配置
        print('network information:', wlan.ifconfig())

WIFI_Connect()