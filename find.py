#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time           

                
def findGroupsinLog(input, group, run):
    today = time.strftime('%d.%m.%Y')
    with open(input) as f:
        for line in f:
            if "The " + group + " are Completet for Run " + run in line:
#                print line
#                print line[0:10]
                if line[0:10] == today:
                    print 'super, das File für ' + group + ' ist vorhanden' 
                    return True
                else:
                    print 'scheisse kein File vorhanden'
        return False


while not findGroupsinLog('/Users/Heinz-MacBook/Documents/workspace/Privat/testlog.txt', 'GROUP01', 'K31T'):
    print "Sleeping for 30 sec"
    time.sleep(5)

while not findGroupsinLog('/Users/Heinz-MacBook/Documents/workspace/Privat/testlog.txt', 'GROUP02', 'K31T'):
    print "Sleeping for 30 sec"
    time.sleep(5)

while not findGroupsinLog('/Users/Heinz-MacBook/Documents/workspace/Privat/testlog.txt', 'GROUP03', 'K31T'):
    print "Sleeping for 30 sec"
    time.sleep(5)
    