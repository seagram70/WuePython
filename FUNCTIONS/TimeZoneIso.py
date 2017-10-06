#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        22.01.2017
# Modified:       
# Program:        TimeZoneIso.py

# Description:    rechnen der UTC ISO-8061 Time Zone


import time
import datetime

def UTCDiff():
    '''
    Return the Differenz to UTC-Timezone like '+01:00'
    '''
    time_offset = - time.timezone / 3600
    offset_hours = int(time_offset)
    offset_minutes = (time_offset - offset_hours) * 60
    return "+%02d:%02d" %(offset_hours, offset_minutes)
    
def getCurISODateTime():
    '''
    Return the current datetime in ISO-8061 Format, excl. Timezonedelta
    '''
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S')


date_time = getCurISODateTime()
date_time_tzDelta = date_time + UTCDiff()
print date_time_tzDelta

