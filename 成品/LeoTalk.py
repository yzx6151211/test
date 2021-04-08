import requests,re
from fake_useragent import UserAgent
from lxml import etree
import json

class LeoTalk:
    def __init__(self):
        self.headers = self.ret_augst()
        self.url_all = []
    def ret_augst(self):
        ua = UserAgent()
        return {'User-Agent': ua.random}

    def data_leo(self,name,from_url):
        self.data = {
            "input": name,
            "filter": "name",
            "type": from_url,
            "page": "1"
        }



    def parse(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                   "x-requested-with":"XMLHttpRequest"


        }

        responst = requests.post("https://www.leoshow.cn/music/?name=",data = self.data,headers = headers,verify = False )
        return responst.content.decode('unicode-escape')

    def str_parse(self,res):
        ret = res.replace('\/','/')
        #print(ret)
        pat = '''"(url)":"(http.*?.mp3).*?(title)":"(.*?)"'''
        res1 = re.compile(pat, re.S).findall(ret)
        for i in res1:
            self.url_all.append(i)

    def run(self,name,type):
        open("C:\\Users\\Administrator\\Desktop\\1.txt",'w').close()
        for i in type:
            self.data_leo(name,i)
            res =  self.parse()
            url = self.str_parse(res)
        for i in self.url_all:
            print(i)
            f = open("C:\\Users\\Administrator\\Desktop\\1.txt",'a')
            f.write(i[3]+i[1]+"\n")
            f.close()

if __name__ == '__main__':
    name =  input("请输入歌名")
    #name = "有一位神"
    type = ["netease","qq","kugou","kuwo","xiami","baidu",]
    LeoTalk = LeoTalk()
    LeoTalk.run(name,type)
    bool= input("是否继续查询，是选1")
    if bool =="1":
        type = ["1ting", "migu", "ximalaya", "5singfc", "5singyc"]
        LeoTalk.run(name, type)