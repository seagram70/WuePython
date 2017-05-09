#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys


file = open('/Users/Heinz-MacBook/Documents/workspace/Privat/test.log', 'r')

print file.readlines(49)

keyword = 'HXD'
count = 0
for line in file:
#    print line
    if keyword in line:
        count = count + 1

print count