#!/usr/bin/env python
# coding: utf-8

# Hot Dining

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from datetime import date


# In[2]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine('sqlite://', echo=False)
connection = engine.connect()


# In[3]:


# Import scrapting dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
#from selenium import webdriver


# In[4]:


michelin_df= pd.read_csv('Michelin-Starred Restaurants.csv') 


# In[5]:


#michelin_df


# In[6]:


michelin_df['Reservation platform']=''


# In[7]:


#michelin_df


# In[8]:


#scrap resy reserable restaurants
executable_path = {'executable_path': '/Users/jeqian/Documents/DA Bootcamp/CU-NYC-DATA-PT-10-2019-U-C/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False,user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36")
resy_mich_url = 'https://blog.resy.com/2019/10/new-york-restaurants-michelin-star-2020/'
browser.visit(resy_mich_url)
#testing = first_found = browser.find_by_name('styled__AvailabilityDayWrapper').first
#print
# browser.click_link_by_partial_text('FULL IMAGE')
# browser.click_link_by_partial_text('more info')
resy_mich_html = browser.html
resy_mich_soup = BeautifulSoup(resy_mich_html, 'html.parser')
print(resy_mich_soup.prettify())
#resy_path = resy_soup.find(class_='ResyInlineBooking')
#browser.click_link_by_partial_text('next article arrow')


# In[16]:


resy_mich_list = resy_mich_soup.find_all('h3',class_="venue1-title")


# In[13]:


resy_mich_list.find_all("span")


# In[17]:


resy_restaurant_list = [result.find("span").text.strip() for result in resy_mich_list]


# In[18]:


michelin_df['Reservation platform']= michelin_df['name'].map(lambda res_name: "Resy" if res_name.strip() in resy_restaurant_list else None)


# In[19]:


michelin_df = michelin_df.drop(columns = "Unnamed: 0")




# In[21]:


#scrap open table reserable restaurants
executable_path = {'executable_path': '/Users/jeqian/Documents/DA Bootcamp/CU-NYC-DATA-PT-10-2019-U-C/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False,user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36")
opentable_mich_url = 'https://blog.opentable.com/2018/nyc-2019-michelin-starred-restaurants-reserve-your-next-best-meal-today/'
browser.visit(opentable_mich_url)
#testing = first_found = browser.find_by_name('styled__AvailabilityDayWrapper').first
#print
# browser.click_link_by_partial_text('FULL IMAGE')
# browser.click_link_by_partial_text('more info')
opentable_mich_html = browser.html
opentable_mich_soup = BeautifulSoup(opentable_mich_html, 'html.parser')
print(opentable_mich_soup.prettify())


# In[22]:


#opentable_mich_soup.find(class_="entry-content").find_all("strong")[1].find("a").text


# In[24]:


#[result.find("a").text for result in opentable_mich_soup.find(class_="entry-content").find_all("strong")[1:]]


# In[25]:


opentable_mich_list= []
for result in opentable_mich_soup.find(class_="entry-content").find_all("strong"):
    try: 
        res_name=result.find("a").text.strip()
        if len(res_name)> 0:
            opentable_mich_list.append(res_name)
    except: 
        pass





# In[26]:


michelin_df['Reservation platform']= michelin_df.apply(lambda row: "OpenTable" if row["name"].strip() in opentable_mich_list else row["Reservation platform"], axis=1)





# Convert to SQL
michelin_df.to_sql('users', con=engine, if_exists="replace")


# In[31]:


# Import Dependencies
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv

nRowsRead = 1000 # specify 'None' if want to read whole file
df1 = pd.read_csv('Michelin-Starred Restaurants.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'Michelin-Starred Restaurants.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')


# In[32]:


# Create a SQL Database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///restaurants.sqlite', echo=False)

# Convert to SQL
michelin_df.to_sql('restaurants', con=engine, if_exists="replace")


