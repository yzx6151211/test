import requests
class TiebaSpider:
    def __init__(self,tieba_name,tieba_page):
        self.tieba_page = tieba_page
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers ={"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"}
    def url_list(self):#构造url列表
        return [self.url_temp.format(i+50) for i in range(self.tieba_page)]
    def parse_url(self,url):# 发送请求，获取响应
        response = requests.get(url,headers =self.headers)
        return response.content.decode()
    def html_save(self,html_str,page):# 保存html字符串
        file_path = "{}_第{}页.html".format(self.tieba_name,page)
        with open(file_path,"w") as f:
            f.write(html_str)
    def run(self):# 运行
        url_list = self.url_list()
        for u in url_list:
            url_str = self.parse_url(u)
            list_page = url_list.index(u)+1
            self.html_save(url_str,list_page)







if __name__ == '__main__':
    tieba_spider=TiebaSpider("李毅",20)
    tieba_spider.run()