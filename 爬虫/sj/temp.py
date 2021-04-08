
import re
import urllib.request
from selenium import webdriver
import time

url = "https://mp.weixin.qq.com/s?__biz=MzIwNzM1MDEyMQ==&mid=2247487064&idx=4&sn=09c12489145f7e9826c4770a292e33fe&chksm=9712fe5ea065774853e9b461b44ff9bd19d91a1a0bea81fb011c49bdea4743566bfdfdfd1411&scene=21"
driver = webdriver.Chrome()
res = driver.get(url)
time.sleep(5)

print(driver.page_source)
# a = re.findall('''origin_src="(.*?)"''', res)
# print(a)