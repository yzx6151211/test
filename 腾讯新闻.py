import urllib.request
import re
url = "https://blog.csdn.net/"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener = urllib.request.build_opener()
#安装全局
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat =
alllink = re.compile(pat).findall(data)
for i in alllink:
    localpath = ""#地址
    thislink = alllink[i]
    urllib.request.urlretrieve(thislink,filename=localpath)

