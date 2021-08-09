#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()

'''对浏览器进行操作'''
# 访问一个网页
url = "http://synyibiplatformfontend-179-test.synyi.sy/"
driver.get(url)

# 窗口最大化
driver.maximize_window()

# # 设置窗口大小
# driver.set_window_size()

# 回退上一页
driver.back()

# 回到下一页
driver.forward()

# 刷新
driver.refresh()

# # 关闭当前窗口
# driver.close()
#
# # 结束会话
# driver.quit()

'''获取属性'''
#获取标题
print(driver.title)

#获取网址
print(driver.current_url)

#获取窗口句柄
print(driver.current_window_handle)