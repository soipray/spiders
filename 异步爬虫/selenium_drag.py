# -*- codeing = utf8 -*-
# @Time 2020/9/22 20:45
# @Author : xxx
# @File : selenium_drag.py
# @Software: PyCharm
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

chrome = webdriver.Chrome(executable_path='../chromedriver.exe')

chrome.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#切换到子网页
chrome.switch_to.frame('iframeResult')

div = chrome.find_element_by_id('draggable')

#动作链
action = ActionChains(chrome)
#点击长按指定标签
action.click_and_hold(div)
for i in range(5):
    #perform立即执行动作链操作
    action.move_by_offset(17, 0).perform()
    sleep(0.5)

action.release()
chrome.quit()