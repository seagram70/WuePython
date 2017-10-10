#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        04.04.2017
# Modified:       
# Program:        LogRollOverSlaveserverVDFS.py

# Description:    Rollt alle Logfiles aus dem LOG Directory. Ab der Version 5 im
#                 log_archive Directory werde die Files gezippt und in einen neu
#                 angelegten Ordner abgelegt.
#


import os, shutil 
import time
import logging.handlers
import zipfile
from os import listdir
from os.path import isfile, join, exists
import socket
import win32serviceutil

#today = time.strftime("%d.%m.%Y")
#hms   = time.strftime("%H:%M:%S")

# ***************************************************************
#    Variablen definition                                       *
# ***************************************************************
#rolloverlog = 'E:\\rollover.log'
logPath     = "D:\\rollover.log"
PFAD_ARCH   = 'D:\\logs\\log_archive'
PFAD_LOG    = 'D:\\logs'
HOST        = (socket.gethostname())

listeServices = ["PatrolAgent", "VDFSAgentControllerService"]

# ******************************************************
# *** Logger                                         ***
# ******************************************************
logger = logging.getLogger("   v1.1.0  ")
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
# *** Definitions Stop Service                       ***
# ******************************************************
def stop_service(service):
    try:
        ret =  win32serviceutil.QueryServiceStatus(service)
        print "check if Services exists"
        logger.info('check if Services exists')
        while ret[1] != 1:
            if ret[1] == 4:
                win32serviceutil.StopService(service)
            time.sleep(1) 
            ret =  win32serviceutil.QueryServiceStatus(service)
        print "" + service + " stopped"
        logger.info('Service ' + service + ' stopped')
#        return "" + service + " stopped"
    except:
        print "Error 1060 is allowd. The Service did not exist"
        logger.info('The Service does not exist ' + service + ' Error 1060 is allowed.')


# ***************************************************************
#    Stop der VDFS Services   je nach Umgebung                  *
# ***************************************************************
for service in listeServices:
    stop_service(service)
    
# ***************************************************************
#    list logfiles without Directorys                           *
# ***************************************************************
logfiles = [f for f in listdir(PFAD_LOG) if isfile(join(PFAD_LOG, f))]
logger.info('listdir to the logdirectory')

# ***************************************************************
#    Create Zip Directory for Versions > 5                      *
# ***************************************************************
os.chdir(PFAD_ARCH)
zipdir = (time.strftime("Logfiles-%Y-%m-%d"))
if exists(zipdir):
    logger.info('The Zip archive Dir allready exists, the Script allows just one run per Day')
    exit()
else:
    os.mkdir(zipdir)
    logger.info('ZIP Directory created for versions >5')

    for files in os.listdir(PFAD_ARCH):
        if files.endswith(".5"):
            newZip = zipfile.ZipFile(files + '.zip', 'w')
            newZip.write(files, compress_type=zipfile.ZIP_DEFLATED)
            newZip.close()
            shutil.move(files + ".zip", zipdir)

logger.info('all Files with version >5 are zipped and moved')
    
# ***************************************************************
#    Log Files wrden in das log_archive Directory verschoben    *
#    und wieder als leere Files angelegt                        *
# ***************************************************************
os.chdir(PFAD_LOG)
for lFiles in logfiles:
    try:
        shutil.move(lFiles, PFAD_ARCH)
    except:
        logger.info('One or more logfiles allready exists in the log_archive Directory without any extensions')
logger.info('Logfiles moved to the log_archive Directory')
    
for nFiles in logfiles:
    f = open(nFiles, 'w+')
    f.close()
logger.info('New empty lofiles are created')

# ***************************************************************
#    LogRollover im Log_archive Directory, max 20 Versionen     *
#    und wieder als leere Files angelegt                        *
# ***************************************************************
os.chdir(PFAD_ARCH)
for ff in logfiles:
    my_logger = logging.getLogger(ff)
#    my_logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(ff, backupCount=5)
    my_logger.addHandler(handler)
    my_logger.handlers[0].doRollover()
    handler.close()
logger.info('Logfiles are rolled in the log_archive Directory')

# ***************************************************************
#    Die Temporaer angelegten logdateien werden geloescht       *
# ***************************************************************
for fFiles in logfiles:
    os.remove(fFiles)
logger.info('all empty logfiles in the log_archive Directory are deletet')

