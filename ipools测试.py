import urllib.request
import re
import random


ippools=[
    "82.177.38.187:8080",
    "89.237.32.129:37647",
    "91.187.113.205:53281",
    "168.232.20.155:8080",
    "185.61.246.57:33021",
    "190.61.55.146:9991",
    "45.177.108.82:999",
]
def ip():

   # print(res)
    thisip = random.choice(ippools)
    print((thisip))
    proxy = urllib.request.ProxyHandler({"http": thisip})  # 转成特定格式
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
    urllib.request.install_opener(opener)
for i in range(0,5):
    try:
        ip()
        '''url = "https://www.qiushibaike.com/"
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8","ignore")
        print(len(data))
        fh = open('C:\\Users\\Administrator\\Desktop\\1\\新建文件夹\\ip_baidu.html',"wr")
        fh.write(data)
        fh.close()'''
    except Exception as err:
        print(err)
