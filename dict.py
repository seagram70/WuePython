#!/usr/bin/env python
# -*- encoding: utf-8 -*-



from time import sleep

dict1 = {1 : "a test", (2, 54) : True, False : 0}
dict2 = {}

if False in dict1:

    print dict1[False]

print dict1.keys()

sleep (5)