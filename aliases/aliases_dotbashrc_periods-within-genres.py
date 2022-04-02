# Creating aliases in .bashrc

dic_genres = {"bible":0, "biosaint":0, "fiction":0, "handbastro":0, "handbmed":0, "handbother":0, "history":0, "homily":0, "philosophy":0, "reltreat":0, "romance":0, "rule":0, "sermon":0, "travelogue":0}
dic_periods = {"m1":0, "mx1":0, "m2":0, "m23":0, "m24":0, "m3":0, "m34":0, "m4":0, "mx4":0}
keys1 = list(dic_genres.keys())
#print(dic.keys())

# index gets all positions within dic_genres 
# index2 gets all positions within dic_periods 
# Both loops combine both indexes to cross keys in both dictionaries and print them 
# (as in combinatory analysis)

with open("aliases_dotbashrc_periods-within-genres.txt", "w") as file:
    for index in range(len(dic_genres.items())):
        for index2 in range(len(dic_periods.items())):
            chave_genres = list(dic_genres.keys())[index]
            valor_genres = list(dic_genres.values())[index]
            chave_periods = list(dic_periods.keys())[index2]
            valor_periods = list(dic_periods.values())[index2]
  #for chave, valor in dic_genres.items():
    #if valor_genres == 0 or valor_periods == 0:
            alias = f'export me{chave_genres}{chave_periods}=\"$corp/PPCME2-RELEASE-4/corpus/psd/megenres/{chave_genres}/{chave_genres}_periods/{chave_genres}{chave_periods}"\nalias me{chave_genres}{chave_periods}=\"cd $me{chave_genres}{chave_periods}"'
            file.write(alias)
            file.write("\n")
            print(alias)