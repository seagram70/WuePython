#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('conftest.cfg')

items = parser.items( "service" )
for key, value in items:
    #do something with path
    print key
    print value





'''
for section_name in parser.sections():
    print 'Section:', section_name
    print '  Options:', parser.options(section_name)
    print section_name
    print parser.options(section_name)
    for name, value in parser.items(section_name):
        print '  %s = %s' % (name, value)
    print

a = parser.get('service', 'servicelist')
print a
'''

    
