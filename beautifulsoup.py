import urllib.request
import re
#url = "http://yj1.b96dure93e9.rocks/pw/html_data/3/2009/4941395.html"
import urllib.request
import re
url = "http://yj1.b96dure93e9.rocks/pw/html_data/3/2009/4941395.html/"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener = urllib.request.build_opener()
#安装全局
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
#pat ='<br><br><img.*?src="(.*?)".*?border="0"'
#alllink = re.compile(pat,re.S).findall(data)
print(data)
'''for i in alllink:

    thislink = alllink[i]
    urllib.request.urlretrieve(thislink,filename='C:/Users/Administrator/Desktop/1/i.jpg')
    print(i)'''

