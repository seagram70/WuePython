#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        22.01.2017
# Modified:       08.02.2017        Service Stop eingebaut
#                 18.02.2017        Master Server als letzten Server eingefügt
#                 07.03.2017        config File anpassung in liste gesetzt
#                 12.03.2017        Logmeldungen angepasst
# Program:        ShutdownVDFS.py
# Version:        2.0.0

# Description:    Rollt alle Logfiles aus dem LOG Directory. Ab der Version 5 im
#                 log_archive Directory werde die Files gezippt und in einen neu
#                 angelegten Ordner abgelegt.


import os, shutil 
import time
import logging.handlers
import zipfile
from os import listdir
from os.path import isfile, join, exists
#import socket
import win32serviceutil
import subprocess
import glob

# ****************************
#    Configfile variablen    *
# ****************************
try:
    from configparser import SafeConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser       # ver. < 3.0

parser = SafeConfigParser()
parser.read('..\\cfg\\Shut.cfg')    # For local use

#config.read('F:\\Programs\\Shutdown-LogRollover\\cfg\\Shut.cfg')        # For server use


rolloverlog     = parser.get('pfade', 'rolloverlog')
PFAD_ARCH       = parser.get('pfade', 'PFAD_ARCH')
PFAD_LOG        = parser.get('pfade', 'PFAD_LOG')
environment     = parser.get('pfade', 'environment')

# ******************************************************
# *** Logger                                         ***
# ******************************************************
logger = logging.getLogger("   v2.0.0  ")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(rolloverlog)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]  %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

# ***************************************************************
#    def Functions                                              *
# ***************************************************************

# Wait for the input File are createt
def wait4Files(path, filenamePattern):
    for name in glob.glob(path + filenamePattern):
        print name
        return True
    return False

# Stopped the running windows Services
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
    except Exception:
        logger.warn('The Service does not exist ' + service + ' Error 1060 is allowed.', exc_info=False)


def reboot_server(env):
    try:
        for server in env:
            subprocess.call('shutdown -r -f -t 10 /m \\\\%s' % server)
            logger.info('Server ' + server + ' start rerboot')
    except Exception:
        logger.error('The Server ' + server + ' will not rebooted', exc_info=True)
        

# ***************************************************************
#    auslesen der config section "server" und section           *
#    services aus dem config File                               *
# ***************************************************************
#HOST        = (socket.gethostname())
items = parser.items( "server" )
liste = []
for keyServer, valueServer in items:
    liste.append(valueServer)
serverlist = liste


items = parser.items( "services" )
listeserv = []
for keyservices, valueservices in items:
    listeserv.append(valueservices)
listeServices = listeserv

# ***************************************************************
#    check is Database Backup File exists                       *
# ***************************************************************
while not wait4Files("H:\\", "VDFS_DATA_????????_??????_T01S.BAK"):
    print "Sleeping for 60 sec"
    logger.info('Sleeping for 60 sec')
    time.sleep(60)

# ***************************************************************
#    30 min wait until the DB Backup file is closed             *
#    VDFS_DATA_????????_??????_T01S.BAK                         *
# ***************************************************************
time.sleep(1800)

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
    logger.error('The Zip archive Dir allready exists, the Script allows just one run per Day')
    try:
        reboot_server(serverlist)
    except Exception,e:
        logger.error('not all Server are rebootet', exc_info=True)
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
    except Exception,e:
        logger.warn('One or more logfiles allready exists in the log_archive Directory without any extensions', exc_info=True)
logger.info('Logfiles moved to the log_archive Directory')
    

try:
    for nFiles in logfiles:
        f = open(nFiles, 'w+')
        f.close()
except Exception, e:
    logger.error('IOError: [Errno 13] Permission denied: ' + nFiles + ' ', exc_info=True)

logger.info('New empty lofiles are created')

# ***************************************************************
#    LogRollover im Log_archive Directory, max 5 Versionen     *
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
try:
    for fFiles in logfiles:
        os.remove(fFiles)
except IOError:
    logger.error(' ', exc_info=True)

logger.info('all empty logfiles in the log_archive Directory are deletet')

# *************************************************************
#    Shutdown Slave und Fileserver                            *
# *************************************************************
try:
    reboot_server(serverlist)
except Exception,e:
    logger.error('not all Server are rebootet', exc_info=True)

