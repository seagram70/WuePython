<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

logfile = "/Users/Heinz-MacBook/CloudStation/Python/intest.txt"

def log(stat, msg):
    f = open(logfile,"a")
    f.write("%s %s %s\n" % (time.strftime("%d.%m.%Y %H:%M:%S"), stat, msg))
    f.close


log("[INFO]", " Eine neue Nachricht für die Log-Datei")
=======
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def pow_example(n, p=2):
    '''works only with p >= 1'''
    if p <= 1:
        return n
    return n * pow_example(n, p-1)

print (pow_example(3, 3))

print('test')
>>>>>>> integration
