
from fake_useragent import UserAgent
# 调用
ua = UserAgent()
headers = {'User-Agent':ua.random}
print(headers)