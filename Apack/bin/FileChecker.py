#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        29.04.2017
# Modified:       
# Program:        Filechecker.py

# Description:    Checkt ob die Files existieren


import os
import time
import glob
import fnmatch 

# **********************************************
# * Prüft ob ein File vorhanden ist oder nicht *
# **********************************************
def FileExists(Filename):
    if os.path.exists(Filename) == True:
        if os.path.isfile(Filename) == True:
            print ('Das File ' + Filename + ' ist vorhanden')
        else:
            print ('' + Filename + ' ist kein File') 
    else:
        print ('Kein File und kein Directory mit dem namen ' + Filename + ' vorhanden')


# ************************************************
# *          Prüft ob es ein File ist            *
# ************************************************
def IsFile(Filename):
    if os.path.isfile(Filename) == True:
        print ('Das File ' + Filename + ' ist vorhanden') 
        print ("last modified: %s" % time.ctime(os.path.getmtime(Filename)))
        print ("created: %s" % time.ctime(os.path.getctime(Filename)))
    else:
        print ('' + Filename + ' ist kein File')
        

# ************************************************
# *     Prüft ob es ein Directory ist            *
# ************************************************
def IsDir(Dirname):
    if os.path.isdir(Dirname) == True:
        print ('Das Directory ' + Dirname + ' ist vorhanden')
        print ("last modified: %s" % time.ctime(os.path.getmtime(Dirname)))
        print ("created: %s" % time.ctime(os.path.getctime(Dirname)))
    else:
        print ('' + Dirname + ' ist kein Directory')
        
                
# *****************************************************************************************
# *     Prüft ob das File von heute ist, checkt den last modified Zeitstempel des Files   *
# *****************************************************************************************
def FileExistsFromToday(Filename):
    nowdate   = time.strftime("%d.%m.%Y")
    if os.path.isfile(Filename) == True:
        if time.strftime("%d.%m.%Y",time.localtime(os.path.getmtime(Filename))) == nowdate:
            print ('Das File ' + Filename + ' von Heute ist vorhanden')
        else:
            print ('Kein File mit dem last modified date von Heute vorhanden vorhanden')
    else:
        print ('' + Filename + ' ist kein File')
        

# ******************************************************
# *     Prüft ob das File im Filenamen von heute ist   *
# ******************************************************      
def FileExistsWithJulDateFromToday(rootPath, FilePattern):
    juldate   = time.strftime("%j")
    year   = time.strftime("%Y")    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, FilePattern):
#            print( os.path.join(root, filename))
            print(os.path.join(filename))
            print (filename[10:17])
            if filename[10:17] == year + juldate:
                print ('Das File ' + filename + ' von Heute ist vorhanden')
            else:
                print ('Es ist kein File vorhanden') 


def FileExistsWithDateFromTodayInFilename(rootPath, FilePattern):
    date   = time.strftime("%Y%m%d")    
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, FilePattern):
#            print( os.path.join(root, filename))
            print(os.path.join(filename))
            print (filename[10:18])
            if filename[10:18] == date:
                print ('Das File ' + filename + ' von Heute ist vorhanden')
            else:
                print ('Es ist kein File vorhanden') 


                
# *********************************************************
# *     Prüft ob das Datum im Filenamen vom Vortag ist    *
# *********************************************************      
def FileExistsWithJulDateFromYesterday(rootPath, FilePattern):
    juldate   = time.strftime("%Y%j")
    juldateYester = int(juldate) -1
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, FilePattern):
            if filename[10:17] == str(juldateYester):
                print ('Das File ' + filename + ' von Heute ist vorhanden')
            else:
                print ('Es ist kein File vorhanden')


# ***********************************************************************
# *     Prüft ob das File vorhanden ist, wenn nein, wird es erstellt    *
# ***********************************************************************     
def open_if_not_exists(filename):
    try:
        fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except OSError as e:
        if e.errno == 17:
            print (e)
            return None
        else:
            raise
    else:
        return os.fdopen(fd, 'w') 





#FileExists('U:\\ZZZ\\CH31')                                                     # Aufruf der Funktion  
#IsFile('U:\\ZZZ\\rollover.log')                                                 # Aufruf der Funktion
#IsDir('U:\\ZZZ\\CH31')                                                          # Aufruf der Funktion
#FileExistsFromToday('U:\\ZZZ\\rollover.log')                                    # Aufruf der Funktion
#FileExistsWithJulDateFromToday('U:\\ZZZ\\CH31\\hah\\DATA\\', 'A*.*.EDI')        # Aufruf der Funktion  
#FileExistsWithDateFromTodayInFilename('U:\\ZZZ\\CH31\\hah\\DATA\\', 'A*.*.EDI')  # Aufruf der Funktion
#FileExistsWithJulDateFromYesterday('U:\\ZZZ\\CH31\\hah\\DATA\\', 'A*.*.EDI')    # Aufruf der Funktion
#open_if_not_exists('U:\\ZZZ\\rollover.log')                                     # Aufruf der Funktion


'''
print os.path.getmtime('U:\\ZZZ\\rollover.log')
print os.stat('U:\\ZZZ\\rollover.log').st_mtime
print time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime('U:\\ZZZ\\rollover.log')))
print time.strftime("%d.%m.%Y %I:%M:%S",time.localtime(os.path.getmtime('U:\\ZZZ\\rollover.log')))
print time.strftime("%m.%d.%Y",time.localtime(os.path.getmtime('U:\\ZZZ\\rollover.log')))
print time.strftime("%Y%j",time.localtime(os.path.getmtime('U:\\ZZZ\\rollover.log')))
'''

