# This script assigns ME forms to lemmas from spreadsheet from verblex4_lemma.xlsx '15-07-21 verblex4_lemma3'.

# Importing libraries

#C:\Users\Izabella\Desktop\CorpusSearch\CorpusStuff\output_files\me_form_lemma.py

import pandas as pd
import numpy as np
import openpyxl
import re

def sets_wordlength(lemma_list,wordlength):
    str_list = [] # empty list to fill when looping
    str_template = '' # empty string to fill when looping

    for index in range(len(lemma_list)):
        str_template = f'%{wordlength}: (*VAG*|*DAG*|*HAG* idoms '
        for item in lemma_list:
            # print(item) # each item of the ME_lemma column that is TRUE for 1 
            vchar = item + '|' # verb + bar
            # print(f"vchar: {vchar}")
            str_template = str_template  + vchar
            
        str_list.append(str_template)


    # replaces last character (bar) with parenthesis
    str_template = str_template[:-1] + ')'

    return(str_template) # exports function's object

# Open .xlsx file

xlsx_file = pd.read_excel('verblex4_lemma.xlsx', sheet_name = '21-10-21 verblex4_lemma3')
xlsx_file.columns = xlsx_file.columns.str.replace(' ','_')
print(xlsx_file.head)

# Extracting columns C, E, L, M, N, O, P, Q

# print(xlsx_file.columns)
columns = ['ME_lemma', 'word-length_ME', 'ME_lemma_1', 'ME_lemma_1half', 'ME_lemma_2', 'ME_lemma_2half', 'ME_lemma_3', 'ME_lemma_else']
df_wl = xlsx_file[columns]
print(df_wl)

# Filtering lemmas according to origin

df_1 = df_wl[(df_wl['ME_lemma_1'] == True)]
#print(df_1)
df_1half = df_wl[(df_wl['ME_lemma_1half'] == True)]
#print(df_1half)
df_2 = df_wl[(df_wl['ME_lemma_2'] == True)]
#print(df_2)
df_2half = df_wl[(df_wl['ME_lemma_2half'] == True)]
#print(df_2half)
df_3 = df_wl[(df_wl['ME_lemma_3'] == True)]
#print(df_3)
df_else = df_wl[(df_wl['ME_lemma_else'] == True)]
#print(df_else)


# 2. processing dataframe


# creating a list of all lemmas without repetitions
lemmas_1 = df_1.ME_lemma.unique() #1

print(f"lemmas_1:")
print(lemmas_1)

lemmas_1half = df_1half.ME_lemma.unique() #1half

print(f"lemmas_1half:")
print(lemmas_1half)

lemmas_2 = df_2.ME_lemma.unique() #2

print(f"lemmas_2:")
print(lemmas_2)

lemmas_2half = df_2half.ME_lemma.unique() #2half

print(f"lemmas_2half:")
print(lemmas_2half)

lemmas_3 = df_3.ME_lemma.unique() #3

print(f"lemmas_3:")
print(lemmas_3)

lemmas_else = df_else.ME_lemma.unique() #else

print(f"lemmas_else:")
print(lemmas_else)

# remove "nan"

# convert np array to list to remove nan
lemmas_else = list(lemmas_else)

lemmas_else.remove(np.nan)

# go through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping
#print(str_template)

# List of 1-syllable lemmas
list_1 = sets_wordlength(lemmas_1, '1')
print(list_1)
print('\n')

# List of 1half-syllable lemmas
list_1half = sets_wordlength(lemmas_1half, '1half')
print(list_1half)
print('\n')

# List of 2-syllable lemmas
list_2 = sets_wordlength(lemmas_2, '2')
print(list_2)
print('\n')

# List of 2half-syllable lemmas
list_2half = sets_wordlength(lemmas_2half, '2half')
print(list_2half)
print('\n')

# List of 3-syllable lemmas
list_3 = sets_wordlength(lemmas_3, '3')
print(list_3)
print('\n')

# List of else/nan lemmas
list_else = sets_wordlength(lemmas_else, 'else')
print(list_else)
print('\n')

# Exporting files

# saving a file with a header and the lemma list, including all the forms available
with open("prog_wordlength_layers.txt", 'w', encoding='utf-8') as f:
    f.write(list_1)
    f.write('\n')
    f.write(list_1half)
    f.write('\n')
    f.write(list_2)
    f.write('\n')
    f.write(list_2half)
    f.write('\n')
    f.write(list_3)
    f.write('\n')
    f.write(list_else)
    f.write('\n')