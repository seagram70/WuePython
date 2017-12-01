#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        03.05.2017
# Modified:       
# Program:        Zeitumstellung.py

# Description:    Stellt die Configfiles automatisch um am Datum der Zeitumstellung.
#                 funktioniert bis 2023


import socket

def EnvironmentsVDFS():
    if socket.gethostname() in ['mpzhwmvdfs01', 'mpzhwsvdfs02', 'mpzhwsvdfs03', 'mpzhwsvdfs04', 'mpzhwsvdfs05', 'mpzhwsvdfs06', 'mpzhwfvdfs07']:
        env = 'PROD'
        print env

    elif socket.gethostname() in ['mislwmvdfs41', 'mislwsvdfs42', 'mislwsvdfs43', 'mislwsvdfs44', 'mislwsvdfs45', 'mislwsvdfs46', 'mislwfvdfs47']:
        env = 'INTEG'
        print env
        
    elif socket.gethostname() in ['N36165']:
        env = 'LOCAL'
        print env
        
    else:
        print 'Wrong Environment'
        exit()    


EnvironmentsVDFS()