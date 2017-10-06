#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
print('Bitte Zahl eingeben:')
input=sys.stdin.readline()
input=input.strip() # Newline (\n) am Ende der Eingabe entfernen
i=int(input)

if i<20:
    print('%s ist kleiner als 20.' % i)

elif i==20:
    print('%s ist gleich 20.' % i)

else:
    print('%s ist größer als 20.' % i)