#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# import time module
import time

# print current date and time
print(time.strftime("%d.%m.%Y %H:%M:%S"))

# Abgekürzter Name des Wochentags.
print(time.strftime("%a"))

# Vollständiger Name des Wochenstags.
print(time.strftime("%A"))

# Abgekürzter Name des Monats.
print(time.strftime("%b"))

#Vollständiger Name des Monats.
print(time.strftime("%B"))

#Datum und Uhrzeit im Format des lokalen Systems.
print(time.strftime("%c"))

#Nummer des Tages im aktuellen Monat [01..31].
print(time.strftime("%d"))

#Stunde im 24-Stunden-Format [00..23].
print(time.strftime("%H"))

#Stunde im 12-Stunden-Format [01..12].
print(time.strftime("%I"))

#Nummer des Tages im Jahr [001..366].
print(time.strftime("%j"))

#Nummer des Monats [01..12].
print(time.strftime("%m"))

#Minute [00..59].
print(time.strftime("%M"))

#Die lokalisierte Form für AM beziehungsweise PM.
print(time.strftime("%p"))

#Sekunde [00..61].
print(time.strftime("S"))

#Nummer der aktuellen Woche im Jahr [00..53].
#Der Sonntag ist der erste Tag der Woche.
#Der Zeitraum vor dem ersten Sonntag Im Jahr wird als 0. Woche gewertet.
print(time.strftime("%U"))

#Nummer das aktuellen Tages in der Woche [0..6].
#     Der Sonntag wird als 0. Tag betrachtet.
print(time.strftime("%w"))

#Wie %U, nur dass der Montag der erste Tag der Woche ist.
print(time.strftime("%W"))

#Datum im Format des lokalen Systems.
print(time.strftime("%x"))

#Zeit im Format des lokalen Systems.
print(time.strftime("%X"))

#Jahreszahl ohne Jahrhundertangabe [00..99].
print(time.strftime("%y"))

#Jahreszahl mit Jahrhundertangabe.
print(time.strftime("%Y"))

#Name der lokalen Zeitzone oder ein leerer String, wenn keine lokale Zeitzone festgelegt wurde.
print(time.strftime("%Z"))

#%%   Erzeugt ein Prozentzeichen.