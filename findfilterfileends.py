#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

path = '/Users/Heinz-MacBook/Downloads'
level = 5 # Sucht aktuell 4 Ebenen tief, mit -1 wird gesucht was das Zeug hält :)
filter = '.pdf'

def search(path, level, filter):
    local_list = []
    if os.path.islink(path):
        print('Link: %s' % path)
    elif level > 0 or level < 0:
        directorylist = os.listdir(path)
        for element in directorylist:
            if os.path.isdir(path + os.sep + element):
                newpath = path + os.sep + element
                newlevel = level - 1
                search(newpath, newlevel, filter)
            else:
                newpath = path + os.sep + element
                if not newpath.endswith(filter):
                    print(newpath)

if __name__ == '__main__':
    search(path, level, filter)