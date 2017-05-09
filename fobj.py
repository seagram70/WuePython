#!/usr/bin/env python
# -*- encoding: utf-8 -*-

fobj = open("C:\Daten\Python\gaga.txt", 'a')
fobj.write("new last line gaga\n")
fobj.write("ydfdljfksdfjklsdfjlsdf\n")
fobj.write("adfssfsdfsfsdfsdf\n")
fobj.write("sffssff\n")

fobj.close()

fobj = open("C:\Daten\Python\gaga.txt")
print fobj.read()
fobj.close()