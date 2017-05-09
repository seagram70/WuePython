#!/usr/bin/env python
# -*- encoding: utf-8 -*-


mini=input('Geben Sie die kleinste gewünschte Zahl ein!')
maxi=input('Geben Sie die Höchstgrenze ein!')



pruefung = 0
 
print "Dieses Programm prueft, ob eine Zahl n eine Primzahl ist."


#for n in range (1550, 2000):
for n in range (mini, maxi):
 
    for i in range (2,  n):
 
        if n * 1.0 % i == 0:
            pruefung = 1
            break
 
    if pruefung == 1:
        pruefung = 0
    else:
        print n,  "ist eine Primzahl."