#!/usr/bin/python
#Datei test.txt einlesen

fobj_in = open('test_in.txt')
fobj_out = open('test_out.txt','w')

i = 1
for line in fobj_in:
    print(line.rstrip())
#    fobj_out.write(str(i) + "Zeile : " + line)
    fobj_out.write("Zeile: " +(str(i))  +(" ") + line)
    i = i + 1
fobj_in.close()
fobj_out.close()