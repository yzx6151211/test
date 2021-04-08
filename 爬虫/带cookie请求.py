import requests
session = requests.session()
post_url = "http://cdr.114yun.net:8001/login!login.act"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36",
           "Cookie":"JSESSIONID=BFDA27EEBFF42E3B100D032170D3879E"}

r=session.get('http://cdr.114yun.net:8001/login!toPage.act',headers = headers)
with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())