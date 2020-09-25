# -*- codeing = utf8 -*-
# @Time 2020/9/18 14:56
# @Author : xxx
# @File : xpath_all_city.py
# @Software: PyCharm
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    page_text = requests.get(url=url, headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)

    #热门城市
    li_list_hot = tree.xpath('//div[@class="bottom"]/ul/li')
    for li in li_list_hot:
        hot_city_name = li.xpath('./a/text()')[0]
        #print(1, hot_city_name)

    #城市
    li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in li_list:
        city_name = li.xpath('./a/text()')[0]
        #print(2, city_name)

    #所有城市
    li_list_all = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for li in li_list_all:
        city_name = li.xpath('./text()')[0]
        print(3, city_name)