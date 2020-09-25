# -*- codeing = utf8 -*-
# @Time 2020/9/21 22:12
# @Author : xxx
# @File : coroutine.py
# @Software: PyCharm

import asyncio


async def request(url):
    print('正在请求的url是', url)
    print('请求成功', url)

c = request('www.baidu.com')

#方法1 创建一个事件循环对象，将协程对象注册到loop中，然后启动loop
#loop = asyncio.get_event_loop()
#loop.run_until_complete(c)

#task的使用
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callback_func(task):
    print(task.result())

#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
