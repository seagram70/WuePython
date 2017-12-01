#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import zipfile



zipf = "U:\\ZZZ\\compress.zip"  

def main():
    directory = r"U:\\ZZZ\\"
    toZip(directory)

def toZip(directory):
    zippedHelp = zipfile.ZipFile(zipf, "w", compression=zipfile.ZIP_DEFLATED )

    liste = os.listdir(directory)
    for file_list in liste:
        file_name = os.path.join(directory,file_list)

        if os.path.isfile(file_name):
            print file_name
            zippedHelp.write(file_name)
        else:
            addFolderToZip(zippedHelp,file_list,directory)
            print "---------------Directory Found-----------------------"
    zippedHelp.close()


def addFolderToZip(zippedHelp,folder,directory):
    path=os.path.join(directory,folder)
    print path
    file_list=os.listdir(path)
    for file_name in file_list:
        file_path=os.path.join(path,file_name)
        if os.path.isfile(file_path):
            zippedHelp.write(file_path)
        elif os.path.isdir(file_name):
            print "------------------sub directory found--------------------"
            addFolderToZip(zippedHelp,file_name,path)


if __name__=="__main__":
    main()
    