#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

google_url = 'https://www.google.com.tw/search'

my_params = {'q': '寒流'}

r = requests.get(google_url, params = my_params)

soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify())

items = soup.select('div.kCrYT > a[href^="/url"]')
#print(items)

for i in items:
    # 標題
    print("標題：" + i.text)
    # 網址
    print("網址：" + i.get('href'))
    print()


# In[ ]:




