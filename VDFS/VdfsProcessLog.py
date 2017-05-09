#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        14.01.2017
# Modified:       14.01.2017
# Program:        VdfsProcesslog.py

# Description:    Create Drivemap to VDFS an make a get to f:\logs Directory on the Master VDFS Server.
#                 Copy Logfiles named VDFS-processlog to the local Drive
#                 Drive letter: Z
# Shared path:    \\mislwmvdfs41\F$
# Username:       domain01\*****
# Password:       ********


import os, shutil
from os.path import exists
import subprocess


# Disconnect anything on Z
subprocess.call('net use z: /delete /yes', shell=True)

# Connect to shared drive, use drive letter Z
#subprocess.call(r'net use z: \\mislwfvdfs47\F$ /user:domain01\tkwue $Lon1don', shell=True)                   #VDFS Integ File Server
subprocess.call(r'net use z: \\mpzhwmvdfs01\F$ $Nil22pferd /user:mpzhwmvdfs01\vdfsadmin', shell=True)         #VDFS Integ Master Server


# Pfad Variablen
pfadin  = "Z:\\logs\\log_archive"
pfadout = "U:\\ZZZ"

f       = open("U:\\ZZZ\\K-Runsout.txt", "w")
pfad    =      "U:\\ZZZ\\K-Runsout.txt"

logvar1 = ['U:\\ZZZ\\VDFS-processlog.txt.5'
          ,'U:\\ZZZ\\VDFS-processlog.txt.4', 'U:\\ZZZ\\VDFS-processlog.txt.3'
          ,'U:\\ZZZ\\VDFS-processlog.txt.2']


# Check is Drive to VDFS Server mapped
if exists("Z:\\"):
    print "Drive bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive wurde gemappt"

# List of Files named VDFS-processLog and copy to the local Drive
dirList = os.listdir(pfadin)
for sFile in dirList:
    if sFile.find('VDFS-processlog') == -1:
        continue
    print sFile

    full_file_name = os.path.join(pfadin, sFile)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, pfadout)
        
        


#***************************************************
# ***    K11T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK11TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K11T' in line:
            matching_lines.append(line)        
    with open(datei, 'a+') as FW:                            #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
#    with open(datei, 'w+') as FW:                           #mit 'a+', wir das File appended

        for match in matching_lines:
            FW.write(match)            
file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for files in logvar1:
    with open (files,'r') as FO:                             #Datei schliesst nach dem with
        file_content = FO.readlines()                       #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK11TLineIntoFile(file_content)
        
        
'''
#  Mit diesen zwei Zeilen wird es nur mit einem Logfile funktionieren
with open (logvar1,'r') as FO:
    file_content = FO.readlines()
'''
print "K11T auslesen beendet"


#***************************************************
# ***    K21T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK21TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K21T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (filess,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK21TLineIntoFile(file_content)
print "K21T auslesen beendet"


#***************************************************
# ***    K31T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK31TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K31T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (filess,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK31TLineIntoFile(file_content)
print "K31T auslesen beendet"


#***************************************************
# ***    K41T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK41TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K41T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK41TLineIntoFile(file_content)
print "K41T auslesen beendet"


#***************************************************
# ***    K51T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK51TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K51T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK51TLineIntoFile(file_content)
print "K51T auslesen beendet"



#***************************************************
# ***    K61T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK61TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K61T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK61TLineIntoFile(file_content)
print "K61T auslesen beendet"



#***************************************************
# ***    K81 Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK81TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K81T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK81TLineIntoFile(file_content)
print "K81T auslesen beendet"



#***************************************************
# ***    K01S Run wird aus den Logfiles gelesen    *
#***************************************************
def writeK01SLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: K01S' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeK01SLineIntoFile(file_content)
print "K01S auslesen beendet"
print "Scripts fuer alle K-Runs sind durchegelaufen"







#***************************************************
# ***    T10T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeT10TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: T10T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for filess in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeT10TLineIntoFile(file_content)
print "T10T auslesen beendet"



#***************************************************
# ***    T20T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeT20TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: T20T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for files in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeT20TLineIntoFile(file_content)
print "T20T auslesen beendet"



#***************************************************
# ***    T30T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeT30TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: T30T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for files in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeT30TLineIntoFile(file_content)
print "T30T auslesen beendet"



#***************************************************
# ***    D01T Run wird aus den Logfiles gelesen    *
#***************************************************
def writeD01TLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: D01T' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for files in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeD01TLineIntoFile(file_content)
print "D01T auslesen beendet"



#***************************************************
# ***    T01S Run wird aus den Logfiles gelesen    *
#***************************************************
def writeT01SLineIntoFile(content, datei=pfad):
    matching_lines = []
    for line in content:
        if 'Run completed: T01S' in line:
            matching_lines.append(line)
    with open(datei, 'a+') as FW:                           #mit 'w+', falls die Datei noch nciht existiert, wird sie erstellt
        for match in matching_lines:
            FW.write(match)            

file_content= []                                            #Variable vor dem with initiieren, damit ausserhalb sichtbar

for files in logvar1:
    with open (files,'r') as FO:
        file_content = FO.readlines()                           #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeT01SLineIntoFile(file_content)
print "T01S auslesen beendet"
print "Scripts fuer alle T-Runs sind durchegelaufen"

f.close()



