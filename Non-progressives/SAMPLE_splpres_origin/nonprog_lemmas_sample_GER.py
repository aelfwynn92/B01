# This script extracts a randomised sample of Non-progressives' Germanic lemmas (spreadsheet for present tense "verblex_present.xlsx").

# Importing libraries

#C:\Users\Izabella\Desktop\CorpusSearch\CorpusStuff\output_files\me_form_lemma.py

import pandas as pd
import openpyxl
import re
import random
import string

#LOOP

def sets_origin(lemma_list,origin):
    str_list = [] # empty list to fill when looping
    str_template = '' # empty string to fill when looping

    for index in range(len(lemma_list)):
        str_template = f'24.02.2022 - The sample out of {length} {origin} lemmas are: \r{ger_choice}'
    return(str_template) # exports function's object

# 1. Open .xlsx file

xlsx_file = pd.read_excel('verblex_present2.xlsx', sheet_name = 'verblex_present_forspreadsheet')
#xlsx_file.columns = xlsx_file.columns.str.replace(' ','_')
print(xlsx_file.head)


# 2. Extracting column C (ME lemmas)

print(xlsx_file.columns)
columns = ['ME_lemma', 'Germanic', 'Romance', 'Blended', 'ELSE']
df_lemma = xlsx_file[columns]

# 2.1. convert columns to text type
df_lemma['ME_lemma'] = df_lemma['ME_lemma'].astype(str)


# 3. Filtering lemmas according to origin

df_ger = df_lemma[(df_lemma['Germanic'] == True)]
print(df_ger)


# 4. Processing dataframe

# 4.1. creating a list of all lemmas without repetitions
lemmas_ger = df_ger.ME_lemma.unique() #germanic

print(f"lemmas_ger:")
print(lemmas_ger)


# 5. Sampling lemmas_ger

# 5.1. Counting Germanic lemmas
length = len(lemmas_ger)
print(length) # 205 Germanic lemmas

print(f"gerlist:{lemmas_ger}")

# def germanic_verbs(gerlist,size=10): 
#     result_ger = '\n'.join(random.choice(gerlist) for i in range(size))
#     return(result_ger)

# ger_choice = germanic_verbs(gerlist=lemmas_ger, size=100)

# print(ger_choice)

def sample_germanic_verbs (ger_list, size = 10):
    unique_list = list(set(ger_list))
    sampled_ger = random.sample(unique_list, size)
    return (sampled_ger)

sampled_germanic_verbs = sample_germanic_verbs(ger_list=lemmas_ger, size=100)

def concat_str_germanic_verbs(sampled_gerlist):    
    
    result_ger = ''
    for item in sampled_gerlist:
        result_ger += item
        result_ger += '|'
    result_ger = result_ger[:-1] # remove final '|'
    return(result_ger)

ger_choice = concat_str_germanic_verbs(sampled_germanic_verbs)

print(ger_choice)
print(len(ger_choice))

# 5.2. going through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping

# 5.3. List of Germanic lemmas
list_ger = sets_origin(lemmas_ger, 'germanic')
#print(list_ger)
#print('\n')

# 6. Exporting files

# 6.1. saving a file with the lemma list
with open("nonprog_present_sample_GER.txt", 'w', encoding='utf-8') as f:
    f.write(list_ger)
    f.write('\n')
