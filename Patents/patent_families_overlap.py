"""
Reads in patent families excels and finds overlap between sectors.
"""

import os
import pandas as pd
from collections import defaultdict


# find duplicate Lens IDs per country | if possible: export data from Lens with index, as this is also identifier.
def calculate_overlapping_ids(df):
    # Keep id's that are seen and list with duplicates (based on that it is seen before)
    seen_ids = set()
    overlapping_ids = []

    for identifier in df['Lens IDs']:
        if identifier in seen_ids:
            overlapping_ids.append(identifier)
        else:
            seen_ids.add(identifier)

    return len(overlapping_ids)


def main():
    folder = "Patent families/"
    df_dict = defaultdict(list)

    overlap_dict = defaultdict(int)
    semicon_dict = defaultdict(int)
    digket_dict = defaultdict(int)

    for file_name in os.listdir(folder):
        country = file_name[:2]  # based on first two letters of files e.g. JPdigket_families

        # preprocess file
        file = pd.read_excel(folder + file_name)
        file['Lens IDs'] = file['Lens IDs'].apply(lambda x: ';;'.join(
            sorted(x.split(';;'))))  # sort the Lens IDs to find overlap when data was not exported with identifier

        if 'semicon' in file_name:
            semicon_dict[country] = len(file)

        elif 'digket' in file_name:
            digket_dict[country] = len(file)

        df_dict[country].append(file)  # create dictionary with country as key and add each dataframe as value

    for country in df_dict.keys():
        df_dict[country] = pd.concat(df_dict[country], ignore_index=True)
        df = df_dict[country]
        number_of_overlap = calculate_overlapping_ids(df)
        overlap_dict[country] = number_of_overlap

    # create excel file
    overlap_df = pd.DataFrame.from_dict([overlap_dict, semicon_dict, digket_dict]).transpose()
    overlap_df.columns = ['shared', 'semicon', 'digital']
    overlap_df.to_excel('patent-families-overlap-software-hardware.xlsx')

if __name__ == "__main__":
    main()
