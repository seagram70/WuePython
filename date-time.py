#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# import time module
import time

print(time.strftime("%d.%m.%Y %H:%M:%S"))   # print current date and time
print(time.strftime("%a"))                  # Abgekürzter Name des Wochentags.
print(time.strftime("%A"))          # Vollständiger Name des Wochenstags.
print(time.strftime("%b"))          # Abgekürzter Name des Monats.
print(time.strftime("%B"))          #Vollständiger Name des Monats.
print(time.strftime("%c"))              #Datum und Uhrzeit im Format des lokalen Systems.
print(time.strftime("%d"))              #Nummer des Tages im aktuellen Monat [01..31].
print(time.strftime("%H"))              #Stunde im 24-Stunden-Format [00..23].
print(time.strftime("%I"))              #Stunde im 12-Stunden-Format [01..12].
print(time.strftime("%j"))                  #Nummer des Tages im Jahr [001..366].
print(time.strftime("%m"))                  #Nummer des Monats [01..12].
print(time.strftime("%M"))              #Minute [00..59].
print(time.strftime("%p"))                  #Die lokalisierte Form für AM beziehungsweise PM.
print(time.strftime("S"))                       #Sekunde [00..61].
print(time.strftime("%U"))                  #Nummer der aktuellen Woche im Jahr [00..53].#Der Sonntag ist der erste Tag der Woche.
                                            #Der Zeitraum vor dem ersten Sonntag Im Jahr wird als 0. Woche gewertet.
print(time.strftime("%w"))                  #Nummer das aktuellen Tages in der Woche [0..6].
                                            #     Der Sonntag wird als 0. Tag betrachtet.
print(time.strftime("%W"))          #Wie %U, nur dass der Montag der erste Tag der Woche ist.
print(time.strftime("%x"))          #Datum im Format des lokalen Systems.
print(time.strftime("%X"))      #Zeit im Format des lokalen Systems.
print(time.strftime("%y"))      #Jahreszahl ohne Jahrhundertangabe [00..99].
print(time.strftime("%Y"))      #Jahreszahl mit Jahrhundertangabe.
print(time.strftime("%Z"))          #Name der lokalen Zeitzone oder ein leerer String, wenn keine lokale Zeitzone festgelegt wurde.



# oder zum Beispiel als parameter SET
today = time.strftime("%d.%m.%Y")
year  = time.strftime("%Y")
hms   = time.strftime("%H:%M:%S")
jul   = time.strftime("%j")
day   = time.strftime("%A")

print (day)
