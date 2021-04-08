import requests
session = requests.session()
post_url = "http://www.renren.com/PLogin.do/"
post_data = {"email":"523882246@qq.com","password":"a6151211"}
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"}
session.post(post_url,data=post_data,headers = headers)
r=session.get('http://www.renren.com/348041730/newsfeed/photo',headers = headers)
with open("renren.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())