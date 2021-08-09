#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()

'''对浏览器进行操作'''
# 访问一个网页
url = "https://www.baidu.com/"
driver.get(url)

'''元素定位'''

# xpath
driver.find_element_by_xpath("//div[@id='u1']/a").click()