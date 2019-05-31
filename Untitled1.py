
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


import seaborn as sns


# In[9]:


get_ipython().magic('matplotlib inline')


# In[10]:


from urllib.request import urlopen


# In[11]:


from bs4 import BeautifulSoup


# In[12]:


url = "http://stats.espncricinfo.com/ci/content/records/83548.html"


# In[13]:


html = urlopen(url)


# In[14]:


soup = BeautifulSoup(html, 'lxml')


# In[15]:


type(soup)


# In[16]:


title = soup.title


# In[17]:


print(title)


# In[18]:


text = soup.get_text()


# In[19]:


print(soup.text)


# In[20]:


soup.find_all('a')


# In[21]:


all_links = soup.find_all("a")


# In[22]:


for link in all_links:
    print(link.get("href"))


# In[23]:


rows = soup.find_all('tr')


# In[24]:


print(rows)


# In[25]:


for row in rows:
    row_td = row.find_all('td')


# In[26]:


print(row_td)


# In[27]:


type(row_td)


# In[28]:


str_cells = str(row_td)


# In[29]:


cleantext = BeautifulSoup(str_cells, "lxml").get_text()


# In[30]:


print(cleantext)


# In[31]:


import re


# In[32]:


list_rows = []


# In[33]:


for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
    


# In[34]:


print(clean2)


# In[35]:


type(clean2)


# In[36]:


df = pd.DataFrame(list_rows)


# In[37]:


df1 = df[0].str.split(',', expand=True)
df1.head(10)


# In[38]:


df1[0] = df1[0].str.strip('[')
df1.head(10)


# In[39]:


col_labels = soup.find_all('th')


# In[40]:


all_header = []


# In[41]:


col_str = str(col_labels)


# In[42]:


cleantext2 = BeautifulSoup(col_str, "lxml").get_text()


# In[43]:


all_header.append(cleantext2)


# In[44]:


print(all_header)


# In[45]:


df2 = pd.DataFrame(all_header)


# In[46]:


df2.head()


# In[47]:


df2 = pd.DataFrame(all_header)


# In[48]:


df2.head()


# In[49]:


df3 = df2[0].str.split(',', expand=True)


# In[50]:


df3.head()


# In[51]:


frames = [df3, df1]


# In[52]:


df4 = pd.concat(frames)


# In[53]:


df4.head(10)


# In[54]:


df5 = df4.rename(columns=df4.iloc[0])


# In[55]:


df5


# In[56]:


df5.info()


# In[57]:


df5.shape


# In[58]:


df6 = df5.dropna(axis=0, how='any')


# In[59]:


df7 = df6.drop(df6.index[0])


# In[60]:


df7.head()


# In[61]:


df7.rename(columns={'[Player': 'Player'},inplace=True)
df7.rename(columns={' 6s]': '6s'},inplace=True)
df7.head()


# In[62]:


df7['6s'] = df7['6s'].str.strip(']')
df7.head()


# In[63]:


df7.shape


# In[64]:


df7.columns


# In[65]:


df7.columns = df7.columns.str.strip()


# In[66]:


df7[['Player', 'Mat', 'Inns', 'Runs','HS']].head()


# In[67]:


df7.describe()


# In[68]:


df7[['Player', 'Span', 'Inns','Runs']].max()


# In[69]:


df7['Runs'].max()


# In[70]:


df7.sort_values(by='Runs')


# In[71]:


df7.sort_values(by=['Span','Runs'])


# In[72]:


df7.sort_values(by='Runs', ascending = False)


# In[73]:


df7.columns


# In[74]:


df7.sum(axis = 0, skipna = True) 


# In[75]:


df7[df7['Player'] == "Yuvraj Singh (Asia/INDIA)"]


# In[76]:


df7.columns


# In[83]:


df7.dtypes


# In[99]:


df7['Mat'] = df7.Mat.astype(int)
df7['Inns'] = df7.Inns.astype(int)
df7['Runs'] = df7.Runs.astype(int)


# In[95]:


df7.dtypes


# In[109]:


df7[df7['Runs'] > 15000]


# In[110]:


df7[(df7['Runs']>15000) & (df7['Inns']>400)]


# In[111]:


df7[(df7['Runs']>15000) | (df7['Inns']>400)]


# In[112]:


df7.describe()

