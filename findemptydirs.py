#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join, isfile

def walksub(dir):
    isEmpty=True
    subDirs=[]
    for entry in os.listdir(dir):
        try:
            if isfile(join(dir,entry))==True:
                isEmpty = False
            else:
                subEmpty =  walksub(join(dir, entry))
                if subEmpty==True:
                    subDirs.append(join(dir, entry))
                else:
                    isEmpty=False
        except :
            print ("error checking: "+entry)
            isEmpty=False
    if isEmpty == False:
        for subDir in subDirs:
            print subDir
    return isEmpty


walksub('/Users/Heinz-MacBook/Downloads/')


