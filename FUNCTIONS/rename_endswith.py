#! /usr/bin/python

import os
import re

# Alle Files mit der endung .bat werden durh .cmd ersetzt

def BadEnding(pfad, bad, good):
    path=pfad
    files=os.listdir(path)
    files = [ f for f in files if re.search(bad + '$', f, re.I)]
    for fname in files:
        newname=fname.replace(bad,good)
        os.rename(path + "/" + fname, path + "/" + newname)
    

BadEnding('U:\\ZZZ', '.7', '.5')