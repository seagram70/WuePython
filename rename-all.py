#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil, os, glob
from os.path import exists


#Source Directory in Variable setzen
pfad1="U:\\ZZZ"
pfad2="U:\\ZZZ\\AAA"
pfad3="U:\\ZZZ\\BBB"
pfad4="U:\\ZZZ\\CCC"
pfad5="U:\\ZZZ\\QQQ"


# Prüfen ob das Directory vorhanden ist
if os.path.exists(pfad4) == True:
    print(pfad4, "existiert.")
else:
#    print(pfad4, "existiert nicht, wird aber angelegt")
    print(pfad4 + "existiert nicht, wird aber angelegt" + "".join(pfad5)+ "gagagaga")
    os.mkdir(pfad4)


if os.path.exists(pfad5) == True:
    print(pfad5, "existiert.")
    
else:
    print(pfad5, "existiert nicht, wird aber angelegt")
    os.mkdir(pfad5)



# Kopiert den Inhalt aus dem Directory variable (pfad3) in das Directory pfad4 und pfad5
# Zwingend muss der Import glob angewendet werden.
for filename in glob.glob(os.path.join(pfad3, '*.*')):
    shutil.copy(filename, pfad4)
    shutil.copy(filename, pfad5)
    

# Kopiert nur *.txt Files in den den Ordner FFF
dir_src = ("U:\\ZZZ\\CCC\\")
dir_dst = ("U:\\ZZZ\\FFF\\")

for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.copy( dir_src + filename, dir_dst)
    print(filename)


#Ausgeben der Files in einer Liste  
files=os.listdir(pfad1)

for file in files:
    print file
