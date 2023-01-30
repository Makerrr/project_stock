import requests
from bs4 import BeautifulSoup

req=requests.get(url="http://finance.eastmoney.com/a/202301112609941744.html")
req.encoding='utf-8'
html=req.text
soup=BeautifulSoup(html,'html.parser')
infos=soup.find_all("div",class_="item")
title=soup.find("div",class_="title")
article=soup.find("div",class_="contentbox")
info_lst=[]

for info in infos:
    info_lst.append(info.text.strip())

time=info_lst[0]
source=info_lst[1].replace('\n','').replace('\r','')
title=title.text.strip()
article=article.text.strip().replace('\n','').replace('\r','')

print(title)
print(time)
print(source)
print(article)

