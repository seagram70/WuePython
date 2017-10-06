#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    
import os
import glob
import logging
import logging.handlers
import time
import logging
from logging.handlers import RotatingFileHandler


pfad = '/Users/Heinz-MacBook/Documents/workspace/Privat/logs'
logfiles = [f for f in os.listdir(pfad)]

#logfiles = [f for f in os.listdir(pfad) if os.path.isfile(f)]
#print logfiles


def logRollover():
    for ff in logfiles:
        print ff
        logger = logging.getLogger(ff)
        handler = logging.handlers.RotatingFileHandler(ff, backupCount=5)
        logger.addHandler(handler)



        logger = logging.getLogger(ff)
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler('testlog.log', backupCount=10)
        logger.addHandler(handler)


    
    
logRollover()


