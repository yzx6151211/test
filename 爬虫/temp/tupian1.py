import requests
import urllib
import os
from lxml import etree
import re
from fake_useragent import UserAgent



class down_mage:
    def __init__(self):
        self.headers = ""
        self.i = 0
    # 获取随机User-Agent
    def ua(self):
        ua = UserAgent()

        self.headers = {"User-Agent":ua.chrome}
        # print(self.headers)
        return self.headers
        #根据page返回response

    def parse_page(self,page):
        page_url = "http://yj1.b96dure93e9.rocks/pw/thread.php?fid=3&page={}"
        #print(page_url.format(page))
        #print(page_url)
        try:
            ret = requests.get(page_url.format(page),headers = self.headers,timeout=3,verify=False)
        except Exception as ex:  # 异常
            ret = requests.get(page_url.format(page+1),headers = self.headers,timeout=3,verify=False)
            print(page)
            self.i*=self.i
        #print(ret.content.decode())
        # with open('html.html', "w", encoding="utf8") as f:
        #     f.write(ret.content.decode())
        #print(ret.content.decode())
        return ret.content.decode()

        # get子页地址，返回path和response
    def parse_url(self,url,i,j):
        # path = "./"+str(i)+"-"+str(j)
        # os.makedirs(path)
        url = "http://yj1.b96dure93e9.rocks/pw/"+url
        #print(path)
        ret = requests.get(url,self.headers)
        #print(ret.content.decode())
        return ret.content.decode()
    # 根据关键字搜索上一个href
    def xpath_page(self,ret):
        html = etree.HTML((ret))
        a = html.xpath("//tr[@align = 'center']//a/font[contains(string(), 'の亚洲无码')]/../@href")
        print(a)
        return a
    # 获取下载地址
    def get_path(self,ret,name):
        html = etree.HTML(ret)
        src_list = html.xpath("//div[@class = 'f14']/img/@src")

        b = re.findall(name + '''.*?下载网址.*?href="(.*?)"''', ret)
        print(b)
        if len(b)>0:
            print(name)
            print(b)

        return src_list


    # 获取图片
    def get_down_img(self,src_list,url,i,j):

        path = "./" + str(i) + "-" + str(j)
        os.makedirs(path)
        with open(path+"\\"+'html.txt', "w", encoding="utf8") as f:
            f.write(url)
        name = 1

        for img_url in src_list:
            try:
                image = requests.get(img_url, headers=self.headers,timeout=3,verify=False)
                image = image.content
                #print(path)
                with open(path+"\\" +str(name)+ '.jpg', 'wb') as f:
                    f.write(image)
            except Exception as ex:  # 异常
                pass
                print(ex)  # 打印异常但不会报错
            name += 1
    def run(self):

        # 生成User-Agent
        self.ua()
        # get
        for i in range(1,500):
            ret = self.parse_page(i)
            re = self.xpath_page(ret)
            j = 1
            for url in re:
                #print("http://yj1.b96dure93e9.rocks/pw/"+url)
                print(i)
                print(url)
                con = self.parse_url(url,i,j)
                #print(i)
                # print(i,j)
                src_list = self.get_path(con,"百合川")
                #print(src_list)
                self.get_down_img(src_list,"http://yj1.b96dure93e9.rocks/pw/"+url,i,j)
                j+=1
            i = self.i
if __name__ == '__main__':
    down_mage = down_mage()
    down_mage.run()
