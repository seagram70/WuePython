#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
import math


grenze=raw_input('Geben Sie die Höchstgrenze ein!')
grenze=int(grenze)
i=10


mylist=[2,3,5,7]

while (i<=grenze):
    primzahl=True
    Nr=0
    y=mylist[Nr]
    wurzel=math.sqrt(i)
    while(y<=wurzel):
        rest = i%y
        if rest ==0:
            primzahl=False
            break
        Nr=Nr+1
        y=mylist[Nr]
   
      
      
    if (primzahl == True):
        print str(i) +' ist eine Primzahl!'
        mylist.append(i)
    i=i+1   
      

   
anzahl= len(mylist)
print 'Es wurden '+str(anzahl)+' Primzahlen gefunden!'