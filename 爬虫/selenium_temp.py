from selenium import webdriver
import time
class TouYu:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()
    def get_content_list(self):
        # li_list = self.driver.find_elements_by_xpath("//li[@class = 'layout-Cover-item']/div/a")
        # content_list = []
        # for i in li_list:
        #     a=  i.get_attribute("href")
        #     print(a)

        li_list = self.driver.find_elements_by_xpath("//li[@class = 'layout-Cover-item']")
        content_list = []
        for li in li_list:
            item={}
            item["image"] = li.find_element_by_xpath("./div/a").get_attribute("href")
            item["title"] = li.find_element_by_xpath("./div/a/div[@class = 'DyListCover-content']//h3").text
            content_list.append(item)
            #print(item)
        next_url = self.driver.find_elements_by_xpath("//span[@class = 'dy-Pagination-item-custom']")[0]
        print(next_url)
        next_url1 = self.driver.find_elements_by_xpath("//span[@class = 'dy-Pagination-item-custom']")[1]
        print(next_url1)
        return content_list,next_url1
    def save_content_list(self,contnt_list):
        print(contnt_list)
    def run(self):
        # 发送请求
        self.driver.get(self.start_url)
        time.sleep(3)
        content_list = self.get_content_list()
        content_list,next_url = self.
        self.save_content_list(content_list)

if __name__ == '__main__':
    touyu = TouYu()
    touyu.run()