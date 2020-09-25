# -*- codeing = utf8 -*-
# @Time 2020/9/18 11:14
# @Author : xxx
# @File : ba4_shici_mingju.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

# 需求 爬取诗词名句网的小说
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    page_text = requests.get(url=url, headers=headers).text

    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./file_shicimingju.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功！！')
