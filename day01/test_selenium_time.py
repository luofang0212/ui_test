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
url = "https://www.baidu.com/"
driver.get(url)
# 窗口最大化
driver.maximize_window()

# 强制等待
# time.sleep(3)

# 隐性等待，全局生效
# driver.implicitly_wait(10)

# 点击【登录】
driver.find_element_by_xpath("//a[@id='s-top-loginbtn']").click()

xpath = "//p[@id='TANGRAM__PSP_11__footerULoginBtn']"

# 显性等待10s
web_locted = EC.visibility_of_element_located((By.XPATH,xpath))
WebDriverWait(driver,10).until(web_locted)

# 进入登录弹窗，选择【用户名密码】进行登录
driver.find_element_by_xpath("//p[@id='TANGRAM__PSP_11__footerULoginBtn']").click()






