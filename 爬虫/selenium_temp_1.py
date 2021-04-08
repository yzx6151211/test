from selenium import webdriver

url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_id("kw").send_keys("baidu")
driver.find_element_by_id("su").click()
a= driver.find_element_by_xpath('//div[@class ="page-inner"]')
print(a)