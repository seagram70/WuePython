#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os

# Alle Verzeichnisse und Dateien unterhalb dem Ordner ZZZ wird alles gelöscht.

for pathentry in os.walk('U:\\ZZZ', False):
    for dir in pathentry[1]:
        path = os.path.join(pathentry[0], dir)
        if os.path.islink(path):
            os.unlink(path)
        else:
            os.rmdir(path)
 
    for file in pathentry[2]:
        path = os.path.join(pathentry[0], file)
        os.unlink(path)