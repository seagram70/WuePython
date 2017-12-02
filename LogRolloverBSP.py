#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# Author:         Heinz Wuethrich
# Created:        19.01.2017
# Modified:       19.01.2017
# Program:        LogRollover.py

# Description:    Rollt Logfiles, append 1-20 auf alle Files im Directory mit dem Namen "LOG_FILENAME"
#                 Bevor die Logs gerollt werden wird eine Message ans ende des Logs geschrieben.


import os
import glob
#import logging
import logging.handlers
import time

LOG_FILENAME = 'U:\\ZZZ\\Logs\\test.log'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.INFO)

# Check if log exists and should therefore be rolled
needRoll = os.path.isfile(LOG_FILENAME)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, backupCount=20)
my_logger.addHandler(handler)


# This is a stale log, so roll it
if needRoll:    
    # Add timestamp wenn das Log geschlossen wurde
    my_logger.info('\n------------------------------------------\nLog closed on %s.\n------------------------------------------\n' % time.asctime())

    # Roll over on application start
    my_logger.handlers[0].doRollover()

# Add timestamp wenn das leere neue Logfile angelegt wurde.
my_logger.info('\n\n------------------------------------------\nLog started on %s.\n------------------------------------------\n' % time.asctime())

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)

print '\n'.join(logfiles)
