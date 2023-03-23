#!/usr/bin/env python
# coding: utf-8




from collections import defaultdict
import lens_analysis as la
from lens_analysis.applicant_labeler import TW_LABELER
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
import pickle as pkl
from tqdm.notebook import tqdm_notebook




folder = "Patents - Key Enabling Technologies Clusters datasets/"
df_dict = defaultdict(list)

for file_name in os.listdir(folder):
    if file_name.endswith(".csv"):
        # Identify category and subcategory of file
        ids = file_name.split('-')
        category = ids[0]
        sub_category = ids[1]
        
        category_name = category + sub_category
        # read in file
        path = folder + file_name
        df =  pd.read_csv(path, index_col=0) # file_name #can be used for check
        df_dict[category_name].append(df)
        
# Concatenate all the dataframes within the same key. Update value in key with concatenated version of value lists in key
for key in df_dict.keys():
    df_dict[key] = pd.concat(df_dict[key], ignore_index=True).drop_duplicates()
    # display(df_dict[key]) # to check 




df_dict['JPdigket']




# # Concatenate dataframes per subcategory/subfield and append to list
# all_dfs = []
# folder = 'Lens-data/' # or whatever folder you wish

# df_dict = defaultdict(list)

# for file_name in os.listdir(folder):
#     if file_name.endswith(".csv"):
#         # Identify category and subcategory of file
#         ids = file_name.split('-')
#         category = ids[0]
#         sub_category = ids[1]
        
#         category_name = category + sub_category
#         # read in file
#         path = folder + file_name
#         df =  pd.read_csv(path, index_col=0) # file_name #can be used for check
#         df_dict[category_name].append(df)
        
# # Concatenate all the dataframes within the same key. Update value in key with concatenated version of value lists in key
# for key in df_dict.keys():
#     df_dict[key] = pd.concat(df_dict[key]).drop_duplicates()
#     # display(df_dict[key]) # to check 





applicant_types_list = [] # indices match indices of keys of dictionary

for key, df in tqdm_notebook(df_dict.items()):
    print(key) # to keep track of progress
    families = la.aggregate_to_family(df)
    name = key + '_families.xlsx'
    families.to_excel(name, index=True)
#     families = la.add_extra_family_information(families)
#     applicants = la.aggregate_to_applicants(families)
#     applicants = la.add_labels(applicants, labeler=TW_LABELER)
#     applicant_types = la.aggregate_to_applicant_types(applicants)
#     applicant_types_list.append(applicant_types)





# with open('applicants_types_list.pickle', 'wb') as f:
#     pkl.dump(applicants_types_list, f)





# applicants.to_excel('applicants-photonics-1.xlsx')

