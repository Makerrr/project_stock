from lxml import etree
from tqdm import tqdm
import pandas as pd
import time
import requests
import pickle as pkl
import pdb


# (1)导入selenium
from selenium import webdriver

# (2)创建浏览器操作对象
path='./chromedriver'

browser=webdriver.Chrome(path)

# (3)访问网站
base_url_lst = [
"https://finance.eastmoney.com/a/csygc_{}.html",
# "https://biz.eastmoney.com/a/csyzx_{}.html",
# "https://finance.eastmoney.com/a/cjjsp_{}.html",
# "https://finance.eastmoney.com/a/ccyts_{}.html",
# "https://finance.eastmoney.com/a/cgspl_{}.html",
# "https://enterprise.eastmoney.com/a/ccyyj_{}.html"
]
# page_source获取网页源码
# browser.get(url)
# content=browser.page_source

# # (4)解决selenium中不支持xpath中直接获取text
# #    使用from lxml import etree中的xpath
# html=etree.HTML(content)
# title=html.xpath('//p[@class="title"]/a/text()')
# print(title)
# print(len(title))

# 爬取新闻页面的url
url_dict = {}
def get_news_url(base_url,page):
    url = base_url.format(page)
    browser.get(url)
    content=browser.page_source
    #将html字符串转化为element对象
    html = etree.HTML(content) 
    url_lst = html.xpath('//p[@class="title"]/a/@href')
    title_lst = [url.strip() for url in html.xpath('//p[@class="title"]/a/text()')] 
   
    return dict(zip(title_lst,url_lst))

title_url_dict = {}
for base_url in tqdm(base_url_lst):
    
    for page in range(1,2):
        print(page)
        title_url_dict.update(get_news_url(base_url,page))
        

# DataFrame表格型数据结构
#   title_url_dict={'中金2023年造纸行业展望': '111', '中天国富证券': '2222'}
# DataFrame
    #      中金2023年造纸行业展望 中天国富证券
    # url  111                     2222
title_url_df = pd.DataFrame(title_url_dict,index=["url"]).T
title_url_df["html"] = ""


for title in tqdm(title_url_df.index):
    url_i = title_url_df.loc[title,"url"]
    #获取具体文章的网页源代码 
    html_i =  requests.get(url_i).content.decode('utf-8') 
    
    # 写入数据
    title_url_df.loc[title,"html"]=html_i
    time.sleep(0.5)

# print(title_url_df.loc[title,"html"])
# import pdb;pdb.set_trace() 
print(title_url_df)
# with open("title_url_df.pkl","wb") as f: 
#     pkl.dump(title_url_df,f)  #dump方法将变量保存在pickle文件中 


# # 测试 html网页的内容
# url='http://finance.eastmoney.com/a/202301072607715648.html'
# res=requests.get(url).content.decode('utf-8') 
# print(res)


 
# html = etree.HTML(res)  #分析HTML，返回DOM根节点
# tit = html.xpath('//div[@class="title"]/text()')
# # publish_time=html.xpath('//div[@class="item"]/text()')
#  publish_time=html_i.xpath('//div[@class="item"]/text()')
# publish_time=html.xpath('/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/text()')
# source=html.xpath('/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/text()')
# abstract_txt=html.xpath('//div[@class="txt"]/text()')
# con=html.xpath("//p/text()")



# print("------------------------------------------------------------------")
# print("标题:",tit)
# print(publish_time)
# print(source)
# print(abstract_txt)
# print(con)

 