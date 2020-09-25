import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    #链接提取器：根据指定规则（正则）进行指定链接的提取
    #从网页提取到的源代码，只要包含符合的链接，会自动提取,自动去重
    link = LinkExtractor(allow=r'id=1&page=\d+')

    #follow=True 允许递归爬取

    rules = (
        #规则解析器
        Rule(link, callback='parse_item', follow=False),
        #Rule(link_detail, callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        print(response)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
