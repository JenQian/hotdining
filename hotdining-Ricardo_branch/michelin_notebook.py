#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# In[2]:


nRowsRead = 1000 # specify 'None' if want to read whole file
df1 = pd.read_csv('Michelin-Starred Restaurants.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'Michelin-Starred Restaurants.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')


# In[3]:


df1.head()


# In[4]:


# Import BeautifulSoup (just in case)
from bs4 import BeautifulSoup as bs


# In[5]:


# Import Browser (just in case)
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


# In[6]:


# List out the columns in df1
df1.columns


# In[7]:


# Create Michelin df w/ set to restuarant name
michelin_df = df1.set_index('name')
michelin_df.drop(["Unnamed: 0"], axis=1)
michelin_df.head()


# In[8]:


michelin_df.columns


# In[9]:


from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)

df = michelin_df


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)



if __name__ == '__main__':
    app.run(host='8.0.0.0')







