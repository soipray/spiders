# -*- codeing = utf8 -*-
# @Time 2020/9/17 17:52
# @Author : xxx
# @File : requests_douban_xiju.py
# @Software: PyCharm
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '40',
        'limit': '20'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    response = requests.get(url=url, params=params, headers=headers)
    # 响应数据是application/json
    dic_obj = response.json()
    print(dic_obj)

    fp = open('file_douban_xiju.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!!')
