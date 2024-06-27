#!/usr/bin/env python
# coding: utf-8

# In[1]:


#read data from file
import pandas as pd
df=pd.read_csv("D:\Data Analyst\Retail_orders.zip")
df.head(10)


# In[2]:


#handle null values
df['Ship Mode'].unique()


# In[3]:


df=pd.read_csv("D:\Data Analyst\Retail_orders.zip",na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[6]:


#rename columns(convert to lowercase and replace space with underscore)
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head()


# In[8]:


#add new columns- discount,sale price and profit
df['discount']=df['list_price']*df['discount_percent']/100
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']


# In[9]:


#drop the list_price,cost_price,discount_percent columns
df.drop(['list_price','cost_price','discount_percent'],axis=1,inplace=True)
df


# In[10]:


#change datatype of order_date to datetime
df['order_date']=pd.to_datetime(df['order_date'],format='%Y-%m-%d')


# In[11]:


df.dtypes


# In[12]:


#create a connection to load data to MySQL workbench
get_ipython().system(' pip install pymysql')


# In[13]:


get_ipython().system(' pip install sqlalchemy')


# In[14]:


from sqlalchemy import create_engine
engine= create_engine(f'mysql+pymysql://root:NeerajaMySQL@localhost/retail_orders')


# In[20]:


table_name = 'orders'
df.to_sql(name= 'orders', con=engine, if_exists='append', index=False)


# In[ ]:




