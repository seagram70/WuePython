#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
from logging.handlers import RotatingFileHandler
import logging
#import logging.handlers
import time
import shutil
from os.path import isfile, join


# pfad definitionen
pfadlocal = "C:\\Daten\\workspace\\rddelivery\\FUNCTIONS\\Logs\\"
pfadarch  = "C:\\Daten\\workspace\\rddelivery\\FUNCTIONS\\Logs\\Log_Archive\\"


# Nur Files aus dem Directory einlesen, muss mit LOG oder TXT enden.
logfiles  = [f for f in os.listdir(pfadlocal) if isfile(join(pfadlocal, f)) and f.endswith('.log') or f.endswith('.txt')]
logfiles5 = [f for f in os.listdir(pfadlocal) if isfile(join(pfadlocal, f)) and f.endswith('.5')]

# Function
def rotating_log_archive(path, path_arch, archive_Dir, logfilename, versions):
    try:
        if os.path.exists(archive_Dir):
            print '' + archive_Dir + ' existiert in der ersten schleife'
        else:
            os.mkdir(archive_Dir)
            print '' + archive_Dir + ' wurde in der else schleife erstellt'
        
        if logfilename.endswith(".5"):
            print logfilename
            shutil.move(logfilename, archive_Dir)
            print '' + logfilename + ' wurde kopiert'
        else:
            print 'Es ist kein Logfile mit der angegebenen Version vorhanden'
            
    except:
        print "da scheint was in die Hosen gegangen zu sein"
    
    logger = logging.getLogger(logfilename)
    handler = RotatingFileHandler(logfilename, backupCount=versions)
    logger.addHandler(handler)
    logger.handlers[0].doRollover()
    handler.close()


os.chdir(pfadlocal)
for names5 in logfiles5:
    print names5
    
for names in logfiles:
    print names
    rotating_log_archive(pfadlocal, pfadarch, pfadlocal + "logfiles-" + time.strftime("%Y-%m-%d"), names, 5)


  
if __name__ == "__main__":
    pass
