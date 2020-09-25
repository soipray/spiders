# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse

class WangyiproDownloaderMiddleware:
    def process_request(self, request, spider):
        print('process_request', request.url)
        return None

    #通过该方法拦截五大版本对应的响应对象,进行篡改
    def process_response(self, request, response, spider):
        print(1, request.url)
        chrome = spider.chrome
        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:
            print("specail middle")
            #response    #五大板块响应对象
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象
            #如何获取动态加载中的新闻数据
            #基于selenium获取动态加载的数据
            chrome.get(request.url)
            sleep(2)
            page_text = chrome.page_source #包含动态加载数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        #response    #其他请求对应的响应对象
        print(2, "return normal")
        return response

    def process_exception(self, request, exception, spider):
        pass
