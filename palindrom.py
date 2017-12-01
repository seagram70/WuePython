#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creation:    07.01.2017
# Last Update: 07.01.2017
#
# Author:		Heinz Wüthrich


infile = open("test_in.txt","r")     
text = infile.read()    
infile.close()    
word = text.find("K11T")
print (word)
