#!/usr/bin/env python
# -*- encoding: utf-8 -*-


varsetR = {'Run completed: K11T', 'Run completed: K21T','Run completed: K31T', 'Run completed: K41T', 'Run completed: K51T', 'Run completed: K61T'}
varsetD = {'U:\\ZZZ\\VDFS-processlog.txt.1', 'U:\\ZZZ\\VDFS-processlog.txt.2', 'U:\\ZZZ\\VDFS-processlog.txt.3', 'U:\\ZZZ\\VDFS-processlog.txt.4', 'U:\\ZZZ\\VDFS-processlog.txt.5', 
           'U:\\ZZZ\\VDFS-processlog.txt.6', 'U:\\ZZZ\\VDFS-processlog.txt.7', 'U:\\ZZZ\\VDFS-processlog.txt.8', 'U:\\ZZZ\\VDFS-processlog.txt.9', 'U:\\ZZZ\\VDFS-processlog.txt.10'}

def writeK11TLineIntoFile(content, datei='U:\\ZZZ\\testout.txt'):
    matching_lines = []
    for line in content:
        for run in varsetR:
            if run in line:
                matching_lines.append(line)
                break
#    with open(datei, 'w+') as FW:           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
    with open(datei, 'a+') as FW:           #mit 'a+', wir das File appended

        for match in matching_lines:
            FW.write(match)
            

#Variable vor dem with initiieren, damit ausserhalb sichtbar
file_content= []

#Datei schliesst nach dem with
for dat in varsetD:
    with open (dat,'r') as FO:
        file_content = FO.readlines()#Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
    writeK11TLineIntoFile(file_content)




#Sortieren
def sorting(filename):
    words = []
    with open(filename) as file_handle:
        for line in file_handle:
            words += line.split()
    return sorted(words)

print '\n'.join(sorting('U:\\ZZZ\\testout.txt'))