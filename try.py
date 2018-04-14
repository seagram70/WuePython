#!/usr/bin/python3

import sys

arglist = ['start', 'stop', 'restart']

try:
    if sys.argv[1] in arglist:
        print("You have passed in", sys.argv[1])
        
        try:
            print("You have passed in", sys.argv[2])
        except IndexError:
            print("2222 No argument was passed, I'll do something else")
            exit()
            
    else:
        print(sys.argv[1], ' is not a valid argument')
        exit()

except IndexError:
    print("No argument was passed, I'll do something else")
    exit()
    

print('weiter')



    