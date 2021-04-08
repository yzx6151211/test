import urllib.request,re
import random



ip = "101.4.136.34:81"
proxy = urllib.request.ProxyHandler({"http": ip})  # 转成特定格式
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
urllib.request.install_opener(opener)
url = "http://www.taizhou.com.cn/index.htm"
data1 = urllib.request.urlopen(url).read()
data = data1.decode("utf-8", "ignore")
print(len(data))
fh =  open("C:\\Users\\Administrator\\Desktop\\1\\新建文件夹\\1.html","w",encoding='utf-8')
fh.write(data)
fh.close()