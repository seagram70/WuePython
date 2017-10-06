#!/usr/bin/python
#Datei test.txt einlesen

f = open ('test_in.txt')
print f.readlines()


'''
fobj_in = open('test_in.txt')
fobj_out = open('test_out.txt','w')

x = K51T
f.write (str(x))
'''
'''
i = 1
for line in fobj_in:
#    print(line.rstrip())
#    fobj_out.write(str(i) + "Zeile : " + line)
    fobj_out.write(K11T) + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

'''