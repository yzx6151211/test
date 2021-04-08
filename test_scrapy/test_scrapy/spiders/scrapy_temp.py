import scrapy

#   scrapy crawl scrapy_temp
class ScrapyTempSpider(scrapy.Spider):
    name = 'scrapy_temp'
    allowed_domains = ['domp4.com']
    start_urls = ['https://www.domp4.com/list/1-1.html']

    def parse(self, response):
        # ret =response.xpath("//div[@id = 'list_all']/ul/li/a/img/@alt").extract()
        # print(ret)


        li_list = response.xpath("//div[@id = 'list_all']/ul/li/a")
        for i in li_list:
            item = {}
            item["data"] =i.xpath("./img/@alt").extract_first() # 多个取第一个

            yield item  #　传到pipelines　