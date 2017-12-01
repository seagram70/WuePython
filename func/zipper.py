#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time
import zipfile


today = time.strftime("%d.%m.%Y")
hms   = time.strftime("%H:%M:%S")


# ***************************************************************
#    Create Zip Directory for Versions > 5                      *
# ***************************************************************
def ZipFiles(pfad):
    os.chdir(pfad)
    for files in os.listdir(pfad):
        if files.endswith(".5"):
            newZip = zipfile.ZipFile(files + '.zip', 'w')
            newZip.write(files, compress_type=zipfile.ZIP_DEFLATED)
            newZip.close()


ZipFiles('U:\\ZZZ\\')





