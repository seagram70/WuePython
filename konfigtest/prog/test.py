#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from ConfigParser import ConfigParser

def read_single_value(spath, section, key):
    config = ConfigParser()
    config.read(spath)
    return config.get(section, key)

print read_single_value('conftest.cfg', 'service', 'service1')


'''
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
    
'''