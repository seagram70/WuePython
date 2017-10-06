#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creation:    07.01.2017
# Last Update: 07.01.2017
#
# Author:		Heinz Wüthrich

#Wörterbuch

# Einlesen der Datei
woerter = {}

fobj = open("woerter.txt", "r") 
for line in fobj: 
    line = line.strip() 
    zuordnung = line.split(" ") 
    woerter[zuordnung[0]] = zuordnung[1] 
fobj.close()

while True: 
    wort = raw_input("Geben Sie ein Wort ein: ") 
    if wort in woerter: 
        print "Das deutsche Wort lautet:", woerter[wort] 
    else: 
        print "Das Wort ist unbekannt"


'''

fobj = open("Woerterbuch.txt", "r")
for line in fobj:
	print line
fobj.close()



woerter = {}

fobj = open("woerterbuch.txt", "r") 
for line in fobj: 
    zuordnung = line.split(" ") 
    woerter[zuordnung[0]] = zuordnung[1] 
fobj.close()


'''