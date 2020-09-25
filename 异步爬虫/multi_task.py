# -*- codeing = utf8 -*-
# @Time 2020/9/22 10:34
# @Author : xxx
# @File : multi_task.py
# @Software: PyCharm
import asyncio
import time


async def request(url):
    print("正在下载", url)
    #异步协程中如果出现了同步代码，那么无法实现异步
    #time.sleep(2)
    #asyncio中遇到阻塞必须手动挂起
    await asyncio.sleep(2)
    print("下着完毕", url)


start = time.time()
urls = {
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
}

stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))


print(time.time() - start)
