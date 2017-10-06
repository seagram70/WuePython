#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        06.02.2017
# Modified:       
# Program:        delOlderVddGrp.py

# Description:    Löscht alle Files älter als 2 Tage im NFS Directory auf dem Master Server


import os
import time
 
pathsigend = r"F:\\NFS\\bwksignalend\\"
pathsigvdd = r"F:\\NFS\\bwksignal-vdd\\"
pathgrp10  = r"F:\\NFS\\GROUP10\\"
pathgrp20  = r"F:\\NFS\\GROUP20\\"
pathgrp30  = r"F:\\NFS\\GROUP30\\"

now = time.time()
cut = time.time() - 2 * 86400

# Delete all Files older then 2 Day's GROUP10
for dirpath, dirs, files in os.walk(pathgrp10):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
            os.remove(filename)
            

# Delete all Files older then 2 Day's GROUP20
for dirpath, dirs, files in os.walk(pathgrp20):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
            os.remove(filename)
            
            
# Delete all Files older then 2 Day's GROUP30
for dirpath, dirs, files in os.walk(pathgrp30):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
            os.remove(filename)
            

# Delete all Files older then 2 Day's bwksignalend
for dirpath, dirs, files in os.walk(pathsigend):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
            os.remove(filename)
            
            
# Delete all Files older then 2 Day's bwksignal-vdd
for dirpath, dirs, files in os.walk(pathsigvdd):
    for name in files:
#        print name
        filename = os.path.join(dirpath, name)
        if os.stat(filename).st_mtime < cut:
            print filename
            os.remove(filename)
