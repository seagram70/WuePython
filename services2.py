#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import win32serviceutil
import time


listeServices = ["VDFSUpdateAgentService_1", "VDFSStatisticAgentService_1", "VDFSWebAgentService_1", "VDFSSchedulerService",
                     "VDFSFlashAgentService_1", "VDFSAgentControllerService", "PatrolAgent", "MQCLI-RW", "SixMessengerClientAgent",
                     "SysNfsIpAgent", "VDFS-Cron-Service", "VDFSMQ-Client", "Watchdog-VDFS"]


def stop_service(service):
    try:
        ret =  win32serviceutil.QueryServiceStatus(service)
        print "check ob Service existiert"
        while ret[1] != 1:
            if ret[1] == 4:
                win32serviceutil.StopService(service)
            time.sleep(1) 
            ret =  win32serviceutil.QueryServiceStatus(service)
        print "" + service + "stopped"
        return "" + service + "stopped"
    except:
        print "1060 is allowd. The Service did not exist"    



for service in listeServices:
    stop_service(service)
