#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time
from types import *
if os.name == 'nt':
    
    import win32service
    import win32serviceutil
    RUNNING = win32service.SERVICE_RUNNING
    STARTING = win32service.SERVICE_START_PENDING
    STOPPING = win32service.SERVICE_STOP_PENDING
    STOPPED = win32service.SERVICE_STOPPED
    
    def svcStatus(svc_name):
        return win32serviceutil.QueryServiceStatus(svc_name)





svc_name     = 'PatrolAgent'
status  = svcStatus(svc_name)
print svc_name


'''
    
    if status == RUNNING:

    if status == STOPPING:
        
        print "Status is stopping"
    elif status == RUNNING:
        print "Status is Running"
    elif status == STOPPED:
        print "Status is Running"
    else:
        if status == STARTING:
            print "Status nicht bekannt"
'''