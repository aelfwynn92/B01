# SAMPLE 07-02-22: This script assigns ME forms to lemmas from spreadsheet from verblex_present.xlsx 'verblex_present_forspreadsheet'. It creates a list of lemmas by Origin.

# Importing libraries

#C:\Users\Izabella\Desktop\CorpusSearch\CorpusStuff\output_files\me_form_lemma.py

import pandas as pd
import numpy as np
import openpyxl
import re

def sets_origin(lemma_list,origin):
    str_list = [] # empty list to fill when looping
    str_template = '' # empty string to fill when looping

    for index in range(len(lemma_list)):
        str_template = f'%{origin}: (*VBP*|*HVP*|*DOP*|*BEP* idoms '
        for item in lemma_list:
            item = item.replace(' ','|')
            # print(item) # each item of the ME_lemma column that is TRUE for Germanic 
            vchar = item + '|' # verb + bar
            # print(f"vchar: {vchar}")
            str_template = str_template  + vchar

        str_list.append(str_template)

    # replaces last character (bar) with parenthesis
    str_template = str_template[:-1] + ')'

    return(str_template) # exports function's object

# Open .xlsx file


xlsx_file = pd.read_excel('verblex_present.xlsx', sheet_name = 'verblex_present_forspreadsheet')
xlsx_file.columns = xlsx_file.columns.str.replace(' ','_')
#print(xlsx_file.head)

# Extracting columns C (ME_lemma) and H, I, J, K

# print(xlsx_file.columns)
columns = ['ME_lemma', 'Germanic', 'Romance', 'Blended', 'ELSE']
df_lemma = xlsx_file[columns]
#print(df_lemma)

# Filtering lemmas according to origin

df_ger = df_lemma[(df_lemma['Germanic'] == True)]
#print(df_ger)
df_rom = df_lemma[(df_lemma['Romance'] == True)]
#print(df_rom)
df_blend = df_lemma[(df_lemma['Blended'] == True)]
#print(df_blend)
df_else = df_lemma[(df_lemma['ELSE'] == True)]
#print(df_else)

# 2. processing dataframe


# creating a list of all lemmas without repetitions
lemmas_ger = df_ger.ME_lemma.unique() #germanic

print(f"lemmas_ger:")
print(lemmas_ger)

lemmas_rom = df_rom.ME_lemma.unique() #romance

#print(f"lemmas_rom:")
#print(lemmas_rom)

lemmas_blend = df_blend.ME_lemma.unique() #blended

#print(f"lemmas_blend:")
#print(lemmas_blend)

lemmas_else = df_else.ME_lemma.unique() #else

# remove "nan"

# convert np array to list to remove nan
lemmas_else = list(lemmas_else)

lemmas_else.remove(np.nan)


# go through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping

# Return like this: %germanic: (*VBG*|*DAG*|*HAG* idoms depart|pray|ordain|save)

# for index in range(len(lemmas_ger)):
#     str_template = f'%germanic: (*VBG*|*DAG*|*HAG* idoms '
#     for item in lemmas_ger:
#         # print(item) # each item of the ME_lemma column that is TRUE for Germanic
#         vchar = item + '|'  # verb + bar
#         # print(f"vchar: {vchar}")
#         str_template = str_template + vchar

#     str_list.append(str_template)

# # replaces last character (bar) with parenthesis
# str_template = str_template[:-1] + ')'

# print(str_template)

# List of Germanic lemmas
list_ger = sets_origin(lemmas_ger, 'germanic')
# print(list_ger)
# print('\n')

# List of Romance lemmas
list_rom = sets_origin(lemmas_rom, 'romance')
# print(list_rom)
# print('\n')

# List of Blended lemmas
list_blend = sets_origin(lemmas_blend, 'blended')
# print(list_blend)
# print('\n')

# List of other lemmas (ELSE)
list_else = sets_origin(lemmas_else, 'other')
# print(list_else)


# Exporting files

# saving a file with a header and the lemma list, including all the forms available
with open("SAMPLE_nonprog_present_origin_layers.txt", 'w', encoding='utf-8') as f:
    f.write(list_ger)
    f.write('\n')
    f.write(list_rom)
    f.write('\n')
    f.write(list_blend)
    f.write('\n')
    f.write(list_else)
    f.write('\n')
