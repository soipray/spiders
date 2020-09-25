import requests


def request_sogou():
    # 指定url
    url = "https://www.sogou.com/"
    # 发送请求
    response = requests.get(url=url)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('file_sogou_index.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")



if __name__ == '__main__':
    request_sogou()
