#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        04.05.2017
# Modified:       
# Program:        DocCounter.py
# Version:        1.0.5

# Description:    Liest ein Delta File ein und zählt jeden einzelnen
#                 Doctyp und schreibt diese Zahlen in Statistik File
#


import logging
import sys
import time
import socket

# ----  Abfrage des Environments ------
if socket.gethostname() in ['mpzhwmvdfs01', 'mpzhwsvdfs02', 'mpzhwsvdfs03', 'mpzhwsvdfs04', 'mpzhwsvdfs05', 'mpzhwsvdfs06', 'mpzhwfvdfs07']:
        env = 'prodenv'
        print env
elif socket.gethostname() in ['mislwmvdfs41', 'mislwsvdfs42', 'mislwsvdfs43', 'mislwsvdfs44', 'mislwsvdfs45', 'mislwsvdfs46', 'mislwfvdfs47']:
        env = 'intenv'
        print env
elif socket.gethostname() in ['N36165']:
        env = 'localenv'
        print env
else:
        print 'Wrong Environment'
        exit()    


# ****************************
#    Configfile variablen    *
# ****************************
try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser                           # ver. < 3.0

parser = SafeConfigParser()                                             # instantiate

try:
    parser.read('..\\cfg\\DocStat.cfg')                                   # For local use
except:
    parser.read('F:\\Programs\\DocStatistic\\cfg\\DocStat.cfg')        # For server use


logPath      = parser.get(env, 'logPath')
DeltaFiles   = parser.get(env, 'DeltaFiles')
StatDir      = parser.get(env, 'StatDir')
DeltaFake    = parser.get(env, 'DeltaFake')
StatFile     = parser.get(env, 'StatFile')
outputFile   = parser.get(env, 'outputFile')
server       = parser.get(env, 'server')
environment  = parser.get(env, 'environment')
labelTrun    = parser.get(env, 'labelTrun')
labelNetting = parser.get(env, 'labelNetting')



logger = logging.getLogger("   v1.0.5  ")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(logPath)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]  %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


# ***************************************************************
#    Input variablen und Pfade                                  *
# ***************************************************************
inputFile   = sys.argv[1]
#inputFile   =  'VDMMAPS.Y2017075.T10T'

logger.info('Starting DocCounter per Doc Type')

# ***************************************************************
#    Start reading inputFile                                    *
# ***************************************************************
key_count = dict()
lines = []
try:
    with open (DeltaFiles + inputFile) as LOG:
        lines = LOG.readlines()
except IOError:
    print("Could not open Log-File, exiting")
    logger.info('Could not open Log-File, exiting')
    exit()


for line in lines:
    keyword = line[:3]
#    if first_three_letters[0][0] is not None:
#    keyword = first_three_letters[:3][:3]
    if keyword in key_count:
        key_count[keyword] += 1
    else:
        key_count[keyword] = 1


logger.info('write counted Docs to the Outputfile')

'''
# Output im Textfile
#print(key_count)
out = open(StatDir + outputFile, 'a')
out.write('************************************' + '\n')
out.write('*** DOC Statistik vom ' + time.strftime('%Y-%m-%d') + ' ***' + '\n')
out.write('***  File ' + inputFile +  '  ***' + '\n')
out.write('************************************' + '\n')


for entr in key_count:
    print(entr + " = "+ str(key_count[entr]))
    out.write(entr + " = "+ str(key_count[entr]) + '\n')
    
out.close()
logger.info('File close, DocCount per Docs are writed to ' + outputFile + ' File')
'''


#Output in csv File
outx = open(StatDir + 'DocTypeCount.csv', 'a')

for entry in key_count:
    print(entry + " ; "+ str(key_count[entry]))
    outx.write(time.strftime('%Y-%m-%d') + ";" + inputFile[17:21] + " ; " + entry + " ; "+ str(key_count[entry]) + '\n')
    
outx.close()

