# -*- codeing = utf8 -*-
# @Time 2020/9/18 14:14
# @Author : xxx
# @File : xpath_58_house.py
# @Software: PyCharm
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://zhangzhou.58.com/ershoufang/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    page_text = requests.get(url=url, headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)