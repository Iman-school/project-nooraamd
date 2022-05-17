#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np 


# In[47]:


import pandas as pd 


# In[48]:


df = pd.read_csv('StudentsPerformance.csv', )
df.head(10)


# In[49]:


df.info()


# In[53]:


df.isnull().sum()


# In[58]:


import numpy as np
numeric=df.select_dtypes(include-np.number)
numeric_columns=numeric.columns


# In[40]:


#print the numeric columns
numeric


# In[55]:


df['math score'].fillna(df['math score*].mean(),inplace-True)
df.info()


# In[42]:


df['reading score'].fillna(df['reading score*].mean(), inplace-True)
df.info()


# In[43]:


df['writing score'].fillna(df['writing score*].mean(), inplace-True)
df.info()


# In[44]:


df.drop("test preparation course', axis=1, inplace= True)


# In[45]:


df.info()


# In[ ]:





# In[ ]:




