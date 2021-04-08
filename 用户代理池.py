import urllib.request
import re
import random
x = 1
uapools = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
]
def ua(uapllls):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    #安装全局
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

for i in range(1, 10):
    ua(uapools)
    thisurl = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
    date = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    res = re.compile(pat, re.S).findall(date)
    print(i + i + i + i + i + i + i + i + i + i + i)

    for j in range(0, len(res)):
        file = open("C:\\Users\\Administrator\\Desktop\\1\\新建文件夹\\%d.txt" % x, "w", encoding='utf-8')
        print(res[j])
        file.write(res[j])
        file.close()
        x += 1
