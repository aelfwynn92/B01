# This script assigns ME forms to lemmas from spreadsheet from verblex4_lemma.xlsx '15-07-21 verblex4_lemma3'.

# Importing libraries

#C:\Users\Izabella\Desktop\CorpusSearch\CorpusStuff\output_files\me_form_lemma.py

import pandas as pd
import openpyxl
import re

# Open .xlsx file


xlsx_file = pd.read_excel('verblex4_lemma.xlsx', sheet_name = '21-10-21 verblex4_lemma3')
xlsx_file.columns = xlsx_file.columns.str.replace(' ','_')
#print(xlsx_file.head)

# Extracting columns B (forms) and C (ME lemmas) for assignment

# print(xlsx_file.columns)
columns = ['PROG_form', 'ME_lemma']
df_lemma = xlsx_file[columns]

# convert columns to text type
df_lemma['PROG_form'] = df_lemma['PROG_form'].astype(str)

## replace + in PROG_form column by "___" and "-" by "__"

df_lemma['PROG_form'] = df_lemma['PROG_form'].replace('\+','___', regex = True)
df_lemma['PROG_form'] = df_lemma['PROG_form'].replace('\-','!', regex = True)


# Assign all equal cells in C to every corresponding cell in B

# 1. editing column B to get ONLY the form
df_lemma['PROG_form'] = df_lemma['PROG_form'].replace(' [0-9]+.*','', regex = True)
print(df_lemma)

# Return like this: accorden: a-cordyng|according|accordyng|accordynge|accordand|acording|acordyng|acordynge|$acordynge

# 2. processing dataframe


# creating a list of all lemmas without repetitions
lemma_list = df_lemma.ME_lemma.unique()

print(f"lemma list:")
print(lemma_list[0:10])

# go through dataframe in order to produce forms

str_list = [] # empty list to fill when looping
str_template = '' # empty string to fill when looping

for index in range(len(lemma_list)):
    condition = df_lemma['ME_lemma'] == lemma_list[index] # variable to filter lines - sequence of true and false
    filter_df = df_lemma[condition] # filter lines according to condition above
    # print(filter_df)

# Return like this: accorden: a-cordyng|according|accordyng|accordynge|accordand|acording|acordyng|acordynge|$acordynge

    str_template = str(lemma_list[index]) + ': ' # filled with lemma taken from lemma_list

    # print(f"str_template: {str_template}")
    prog_form_as_list = list(filter_df['PROG_form'])
    # print(f"prog_form_as_list: {prog_form_as_list}")
    for item in prog_form_as_list:
        item = item.replace(' ','|')
        # print(item) # each item of the PROG_form column 
        vchar = item + '|' # verb + bar
        # print(f"vchar: {vchar}")
        str_template = str_template  + vchar
       
    str_list.append(str_template)

# print(str_list)

# last item - remove bar as the last character
for index in range(len(str_list)):
    str_list[index] = str_list[index][:-1]


## replace '___' in list (from PROG_form column) by "+" and "__" by "-"
# make forms back as they were in the beginning

for index in range(len(str_list)):
    str_list[index] = str_list[index].replace('___','+')
    str_list[index] = str_list[index].replace('!','-')

# remove "nan:" (row 118)

str_list.remove('nan:')


# Exporting files

# saving a file with a header and the lemma list, including all the forms available
with open("my_lemma_file4.txt", 'w', encoding='utf-8') as f:
    for item in str_list:
        f.write(item)
        f.write('\n')