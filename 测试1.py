import urllib.request,re
import random
import time

ippool =["113.194.28.180:9999",
"101.4.136.34:81",
"124.232.133.199:3128",
"221.180.170.104:8080",
"114.55.95.112:8999",
"36.249.109.33:9999",
"58.220.95.44:10174",
"211.137.52.158:8080",
"36.103.223.96:3128",
"222.66.94.130:80",
"80.241.222.137:80",
"120.78.200.31:3128",
"80.241.222.137:80",
"3.211.17.212:80",
"3.211.17.212:80",
"122.239.2.234:80",
"61.135.185.172:80",
"3.211.17.212:80",
"122.239.2.234:80",
"3.211.17.212:80",
"122.239.2.234:80",
"3.211.17.212:80",
"122.239.2.234:80",
"3.211.17.212:80",




]
for ip in ippool:
    try:
        print(ip)
        proxy = urllib.request.ProxyHandler({"http": ip})  # 转成特定格式
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
        urllib.request.install_opener(opener)
        url = "http://www.taizhou.com.cn/index.htm"
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8", "ignore")
        print(len(data))

    except Exception as err:
        print(err)