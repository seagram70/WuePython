#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        09.02.2017
# Modified:       18.02.2017        Pfade für VDFS angepasst
#                 19.02.2017        Startswith auf NOT Startwith angepasst damit nur die K Runs keine Docs zählen.
# Program:        DamonFill.py

# Description:    Die VDFS Complete Meldungen und der Doc Zähler werden
#                 merged und in ein JSON File geschrieben welche vom Damon abgearbeitet wird.

import json
import os
import glob
import time
import socket

today = time.strftime("%d.%m.%Y")
hms   = time.strftime("%H%M%S")
HOST        = (socket.gethostname())


def log(datum, zeit, stat, msg):
    f = open(damonlog,"a")
    f.write("%s %s %s %s\n" % (datum, zeit, stat, msg))
    f.close

pfad_merge = "F:\\Programs\\Damon\\merge\\"
pfad_json  = "F:\\Programs\\Damon\\Files\\"
file_doc   = "DocStatisik.txt"
damonlog   = 'F:\\Logs\\damonlog.log'


# ******************************************************
# *** Server abfrage, Integaration oder Prod VDFS    ***
# ******************************************************
if HOST == "mislwmvdfs41":
    server = "VDFS-int"
elif HOST == "mpzhwmvdfs01":
    server = "VDFS-Prod"
else:
    log(today, hms, "[INFO]", " Die Umgebung ist weder VDFS Integration noch VDFS Produktion, abbruch des Scripts")
    exit()

# *************************************************************************
# *** Wechselt in das Merge Directory und sucht nach den input Files    ***
# *************************************************************************
os.chdir(pfad_merge)
for fi in glob.glob("????"):
    inputfile = fi
#    print inputfile
    log(today, hms, "[INFO]", " Inputfile " + inputfile + " vorhanden" )

runFile = open(inputfile, 'w')
runFile.write("Date: " + today + '\n')
runFile.write("Time: " + hms + '\n')
runFile.write("Appl: " + "VDF" + '\n')
runFile.write("Run: " + inputfile + '\n')
runFile.write("Status: " + "completed" + '\n')
#runFile.write("Server: " + "VDFS-Int" + '\n')
runFile.write("Server: " + server + '\n')
runFile.close()
runFile = inputfile
#print runFile
log(today, hms, "[INFO]", " Parameter in das " + inputfile + " File abgefüllt" )

# *************************************************************************
# *** Lesen aus dem Doc zähler File, sucht nur die anzahl Docs im File  ***
# *** Die Docs werden nur gezählt wenn es sich um ein T File handelt    ***
# *************************************************************************
if not runFile.startswith("K"):
    doc = open(pfad_merge + file_doc, "r")
    daten = doc.read() 
    doc.close() 
    docs = daten[48:55]
    log(today, hms, "[INFO]", " Doc anzahl aus dem Docstatistik File gelesesen" )


# **********************************************
# *** Merge der beiden generierten Files     ***
# **********************************************
    merge = open(pfad_merge + runFile, "a+")
    merge.write("Docs: " + docs)
    merge.close()
#    damonfile = runFile
    log(today, hms, "[INFO]", " Mergen der beiden Files" )

else:
    print "Es ist ein K-Rund, es werden keine Docs gezaehlt"
    log(today, hms, "[INFO]", " Es ist ein K-Rund, es werden keine Docs gezaehlt" )


damonfile = runFile
# **********************************************
# *** JSON File erstellen                    ***
# **********************************************
damoninp = {}
damonin = open(pfad_merge + damonfile, "r")
for zeile in damonin:
    liste = zeile.split(":")
    damoninp[liste[0].strip()] = liste[1].strip()
    print damoninp
damonin.close()
    
datei = open(pfad_json + damonfile + ".json", "w")
datei.write(json.dumps(damoninp))
datei.close()
log(today, hms, "[INFO]", " JSON File wurde geschrieben" )


for output in glob.glob(pfad_merge + "*"):
    os.remove(output)
    log(today, hms, "[INFO]", " Das File " + output + " wurde aus dem Merge Directory gelöscht" )
