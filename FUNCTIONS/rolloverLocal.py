#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
from logging.handlers import RotatingFileHandler
import logging
from os.path import isfile, join


# pfad definitionen
pfadlocal = "C:\\Daten\\workspace\\rddelivery\\FUNCTIONS\\Logs\\"


# Nur Files aus dem Directory einlesen, muss mit LOG oder TXT enden.
logfiles = [f for f in os.listdir(pfadlocal) if isfile(join(pfadlocal, f)) and f.endswith('.log') or f.endswith('.txt')]


# Function
def rotating_log_local(path, logfilename, versions):
    logger = logging.getLogger(logfilename)
    handler = RotatingFileHandler(logfilename, backupCount=versions)
    logger.addHandler(handler)
    logger.handlers[0].doRollover()
    handler.close()


# Ausführung der definition
os.chdir(pfadlocal)
for names in logfiles:
    rotating_log_local(pfadlocal, names, 5)




if __name__ == "__main__":
    pass

