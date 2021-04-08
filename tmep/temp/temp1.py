from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
import requests
from fake_useragent import UserAgent
import re
import json
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options


class get_selenium():
    def __init__(self):



        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.cookies = []
        self.session = requests.session()
        self.headers = {}
    def parse_se(self):

        self.driver.get(
            "https://account.wps.cn/?qrcode=kdocs&logo=kdocs&cb=https%3A%2F%2Faccount.wps.cn%2Fapi%2Fv3%2Fsession%2Fcorrelate%2Fredirect%3Ft%3D1611976250971%26appid%3D375024576%26cb%3Dhttps%253A%252F%252Fwww.kdocs.cn%252FsingleSign4CST%253Fcb%253Dhttps%25253A%25252F%25252Fwww.kdocs.cn%25252Flatest%25253Ffrom%25253Ddocs")
        time.sleep(1)
        self.driver.find_element_by_id("wechat").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("dialog-footer-ok").click()
        time.sleep(2)
        a = self.driver.find_element_by_xpath("//img[@id = 'miniprogramImportImg']").get_attribute("src")

        response = requests.get(a)
        # 显示二维码

        image = Image.open(BytesIO(response.content)).show()

        time.sleep(10)

    def get_cookies(self):
        self.cookies =  self.driver.get_cookies()
        for cookie in self.cookies:
            self.session.cookies.set(cookie['name'], cookie['value'])
        return self.cookies
    def close(self):
        self.driver.close()


    def ret_augst(self):
        ua = UserAgent()

        return {'User-Agent':ua.random}

    def parse_downadd(self):
        self.headers = self.ret_augst()
        ret = self.session.get("https://www.kdocs.cn/latest?from=docs", headers=self.headers)
        html =ret.content.decode()
        with open("renren.html", "w", encoding="utf-8") as f:
            f.write(html)
        file_name = "2021年2月1日-2月5日.xls"
        a = re.findall(r'''"fileid":"(.+?)",.*?''' + file_name, html)
        id_url = "https://www.kdocs.cn/3rd/drive/api/v3/groups/1040371001/files/"+a[0]+"/download?isblocks=false"
        parse_str = self.session.get(id_url, headers=self.headers)
        prase_con = parse_str.content.decode()
        parse_ret = json.loads(prase_con)
        return parse_ret['fileinfo']['url'],file_name

    def down(self,add,file_name):
            down_url = add
            ret_huru = self.session.get(down_url, headers=self.headers)
            with open("C:\\Users\\Administrator\\Downloads\\" + file_name, "wb") as f:
                f.write(ret_huru.content)
    def run(self):
        self.parse_se()
        self.get_cookies()
        time.sleep(3)
        self.close()
        downadd,file_name = self.parse_downadd()
        self.down(downadd,file_name)
if __name__ == '__main__':
    get_selenium = get_selenium()
    get_selenium.run()

