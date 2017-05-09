#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket

if socket.gethostname() == 'Heinzs-iMac.local':
    pathlocal = '/Users/heinz-ssd/Documents/workspace/gitwue/wuepython/'
else:
    pathlocal == '/Users/Heinz-MacBook/Documents/workspace/gitwue/wuepython/'

print pathlocal

#file = open('/Users/Heinz-MacBook/Documents/workspace/wuepythons/test.log', 'r')
file = open('/Users/heinz-ssd/Documents/workspace/gitwue/wuepython/test.log', 'r')

print file.readlines(49)

keyword = 'HXD'
count = 0
for line in file:
#    print line
    if keyword in line:
        count = count + 1

print count

