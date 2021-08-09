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
# 方式一 根据id 返回的是一个WebElement对象
ele = driver.find_element_by_id("kw")
print(ele)
# 根据属性获取对应的属性值
atr = ele.get_attribute('class')
print(atr)

# 方式二 class 返回的是一个WebElement对象
eles = driver.find_elements_by_class_name("s_ipt")  # 返回的是一组
driver.find_element_by_class_name("s_ipt")  # 返回的是一个，从上到下找到的第一个

# 方式三 name 返回的是一个WebElement对象
driver.find_elements_by_name("wd")
driver.find_element_by_name("wd")

# 方式四 tag_name
driver.find_elements_by_tag_name("input")
driver.find_element_by_tag_name("input")

# 方式五、六 针对链接 对链接内容可以进行完全匹配和模糊匹配
# 完全匹配
driver.find_element_by_link_text("更多产品")
driver.find_elements_by_link_text("更多产品")
# 模糊匹配
driver.find_element_by_partial_link_text("产品")
driver.find_elements_by_partial_link_text("产品")
