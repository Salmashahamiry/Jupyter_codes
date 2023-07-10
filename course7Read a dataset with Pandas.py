#!/usr/bin/env python
# coding: utf-8

# In[1]:


#install specific version of libraries used in  lab
#! mamba install pandas==1.3.3  -y
#! mamba install numpy=1.21.2 -y


# In[4]:


# import pandas library
import pandas as pd
import numpy as np


# In[10]:


path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"

df = pd.read_csv(path, header=None)


# In[11]:


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)


# In[12]:


# Write your code below and press Shift+Enter to execute 
print("The last 10 rows of the dataframe\n")
df.tail(10)


# In[13]:


# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


# In[14]:


df.columns = headers
df.head(10)


# In[16]:


#We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace('?',np.NaN)
df1.head(10)


# In[18]:


df=df1.dropna(subset=["price"], axis=0)
df.head(10)


# In[19]:


# Write your code below and press Shift+Enter to execute 
print(df.columns)


# In[20]:


df.to_csv("automobile.csv", index=False)


# In[21]:


#tell the type of each column
df.dtypes


# In[23]:


#get a statistical summary of each column e.g. count, column mean value, column standard deviation, etc., we use the describe method:
df1.describe()


# In[24]:


# describe all the columns in "df" 
df.describe(include = "all")


# In[26]:


#we can choose some column
df[['length', 'compression-ratio']].describe()


# In[27]:


#It provides a concise summary of your DataFrame.

#This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
# look at the info of "df"
df.info()


# In[ ]:




