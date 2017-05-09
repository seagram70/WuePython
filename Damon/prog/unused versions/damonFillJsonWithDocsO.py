#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        22.02.2017
# Modified:       22.03.2017    Im Dictionary die Beschreibung angepasst
#                 05.04.2017    Anpassung im JSON File, indent 4 ausgeschaltet, es wird nun alles in eine Zeile geschrieben.
#                 
# Program:        DamonFillJsonWithDocsN.py
# Version         v1.2.0

# Description:    Die VDFS Complete Meldungen und der Doc Z�hler werden
#                 merged und in ein JSON File geschrieben welche vom Damon abgearbeitet wird.

import time
import glob
import os
import json
import shutil
import logging
import datetime


# ***************************************
#    ISO Timezone UTC and Juldate       *
# ***************************************
def UTCDiff():
    time_offset = - time.timezone / 3600
    offset_hours = int(time_offset)
    offset_minutes = (time_offset - offset_hours) * 60
    return "+%02d:%02d" %(offset_hours, offset_minutes)
    
def getCurISODateTime():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')

date_time = getCurISODateTime()
date_time_tzDelta = date_time + UTCDiff()
#print date_time_tzDelta

# ****************************
#    Configfile variablen    *
# ****************************
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()                             # instantiate


# parse existing config file


#config.read('..\\cfg\\damon.cfg')                            # For local use
config.read('F:\\Programs\\Damon\\cfg\\damon.cfg')            # For server use

mergPath          = config.get('input', 'mergPath')
logPath           = config.get('input', 'logPath')
jsonPath          = config.get('input', 'jsonPath')
jsonPathSave      = config.get('input', 'jsonPathSave')
onlinestorage     = config.get('input', 'onlinestorage')
service           = config.get('input', 'service')
server            = config.get('input', 'server')
application       = config.get('input', 'application')
environment       = config.get('input', 'environment')
docfile           = config.get('input', 'docfile')
Checkpoint        = config.get('input', 'Checkpoint')
referenceDocsT10T = config.get('input', 'referenceDocsT10T')
referenceDocsT20T = config.get('input', 'referenceDocsT20T')
referenceDocsT30T = config.get('input', 'referenceDocsT30T')
referenceDocsD01T = config.get('input', 'referenceDocsD01T')
referenceDocsT01S = config.get('input', 'referenceDocsT01S')
referenceDocsBWK  = config.get('input', 'referenceDocsBWK')


# ******************************************************
# *** Logger                                         ***
# ******************************************************
logger = logging.getLogger("   v1.2.0  ")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(logPath)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]  %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


# ******************************************************
# *** Dictonary 1 for Json File input                ***
# ******************************************************
logger.info('    Starting Script create JSON File for DAMON')

d = {"Application": application, "Server": server, "Service": service, "Environment": environment, "Timestamp": date_time_tzDelta, "Checkpoint": Checkpoint}
logger.info('    Create Dictionary for fix parameters in config')

# ******************************************************
#      Search RunFile name and create a Dictionary     *
# ******************************************************
os.chdir(mergPath)
try:
    for fi in glob.glob("????"):
        d1 = {"Process": fi}
        d.update(d1)
        logger.info('    Search Filename for Delta or BWK Run in glob var and update dictionary')
except Exception,e:
    logger.critical(' ', exc_info=True)
    exit()

# ******************************************************
#      Fill reference Docs to the JSON File            *
# ******************************************************
if fi == 'T10T':
    refdocs = referenceDocsT10T
elif  fi == 'T20T':
    refdocs = referenceDocsT20T
elif  fi == 'T30T':
    refdocs = referenceDocsT30T
elif  fi == 'D01T':
    refdocs = referenceDocsD01T
elif  fi == 'T01S':
    refdocs = referenceDocsT01S
else:
    refdocs = referenceDocsBWK
    print 'is a K-run, no ref Docs'
    logger.info('is a K-run, no ref Docs')
    
d2 = {"Referencedocs": refdocs}
d.update(d2)
logger.info('    The ' + fi + ' run has ' + refdocs + ' Docs')
    

# **************************************************************************
#  check if the merge Directory are empty exclusic DocStatistik.txt File   *
# **************************************************************************
try:
    if not fi.startswith("K") or not fi.startswith("T") or not fi.startswith("D0"):
        logger.info('    Input File ' + fi + ' available')
except Exception,e:
    logger.critical('No input File available', exc_info=False)
    exit()
    
# ****************************************************************
# Juldate actual and for Sunday when the Run runs on Saturday    *
# ****************************************************************
try:
    if fi == 'T01S' and time.strftime('%A') == "Sunday":
        juldate = time.strftime("%Y%j")
        logger.info('    is it Sunday, the ' + fi + ' Run starts with the normal Julidate')
        
    elif fi == 'T01S' and time.strftime('%A') == 'Saturday':
        juldate = time.strftime("%Y%j")
        juldate = int(juldate) + 1
        logger.info('    is it Saturday, the ' + fi + ' Run starts with then juldate from tomarow')
    
    else:
        juldate = time.strftime("%Y%j")
except Exception,e:
    logger.info('    is it Monday to Friday, no changes on juldate parameter')


# ***************************************************************  
#     Variablen ür VDLMAPS, VDMMAPS, Samstag Sonntag ermitteln  *
# ***************************************************************
if fi == 'D01T':
    label = 'VDLMAPS'
else:
    label = 'VDMMAPS'

logger.info('    the label are set to ' + label + ' now.')


# ************************************************************  
#     create a dictionary for how many Docs are in the run    *
# *************************************************************
try:
    if not fi.startswith("K"):
        with open(onlinestorage + label + '.' + 'Y' + str(juldate) + '.' + fi) as f:
            line_count = len(f.readlines())
            print line_count
            line_count = {"Docs": line_count}
            d.update(line_count)
            logger.info('    is a Delta Run, the Docs are counting for the ' + fi + ' Run')
        
#            j = json.dumps(d, indent=4)
            j = json.dumps(d)
            f1 = open(mergPath + fi + '.json', 'w')
            print >> f1, j
            f1.close()
            logger.info('    JSON File ' + fi + '.json for Damon created')
    
    else:
        logger.info('    It is a BWK Run, NO Docs are counted in the ' + fi + ' Output DAMON File')
#        j = json.dumps(d, indent=4)
        j = json.dumps(d)
        f1 = open(mergPath + fi + '.json', 'w')
        print >> f1, j
        f1.close()
        logger.info('    JSON File ' + fi +'.json for Damon created')

except Exception, e:
    logger.critical('   It is a Delta Run, but no File available for counting DOCS.', exc_info=True)
    logger.info('    create the JSON File when is a T Run File without a Doc File')
#    j = json.dumps(d, indent=4)
    j = json.dumps(d)
    f1 = open(mergPath + fi + '.json', 'w')
    print >> f1, j
    f1.close()
    logger.info('    JSON File ' + fi + '.json for Damon created, but without DOC count')
    

# *************************************************************  
#                 move to the Files (JSON) Directory          *
# *************************************************************
try:
    shutil.copy(mergPath + fi + '.json', jsonPath)
#    shutil.move(mergPath + fi + '.json', jsonPath)
    logger.info('    move JSON File to the Output Directory for transfer over MQ to DAMON')
except:
    logger.warn(' a File with the same name allready exists, no Stopping this Script, the File will are deletet in the next step.')
    os.remove(jsonPath + fi + '.json' )
    shutil.copy(mergPath + fi + '.json', jsonPath)
    logger.info('    The JSON output File are moved')


# ************************************************
#     save and delete Input Files                *
# ************************************************
shutil.move(mergPath + fi + '.json', jsonPathSave + fi + '.json-' + juldate)
logger.info('    The JSON output File are saved in the ' + jsonPathSave + ' Directory')

for output in glob.glob("*"):
    os.remove(output)
    logger.info('    The input File ' + output + ' are deletet')

