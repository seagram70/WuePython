#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    07.04.2015
# Last Update: 07.04.2015
#
# Copyright (c) 2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

def fibonacci(n):
    a, b = 1, 1
    print(a)
    for i in range(1,n,1):
        print(b)
        a, b = b, a+b

if __name__ == '__main__':
    fibonacci(20)