#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def writeK11TLineIntoFile(content, datei='U:\\ZZZ\\testout.txt'):
    matching_lines = []
    for line in content:
        if 'K11T' in line:
            matching_lines.append(line)
    try:
        with open(datei, 'w+') as FW:#mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
            for match in matching_lines:
                FW.write(match)
    except IOError as e:
        print("Could not open File %e" %e)
        exit()
            

#Variable vor dem with initiieren, damit ausserhalb sichtbar
file_content= []

try:
    #Datei schliesst nach dem with
    with open ('U:\\ZZZ\\testin.txt','r') as FO:
        file_content = FO.readlines()#Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
except IOError as a:
    print("Could not open File %e" %e)
    exit()

writeK11TLineIntoFile(file_content)
    

