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
print word

'''

with open ("test_in.txt") as infile:
    text = infile.read ()
index = text.find(str("K71T"))
print()

'''

'''
def isPalindrom(a):
    return a == a[::-1]

fInp = open("test_in.txt")
fOut = open("palindrom.txt", "w")

print "Searching for palindroms..." 
while True:
    word = fInp.readline()
    if word == "":
    if word == K11T:     
    break
    word = word[:-1] # remove trailing \n
    word = word.lower() # make lowercase
    if isPalindrom(word):
        print word
        fOut.write(word + "\n")
fInp.close()        
fOut.close()
print "All done"
'''