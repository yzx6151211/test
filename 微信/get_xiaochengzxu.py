import requests
url = 'http://api.tzedu.net.cn:443'
a = requests.get(url)
print(a.content.decode())