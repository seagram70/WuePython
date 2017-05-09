#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        05.04.2017
# Modified:       
# Program:        DeleteFilePattern.py

# Description:    Löscht alle Files in der Directorys und SubDirectorys mit dem angegebenen File Pattern.


import os
import fnmatch 

rootPath = 'U:\\ZZZ\\'
pattern = '*K2T.Y*088.*'



x = raw_input('möchtest Du wirklich starten, es werden alle File mit dem angebebebn paramerer gelöscht--> J or N : ')
if x == 'J':
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print( os.path.join(root, filename))
            os.remove(os.path.join(root, filename))
            
    print 'all Files are removed'
else:    
    print 'Das Script wird nicht ausgführt'
    exit()

