#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

today = time.strftime("%d.%m.%Y")
year  = time.strftime("%Y")
hms   = time.strftime("%H:%M:%S")
jul   = time.strftime("%j")
day   = time.strftime("%A")

#print day 

#if day != "Saturday" or day != "Sunday":
#if day != "Saturday":

if day == "Friday":
    print "start reboot Samstag"

elif day == "Saturday": 
    print "start reboot da Sonntag"

else:
    print "Kein reboot da weder Sa noch So"
    
        

'''
    monat = int(time.strftime("%m", time.gmtime()))
    tag = int(time.strftime("%d", time.gmtime()))
    stunden = int(time.strftime("%H", time.gmtime()))
    minuten = int(time.strftime("%M", time.gmtime()))
    sekunden = int(time.strftime("%S", time.gmtime()))
    print stunden
    '''