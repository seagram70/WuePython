#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import os
import glob

#print (sys.argv[1])


try:
    if sys.argv[1] == 1:
        print('leider leer')
except IndexError as e:
    print('im der except schleife')
    exit()
    
print('bin raus')

for fil in os.listdir('/Users/Heinz-MacBook/Documents/workspace/Privat/logs'):
    print (fil)
    
    for out in glob.glob('/Users/Heinz-MacBook/Documents/workspace/Privat/logs')
    
    