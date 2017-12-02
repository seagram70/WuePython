#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging.handlers

LOG_FILENAME = '/Users/Heinz-MacBook/Documents/workspace/Privat/logs/testlog.log'

def logroll():
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, backupCount=50)
    my_logger.addHandler(handler)
    my_logger.handlers[0].doRollover()


if __name__ == "__main__":
    logroll()