# -*- codeing = utf8 -*-
# @Time 2020/9/18 14:34
# @Author : xxx
# @File : xpath_4k_pic.py
# @Software: PyCharm

import requests
from lxml import etree
import os

#4k图片爬取
if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text

    # 数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('./folder_4k_pic'):
        os.mkdir('./folder_4k_pic')
    for li in li_list:
        img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用解决中文乱码办法
        img_name = img_name.encode('ios-8859-1').decode('gbk')

        img_data = requests.get(url=img_src, headers=headers).content
        img_path = './folder_4k_pic/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功')
