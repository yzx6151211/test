import requests
from lxml import etree


class TiebaC1:
    def __init__(self):
        self.url = "https://www.domp4.com/list/1-{}.html"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def get_url_list(self):
        a =[]
        b = self.url.format("1")
        print(b)
        return [self.url.format(i) for i in range(1,242)]
if __name__ == '__main__':
    tiebaC1 =TiebaC1()
    print(tiebaC1.get_url_list())