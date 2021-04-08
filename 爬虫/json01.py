import json
import requests
from pprint import pprint
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
response = requests.get(url,headers = headers )
print(response)
ret = response.content.decode()
print(ret)
print(type(ret))
ret1 = json.loads(ret)
print(ret)
with open("douban.json","w",encoding="utf-8")as f:
    f.write(json.dumps(ret,ensure_ascii=False,indent="5"))