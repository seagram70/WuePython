#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import sys


# path and name of the log file
logfile = 'U:\\ZZZ\\logs\\VdfsMemoryLogs.log'

# function to save log messages to specified log file
def log123(msg):
    f = open(logfile,"a")
    f.write("%s: %s\n" % (time.strftime("%d.%m.%Y %H:%M:%S"), msg))
    f.close

# main function
def main():
# create new log message
    log123("Die Menory Losgs wurde von den VDFS Servern Downloaded un Zipped")

    sys.exit(0)

if __name__ == '__main__':
    main()