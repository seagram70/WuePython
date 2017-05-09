#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        14.01.2017
# Modified:       14.01.2017
# Program:        VdfsProcesslog.py

# Description:    Das Script sucht in einem File in welchem das Wort " <OutputFileName> " vorkommt, schreibt es in ein tempfile
#                 und zählt alle vorkomnisse pro Zeile.

#XMLFILE = 'Y2017107.K61.xml'

#***************************************************
# ***    K11T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeSubscriptions2File(content, datei="U:\\nfs\\temp.txt"):
    matching_lines = []
    for line in content:
        if '<OutputFileName>' in line:                      #nach diesem Wort in der Zeile wird gesucht.
            matching_lines.append(line)        
    with open(datei, 'w') as FW:                            #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
#    with open(datei, 'a+') as FW:                          #mit 'a+', wird das File appended

        for match in matching_lines:
            FW.write(match)            
file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar



'''

#for files in logvar:
with open ("U:\\ZZZ\\GROUP02\\selection\\" + XMLFILE,'r') as FO:                            #Datei schliesst nach dem with
    file_content = FO.readlines()                                                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
    writeSubscriptions2File(file_content)
        
with open("U:\\ZZZ\\temp.txt", 'r') as f:
            line_count = len(f.readlines())
            print line_count

'''

