#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import shutil, os
from os.path import exists



#Source Directory's in Variablen setzen
pfad_in="U:\\ZZZ"
pfad_out1="U:\\ZZZ\\AAA"
pfad_out2="U:\\ZZZ\\BBB"
pfad_out3="U:\\ZZZ\\CCC"



#create von einem einzelnen Directory und prüfenob vorhanden.
'''
if os.path.exists(pfad_out1) == True:
    print(pfad_out1, "existiert.")
else:
    print(pfad_in, "existiert nicht.")
    os.mkdir(pfad_out1)

'''

#Löschen der Directorys
#shutil.rmtree(pfad_out2)    #Verzeichns wird gelöscht auch wenn es nicht leer ist
#os.rmdir(pfad_out2)         # Löscht nur ein leeres Verzeichnis

# Directorys anlegen und prüfen ob vorhanden.
for pfad in pfad_in, pfad_out1, pfad_out2, pfad_out3:
    if os.path.exists(pfad) == True:
       print(pfad, "existiert.")
    else:
        print(pfad, "existiert nicht. Das Directory wird angelegt")
        os.mkdir(pfad) 


# Change in das Directory
os.chdir('U:\\ZZZ')


# File anlegen und reinschreiben
f = file('spam.txt', 'w')
f.write('tolle erste Zeile\n')
f.write('tolle zweite Zeile\n')
print >>f, 'tolle dritte Zeile'
f.close()



#Copy eines Files / Das Directory AAA muss vorhanden sein.
shutil.copy('U:\\ZZZ\\spam.txt', pfad_out1)
shutil.copy('U:\\ZZZ\\spam.txt', pfad_out2)
shutil.copy('U:\\ZZZ\\spam.txt', 'U:\\ZZZ\\CCC')


#Rename eines Files
shutil.move('U:\\ZZZ\\AAA\\spam.txt', 'U:\\ZZZ\\AAA\\spam1.txt')
shutil.move('U:\\ZZZ\\BBB\\spam.txt', 'U:\\ZZZ\\BBB\\spam1.txt')
shutil.move('U:\\ZZZ\\CCC\\spam.txt', 'U:\\ZZZ\\CCC\\spam1.txt')



#Change Directory und Copy File mit rename
os.chdir('U:\\ZZZ\\AAA')
shutil.copy('spam1.txt', 'U:\\ZZZ\\BBB\\spam.txt')  #copy / rename

os.chdir('U:\\ZZZ\\BBB')
shutil.copy('spam1.txt', 'U:\\ZZZ\\CCC\\spam.txt')  #copy / rename

os.chdir('U:\\ZZZ\\CCC')
shutil.copy('spam1.txt', 'U:\\ZZZ\\AAA\\spam.txt')  #copy / rename



# Löschen des input Files
if os.path.exists('U:\\ZZZ\spam.txt') == True:
    print('U:\\ZZZ\\spam.txt', "existiert, wird daher geloescht.")
    os.remove('U:\\ZZZ\\spam.txt')

else:
    print('U:\\ZZZ\spam.txt', "existiert nicht.")
#    os.mkdir(pfad_out1)



#Ausgeben aller Files und Directoriys im Verzeichnis U:\ZZZ in einer Liste  
files=os.listdir(pfad_in)

for file in files:
    print file
