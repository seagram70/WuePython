#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.handlers
import os


def logroll(LOG_PATH):
    logfiles = [f for f in os.listdir(LOG_PATH)]
    for ff in logfiles:
        print(ff)
        my_logger = logging.getLogger('MyLogger')
        my_logger.setLevel(logging.DEBUG)
        handler = logging.handlers.RotatingFileHandler(ff, backupCount=50)
        my_logger.addHandler(handler)
        my_logger.handlers[0].doRollover()


if __name__ == "__main__":
    logroll('/Users/Heinz-MacBook/Documents/workspace/Privat/logs/')
    
    