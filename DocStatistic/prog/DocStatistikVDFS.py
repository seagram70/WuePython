#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        03.02.2017
# Modified:       11.04.2017    Config Parser angepasst, local und Server use.
#                 11.04.2017    Mail step eingefügt
#
# Program:        DocStatistikVDFS.py
# Version:        1.0.5

# Description:    Zählt lines im Delta Files und gibt die anzahl DOCS zurück.

import time
import glob
import os
import logging
import subprocess
import socket
from mail import sendEmail

print(socket.gethostname())

# ----  Abfrage des Environments ------
if socket.gethostname() in ['mpzhwmvdfs01', 'mpzhwsvdfs02', 'mpzhwsvdfs03', 'mpzhwsvdfs04', 'mpzhwsvdfs05', 'mpzhwsvdfs06', 'mpzhwfvdfs07']:
        env = 'prodenv'
        print (env)
elif socket.gethostname() in ['mislwmvdfs41', 'mislwsvdfs42', 'mislwsvdfs43', 'mislwsvdfs44', 'mislwsvdfs45', 'mislwsvdfs46', 'mislwfvdfs47']:
        env = 'intenv'
        print (env)
elif socket.gethostname() in ['Heinzs-MacBook-Pro.local']:
        env = 'localenv'
        print (env)
else:
        print ('Wrong Environment')
        exit()    


# ****************************
#    Configfile variablen    *
# ****************************
try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser                              # ver. < 3.0

parser = SafeConfigParser()                                                # instantiate


# parse existing config file
parser.read('../cfg/DocStat.cfg')                                # For local use
#parser.read('F:\\Programs\\DocStatistic\\cfg\\DocStat.cfg')        # For server use

DeltaFiles   = parser.get(env, 'DeltaFiles')
StatDir      = parser.get(env, 'StatDir')
DeltaFake    = parser.get(env, 'DeltaFake')
StatFile     = parser.get(env, 'StatFile')
outputFile   = parser.get(env, 'outputFile')
logPath      = parser.get(env, 'logPath')
server       = parser.get(env, 'server')
environment  = parser.get(env, 'environment')
labelTrun    = parser.get(env, 'labelTrun')
labelNetting = parser.get(env, 'labelNetting')


# ******************************************************
# *** Logger                                         ***
# ******************************************************
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



today = time.strftime("%d.%m.%Y")
year  = time.strftime("%Y")
hms   = time.strftime("%H:%M:%S")
jul   = time.strftime("%j")
dowl  = time.strftime("%A")


def wait4Files(path, filename, Y, year, jul, pattern):
    for name in glob.glob(path + filename + Y + year + jul + pattern):
        print (name)
        logger.info('File ' + filename + Y + year + jul + pattern + ' found in the input Directory.')
        for name1 in glob.glob(DeltaFake + filename + Y + year + jul + pattern):
            print (name1)
            if os.path.exists(name1):
                logger.info('The Docs was allready counted for the File ' + filename + Y + year + jul + pattern + ' today.')
                return False
        with open(path + filename + Y + year + jul + pattern) as f:
            line_count = len(f.readlines())
            print (line_count)
            out = open(StatDir + StatFile, 'a')
            out.write(today + "  " + hms + "   " + "RUN" + pattern + "  Docs in File " + "  " + (str(line_count)) + "\n")
            out.close()
            logger.info('The Docs are counted and writied to the File ' + StatDir + StatFile + '.')

            sendEmail(server + "@six-group.com", 'heinz.wuethrich@six-group.com', 
#            "Docstatistic VDFS " + environment, today + "     RUN" + pattern + "   " + (str(line_count)) + " Docs", files=[])
            "Docstatistic VDFS " + environment, pattern + "  " + (str(line_count)) + " Docs", files=[])
            s1 = open(DeltaFake + filename + Y + year + jul + pattern, 'w')
            s1.close()
            
            inputFile = filename + Y + year + jul + pattern
            logger.info('call subprocess DocCounter.py with the inputFilename ' + inputFile + '.')
            subprocess.call(['python.exe', 'DocCounter.py', inputFile])
        return True
    return False



logger.info('Starting Script to search inputFile to create Statisic for Doc Counts')


# ************************************
# ***    Run Doc_Count for T10T    ***
# ************************************
if not wait4Files(DeltaFiles, labelTrun, ".Y", year, jul + ".", "T10T"):
    print ('The input File ' + labelTrun + ".Y" + year + jul + 'T10T' + ' are not available, Sleeping for 5 sec')
    time.sleep(1)

if not wait4Files(DeltaFiles, labelTrun, ".Y", year, jul + ".", "T20T"):
    print ('The input File ' + labelTrun + ".Y" + year + jul + 'T20T' + ' are not available, Sleeping for 5 sec')
    time.sleep(1)
        
if not wait4Files(DeltaFiles, labelTrun, ".Y", year, jul + ".", "T30T"):
    print ('The input File ' + labelTrun + ".Y" + year + jul + 'T30T' + ' are not available, Sleeping for 5 sec')
    time.sleep(1)

if not wait4Files(DeltaFiles, labelNetting, ".Y", year, jul + ".", "D01T"):
    print ('The input File ' + labelNetting + ".Y" + year + jul + 'D01T' + ' are not available, Sleeping for 5 sec')
    time.sleep(1)
        
if dowl == 'Sunday':
    if not wait4Files(DeltaFiles, labelTrun, ".Y", year, jul + ".", "T01S"):
        print ('The input File ' + labelTrun + ".Y" + year + jul + 'T01S' + ' are not available, Sleeping for 5 sec')

        time.sleep(1)
else:
    print ("not Sunday, the Script will be abort")
    logger.info('not Sunday, the Script will be abort')

time.sleep(5)


#if __name__ == "__main__":
    