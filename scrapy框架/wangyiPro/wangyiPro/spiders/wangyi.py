import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []

    # 实例化一个浏览器对象
    def __init__(self):
        self.chrome = webdriver.Chrome(executable_path=r'E:\src\python\test\requestsSpider\chromedriver.exe')

    # 解析五大板块url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3, 4, 6, 7, 8]

        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        # 一次对每一个板块对应的页面请求
        for url in self.models_urls:
            print(3,url)
            yield scrapy.Request(url=url, callback=self.parse_model)

    # 解析每一个板块页面中对应新闻的标题和新闻详情页的url
    # 页面都是动态加载的
    def parse_model(self, response):
        print("item")
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            # 对新闻详情页的url请求
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detaila, meta={'item': item})

    def parse_detail(self, response):
        print("detail")
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self, spider):
        print('chrome close...')
        self.chrome.quit()