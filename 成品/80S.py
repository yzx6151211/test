import requests
from fake_useragent import UserAgent
from lxml import etree
import re
class _80s:
    def __init__(self):
        self.headers = self.ret_augst()

    def ret_augst(self):
        ua = UserAgent()
        return {'User-Agent': ua.random}

    def structure_get_80s(self,name):
        url = 'http://k5.cc/movie/search/'
        data = {"search_typeid": "1",
                "skey": name,
                "Input": "搜索"}
        return url,data

    def parse_url(self,url,data):
        headers = self.ret_augst()
        response = requests.post(url,headers = headers,data = data)
        return response.content.decode()

    def get_content_list_80s(self,url):
        html = etree.HTML(url)
        ret = html.xpath("//ul[@class = 'me1 clearfix']/li/a")
        item = {}
        j = 1
        for i in ret:

            name = i.xpath("./img/@alt")[0] if len(i.xpath("./img/@alt")) > 0 else None
            href = "http://k5.cc" + i.xpath("./@href")[0] if len(i.xpath("./@href")[0]) > 0 else None
            item[j]=name+"+"+href
            j+=1
        #print(item)
        return item

    def choose_url(self,dict):
        for key in dict:
            print(str(key) + ':' + dict[key])

        choose = int(input("请选择"))
        in_url = str(dict.get(choose)).split("+")[1]
        in_html = self.parse_url(in_url,"")
        return in_html,in_url

    def get_last_url_80s(self,in_html,in_url):
        #print(in_url)
        pat = '载入全部下载资源'
        res1 = re.compile(pat, re.S).findall(in_html)
        if len(res1)>0:
            in_url = in_url+"/bd-2"
            response = requests.get(in_url,headers = self.headers)
            in_html = response.content.decode()
            #print(html)
        html = etree.HTML(in_html)
        ret = html.xpath("//ul[@class ='dllist1' ]/li/span")
        sum_list = []

        for i in ret:
            item = {}

            name = i.xpath("./span/a/text()")
            href = i.xpath("./span/a/@href")
            href1 = i.xpath(".//@value")

            for i in href1:
                # print(name)
                # print(href)
                # print(i)
                item["name"] = name
                item["href"] = href
                item["href1"] = i
                if len(item) > 0:
                    sum_list.append(item)

        for i in sum_list:
            print(i.get("name")[0] + ":" + i.get("href")[0] )
        print("\n"*5)
        for i in sum_list:
            print(i.get("name")[0] + ":" + i.get("href1"))

    def run(self,name):
        # 80s
        url,data = self.structure_get_80s(name)
        parse_url = self.parse_url(url,data)
        url_dict =  self.get_content_list_80s(parse_url)
        in_html,in_url = self.choose_url(url_dict)
        last_url = self.get_last_url_80s(in_html,in_url)

if __name__ == '__main__':
    _80s = _80s()
    name = input("请输入电影（电视剧名称）")
    _80s.run(name)
