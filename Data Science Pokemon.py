#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool


# In[3]:


df = pd.read_csv('pokemon.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.corr()


# In[7]:


f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()


# In[8]:


df.head(10)


# In[9]:


df.columns


# In[10]:


df.Speed.plot(kind='line', color = 'b', label = 'Speed', linewidth = 1, alpha = 0.5, grid = True)
df.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()


# In[11]:


# Scatter Plot 
# x = attack, y = defense
df.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')            # title = title of plot


# In[12]:


# Histogram
# bins = number of bar in figure
df.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.show()


# In[13]:


series = df['Defense']        # data['Defense'] = series
print(type(series))
data_frame = df[['Defense']]  # data[['Defense']] = data frame
print(type(data_frame))


# In[18]:


data = pd.read_csv('pokemon.csv')
data.head()


# In[17]:


data.tail()


# In[20]:


# columns gives column names of features
data.columns


# In[21]:


# shape gives number of rows and columns in a tuble
data.shape


# In[22]:


# info gives data type like dataframe, number of sample or row, number of feature or column, feature types and memory usage
data.info()


# In[23]:


print(data['Type 1'].value_counts(dropna =False))  # if there are nan values that also be counted
# As it can be seen below there are 112 water pokemon or 70 grass pokemon


# In[24]:


# For example max HP is 255 or min defense is 5
data.describe() #ignore null entries


# In[25]:


# For example: compare attack of pokemons that are legendary  or not
# Black line at top is max
# Blue line at top is 75%
# Red line is median (50%)
# Blue line at bottom is 25%
# Black line at bottom is min
# There are no outliers
data.boxplot(column='Attack',by = 'Legendary')


# In[26]:


data_new = data.head() #using only the top 5 rows and adding them to a new dataframe
data_new


# In[27]:


# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted


# In[28]:


# Index is name
# I want to make that columns are variable
# Finally values in columns are value
melted.pivot(index = 'Name', columns = 'variable',values='value')


# In[29]:


# Firstly lets create 2 data frame
data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row


# In[30]:


data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 0 : adds dataframes in row
conc_data_col


# In[31]:


# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')


# In[32]:


data.dtypes


# In[33]:


data.describe()


# In[ ]:





# In[ ]:




