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

