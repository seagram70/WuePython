#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from stat import ST_MTIME

pfad = '/Users/Heinz-MacBook/Documents/workspace/Privat/logs/testlog.log'

def FileStat(filename):
    try:
        if os.stat(filename)ST_MTIME:
            print 'ein file ist vorhanden'
        else:
            print 'ein file ist NICHT vorhanden'
    except:
        print 'scheisse'

FileStat(pfad)


'''
def FileExistsToday(filename):
    try:
        if os.path.exists(filename) == True:
            print 'ein file ist vorhanden'
        else:
            print 'ein file ist NICHT vorhanden'
    except:
        print 'scheisse'

FileExistsToday(pfad)

'''