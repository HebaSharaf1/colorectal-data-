#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


df = pd.read_csv('normal_data.csv')
df.head()


# In[13]:


df['smoking_history'].replace({'Non-smoker': 'no' , 'Ex-smoker': 'no' ,'Smoker: pack years unknown': 'yes'} , inplace=True)
df['sex'].replace({'Male': 'M' , 'Female': 'F'} , inplace=True)
df.head()


# In[14]:


df.rename(columns={'smoking_history' :'smoker' ,'Unnamed: 0' : 'rank' , 'sex':'gender'} , inplace=True )
df.head()


# In[15]:


dh=pd.read_csv('hospital_data1.csv')
dh.head()


# In[17]:


dh.rename(columns={'Unnamed: 0' : 'rank'} , inplace=True)
dh.head()


# In[20]:


frames=[df,dh]
WDATA=pd.concat([df,dh])
WDATA.head()


# In[ ]:




