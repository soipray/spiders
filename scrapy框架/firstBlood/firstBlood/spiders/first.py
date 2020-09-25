import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称，爬虫源文件的唯一标识
    name = 'first'
    #allowed_domains = ['www.xxx.com']

    #url列表,urls被scrapy自动请求发送
    start_urls = ['http://www.baidu.com/', 'http://www.sogou.com/']

    #用于数据解析，response表示请求成功的返回对象
    def parse(self, response):
        print(response)
