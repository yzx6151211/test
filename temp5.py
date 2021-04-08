
import urllib.request,re
import random
import time
number = 0
def ip():
    thisurl = "https://seofangfa.com/proxy/"
    date = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))'
    res1 = re.compile(pat, re.S).findall(date)
    ip =[]
    for i in res1:

        res = re.sub(r'</td><td>',':',i[0])
        ip.append(res)
    #print(thisip)
    #thisip = random.choice(thisip)
    return ip
def opener(number):

    thisip = ip()
    thisip = thisip[number]
    print(thisip)
    proxy = urllib.request.ProxyHandler({"http": thisip})  # 转成特定格式
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
    urllib.request.install_opener(opener)
for i in range(0,20):
    try:
        opener(i)
        url = "http://www.taizhou.com.cn/index.htm"
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8", "ignore")
        print(len(data))
        #ip = ip()
        if len(data):
            print(ip()[i])

            print("111111111111")
            f = open("C:\\Users\\Administrator\\Desktop\\1.txt", "a")  # 设置文件对象
            f.write(ip()[i]+"\n")
            f.close()
    except Exception as err:
        print(err)
    i+=1
