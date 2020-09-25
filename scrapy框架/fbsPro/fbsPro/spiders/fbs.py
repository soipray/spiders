import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    #allowed_domains = ['www.xxx.com']
    #start_urls = ['http://www.xxx.com/']
    redis_key = 'sun'
    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item = FbsProItem()
        #yield item
        return item
