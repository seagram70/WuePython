#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

print('hallo')

for i in range(3):
    print(i)
    time.sleep(1)

print('a ist jetzt auch fertig')
fobj = open("/Users/Heinz-MacBook/Documents/workspace/gitwue/wuepython/aaaagaga.txt", 'a')
fobj.write("ende teil aaa\n")
fobj.write("ende teil aaa\n")
fobj.write("ende teil aaa\n")
fobj.write("ende teil aaa\n")

fobj.close()
