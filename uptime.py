#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Creation:    25.05.2015
# Last Update: 25.05.2015
#
# Copyright (c) 2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

# import required modules
from datetime import timedelta

# function to get system uptime
def uptime():
    with open('/proc/uptime', 'r') as file:
        return str(timedelta(seconds = float(file.readline().split()[0])))

# main function
def main():
    print "System uptime: %s" % uptime()

#if __name__ == '__main__':
#  main()