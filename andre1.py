#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# test eintrag

varRun1 = 'Run completed: K11T'
varRun2 = 'Run completed: K21T'
varRun3 = 'Run completed: K31T'
varRun4 = 'Run completed: K41T'
varRun5 = 'Run completed: K51T'
varRun6 = 'Run completed: K61T'

varlog1 = 'U:\\ZZZ\\VDFS-processlog.txt.1'
varlog2 = 'U:\\ZZZ\\VDFS-processlog.txt.2'



def writeK11TLineIntoFile(content, datei='U:\\ZZZ\\testout.txt'):
    matching_lines = []
    for line in content:
#        if 'K11T' in line:        # Wenn nicht mit der Variable gearbeitet wird.
        if varRun1 in line:
            matching_lines.append(line)
#    with open(datei, 'w+') as FW:              #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
    with open(datei, 'a+') as FW:               #mit 'a+', wir das File appended
        for match in matching_lines:
            FW.write(match)
            

#Variable vor dem with initiieren, damit ausserhalb sichtbar
file_content= []

#Datei schliesst nach dem with
with open ('U:\\ZZZ\\VDFS-processlog.txt.1','r') as FO:
    file_content = FO.readlines()#Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck


writeK11TLineIntoFile(file_content)



def writeK21TLineIntoFile(content, datei='U:\\ZZZ\\testout.txt'):
    matching_lines = []
    for line in content:
#        if 'K11T' in line:
        if varRun2 in line:
            matching_lines.append(line)
#    with open(datei, 'w+') as FW:#mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
    with open(datei, 'a+') as FW:           #mit 'a+', wir das File appended
        for match in matching_lines:
            FW.write(match)
            

#Variable vor dem with initiieren, damit ausserhalb sichtbar
file_content= []

#Datei schliesst nach dem with
with open ('U:\\ZZZ\\VDFS-processlog.txt.1','r') as FO:
    file_content = FO.readlines()#Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck


writeK21TLineIntoFile(file_content)



