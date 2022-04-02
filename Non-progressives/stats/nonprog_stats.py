import glob
from hmac import new
import os
import re
import pandas as pd

##############################################################
def get_list_from_tgt_str (cod_regex, target_string, group_number):

    pattern = re.compile(cod_regex)

    grp = []

    # find all matches to groups
    for match in pattern.finditer(target_string):
        # extract words
        # print(f"group {group_number}")
        grp.append(match.group(group_number))
        # print(match.group(group_number))
        
            
    # print(f"group {group_number}: {grp}\n")
    return (grp)    
##############################################################


# getting current directory

curr_dir = os.getcwd()
print(f"current dir: {curr_dir}")

# reading .cod file

cod = []
with open('SAMPLE_1nonprog_splpres.cod.ooo') as f:
    cod = f.readlines()
    #print(cod)

# so far so good

cod_string = '\n'.join(cod)
#print(cod_string)
cod_regex = r"(\%spl_present)(\:)(\%germanic|\%romance|\%blended)(\:)(\%[0-9](half)?)(\:)(\%transitive|\%intransitive|\%prep_intransitive|\%ambiguous)(\@)([A-Z0-9\-]+)(\,)([A-Z0-9\.\,]+)"
filtered_list = re.findall(cod_regex, cod_string)
#print(filtered_list)

# so far so good

# Transforming tuples in lists
print("Transforming list of tuples into list of lists and filtering")
new_matchlist = [] # new list of lists instead of tuples
for item in filtered_list:
    item = list(item)
    new_matchlist.append(item)
    #print(new_matchlist)

# so far so good

print("Checking element 1")
print(new_matchlist[1])

##EXAMPLE:
#['%spl_present', ':', '%germanic', ':', '%1', '', ':', '%prep_intransitive', '@', 'CMAELR3-M23', ',', '26.8']

# list of lists to list of strings
list_strings = ['\n'.join(x) for x in new_matchlist]
#print(list_strings)

tam = []
origin = []
wordlength = []
transitivity = []
textname = []
textid = []

for item in new_matchlist:
    tam.append(item[0])
    origin.append(item[2])
    wordlength.append(item[4])
    transitivity.append(item[7])
    textname.append(item[9])
    textid.append(item[11])
    
    
    
    # df to csv - ok
df = pd.DataFrame(list(zip(textname, textid, tam, origin, wordlength, transitivity)), columns = ["Text_name", "sentence", "TAM", "Origin", "Word_length", "Transitivity"])
print(f"df:\n{df}")

df.to_csv("SAMPLE_nonprog_stats.csv", index=False, sep = ',')

# FUS RO DAH