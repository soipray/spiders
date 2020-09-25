# -*- codeing = utf8 -*-
# @Time 2020/9/17 21:31
# @Author : xxx
# @File : qiushi_baike_img.py
# @Software: PyCharm
import requests

if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12358/123584197/medium/6NO0EHFTA39NVELJ.jpg'

    img_data = requests.get(url=url).content
    with open('file_qiushi_baike.jpg','wb') as fp:
        fp.write(img_data)