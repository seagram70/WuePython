#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import zipfile
import os

def unzip(path, file):
    os.chdir(path)    # move to the folder with spam.zip
    spamZip = zipfile.ZipFile(file)
    spamZip.extractall()
    spamZip.close()
    
unzip('U:\\ZZZ\\', 'spam.zip')

