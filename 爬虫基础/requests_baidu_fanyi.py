# -*- codeing = utf8 -*-
# @Time 2020/9/17 17:37
# @Author : xxx
# @File : requests_baidu_fanyi.py
# @Software: PyCharm
import requests
import json

if __name__ == '__main__':
    kw = input('enter a word:')

    post_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': kw
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    response = requests.post(url=post_url, data=data, headers=headers)
    #响应数据是application/json
    dic_obj = response.json()

    print(dic_obj)
    fp = open('file_baidu_fanyi.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!!')
