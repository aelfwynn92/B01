# Creating aliases in .bashrc

dic = {"bible":0, "biosaint":0, "fiction":0, "handbastro":0, "handbmed":0, "handbother":0, "history":0, "homily":0, "philosophy":0, "reltreat":0, "romance":0, "rule":0, "sermon":0, "travelogue":0}
keys1 = list(dic.keys())
#print(dic.keys())

with open("aliases_dotbashrc_genres.txt", "w") as file:
  for chave, valor in dic.items():
    if valor == 0:
      #print("export me",chave,"=\"$corp/PPCME2-RELEASE-4/corpus/psd/megenres/",chave,"\"\nalias me",chave,"=\"cd $me",chave,"\"")
      alias = f'export me{chave}=\"$corp/PPCME2-RELEASE-4/corpus/psd/megenres/{chave}"\nalias me{chave}=\"cd $me{chave}"'
      file.write(alias)
      file.write("\n")
      print(alias)
    else:
      print('')