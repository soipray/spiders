# -*- codeing = utf8 -*-
# @Time 2020/9/17 11:55
# @Author : xxx
# @File : requests_sogou_search.py
# @Software: PyCharm

# 反爬机制 UA伪装
import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'

    # 处理url携带的参数，封装到字典中
    kw = input('enter a word:')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    param = {
        'query': kw
    }

    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    fileName = kw + ".html"
    with open('file_sogou_search.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, '保存成功！！！')
