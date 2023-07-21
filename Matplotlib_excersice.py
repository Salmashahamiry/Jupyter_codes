#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
# we are using the inline backend
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[2]:


df_sale = pd.read_csv('company_sales_data.csv')

df_sale


# In[37]:


y_total_profit=df_sale['total_profit']
x_month_number=df_sale['month_number']

plt.plot(x_month_number,y_total_profit,linestyle=':',color='red',linewidth=3,marker='o',label='Profit')


# In[ ]:


#Exercise 3: Read all product sales data and show it using a multiline plot


# In[61]:


x_month_number=df_sale['month_number']
#y_total_profit=df_sale['total_profit']
y_total_units=df_sale['total_units']
y_moisturizer=df_sale['moisturizer']
y_shampoo=df_sale['shampoo']
y_bathingsoap=df_sale['bathingsoap']
y_toothpaste=df_sale['toothpaste']
y_facecream=df_sale['facecream']
y_facewash=df_sale['facewash']
y_bathingsoap=df_sale['bathingsoap']


plot_lable='Month Number vs. Sold units number'


#plt.plot(x_month_number,y_total_profit,linestyle=':',color='red',linewidth=3,marker='o',label='Profit')
plt.plot(x_month_number,y_total_units,linestyle=':',color='green',linewidth=3,marker='o',label='total units')
plt.plot(x_month_number,y_moisturizer,linestyle=':',color='blue',linewidth=3,marker='o',label='moisturizer')
plt.plot(x_month_number,y_shampoo,linestyle=':',color='pink',linewidth=3,marker='o',label='shampoo')
plt.plot(x_month_number,y_bathingsoap,linestyle=':',color='gold',linewidth=3,marker='o',label='bathingsoap')
plt.plot(x_month_number,y_toothpaste,linestyle=':',color='red',linewidth=3,marker='o',label='toothoaste')

plt.xlabel('Month number')
plt.ylabel('sold unit number')
plt.legend(loc='upper left')
#plt.show()


# In[38]:


#Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
#Also, add a grid in the plot. gridline style should “–“.
x_month_number=df_sale['month_number']
y_toothpaste=df_sale['toothpaste']


# In[55]:


plt.scatter(x_month_number, y_toothpaste,label="toothpaste")
plt.xlabel('Month number')
plt.ylabel('sold unit number')
plt.legend(loc='upper left')
plt.grid(linestyle='--')


# In[60]:


#Exercise 5: Read face cream and facewash product sales data and show it using the bar chart

plt.bar(x_month_number, y_facecream,color='red', label='face cream')
plt.bar(x_month_number, y_facewash,color='blue', label='face wash')
plt.legend(loc='upper left',bbox_to_anchor=(1,1)) 


# In[63]:


#Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
plt.bar(x_month_number, y_bathingsoap,color='pink', label='bathingsoap')

plt.legend(loc='upper left',bbox_to_anchor=(1,1)) 


# In[75]:


#Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
#df_sale_hist= df_sale['month_number']  # , df_sale['total_profit']
#df_sale_hist
#plt.hist(df_sale_hist,bins=10,edgecolor='black')


# In[ ]:




