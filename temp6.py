import urllib.request,re
import random
import time
number = 0

def ip1():
    thisurl = "http://www.66ip.cn/areaindex_27/1.html"
    date = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    #print(date)
    pat = '((\\d+\\.\\d+\\.\\d+\\.\\d+)</td><td>(\\d+))'
    res1 = re.compile(pat, re.S).findall(date)
    #print(res1)
    ip = []
    for i in res1:
        res = re.sub(r'</td><td>', ':', i[0])
        print(res)
        ip.append(res)
    return ip
def opener(number):

    thisip = ippool
    thisip = thisip[number]
    proxy = urllib.request.ProxyHandler({"http": thisip})  # 转成特定格式
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
    urllib.request.install_opener(opener)
ippool = []
ippool = ip1()
for i in range(0,100):
    try:
        opener(i)
        url = "http://www.taizhou.com.cn/index.htm"
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8", "ignore")
        print(len(data))
        #ip = ip()
        if len(data):
            print(ip1()[i])

            print("111111111111")
            fd = open("C:\\Users\\Administrator\\Desktop\\1.txt", "r")
            f = open("C:\\Users\\Administrator\\Desktop\\1.txt", "a")  # 设置文件对象
            lines = fd.readline()
            print(lines)
            if ip1()[i] not in lines:

                f.write(ip1()[i]+"\n")
                print("写入成功"+ip1()[i])
                f.close()
            else:
                print("重复没有写入"+ip1()[i])
    except Exception as err:
        print(err)
    i+=1