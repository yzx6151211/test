import requests
from lxml import etree
import json

class TiebaC1:
    def __init__(self):
        self.url = "https://www.domp4.com/list/1-{}.html"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def get_url_list(self):
        return [self.url.format(i) for i in range(1,242)]

    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,start_url):
        html= etree.HTML(start_url)
        ret1 = html.xpath("//div[@id = 'list_all']/ul/li/a/img")
        Itemlist = []
        for i in ret1:
            item={}
            item["alt"] = i.xpath("./@alt") if len(i.xpath("./@alt")) > 0 else None
            item["data"] = i.xpath("./@data-original") if len(i.xpath("./@alt")) > 0 else None
            Itemlist.append(item)
        return Itemlist

    def save_coutent_list(self,coutent_list):
        with open("text.txt",'a') as f:
            for i in coutent_list:
                print(i)
                f.write(json.dumps(i,ensure_ascii=False))
                f.write("\n")
                print("*"*100)
    def run(self):
        # 1、构建url
        url_list = self.get_url_list()
        # 2、发送请求，获取响应
        # 3、获取第一页
        print(url_list)
        for url in url_list:
            html = self.parse_url(url)
            countent_list =  self.get_content_list(html)
            self.save_coutent_list(countent_list)



if __name__ == '__main__':
    TiebaC1 =TiebaC1()
    TiebaC1.run()