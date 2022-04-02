# This script extracts a randomised sample of Non-progressives' Romance lemmas (spreadsheet for present tense "verblex_present2.xlsx").

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
        str_template = f'24.02.2022 - The sample out of {length} {origin} lemmas are: \r{rom_choice}'
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

df_rom = df_lemma[(df_lemma['Romance'] == True)]
print(df_rom)


# 4. Processing dataframe

# 4.1. creating a list of all lemmas without repetitions
lemmas_rom = df_rom.ME_lemma.unique() #romance

print(f"lemmas_rom:")
print(lemmas_rom)


# 5. Sampling lemmas_rom

# 5.1. Counting Romance lemmas
length = len(lemmas_rom)
print(length) # 294 Romance lemmas

print(f"romlist:{lemmas_rom}")

# def romance_verbs(romlist,size=10): 
#     result_rom = '\n'.join(random.choice(romlist) for i in range(size))
#     return(result_rom)

# rom_choice = romance_verbs(romlist=lemmas_rom, size=100)

# print(rom_choice)

def sample_romance_verbs (rom_list, size = 10):
    unique_list = list(set(rom_list))
    sampled_rom = random.sample(unique_list, size)
    return (sampled_rom)

sampled_romance_verbs = sample_romance_verbs(rom_list=lemmas_rom, size=100)

def concat_str_romance_verbs(sampled_romlist):    
    
    result_rom = ''
    for item in sampled_romlist:
        result_rom += item
        result_rom += '|'
    result_rom = result_rom[:-1] # remove final '|'
    return(result_rom)

rom_choice = concat_str_romance_verbs(sampled_romance_verbs)

print(rom_choice)
print(len(rom_choice))

# 5.2. going through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping

# 5.3. List of Romance lemmas
list_rom = sets_origin(lemmas_rom, 'romance')
#print(list_rom)
#print('\n')

# 6. Exporting files

# 6.1. saving a file with the lemma list
with open("nonprog_present_sample_ROM.txt", 'w', encoding='utf-8') as f:
    f.write(list_rom)
    f.write('\n')
