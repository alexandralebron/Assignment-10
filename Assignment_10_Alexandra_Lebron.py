#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Alexandra Lebron
ISC 4551
Assignment 10
'''


# In[2]:


import pandas as pd
import numpy as np
import plotly.express as px
import requests


# In[3]:


urlUnemployment = "https://www.bls.gov/web/laus/laumstrk.htm"
response = requests.get(urlUnemployment, timeout=60)


# In[4]:


if (response.status_code != requests.codes.ok):
        print("Page not available")


# In[5]:


from html_table_parser.parser import HTMLTableParser

p = HTMLTableParser()
p.feed(response.text)

Unemployment = pd.DataFrame(p.tables[0])
Unemployment.columns = Unemployment.iloc[0]
Unemployment = Unemployment.drop(Unemployment.index[0])
Unemployment.rename(columns = {'February 2023 ( p ) rate':'unemployment'}, inplace = True)


# In[6]:


import us

name_to_abbr = us.states.mapping('name', 'abbr')

Unemployment['abbr'] = Unemployment['State'].map(name_to_abbr)
Unemployment['unemployment'] = pd.to_numeric(Unemployment['unemployment'])

Unemployment.head()


# In[88]:


colorList = [(0, '#f0f9e8'),(1/6, '#b6e3bb'), (2/6, '#75c8c5'),(3/6, '#4ba8c9'),(4/6, '#2989bd'),(5/6, '#0a6aad'),(1, '#254b8c')]

fig = px.choropleth(Unemployment, locations = "abbr", locationmode="USA-states", color = "unemployment",
                    scope = "usa", color_continuous_scale=colorList)
fig.show()


# In[ ]:




