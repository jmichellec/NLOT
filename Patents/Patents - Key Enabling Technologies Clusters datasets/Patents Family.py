#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os
import pandas as pd
from collections import defaultdict


# In[38]:


folder = "Patent families/"
df_dict = defaultdict(list)
for file_name in os.listdir(folder):
    country = file_name[:2]
    file = pd.read_excel(folder+file_name)
    file['Lens IDs'] = file['Lens IDs'].apply(lambda x: ';;'.join(sorted(x.split(';;'))))
    df_dict[country].append(file)


# In[39]:


for key in df_dict.keys():
    df_dict[key] = pd.concat(df_dict[key], ignore_index=True)


# In[34]:


df[df['Lens IDs'] == '199-179-825-057-897']


# In[43]:


dupes_ids = []
for country in df_dict.keys():
    seen = set()
    dupes = []
    df = df_dict[country]
    for x in df['Lens IDs']:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    print(country)
    print(len(dupes))
    dupes_ids.append(dupes)


# In[48]:


dupes_JP = dupes_ids[0]
dupes_KR = dupes_ids[1]
dupes_NL = dupes_ids[2]
dupes_TW = dupes_ids[3]
dupes_US = dupes_ids[4]

dupes_TW


# In[41]:


for file_name in os.listdir(folder):
    if 'semicon' in file_name:
        country = file_name[:2]
        file = pd.read_excel(folder+file_name)
        print(country)
        print(len(file))


# In[42]:


for file_name in os.listdir(folder):
    if 'digket' in file_name:
        country = file_name[:2]
        file = pd.read_excel(folder+file_name)
        print(country)
        print(len(file))

