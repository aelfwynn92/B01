# Creating aliases in .bashrc

dic = {"m1":0, "mx1":0, "m2":0, "m23":0, "m24":0, "m3":0, "m34":0, "m4":0, "mx4":0}
keys1 = list(dic.keys())
#print(dic.keys())

with open("aliases_dotbashrc_periods.txt", "w") as file:
  for chave, valor in dic.items():
    if valor == 0:
      #print("export me",chave,"=\"$corp/PPCME2-RELEASE-4/corpus/psd/meperiods/",chave,"\"\nalias me",chave,"=\"cd $me",chave,"\"")
      alias = f'export me{chave}=\"$corp/PPCME2-RELEASE-4/corpus/psd/meperiods/{chave}"\nalias me{chave}=\"cd $me{chave}"'
      file.write(alias)
      file.write("\n")
      print(alias)
    else:
      print('')