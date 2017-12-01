#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Alle Dateien in einem Directory welch mit "T." beginnen wird das T und de Punkt enfern.

import os
from os import rename, listdir


def BadPrefix(path, prefix):
    os.chdir(path)
    badprefix = prefix
    fnames = listdir('.')
    
    for fname in fnames:
        if fname.startswith(badprefix):
            rename(fname, fname.replace(badprefix, '', 1))
            

BadPrefix('U:\\ZZZ', 'T.')