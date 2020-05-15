#!/usr/bin/env python
# coding: utf-8

# This notebooks primary purpose is for my applied data science capstone project.

# In[1]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab")
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')


# In[2]:


get_ipython().system(u' pip install --upgrade pip')
get_ipython().system(u' pip install beautifulsoup4')
get_ipython().system('pip install lxml')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install requests')

#Importing packages
import requests
from bs4 import BeautifulSoup


# In[3]:


r = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
soup = BeautifulSoup(r.content, 'lxml')
table = soup.find_all('table')[0]

df = pd.read_html(str(table))

neighborhood=pd.DataFrame(df[0])


# In[4]:


postcode = []
borough = []
neighborhood = []
table_post = soup.find('table')
fields = table_post.find_all('td')


# In[5]:


for i in range(0, len(fields), 3):
    postcode.append(fields[i].text.strip())
    borough.append(fields[i+1].text.strip())
    neighborhood.append(fields[i+2].text.strip())


# In[6]:


df2 = pd.DataFrame(data=[postcode, borough, neighborhood]).transpose()
df2.columns = ['Postcode', 'Borough', 'Neighborhood']
df2.head(10)


# Below I removed all rows which have no assigned neighborhood

# In[7]:


df3 = df2[df2['Borough'] !='Not assigned']
df3.head()


# In[8]:


df3.groupby("Postcode").head(10)


# In[ ]:




