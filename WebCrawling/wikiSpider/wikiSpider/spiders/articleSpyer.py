
from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpier(Spider):
    name = "article"
    allowed_domains=["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]


    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is:" + title)
        item['title'] = title
        return item



class HPageSpider(Spider):
    name = "hpage"
    allowed_domains = ["www.gmarket.co.kr"]
    start_urls = ["http://www.gmarket.co.kr"]

    def parse(self, response):
        for sel in response.xpath('//ul[@id="skipnavi"]/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print (title, link, desc)