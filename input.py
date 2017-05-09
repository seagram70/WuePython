#!/usr/bin/python

age = int(input("Gib dein Alter ein: "))
 
if age <= 12:
        print("Es ist toll, ein Kind zu sein!")
elif age in range(13, 20):
        print("Du bist ein Teenager!")
else:
        print("Zeit zum erwachsen werden")
 
# Wenn eine dieser Aussagen wahr ist,
# dann wird die entsprechende Nachricht ausgegeben.
# Wenn keine der Aussagen wahr ist, dann wird die
# "else"-Nachricht ausgegeben.