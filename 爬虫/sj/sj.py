import requests
from lxml import etree
from fake_useragent import UserAgent


def ret_augst():
    ua = UserAgent()

    return {'User-Agent': ua.random}
url = "https://mp.weixin.qq.com/s/dwh3-MkrHbNW87Zgj5C8vg"
res = requests.get(url,headers =  ret_augst())
print(res.content.decode())
ret = res.content.decode()
html = etree.HTML(ret)
htmls = html.xpath("//div[@id ='js_content']/section//@href")


for i in htmls:
    print(i)