#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        06.02.2017
# Modified:       
# Program:        DeleteOlderThan.py

# Description:    Löscht alle Files älter als x Tage im angegebenen Directory
#                 und allen Subdirectorys.


import os
import time
 
path = r"U:\ZZZ\\"
now = time.time()
cut = time.time() - 7 * 86400

for dirpath, dirs, files in os.walk(path):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
#            os.remove(filename)