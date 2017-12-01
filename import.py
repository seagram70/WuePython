#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from log import log123

def writefile(file_name):

    try:
        fobj = open(file_name, "w+")
        fobj.write(file_name)
    
    except:
        print "So ein scheiss Error"
        exit()

    finally:
        fobj.close()
       
fold = "C:\Daten\Python\\"

for _file in range(1,11):
    file_name = fold + str(_file) + ".txt"
    writefile(file_name)
