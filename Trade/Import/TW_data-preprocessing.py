#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os


os.listdir("Downloaded_data")

def preprocess_tw_dfs(df_tw, million=0):
    """
    Function to preprocess dataframes from TW trade gov website
    """
    new_header = df_tw.iloc[7] # get header of datafram3
    df_tw = df_tw[8:] # content
    df_tw.columns = new_header # 
    
    year = df_tw.columns[3][:4]
    df_others = df_tw[df_tw['CCC_CODE'] == 'Others']
    df_tw = df_tw.dropna()
    df_tw['millions in USD'] = df_tw.iloc[:, [3]].squeeze().apply(lambda x: str_to_million_int(x, million))
    df_tw['SHORT_CODE'] = df_tw.CODE_NAME.apply(lambda x: x.split(';')[0])
    df_tw['year'] = year
    df_tw = pd.concat([df_tw, df_others])
    return df_tw    # remove empty rows
    
def str_to_million_int(string, million=0):
    mil_int = float(string.replace(',',''))
    if million == 0:
        return mil_int/1000000
    return mil_int

def transform_excel(file, million=0):
    df = pd.read_excel(file)
    df_tw = preprocess_tw_dfs(df, million)
    df_tw_new = df_tw.iloc[:, [0, 1, 5, -3, -2, -1]]
    df_tw_new.to_csv(file.split('.')[0]+'.tsv', index=False, sep='\t')
    return df_tw_new


# In[ ]:


# Excels are in USD, Import
path = os.getcwd() + '\\EZK_data\\Taiwan_data\\NL-import-from-TW'
excels = glob.glob(os.path.join(path, "*.xlsx"))

df_excels = []

excels_filters = []
for file in excels:
    if '2022.' in file:
        excels_filters.append(file)
for file in excels_filters:
    df_tw_new = transform_excel(file, million=1)
    df_excels.append(df_tw_new) 
        
# df_2018 = df_excels[0]  
# df_2019 = df_excels[1]     
# df_2020 = df_excels[2]
# df_2021 = df_excels[3]
# df_2022 = df_excels[4]

df_22_2 = df_excels[0]  
df_22_4 = df_excels[1]     
df_22_6 = df_excels[2]
df_22_8 = df_excels[3]

