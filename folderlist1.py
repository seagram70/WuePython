#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

path="U:\\ZZZ"
pfad_out1="U:\\ZZZ\\AAA"
pfad_out2="U:\\ZZZ\\BBB"



#path = os.environ["U:\\ZZZ"]  # der aktuelle Benutzerordner
if os.path.exists(path) == True:
    print(path, "existiert.")
else:
    print(path, "existiert nicht.")



def folder_objects(dirname, otype = "all"):
    if (os.path.exists(path) == False or
        os.path.isdir(path) == False or
        os.access(path   , os.R_OK) == False):
        return False
    else:
        objects = os.listdir(path)
        result = []
        for objectname in objects:
            objectpath = path + "/" + objectname
            if (otype == "all" or
                (otype == "dir"  and os.path.isdir(objectpath)  == True) or
                (otype == "file" and os.path.isfile(objectpath) == True) or
                (otype == "link" and os.path.islink(objectpath) == True)):
                result.append(objectname)
        result.sort()
        return result

dirname = os.path
print("Alle:    ", folder_objects(dirname))
print("Ordner:  ", folder_objects(dirname, "dir"))
print("Dateien: ", folder_objects(dirname, "file"))
print("Symlinks:", folder_objects(dirname, "link"))
