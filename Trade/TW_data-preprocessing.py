{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0b22b4fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "23efe5ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['FSC3020R_Rb_2_2022.tsv',\n",
       " 'FSC3020R_Rb_2_2022.xlsx',\n",
       " 'FSC3020R_Rb_4_2018.tsv',\n",
       " 'FSC3020R_Rb_4_2018.xlsx',\n",
       " 'FSC3020R_Rb_4_2019.tsv',\n",
       " 'FSC3020R_Rb_4_2019.xlsx',\n",
       " 'FSC3020R_Rb_4_2020.tsv',\n",
       " 'FSC3020R_Rb_4_2020.xlsx',\n",
       " 'FSC3020R_Rb_4_2021.tsv',\n",
       " 'FSC3020R_Rb_4_2021.xlsx',\n",
       " 'FSC3020R_Rb_4_2022.tsv',\n",
       " 'FSC3020R_Rb_4_2022.xlsx',\n",
       " 'FSC3020R_Rb_4_2022_30.tsv',\n",
       " 'FSC3020R_Rb_4_2022_30.xlsx',\n",
       " 'FSC3020R_Rb_6_2022.tsv',\n",
       " 'FSC3020R_Rb_6_2022.xlsx',\n",
       " 'FSC3020R_Rb_8_2022.tsv',\n",
       " 'FSC3020R_Rb_8_2022.xlsx']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.listdir(\"Downloaded_data\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "effcbd11",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess_tw_dfs(df_tw, million=0):\n",
    "    \"\"\"\n",
    "    Function to preprocess dataframes from TW trade gov website\n",
    "    \"\"\"\n",
    "    new_header = df_tw.iloc[7] # get header of datafram3\n",
    "    df_tw = df_tw[8:] # content\n",
    "    df_tw.columns = new_header # \n",
    "    \n",
    "    year = df_tw.columns[3][:4]\n",
    "    df_others = df_tw[df_tw['CCC_CODE'] == 'Others']\n",
    "    df_tw = df_tw.dropna()\n",
    "    df_tw['millions in USD'] = df_tw.iloc[:, [3]].squeeze().apply(lambda x: str_to_million_int(x, million))\n",
    "    df_tw['SHORT_CODE'] = df_tw.CODE_NAME.apply(lambda x: x.split(';')[0])\n",
    "    df_tw['year'] = year\n",
    "    df_tw = pd.concat([df_tw, df_others])\n",
    "    return df_tw    # remove empty rows\n",
    "    \n",
    "def str_to_million_int(string, million=0):\n",
    "    mil_int = float(string.replace(',',''))\n",
    "    if million == 0:\n",
    "        return mil_int/1000000\n",
    "    return mil_int\n",
    "\n",
    "def transform_excel(file, million=0):\n",
    "    df = pd.read_excel(file)\n",
    "    df_tw = preprocess_tw_dfs(df, million)\n",
    "    df_tw_new = df_tw.iloc[:, [0, 1, 5, -3, -2, -1]]\n",
    "    df_tw_new.to_csv(file.split('.')[0]+'.tsv', index=False, sep='\\t')\n",
    "    return df_tw_new"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca70e73b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Excels are in USD, Import\n",
    "path = os.getcwd() + '\\\\EZK_data\\\\Taiwan_data\\\\NL-import-from-TW'\n",
    "excels = glob.glob(os.path.join(path, \"*.xlsx\"))\n",
    "\n",
    "df_excels = []\n",
    "\n",
    "excels_filters = []\n",
    "for file in excels:\n",
    "    if '2022.' in file:\n",
    "        excels_filters.append(file)\n",
    "for file in excels_filters:\n",
    "    df_tw_new = transform_excel(file, million=1)\n",
    "    df_excels.append(df_tw_new) \n",
    "        \n",
    "# df_2018 = df_excels[0]  \n",
    "# df_2019 = df_excels[1]     \n",
    "# df_2020 = df_excels[2]\n",
    "# df_2021 = df_excels[3]\n",
    "# df_2022 = df_excels[4]\n",
    "\n",
    "df_22_2 = df_excels[0]  \n",
    "df_22_4 = df_excels[1]     \n",
    "df_22_6 = df_excels[2]\n",
    "df_22_8 = df_excels[3]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
