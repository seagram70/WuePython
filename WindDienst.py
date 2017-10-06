#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Windows-Dienst, der einen XMLRPC-Server auf Port 53479 startet und
auf Anfragen wartet.

Filename:      SimpleXmlrpcService.py
Created:       2006-12-23 by Gerold Penz - gerold.penz(at)tirol.utanet.at
Requirements:  Python: http://www.python.org/
               pywin32: http://sourceforge.net/projects/pywin32/
"""

import win32serviceutil
import win32service
import servicemanager
import threading
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import time

PORT = 53479


class MyXmlrpcHandler(object):
    """
    In dieser Klasse stehen alle Funktionen, die per XMLRPC-Server zur Verfügung
    gestellt werden.
    """
    
    def get_quit_dummy(self):
        """
        Gibt den String "Quit" zurück.
        """
        
        # Ins Eventlog schreiben
        servicemanager.LogInfoMsg("Der String 'Quit' wird gesendet...")
        
        return "Quit"
    
    
    def get_helloworld(self):
        """
        Gibt den String "Hallo Welt" zurück.
        """
        
        # Ins Eventlog schreiben
        servicemanager.LogInfoMsg("Der String 'Hallo Welt' wird gesendet...")
        
        return "Hallo Welt"


class MyXmlrpcServer(SimpleXMLRPCServer, threading.Thread):
    """
    Diese Klasse stellt den XMLRPC-Server dar. Der Server läuft als 
    eigenständiger Thread.
    """
    
    def __init__(
        self, addr, requestHandler = SimpleXMLRPCRequestHandler, logRequests = True
    ):
        """
        Initialisiert den XMLRPCServer und den Thread.
        """
        
        # Instanz initialisieren
        SimpleXMLRPCServer.__init__(self, addr, requestHandler, logRequests)
        threading.Thread.__init__(self)
        # Event zum Stoppen des Threads
        self.stopevent = threading.Event()
        # Handler-Klassen an den XMLRPC-Server binden
        self.register_instance(MyXmlrpcHandler())
    
    
    def run(self):
        """
        Hier läuft der Thread und wartet entweder auf das Abbruchsignal oder
        auf einen neuen XMLRPC-Request.
        """
        
        while True:
            # Prüfen ob der Server beendet werden soll
            if self.stopevent.isSet():
                # Ins Eventlog schreiben
                servicemanager.LogInfoMsg("Der XMLRPC-Server wird gestoppt...")
                # Schleife abbrechen
                break
            # Auf eine Anfrage warten
            self.handle_request()
    
    
    def stop(self):
        """
        Stoppt den Thread und somit den XMLRPCServer.
        """
        
        # Stopevent auslösen
        self.stopevent.set()
        
        # Eine Sekunde warten, damit dem Server genug Zeit gelassen wird, einen
        # evt. noch offenen Request zu beenden.
        time.sleep(1)
        
        # Zum Server verbinden und einen Request senden, damit der Server
        # nicht mehr blockiert.
        server = xmlrpclib.ServerProxy("http://localhost:" + str(PORT))
        server.get_quit_dummy()
        
        # Noch eine Sekunde warten, damit auch wirklich genug Zeit zum Beenden
        # gelassen wird.
        time.sleep(1)


class SimpleXmlrpcService(win32serviceutil.ServiceFramework):
    """
    Ich bin der Dienst...
    """
    
    _svc_name_ = "simplexmlrpcservice"
    _svc_display_name_ = "Simple XMLRPC Service"
    _svc_description_ = "Einfacher XMLRPC-Server-Dienst"


    def __init__(self, args):
        """
        Dienst initialisieren und Stopevent erstellen.
        """
        
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stopevent = threading.Event()
    

    def SvcStop(self):
        """
        Wird von Windows ausgeführt wenn der Dienst beendet werden soll.
        """
        # Ins Eventlog schreiben
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # Das Stopevent auslösen. Dadurch wird der Dienst nicht mehr 
        # blockiert und kann sich beenden. Info: Der Code blockiert in dieser
        # Klasse bei ``self.stopevent.wait()`` in der Methode ``SvcDoRun``.
        self.stopevent.set()

    
    def SvcDoRun(self):
        """
        Wird von Windows ausgeführt wenn der Dienst gestartet werden soll.
        Startet den XMLRPC-Server und wartet.
        """
        
        # Ins Eventlog schreiben
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        
        # XMLRPCServer starten
        server = MyXmlrpcServer(("localhost", PORT), logRequests = False)
        server.start()
        
        # Ins Eventlog schreiben
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        
        # Hier wird gewartet, bis der Dienst beendet wird
        self.stopevent.wait()
        
        # XMLRPCServer beenden
        server.stop()
        
        # Ins Eventlog schreiben
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)


def main():
    win32serviceutil.HandleCommandLine(SimpleXmlrpcService)
    
    
if __name__=='__main__':
    main()