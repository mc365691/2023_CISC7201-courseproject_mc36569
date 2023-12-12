#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


# In[20]:


start ='2016-01-01'
end = '2022-12-31'
#apple company stock name
stock = 'AAPL'
#data can download from
data=yf.download(stock, start, end)


# In[24]:


data.reset_index(inplace=True)


# In[25]:


data


# In[26]:


ma_100_days = data.Close.rolling(100).mean()


# In[33]:


plt.figure(figsize=(9,7))
plt.plot(ma_100_days, 'y')
plt.plot(data.Close, 'g')
plt.show()


# In[ ]:




