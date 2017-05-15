#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
'''
today = time.strftime('%d.%m.%Y')

with open('/Users/Heinz-MacBook/Documents/workspace/Privat/testlog.txt') as f:
    for line in f:
        if "The GROUP01 are Completet for Run K31T" in line:
            print line
            print line[0:10]
            if line[0:10] == today:
                print 'super'
            else:
                print 'scheisse'
'''                
def findGroupsinLog(input, group, run):
    today = time.strftime('%d.%m.%Y')
    with open(input) as f:
        for line in f:
            if "The " + group + " are Completet for Run " + run in line:
                print line
                print line[0:10]
                if line[0:10] == today:
                    print 'super'
                else:
                    print 'scheisse'
                    
findGroupsinLog('/Users/Heinz-MacBook/Documents/workspace/Privat/testlog.txt', 'GROUP01', 'K31T')
    