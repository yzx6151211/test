from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
# 先实例化
driver = webdriver.Chrome()
# 设置窗口大小
driver.set_window_size(1920,1280)
# 最大化窗口
driver.maximize_window()
# 打开地址

driver.get("https://www.baidu.com")

# 定位
driver.find_element_by_id("kw").send_keys("c#")
driver.find_element_by_id("su").click()
# driver 获取html字符串
ele = driver.find_element_by_xpath("//*[@text()='入门经典教程,值得收藏']").text
print(ele)
# driver 获取url地址，请求后的地址
time.sleep(3)
# 截屏
driver.save_screenshot("./1.png")


time.sleep(3)
#driver.quit()
