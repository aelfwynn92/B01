# This script extracts a randomised sample of Non-progressives' lemmas (spreadsheet for present tense "verblex_present.xlsx").

# Importing libraries

#C:\Users\Izabella\Desktop\CorpusSearch\CorpusStuff\output_files\me_form_lemma.py

import pandas as pd
import openpyxl
import re

#LOOP

def sets_origin(lemma_list,origin):
    str_list = [] # empty list to fill when looping
    str_template = '' # empty string to fill when looping

    for index in range(len(lemma_list)):
        str_template = f'The {origin} lemmas are:'
    return(str_template) # exports function's object

# 1. Open .xlsx file


xlsx_file = pd.read_excel('verblex_present.xlsx', sheet_name = 'verblex_present_forspreadsheet')
#xlsx_file.columns = xlsx_file.columns.str.replace(' ','_')
print(xlsx_file.head)

# 2. Extracting column C (ME lemmas)

print(xlsx_file.columns)
columns = ['ME_lemma', 'Germanic', 'Romance', 'Blended', 'ELSE']
df_lemma = xlsx_file[columns]

# convert columns to text type
df_lemma['ME_lemma'] = df_lemma['ME_lemma'].astype(str)

# 3. Filtering lemmas according to origin

df_ger = df_lemma[(df_lemma['Germanic'] == True)]
print(df_ger)
df_rom = df_lemma[(df_lemma['Romance'] == True)]
print(df_rom)
df_blend = df_lemma[(df_lemma['Blended'] == True)]
print(df_blend)
df_else = df_lemma[(df_lemma['ELSE'] == True)] # not needed in sample
#print(df_else) # not needed in sample

# 4. Processing dataframe

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

# SO FAR SO GOOD

# go through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping

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



