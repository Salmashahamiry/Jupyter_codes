#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('mamba install openpyxl==3.0.9 -y')


# In[2]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[3]:


df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')


# In[4]:


df_can.head()


# In[5]:


df_can.tail()


# In[6]:


df_can.info(verbose=False)


# In[7]:


df_can.columns


# In[8]:


df_can.index


# In[13]:


print(type(df_can.columns))
print(type(df_can.index))   


# In[15]:


#To get the columns as lists, we can use the tolist() method.

df_can.columns.tolist()


# In[16]:


##To get the index and columns as lists, we can use the tolist() method.

df_can.index.tolist()


# In[17]:


print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))


# In[19]:


#To view the dimensions of the dataframe, we use the shape instance variable of it.

# size of dataframe (rows, columns)
df_can.shape


# In[20]:


#Let's clean the data set to remove a few unnecessary columns. We can use pandas drop() method as follows:

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# In[22]:


df_can.shape


# In[23]:


Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows:

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns


# df_can['Total'] = df_can.sum(axis=0)
# df_can['Total']
# df_can.head()

# In[30]:


#We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:

df_can['Total'] = df_can.sum(axis=1)
df_can['Total']
df_can.head()


# In[31]:


#We can check to see how many null objects we have in the dataset as follows:

df_can.isnull().sum()


# In[32]:


df_can.describe()


# In[ ]:


#pandas Intermediate: Indexing and Selection (slicing)


# In[ ]:


#Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.

 #   df.column_name               # returns series
#Method 2: More robust, and can filter on multiple columns.

#    df['column']                  # returns series
 #   df[['column 1', 'column 2']]  # returns dataframe


# In[33]:


df_can.Country  # returns a series


# In[36]:


#Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.

df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.


# In[45]:


#Select Row
#There are main 2 ways to select rows:

 #   df.loc[label]    # filters by the labels of the index/column
 #   df.iloc[index]   # filters by the positions of the index/column


# In[37]:


#Before we proceed, notice that the default index of the dataset is a numeric range from 0 to 194.
#This makes it very difficult to do a query by a specific country. For example to search for data on Japan,
#we need to know the corresponding index value.

#This can be fixed very easily by setting the 'Country' column as the index using set_index() method.


df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.head(3)


# In[47]:


# optional: to remove the name of the index
df_can.index.name = None
df_can.head(3)


# In[48]:


#Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios: 1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985

# 1. the full row data (all columns)
df_can.loc['Japan']


# In[49]:


# alternate methods
df_can.iloc[87]


# In[52]:


df_can[df_can.index == 'Japan']


# In[53]:


# 2. for year 2013
df_can.loc['Japan', 2013]


# In[54]:


# alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]


# In[55]:


# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]


# In[58]:


#Column names that are integers (such as the years) might introduce some confusion. For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index.

#To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.

df_can.columns = list(map(str, df_can.columns))


# In[59]:


#Filtering based on a criteria 
#To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.

#For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)


# In[60]:


# 2. pass this condition into the dataFrame
df_can[condition]


# In[61]:


#Sorting Values of a Dataframe or Series
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5


# In[ ]:




