#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import time
import glob
import os



today = time.strftime("%d.%m.%Y")
year  = time.strftime("%Y")
hms   = time.strftime("%H:%M:%S")
jul   = time.strftime("%j")


inDir    = "U:\\ZZZ\\XXX\\"
StatDir  = "U:\\ZZZ\\XXX\\Docs\\"
Deltas   = "U:\\ZZZ\\XXX\\Files\\"
StatFile = "DocStatisik.txt"


def wait4Files(path, filename, Y, year, jul, pattern):
    for name in glob.glob(path + filename + Y + year + jul + pattern):
        print name
        for name1 in glob.glob(Deltas + filename + Y + year + jul + pattern):
            print name1
            if os.path.exists(name1):
                return False                                                     #zusatz
        with open(path + filename + Y + year + jul + pattern) as f:
            line_count = len(f.readlines())
            print line_count
            out = open(StatDir + StatFile, 'a+')
            out.write(today + "  " + hms + "   " + "RUN" + pattern + "  Docs in File " + "  " + (str(line_count)) + "\n")
            out.close()
            s1 = open(Deltas + filename + Y + year + jul + pattern, 'w')
            s1.close()
        return True
    return False


while 1:

# ************************************
# ***    Run Doc_Count for T10T    ***
# ************************************
    if not wait4Files(inDir, "VDMMAPS", ".Y", year, jul, ".T10T"):
        print "Sleeping for 60 sec"
        time.sleep(10)

    if not wait4Files(inDir, "VDMMAPS", ".Y", year, jul, ".T20T"):
        print "Sleeping for 60 sec"
        time.sleep(10)
        
    if not wait4Files(inDir, "VDMMAPS", ".Y", year, jul, ".T30T"):
        print "Sleeping for 60 sec"
        time.sleep(10)

    if not wait4Files(inDir, "VDLMAPS", ".Y", year, jul, ".D01T"):
        print "Sleeping for 60 sec"
        time.sleep(10)

    if not wait4Files(inDir, "VDMMAPS", ".Y", year, jul, ".T01S"):
        print "Sleeping for 60 sec"
        time.sleep(10)
        
                    
