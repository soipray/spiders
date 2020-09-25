# -*- codeing = utf8 -*-
# @Time 2020/9/17 21:38
# @Author : xxx
# @File : regex_qiushi_baike_img.py
# @Software: PyCharm
import requests
import re
import os

if __name__ == '__main__':
    img_folder = "./folder_qiutu"
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)

    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_list = re.findall(ex, page_text, re.S)
    # print(img_list)
    for src in img_list:
        src = "https:" + src
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split('/')[-1]
        img_path = img_folder + '/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功!!')
