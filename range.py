#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#lis = range(10)
#for idx in range(1,11):
#    for idx1 in range(1,11):
#        print idx * idx1,
#    print
    
#Version 2
lis = range(1,11) #oder lis = range(1,11) 
for idx in range(1,len(lis)+1):
    for idx1 in range(1,len(lis)+1):
        print idx * idx1,
    print