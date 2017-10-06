#!/usr/bin/env python
# -*- encoding: utf-8 -*-

list1 = []
try:
    fobj = open("C:\Daten\Python\gaga.txt")
    list1 = fobj.readlines()
    print "einfach perfekt das Script"
    
except IOError as e:
    print 'File could not opened: %s' %e
    exit()

except NameError as e:
    print 'falscher Filenam: %s' %e
    exit()

except:
    print 'an another error'
    
finally:
    fobj.close()