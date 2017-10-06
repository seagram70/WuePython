#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        06.02.2017
# Modified:       
# Program:        emptyFolders.py

# Description:    Serch empty Folders

import os

pfad = "F:\\deliveryoutput\\"
output = "emptyFolders.log"

os.remove(output)

for dirpath, dirname, files in os.walk(pfad):
    if os.listdir(dirpath)==[]:
        print dirpath
        f = open(output, 'a+')
        f.write(str(dirpath) + '\n')
        f.close()
        