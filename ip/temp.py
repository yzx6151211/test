import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
f = open("C:\\Users\\Administrator\\Desktop\\1.txt", "r+")
lines = f.readlines()  # 读取全部内容 ，并以列表方式返回

for i in lines:

    proxies = {'http': 'http://'+i, 'https': 'http://'+i}
    url = "https://www.baidu.com"

    try:
        print(i)
        data = requests.get(url, proxies=proxies, headers=headers, timeout=0.1).content.decode()
        print(len(data))

        if len(data):
            print(i)
        break
    except Exception as err:
        print("1111")

f.close()