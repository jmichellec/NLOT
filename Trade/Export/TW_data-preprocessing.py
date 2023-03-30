"""
After downloading files from TW trade data office and putting them in the same folder,
this code can be used to concatenate all files together and clean the files.
Exchange rate etc. or calculations from USD to EUR needs to be done manually or by adaptation of this code.
"""
import pandas as pd
import os

def str_to_million_int(string, million=0):
    mil_int = float(string.replace(',',''))
    if million == 0:
        return mil_int/1000000
    return mil_int

def transform_excel(file, million=0):
    df = pd.read_excel(file)
    df_tw = preprocess_tw_dfs(df, million)
    df_tw_new = df_tw.iloc[:, [0, 1, 5, -3, -2, -1]]
    return df_tw_new

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
    df_others['millions in USD'] = str_to_million_int(df_others.iloc[:, [3]].squeeze(), million)
    df_tw['SHORT_CODE'] = df_tw.CODE_NAME.apply(lambda x: x.split(';')[0])
    df_tw['year'] = year
    df_others['year'] = year
    df_tw = pd.concat([df_tw, df_others])
    return df_tw    # remove empty rows


def main():
    # Excels are in USD
    folder = "TW_export_data-2018-2022"
    path = os.listdir(folder)
    df_excels = []

    excels_filters = []
    for file in path:
        if 'Rb_4' in file:
            if file.endswith('.xlsx'):
                name = folder + '//' + file
                excels_filters.append(name)
    for file in excels_filters:
        df_tw_new = transform_excel(file, million=1)
        df_excels.append(df_tw_new)


    # df_2018 = df_excels[0]
    # df_2019 = df_excels[1]
    # df_2020 = df_excels[2]
    # df_2021 = df_excels[3]
    # df_2022 = df_excels[4]
    df_excels = pd.concat(df_excels)
    df_excels.to_excel("Export-all-updated-USD.xlsx")

if __name__ == "__main__":
    main()