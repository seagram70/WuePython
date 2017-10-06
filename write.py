#!/usr/bin/env python

#Creating a variable to start the count
'''
f = open("/Users/Heinz-MacBook/CloudStation/Python/intest.txt", "w")
count = 0

#Creating while loop
while count < 1000:
    f.write(count)
    print count
    count += 1
f.close()
'''

a = 0
b = "|"
while a < 5000000:
    a += 1 # Same as a = a + 1 
    new = (a,b)
    f = open("/Users/Heinz-MacBook/CloudStation/Python/intest.txt", "a") #opens file with name of "export.txt"
    f.write(str(new))
f.close()