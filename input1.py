#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

#Version 4

name = input("Wie heisst du?\n")
sex = input("Was ist dein Geschlecht?\n")

# In der eckigen Klammer befindet sich die anzahl der eingaben, 0=1
# Steht z.B eine [3] so muss man 4x ein mmmm eingebn.
if sex[0].lower() == "m":
    print("Lieber", name)
elif sex[0].lower() == "f":
    print("Liebe", name)
else:
    print("Hallo", name)



'''
#Version 3

name = input("Wie heisst du?\n")
sex  = input("Was ist dein Geschlecht (m,f)?\n")

if (sex == "m") or (sex == "M"):
    print("Lieber", name)
elif (sex == "f") or (sex == "F"):
    print("Liebe", name)
else:
    print("Hallo", name)
'''    
    
'''    
#Version 1
my_var = input("Kommazahl: ")
f = float(my_var)
print my_var
# oder in einem Schritt
my_var = int(input("Ganzzahl: "))

print my_var

'''

'''
#Version 2
import sys

try:
    a = float(input("  a = "))
    b = float(input("  b = "))
except ValueError:
    print("Fehler: Keine Zahl eingegeben.")
    sys.exit()
print("a+b =", a+b)
print("a-b =", a-b)
print("a*b =", a*b)
try:
    print("a/b =", a/b)
except ZeroDivisionError:
    print("Fehler: Division durch 0")
    
'''