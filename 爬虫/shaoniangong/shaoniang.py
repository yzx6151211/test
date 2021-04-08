import requests
from fake_useragent import UserAgent


headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
data = {"username":"尤子彧",
"password":"18968682676",
"loginKind":"student",
"orgId":"8A4081E62DCAB2D8012E69EC7A280DCF"
}
response = requests.post('http://bm.qsng.cn/eduapp/api/public/sys/user/login',data = data,headers = headers)
r =  response.content.decode()
print(r)