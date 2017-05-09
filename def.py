#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

logfile = "/Users/Heinz-MacBook/CloudStation/Python/intest.txt"

def log(stat, msg):
    f = open(logfile,"a")
    f.write("%s %s %s\n" % (time.strftime("%d.%m.%Y %H:%M:%S"), stat, msg))
    f.close


log("[INFO]", " Eine neue Nachricht für die Log-Datei")