#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import time
import glob
import os
import json

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read('../cfg/damon.cfg')
mergPath     = config.get('input', 'mergPath')
logPath      = config.get('input', 'logPath')
service      = config.get('input', 'service')
server       = config.get('input', 'server')
environment  = config.get('input', 'environment')
docfile      = config.get('input', 'docfile')

d = {"Server": server, "Service": service, "environment": environment, "Date": time.strftime("%Y.%m.%d  %H:%M:%S")}

os.chdir(mergPath)
for fi in glob.glob("????"):
    d1 = {"Filename": fi}
    
f=open(mergPath + docfile, 'r')   
docs = f.read(7);
docs = {"Docs": docs}
f.close()


d.update(d1)
d.update(docs)
print d


j = json.dumps(d, indent=4)
f1 = open(mergPath + 'sample.json', 'w')
print >> f1, j
f1.close()
    
    
    

