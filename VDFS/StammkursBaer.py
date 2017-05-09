#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        02.01.2017
# Modified:       
# Program:        StammkursBaer.py

# Description:    
#                 
#                 

import time
import shutil
import socket

today = time.strftime("%d.%m.%Y")
hms   = time.strftime("%H:%M:%S")
hm    = time.strftime("%H:%M")
wd    = time.strftime("%w")

source = "U:\\ZZZ\\XXX\\Stammkurs.txt"
dest   = "U:\\ZZZ\\YYY"
lst = ['1', '2', '3', '4', '5']
lstS = '6'

def time2run(weekday, zeit):
    if weekday == wd:
        if zeit== hm:
            shutil.copy(source, dest)
            print "Copy Job wurde ausgeführt"
        else:
            print "Falsche Zeit, script wird nicht ausgeführt"
    else:
        print "Es müsste Sonntag sein"
            

# Ausführung von Montag bis Freitag

HOST = (socket.gethostname())   

if HOST == 'mpzhwmvdfs01':
    if wd in lst:
        var = wd
        time2run(var, '12:12')
        if wd == lstS:
            time2run('6', '12:08')
        
elif HOST == 'mpzhwfvdfs07':
    print "gagag"
    
else:
    print "ist noch nicht fertig"
    