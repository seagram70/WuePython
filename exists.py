#!/usr/bin/env python


import os.path


if os.path.exists("/Users/Heinz-MacBook/CloudStation/Python/intest.txt"):
    print "Files ist vorhanden"
    open("/Users/Heinz-MacBook/CloudStation/Python/intest.txt", "a+")
else:
    print " Das Files ist nicht schreibbarr !!!!!"
    
