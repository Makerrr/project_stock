from lxml import etree
# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象
path='./chromedriver'

browser=webdriver.Chrome(path)

# (3)访问网站
url='https://finance.eastmoney.com/a/csygc_1.html'
# url='https://www.baidu.com'
browser.get(url)

# page_source获取网页源码
content=browser.page_source
# print(content)

# (4)解决selenium中不支持xpath中直接获取text
#    使用from lxml import etree中的xpath
html=etree.HTML(content)
title=html.xpath('//p[@class="title"]/a/text()')
# button=browser.find_elements_by_xpath('//input[@id="su"]')
print(title)
print(len(title))
