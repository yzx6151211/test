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
        url = 'https://www.domp4.com/search/'

        data = {"wd":name}
        return url,data

    def parse_url(self,url,data):
        headers = self.ret_augst()
        response = requests.post(url,headers = headers,data = data)
        #print(response.content.decode())
        return response.content.decode()

    def get_content_list_80s(self,url):
        html = etree.HTML(url)
        ret = html.xpath("//div[@id = 'list_all']/ul/li")
        item = {}
        j = 1
        for i in ret:

            name = i.xpath("./a/img/@alt")[0] if len(i.xpath("./a/img/@alt")) > 0 else None
            href = "https://www.domp4.com" + i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")[0]) > 0 else None
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
        # print(in_html)
        # print(in_url)
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
        ret = html.xpath("//div[@class ='article content cclear']/div/ul/li/div/a")
        #print(ret)
        sum_list = []

        open("/storage/emulated/0/新文件夹/1.txt", 'w').close()
        for i in ret:
            name = i.xpath("./@title")
            html = i.xpath("./@href")
            f = open("/storage/emulated/0/新文件夹/1.txt", 'a', encoding="utf-8")
            f.write(name[0] + ":" + html[0] + "\n")
            f.close()
            print(name[0]+":"+html[0])







    def run(self,name):
        # 80s
        url,data = self.structure_get_80s(name)
        parse_url = self.parse_url(url,data)
        url_dict =  self.get_content_list_80s(parse_url)
        in_html,in_url = self.choose_url(url_dict)
        last_url = self.get_last_url_80s(in_html,in_url)

if __name__ == '__main__':
    _80s = _80s()
    #name = input("请输入电影（电视剧名称）")
    name = "山海令"
    _80s.run(name)
