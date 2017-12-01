#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    
import os
from logging.handlers import RotatingFileHandler
import logging

pfad = '/Users/Heinz-MacBook/Documents/workspace/Privat/logs'

logfiles = [f for f in os.listdir(pfad)]
print (logfiles)

def logRollover():
    for ff in logfiles:
        logger = logging.getLogger(ff)
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler('testlog99.log', backupCount=10)
        logger.addHandler(handler)
        

logRollover()
      
'''
        print (ff)
        logger = logging.getLogger(ff)
        handler = logging.handlers.RotatingFileHandler(ff, backupCount=12)
        logger.addHandler(handler)

        logger = logging.getLogger(ff)
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler('testlog99.log', backupCount=10)
        logger.addHandler(handler)

'''
    
    


