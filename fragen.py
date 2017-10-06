#!/usr/bin/python
# -*- coding: utf-8 -*-



Vorname = raw_input('Bitte Vornamen eingeben!')

if Vorname == 'Birne':
    print "Du bist meine Lehrerin, das programm stürzt aus sicherheitsgründen ab."
    exit()

if Vorname == 'Yannick':
    print ""

Nachname = raw_input('Bitte Nachnamen eingeben!')

Alter = raw_input('Bitte Alter eingeben!')

Hobbys = raw_input('Bitte Hobby eingeben!')

Farbe = raw_input('Bitte Deine Lieblingsfarbe eingeben!')



print ""
print "Dein Name ist" ,Vorname, Nachname,  "und Du bist" ,Alter, "alt."
print "Am liebsten gehst Du dem Hobby" ,Hobbys, "nach."
print ""
print "Meine Lieblingsfarbe ist" ,Farbe

if Vorname == 'Yannick':
    print 'und Ich bin der schönschte und beste'
else:
    print ''


