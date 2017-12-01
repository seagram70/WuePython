#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

from os.path import isfile, join
from XMLReader import writeSubscriptions2File
from rolloverLocal import rotating_log_local
from mail import sendEmail


# --- Aufruf XML Reader ---
sendEmail("VDFS-INTEGRATION@SIX-GROUP.COM", 'heinz.wuethrich@six-group.com', 
          "Error from VDFS Production", "Dies ist ein test", files=[])
    
    
    
    
# --- Aufruf XML Reader ---
XMLFILE = 'Y2017107.K61.xml'

pfad         =  "U:\\nfs\\"
selectionDir = [pfad + "GROUP01\\selection\\", pfad + "GROUP02\\selection\\", pfad + "GROUP03\\selection\\"]


for outp in selectionDir:
    with open(outp + XMLFILE,'r') as FO:                            #Datei schliesst nach dem with
        file_content = FO.readlines()                       #Gibt jede Zeile als einzelenen Eintrag in der Liste zurueck
        writeSubscriptions2File(file_content)
        
    with open("U:\\nfs\\temp.txt", 'r') as f:
        line_count = len(f.readlines())
        print (line_count)
        
    os.remove(pfad + "temp.txt")
    
    
    

# ------------- Aufruf rolloverLocal ------------
pfad = "C:\\Daten\\workspace\\rddelivery\\FUNCTIONS\\Logs\\"
logfiles = [f for f in os.listdir(pfad) if isfile(join(pfad, f)) and f.endswith('.log') or f.endswith('.txt')]


os.chdir(pfad)
for names in logfiles:
    rotating_log_local(pfad, names, 5)



'''
if __name__ == "__main__":
    pass
    
'''