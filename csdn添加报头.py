import urllib.request


headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
url = "https://blog.csdn.net/"
date = opener.open(url).read()
print(date)