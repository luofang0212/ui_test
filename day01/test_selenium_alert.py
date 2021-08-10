#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()

'''对浏览器进行操作'''
# 访问一个网页
url = 'D:\\python_work\\ui_test\\day01\\simple_login.html'
driver.get(url)

# 窗口最大化
# driver.maximize_window()

# 窗口切换到alert
alert = driver.switch_to.alert

# 打印弹窗内容
print(alert.text)
# time.sleep(2)
# 选择：确定
alert.accept()
# 选择：否
alert.dismiss()



