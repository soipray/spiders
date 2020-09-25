# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiproPipeline:
    fp = None
    #重写父类方法：该方法只在初始化的时候调用一次
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./quiubai.txt', 'w', encoding='utf-8')
    #专门用来处理item类型对象a
    #该方法每接收一个item就会被调用
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+':'+content+'\n')
        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()

