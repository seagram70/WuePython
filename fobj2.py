#!/usr/bin/env python
# -*- encoding: utf-8 -*-

varsetR = {'K11T', 'K21T','K31T', 'K41T', 'K51T', 'K61T'}
varsetD = {'U:\\ZZZ\\testin1.txt', 'U:\\ZZZ\\testin2.txt'}

def writeK11TLineIntoFile(content, datei='U:\\ZZZ\\testout.txt'):
    matching_lines = []
    for line in content:
        for run in varsetR:
            if run in line:
                matching_lines.append(line)
                break
    with open(datei, 'w+') as FW:           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
#    with open(datei, 'a+') as FW:           #mit 'a+', wir das File appended

        for match in matching_lines:
            FW.write(match)
            

#Variable vor dem with initiieren, damit ausserhalb sichtbar
file_content= []

#Datei schliesst nach dem with
for dat in varsetD:
    with open (dat,'r') as FO:
        file_content = FO.readlines()#Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
    writeK11TLineIntoFile(file_content)
