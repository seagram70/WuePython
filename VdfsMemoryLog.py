#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        14.01.2017
# Modified:       14.01.2017
# Program:        VdfsProcesslog.py

# Description:    Create Drivemap to VDFS an make a get to f:\logs Directory on the Master VDFS Server.
#                 Copy Logfiles named VDFS-processlog to the local Drive
#                 Drive letter: Z
# Shared path:    \\mislwmvdfs41\F$
# Username:       domain01\*****
# Password:       ********


import os, shutil
from os.path import exists
import subprocess
import zipfile




#*******************************************************
# ***    Pfad Variablen                                *
#*******************************************************
pfadin  = "Z:\\logs\\log_archive"
pfadout = "S:\\NAS\\VDFS-Memory-Logs"
file1   = "memory_mpzhwmvdfs01.log.1"
file2   = "memory_mpzhwsvdfs02.log.1"
file3   = "memory_mpzhwsvdfs03.log.1"
file4   = "memory_mpzhwsvdfs04.log.1"
file5   = "memory_mpzhwsvdfs05.log.1"
file6   = "memory_mpzhwsvdfs06.log.1"




#*********************************************************************************
# ***    Drive Map auf VDFS01 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwmvdfs01\F$ $Nil22pferd /user:mpzhwmvdfs01\vdfsadmin', shell=True)                   #VDFS Produktions Master Server

if exists("Z:\\"):
    print "Drive auf VDFS01 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS01 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file1, pfadout)
print "File wurde vom VDFS01 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file1 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file1, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file1)
print " unzipped File wurde geloescht"





#*********************************************************************************
# ***    Drive Map auf VDFS02 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwsvdfs02\E$ $Nil22pferd /user:mpzhwsvdfs02\vdfsadmin', shell=True)                   #VDFS Produktions Slave Server

if exists("Z:\\"):
    print "Drive auf VDFS02 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS02 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file2, pfadout)
print "File wurde vom VDFS02 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file2 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file2, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file2)
print " unzipped File wurde geloescht"



#*********************************************************************************
# ***    Drive Map auf VDFS03 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwsvdfs03\E$ $Nil22pferd /user:mpzhwsvdfs03\vdfsadmin', shell=True)                   #VDFS Produktions Slave Server

if exists("Z:\\"):
    print "Drive auf VDFS03 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS03 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file3, pfadout)
print "File wurde vom VDFS03 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file3 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file3, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file3)
print " unzipped File wurde geloescht"




#*********************************************************************************
# ***    Drive Map auf VDFS04 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwsvdfs04\E$ $Nil22pferd /user:mpzhwsvdfs04\vdfsadmin', shell=True)                   #VDFS Produktions Slave Server

if exists("Z:\\"):
    print "Drive auf VDFS04 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS04 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file4, pfadout)
print "File wurde vom VDFS04 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file4 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file4, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file4)
print " unzipped File wurde geloescht"




#*********************************************************************************
# ***    Drive Map auf VDFS04 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwsvdfs05\E$ $Nil22pferd /user:mpzhwsvdfs05\vdfsadmin', shell=True)                   #VDFS Produktions Slave Server

if exists("Z:\\"):
    print "Drive auf VDFS05 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS05 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file5, pfadout)
print "File wurde vom VDFS05 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file5 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file5, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file5)
print " unzipped File wurde geloescht"




#*********************************************************************************
# ***    Drive Map auf VDFS06 und abhohlen der Memory Logs                       *
#*********************************************************************************
subprocess.call(r'net use z: \\mpzhwsvdfs06\E$ $Nil22pferd /user:mpzhwsvdfs06\vdfsadmin', shell=True)                   #VDFS Produktions Slave Server

if exists("Z:\\"):
    print "Drive auf VDFS06 ist bereits geamappt"
else:
#    os.system('U:\\ZZZ\\MAP_VDFS.bat')        #is it possible to execute a externel cmd script
    print "Drive auf VDFS06 wurde gemappt, Daten koennen abgehohlt werden"

shutil.copy(pfadin + '\\' + file6, pfadout)
print "File wurde vom VDFS06 Server abgehohlt"

subprocess.call('net use z: /delete /yes', shell=True)
print "Disconnect des Share Drives Z"

os.chdir(pfadout)

newZip = zipfile.ZipFile(file6 + ".zip", 'w')                                   #Input File wird gezippt
newZip.write(file6, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
print "Das File wurde gezippt, das unzipped File wird im naechten Step geloescht"

os.remove(file6)
print " unzipped File wurde geloescht"

exit()

