# -*- coding: utf-8 -*-
import requests,re
from bs4 import BeautifulSoup as bs
ip = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
thisurl = "http://www.xiladaili.com/gaoni/2/"
responser = requests.get(thisurl, verify=False, headers=headers, timeout=3)
encoding = responser.apparent_encoding
responser.encoding = encoding
soup = bs(responser.text,'html.parser')
date =soup.decode()
#print(date)

pat ='<td>((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</td>'
res1 = re.compile(pat, re.S).findall(date)
#print(res1)
for i in res1:
    res = re.sub(r'</td>\n<td>', ':', i[0])
    print(res)
    ip.append(res)