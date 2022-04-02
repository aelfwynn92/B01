# Creating aliases in .bashrc

dic_periods = {"m1":0, "mx1":0, "m2":0, "m23":0, "m24":0, "m3":0, "m34":0, "m4":0, "mx4":0}
dic_me13g9p = {"me13g9p":0}
#keys1 = list(dic_periods.keys())
#print(dic.keys())

# index gets all positions within dic_periods 
# index2 gets all positions within dic_me13g9p 
# Both loops combine both indexes to cross keys in both dictionaries and print them 
# (as in combinatory analysis)

with open("aliases_dotbashrc_me13g9p.txt", "w") as file:
    for index in range(len(dic_periods.items())):
        for index2 in range(len(dic_me13g9p.items())):
            chave_periods = list(dic_periods.keys())[index]
            valor_periods = list(dic_periods.values())[index]
            chave_me13g9p = list(dic_me13g9p.keys())[index2]
            valor_me13g9p = list(dic_me13g9p.values())[index2]
  #for chave, valor in dic_genres.items():
    #if valor_genres == 0 or valor_periods == 0:
            alias = f'export {chave_me13g9p}{chave_periods}=\"$corp/PPCME2-RELEASE-4/corpus/psd/me13g-9p/me13g-9p-dist/{chave_periods}"\nalias {chave_me13g9p}{chave_periods}=\"cd $me13g9p{chave_periods}"'
            file.write(alias)
            file.write("\n")
            print(alias)