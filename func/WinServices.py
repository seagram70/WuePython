#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import win32serviceutil

def stop_service(service):
    try:
        ret =  win32serviceutil.QueryServiceStatus(service)
        print "check if Services exists"
        while ret[1] != 1:
            if ret[1] == 4:
                win32serviceutil.StopService(service)
            time.sleep(1) 
            ret =  win32serviceutil.QueryServiceStatus(service)
        print "" + service + " stopped"
#        return "" + service + " stopped"
    except:
        print "Error 1060 is allowd. The Service did not exist"


# ***************************************************************
#    Stop der VDFS Services   je nach Umgebung                  *
# ***************************************************************
listeServices = ["OFCService", "PatrolAgent", "VDFSAgentControllerService"]

for service in listeServices:
    stop_service(service)
    
# -------------------------------------------------------------------------------------------    
def service_info(action, machine, service):
    if action == 'stop': 
        win32serviceutil.StopService(service, machine)
        print '%s stopped successfully' % service
    elif action == 'start': 
        win32serviceutil.StartService(service, machine)
        print '%s started successfully' % service
    elif action == 'restart': 
        win32serviceutil.RestartService(service, machine)
        print '%s restarted successfully' % service
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            print "%s is running normally" % service 
        else:
            print "%s is *not* running" % service 

if __name__ == '__main__':
    machine = 'mislwfvdfs47'
    service = 'Watchdog-FFM'
    action = 'start'
    service_info(action, machine, service)

