#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time
import urllib.request as request
from bs4 import BeautifulSoup as sp

local_time = time.ctime(time.time())
url="https://rate.bot.com.tw/gold?Lang=zh-TW"
with request.urlopen(url) as response:
  data=response.read().decode("utf-8")
  root=sp(data,"html.parser")
  gold_in=(root.find_all("td")[5].text.replace("回售","").strip())
  gold_out=(root.find_all("td")[2].text.replace("買進","").strip()) ###
  print("黃金回售 ->" , gold_in)
  print("黃金買進 ->" , gold_out)
  time.sleep(1)


# In[ ]:




