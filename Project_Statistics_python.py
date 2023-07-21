#!/usr/bin/env python
# coding: utf-8

# Course 7 
# Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The disease was first identified in 2019 in Wuhan, China, and has since spread globally, resulting in the 2019–20 coronavirus pandemic. Common symptoms include fever, cough and shortness of breath. Muscle pain, sputum production and sore throat are less common. The rate of deaths per number of diagnosed cases is on average 3.4%, ranging from 0.2% in those less than 20 to approximately 15% in those over 80 years old.
# Data Source (Date wise) : 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE
# Data Source:

# In[1]:


import pandas as pd
path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-04-2021.csv'
df= pd.read_csv(path)
df.head()    


# In[2]:


df.isna().sum()


# In[3]:


import pandas as pd
import numpy as np

df= pd.read_csv(path)
df.head()


# Field description
# •	Province/State: China - province name; US/Canada/Australia/ - city name, state/province name; Others - name of the event (e.g., "Diamond Princess" cruise ship); other countries - blank.
# •	Country/Region: country/region name conforming to WHO (will be updated).
# •	Last Update: MM/DD/YYYY HH:mm (24 hour format, in UTC).
# •	Confirmed: the number of confirmed cases. For Hubei Province: from Feb 13 (GMT +8), we report both clinically diagnosed and lab-confirmed cases. For lab-confirmed cases only (Before Feb 17), please refer to who_covid_19_situation_reports. For Italy, diagnosis standard might be changed since Feb 27 to "slow the growth of new case numbers." (Source)
# •	Deaths: the number of deaths.
# •	Recovered: the number of recovered cases.
# 
# 
# Using above dataset we have created some exercises on COVID-19 (Spread of the novel coronavirus, Analysis, Visualization, Prediction & Comparisons.
# 
# 
# Please use jupyter lab on your local computer to solve all the questions written below. Each group needs to share one ipynb file.

# 1.	Write a Python program to display first 5 rows from COVID-19 dataset. Also print the dataset information and check the missing values.

# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.isna().sum()


# 2.	Write a python program to replace all the missing values with “Tobefound” for province column.

# In[7]:


df['Province_State'].fillna('To_be_found', inplace= True)
df['Province_State'].value_counts


# 3.	Normalize the values for “Recovered” column as per the z-score.

# In[8]:


df.head()


# In[9]:


df.dtypes


# In[10]:


df['Recovered'].fillna(0, inplace= True)


# In[11]:


from scipy import stats
stats.zscore(df['Recovered'])


# In[12]:


df['Recovered'].isna().sum()


# 4.	Create bin values for “Recovered” column in the data set.

# In[13]:


df['Recovered']


# In[14]:


pd.qcut(df['Recovered'], q= 4 )


# 5.	Write a Python program to get the maximum number of confirmed, deaths, recovered and active cases of Novel Coronavirus (COVID-19) Country wise.

# In[15]:


df['Country_Region'].value_counts()


# In[16]:


result = df.groupby(['Country_Region'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum()
print(result)


# 6.	 Write a Python program to get the total number of confirmed deaths and recovered people of Novel Coronavirus (COVID-19) cases Country/Region - Province/State wise

# In[17]:


df.groupby(['Country_Region', 'Province_State'])['Deaths', 'Recovered', 'Confirmed'].sum()


# 7.	Write a Python program to get the country wise (country name taken as input from user) cases of confirmed, deaths and recovered cases of Novel Coronavirus (COVID-19).

# In[18]:


df.head()


# In[19]:


df.groupby(['Country_Region'])['Deaths', 'Recovered', 'Confirmed'].sum()


# 8.	Write a Python program to get the country wise deaths cases of Novel Coronavirus (COVID-19).

# In[20]:


df.groupby('Country_Region')['Deaths'].sum()


# 9.	Write a Python program to list countries with no cases of Novel Coronavirus (COVID-19) recovered.

# In[21]:


df['Recovered'].value_counts


# 10.	 Write a Python program to list countries where all cases of Novel Coronavirus (COVID-19) died.

# In[22]:


df.columns


# In[23]:


df.loc[df['Confirmed']== df['Deaths']]


# 11.	 Write a Python program to list countries with all cases of Novel Coronavirus (COVID-19) recovered.

# In[24]:


df.loc[df['Confirmed']== df['Recovered']]


# 12.	 Write a Python program to get the top 10 countries data (Last Update, Country/Region, Confirmed, Deaths, Recovered) of Novel Coronavirus (COVID-19).

# In[25]:


df['Last_Update'].dtype


# In[26]:


df.dtypes


# In[27]:


df[['Recovered', 'Active']]= df[['Recovered', 'Active']].astype('int')
df.dtypes


# In[28]:


# Lets assume top 10 countries according to deaths, Recovered', 'Active'

df3= df.sort_values(['Deaths','Recovered', 'Active'], ascending= False)
df3.head(10)


# 13.	Write a Python program to create a plot (lines) of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 150.

# In[29]:


#df4 = df['Deaths'] > 150


# In[34]:


df4= df[df['Deaths'] > 150]
df4.head()


# In[43]:


pd.options.display.max_colwidth = 300


# In[60]:


plt.rcParams["figure.figsize"] = (50, 32)


# In[63]:


import matplotlib.pyplot as plt
#figsize= (20,10)
plt.plot(df['Province_State'], df['Deaths'])
#plt.figure(figsize=(100, 50))
plt.xticks(rotation='vertical')


# In[63]:


import matplotlib.pyplot as plt
#figsize= (20,10)
plt.plot(df['Province_State'], df['Deaths'])
#plt.figure(figsize=(100, 50))
plt.xticks(rotation='vertical')


# In[ ]:




