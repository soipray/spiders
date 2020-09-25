import scrapy
from qiubaiPro.items import QiubaiproItem

class FirstSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     content = response.xpath('//div[@id="content"]')
    #     content_left = content.xpath('./div[1]/div[2]')
    #     div_list = content_left.xpath('./div')
    #     all_data = []
    #
    #     # 解析作者名称 段子内容
    #     for div in div_list:
    #         # xpath返回的是列表，但元素一定是selector类型
    #         # extract可以将select对象中data提取
    #         # author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         # content = div.xpath('./a[1]/div/span//text()')[0].extract()
    #         # 将每一个列表元素的data提取
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    def parse(self, response):
        content = response.xpath('//div[@id="content"]')
        content_left = content.xpath('./div[1]/div[2]')
        div_list = content_left.xpath('./div')

        # 解析作者名称 段子内容
        for div in div_list:
            # xpath返回的是列表，但元素一定是selector类型
            # extract可以将select对象中data提取
            # author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            author = div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()')[0].extract()
            # content = div.xpath('./a[1]/div/span//text()')[0].extract()
            # 将每一个列表元素的data提取
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item