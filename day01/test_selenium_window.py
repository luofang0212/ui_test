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
url = 'https://ke.qq.com/'
driver.get(url)

# 窗口最大化
driver.maximize_window()

# 点击【分类】，新开一个窗口
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='header-index-category-text']/a")))
driver.find_element_by_xpath("//div[@class='header-index-category-text']/a").click()

# 第一步：获取窗口的总数以及句柄
handles = driver.window_handles
print(handles)

# 第二步，切换到新窗口
time.sleep(1)
driver.switch_to.window(handles[-1])

# 第三步：在新窗口进行操作
driver.find_element_by_xpath("//input[@id='js_keyword']").send_keys("python")
driver.find_element_by_xpath("//a[@id='js_search']").click()

#拓展：回到第一个窗口
time.sleep(0.5)
driver.switch_to.window(handles[0])

# 点击【登录】按钮
driver.find_element_by_xpath("//a[@id='js_login']").click()



