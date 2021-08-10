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

# 点击【登录】按钮
driver.find_element_by_xpath("//a[@id='js_login']").click()

# 登录密码弹窗的
login_xpth="//div[@class='login-qq-iframe-wrap']//iframe"
web_locted=EC.visibility_of_element_located((By.XPATH,login_xpth))
WebDriverWait(driver,10).until(web_locted)

# 切换到iframe方式一：使用iframe的name
# driver.switch_to.frame("frame_name")

# 切换到iframe方式二：使用常定位的8种方式,进入到另一个html 进行操作
# driver.switch_to.frame(driver.find_element_by_xpath(login_xpth))

# # 切换到iframe方式三：使用等待
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,login_xpth)))

time.sleep(0.5)
driver.find_element_by_id('switcher_plogin').click()

# 从iframe当中，再回到主页面
driver.switch_to.default_content()

# driver.switch_to.parent_frame()
time.sleep(0.2)
driver.find_element_by_xpath("//a[@class='login-close']").click()