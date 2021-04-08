import urllib.request
import re
#url = "https://www.qiushibaike.com/text/"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener = urllib.request.build_opener()
#安装全局
opener.addheaders=[headers]
urllib.request.install_opener(opener)
#html = urllib.request.urlopen(url).read().decode("utf-8")
x = 1
for i in range(1,10):
    thisurl ="https://www.qiushibaike.com/text/page/"+str(i)+"/"
    date = urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    res = re.compile(pat,re.S).findall(date)
    print(i+i+i+i+i+i+i+i+i+i+i)

    for j in range(0,len(res)):
        file=  open("C:\\Users\\Administrator\\Desktop\\1\\新建文件夹\\%d.txt"%x,"w",encoding='utf-8')
        print(res[j])
        file.write(res[j])
        file.close()
        x+=1




