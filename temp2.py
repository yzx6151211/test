import urllib.request,re
import random

def ip():
    thisurl = "https://seofangfa.com/proxy/"
    date = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))'
    res1 = re.compile(pat, re.S).findall(date)
    thisip =[]
    for i in res1:

        res = re.sub(r'</td><td>',':',i[0])
        thisip.append(res)
    #print(thisip)
    thisip = random.choice(thisip)
    print(thisip)
    proxy = urllib.request.ProxyHandler({"http": thisip})  # 转成特定格式
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
    urllib.request.install_opener(opener)
for i in range(0,20):
    try:
        ip()
        url = "http://www.taizhou.com.cn/index.htm"
        data1 = urllib.request.urlopen(url).read()
        data = data1.decode("utf-8", "ignore")
        print(len(data))
        fh = open("C:\\Users\\Administrator\\Desktop\\1\\新建文件夹\\1.html", "w", encoding='utf-8')
        fh.write(data)
        fh.close()
    except Exception as err:
        print(err)
