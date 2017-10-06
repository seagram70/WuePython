#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        20.02.2017
# Modified:       
# Program:        DamonFillWithConfig.py
#Version          v1.1.0

# Description:    Die VDFS Complete Meldungen und der Doc Zähler werden
#                 merged und in ein JSON File geschrieben welche vom Damon abgearbeitet wird.

import json
import os
import glob
import time
import socket
import logging


try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read("..\\cfg\\damon.cfg")

# read values from a section
pfad_merge = config.get('section_a', 'pfad_merge')
pfad_json  = config.get('section_a', 'pfad_json')
damonlog   = config.get('section_a', 'damonlog')
file_doc   = config.get('section_a', 'file_doc')
service    = config.get('section_a', 'service')
application = config.get('section_a', 'host_env_P')
server      = config.get('section_a', 'server')
environment = config.get('section_a', 'environment')
#bool_val = config.getboolean('section_a', 'bool_val')
#int_val = config.getint('section_a', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')


# ******************************************************
# *** Logger                                         ***
# ******************************************************
logger = logging.getLogger("   v1.1.0  ")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(damonlog)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]  %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

# ******************************************************
# *** variablen                                      ***
# ******************************************************
hms   = time.strftime("%H-%M-%S")
today = time.strftime("%d.%m.%Y")
servername  = (socket.gethostname())

# ******************************************************
# *** Server abfrage, Integaration oder Prod VDFS    ***
# ******************************************************
logger.info(' Abfragen der Systemumgebung, VDFS Produktion oder VDFS Integration')
if servername == server:
    env = environment
    logger.info(' System ist VDFS Integration')

#elif HOST == host_Prod:
#    server = host_env_P
#    logger.info(' System ist VDFS Produktion')
else:
    logger.critical('Die Umgebung ist weder VDFS Integration noch VDFS Produktion, abbruch des Scripts')
#    exit()

# *************************************************************************
# *** Wechselt in das Merge Directory und sucht nach den input Files    ***
# *************************************************************************
os.chdir(pfad_merge)
for fi in glob.glob("????"):
    inputfile = fi
    logger.info(' Inputfile ' + inputfile + ' vorhanden')
    runFile = open(inputfile, 'w')
    runFile.write("Date: " + today + '\n')
    runFile.write("Time: " + hms + '\n')
    runFile.write("Service: " + "VDF" + '\n')
    runFile.write("Application: " + "VDFS" + '\n')
    runFile.write("Run: " + inputfile + '\n')
    runFile.write("Status: " + "completed" + '\n')
    runFile.write("Environment: " + "Production" + '\n')
    runFile.write("Server: " + server + '\n')
    runFile.close()
    runFile = inputfile
    logger.info(' Alle Parameter in das ' + inputfile + ' File abgefüllt')

# *************************************************************************
# *** Lesen aus dem Doc zähler File, sucht nur die anzahl Docs im File  ***
# *** Die Docs werden nur gezählt wenn es sich um ein T File handelt    ***
# *************************************************************************
try:
    if not runFile.startswith("K"):
        logger.info(' Da es kein Krun ist wird das File merged mit der Docanzahl im T-Run')
        try:
            doc = open(pfad_merge + file_doc, "r")
            daten = doc.read() 
            doc.close() 
            docs = daten[48:55]
            logger.info(' Doc anzahl DOCS aus dem Docstatistik File wurde gelesen')
        
            merge = open(pfad_merge + runFile, "a+")
            merge.write("Docs: " + docs)
            merge.close()
            logger.info(" Die Docanzahl wurde in das RunFile geschrieben.", exc_info=False)

        except Exception, e:
            logger.error("Das " + file_doc + " File ist nicht vorhanden, es findet kein merge statt.", exc_info=False)
            logger.info("Das JSON File für Damon wird trotzdem erstellt, die Docanzahl wird aber nicht mitgegeben", exc_info=False)
 
    else:
        logger.info(' Es ist ein K-Rund, es werden keine Docs gezaehlt')
except Exception, e:
    logger.error('Es ist weder ein K noch ein T File vorhanden', exc_info=False)


damonfile = runFile
# **********************************************
# *** JSON File erstellen                    ***
# **********************************************
damoninp = {}
damonin = open(pfad_merge + damonfile, "r")
logger.info(' Das File ' + pfad_merge + damonfile + 'wurde im read modus geöffnet')

try:
    logger.info(' JSON File wird generiert')
    for zeile in damonin:
        liste = zeile.split(":")
        damoninp[liste[0].strip()] = liste[1].strip()
        print damoninp
    damonin.close()
    
    datei = open(pfad_json + damonfile + ".json", "w")
    datei.write(json.dumps(damoninp))
    datei.close()
    logger.info(' JSON File wurde geschrieben')
except Exception, e:
    logger.error(' Das JSON File konnte nicht geschrieben werden')


#Löschen der Input Files
for output in glob.glob(pfad_merge + "*"):
    os.remove(output)
    logger.info(' Das File ' + output + ' wurde aus dem Merge Directory gelöscht')
