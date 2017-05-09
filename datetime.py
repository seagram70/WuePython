#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import datetime
import time

t = datetime.time()
print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo


today = time.asctime()


#yesterday = today - time.timedelta(days = 1)
yesterday = today - time.strftime(days = 1)
print yesterday

lsmt = today - datetime.timedelta(days = 30)

def gaga():
    today = datetime.date.today()
    print today

def gaga2():
    yesterday = today - datetime.timedelta(days = 1)
    print yesterday


def gaga3():
    yesterday2 = yesterday.strftime("%d.%m.%Y")
    print yesterday2

    
def gaga4():
    lsmt = today - datetime.timedelta(days = 30)
    print lsmt


#gaga()
#gaga2()
#gaga3()
gaga3()
