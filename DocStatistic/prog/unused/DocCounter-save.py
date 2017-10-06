#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Author:         Heinz Wuethrich
# Created:        03.03.2017
# Modified:       
# Program:        DocCounter.py

# Description:    Liest ein Delta File ein und zählt jeden einzelnen
#                 Doctyp und schreibt diese Zahlen in Statistik File
#

import os
import time
import logging
import sys

# ****************************
#    Configfile variablen    *
# ****************************
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser                           # ver. < 3.0

config = ConfigParser()                                             # instantiate

# parse existing config file
#config.read('..\\cfg\\DocStat.cfg')                                   # For local use
config.read('F:\\Programs\\DocStatistic\\cfg\\DocStat.cfg')            # For server use
logPath      = config.get('input', 'logPath')
DeltaFiles   = config.get('input', 'DeltaFiles')
StatDir      = config.get('input', 'StatDir')
DeltaFake    = config.get('input', 'DeltaFake')
StatFile     = config.get('input', 'StatFile')
outputFile   = config.get('input', 'outputFile')
server       = config.get('input', 'server')
environment  = config.get('input', 'environment')
labelTrun    = config.get('input', 'labelTrun')
labelNetting = config.get('input', 'labelNetting')



logger = logging.getLogger("   v1.0.1  ")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler(logPath)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]  %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


#print sys.argv[1]


# ***************************************************************
#    Input variablen und Pfade                                  *
# ***************************************************************
inputFile   = sys.argv[1]
#inputFile   =  'VDMMAPS.Y2017065.T01S'

logger.info('Starting DocCounter per Doc Type')

# ***************************************************************
#    def Functions                                              *
# ***************************************************************
def docCountPerDoc(doc):
    f1 = open(DeltaFiles + inputFile, 'r')
    tempfile = StatDir + 'temp-'
    
    for line in f1:
        linestrip = line[0:3]
        if str(doc) in linestrip:
            out = open(tempfile + doc, 'a+')
            out.write(doc + ' Files' + '\n')
            out.close()
            logger.info('Tempfile for DOC ' + doc + '  now created')
    f1.close()
logger.info('strip the first 3 digits an writetd to the tempfile per DocType')

            
    
def writeDocs2StatFile(doc):
    f2 = open(StatDir + outputFile, 'a')

    if os.path.exists(StatDir + 'temp-' + doc):
        with open(StatDir + 'temp-' + doc) as f:
            line_count = len(f.readlines())
            print line_count
#            logger.info(' ' + line_count + doc + ' Docs are in the File')
            f.close()
            f2.write(doc + ' = ' + str(line_count) + '\n')
            f2.close()
            os.remove(StatDir + 'temp-' + doc)
            logger.info('the tempfile ' + StatDir + 'temp-' + doc + ' are removed')
    else:
        print 'Der Doctyp ' + doc + ' ist nicht vorhanden.'
        

# ***************************************************************
#    def Functions                                              *
# ***************************************************************
docCountPerDoc('XCD'); docCountPerDoc('FAD'); docCountPerDoc('XTD'); docCountPerDoc('XRD'); docCountPerDoc('XBD'); docCountPerDoc('EMD')
docCountPerDoc('FSD'); docCountPerDoc('FZD'); docCountPerDoc('XPD'); docCountPerDoc('XSD'); docCountPerDoc('FQD'); docCountPerDoc('DED')
docCountPerDoc('HXD'); docCountPerDoc('DID'); docCountPerDoc('YWD'); docCountPerDoc('EUD'); docCountPerDoc('YSD'); docCountPerDoc('CID') 
docCountPerDoc('FTD'); docCountPerDoc('VKD'); docCountPerDoc('DGD'); docCountPerDoc('FID'); docCountPerDoc('CLD'); docCountPerDoc('CSD')
docCountPerDoc('HUD'); docCountPerDoc('ZTD'); docCountPerDoc('DTD'); docCountPerDoc('IGD'); docCountPerDoc('XUD'); docCountPerDoc('IAD') 
docCountPerDoc('ERD'); docCountPerDoc('ZAD'); docCountPerDoc('DAD'); docCountPerDoc('RFD'); docCountPerDoc('YGD'); docCountPerDoc('CMD') 
docCountPerDoc('YUD'); docCountPerDoc('XND'); docCountPerDoc('CRD'); docCountPerDoc('IUD'); docCountPerDoc('ZSD'); docCountPerDoc('VTD') 
docCountPerDoc('FHD'); docCountPerDoc('IRD'); docCountPerDoc('ISD'); docCountPerDoc('CND'); docCountPerDoc('OPD'); docCountPerDoc('ZKD') 
docCountPerDoc('FDD'); docCountPerDoc('ZED'); docCountPerDoc('CKD'); docCountPerDoc('CWD'); docCountPerDoc('MED'); docCountPerDoc('CFD')
docCountPerDoc('DBD'); docCountPerDoc('HSD'); docCountPerDoc('SAD'); docCountPerDoc('SGD'); docCountPerDoc('SBD'); docCountPerDoc('SDD') 
docCountPerDoc('SED'); docCountPerDoc('SFD'); docCountPerDoc('CAD'); docCountPerDoc('CGD'); docCountPerDoc('ZCD'); docCountPerDoc('SOD') 
docCountPerDoc('SND'); docCountPerDoc('ZVD'); docCountPerDoc('CBD'); docCountPerDoc('FUD'); docCountPerDoc('CDD'); docCountPerDoc('HPD') 
docCountPerDoc('IHD'); docCountPerDoc('SMD'); docCountPerDoc('CED'); docCountPerDoc('SQD'); docCountPerDoc('DCD'); docCountPerDoc('HGD')
docCountPerDoc('SHD'); docCountPerDoc('TMD'); docCountPerDoc('CCD'); docCountPerDoc('YBD'); docCountPerDoc('IBD'); docCountPerDoc('LRD') 
docCountPerDoc('CZD')



f2 = open(StatDir + outputFile, 'a')
f2.write('************************************' + '\n')
f2.write('*** DOC Statistik vom ' + time.strftime('%Y-%m-%d') + ' ***' + '\n')
f2.write('***  File ' + inputFile +  '  ***' + '\n')
f2.write('************************************' + '\n')
f2.close()


writeDocs2StatFile('XCD'); writeDocs2StatFile('FAD'); writeDocs2StatFile('XTD'); writeDocs2StatFile('XRD'); writeDocs2StatFile('XBD'); writeDocs2StatFile('EMD')
writeDocs2StatFile('FSD'); writeDocs2StatFile('FZD'); writeDocs2StatFile('XPD'); writeDocs2StatFile('XSD'); writeDocs2StatFile('FQD'); writeDocs2StatFile('DED')
writeDocs2StatFile('HXD'); writeDocs2StatFile('DID'); writeDocs2StatFile('YWD'); writeDocs2StatFile('EUD'); writeDocs2StatFile('YSD'); writeDocs2StatFile('CID') 
writeDocs2StatFile('FTD'); writeDocs2StatFile('VKD'); writeDocs2StatFile('DGD'); writeDocs2StatFile('FID'); writeDocs2StatFile('CLD'); writeDocs2StatFile('CSD')
writeDocs2StatFile('HUD'); writeDocs2StatFile('ZTD'); writeDocs2StatFile('DTD'); writeDocs2StatFile('IGD'); writeDocs2StatFile('XUD'); writeDocs2StatFile('IAD') 
writeDocs2StatFile('ERD'); writeDocs2StatFile('ZAD'); writeDocs2StatFile('DAD'); writeDocs2StatFile('RFD'); writeDocs2StatFile('YGD'); writeDocs2StatFile('CMD') 
writeDocs2StatFile('YUD'); writeDocs2StatFile('XND'); writeDocs2StatFile('CRD'); writeDocs2StatFile('IUD'); writeDocs2StatFile('ZSD'); writeDocs2StatFile('VTD') 
writeDocs2StatFile('FHD'); writeDocs2StatFile('IRD'); writeDocs2StatFile('ISD'); writeDocs2StatFile('CND'); writeDocs2StatFile('OPD'); writeDocs2StatFile('ZKD') 
writeDocs2StatFile('FDD'); writeDocs2StatFile('ZED'); writeDocs2StatFile('CKD'); writeDocs2StatFile('CWD'); writeDocs2StatFile('MED'); writeDocs2StatFile('CFD')
writeDocs2StatFile('DBD'); writeDocs2StatFile('HSD'); writeDocs2StatFile('SAD'); writeDocs2StatFile('SGD'); writeDocs2StatFile('SBD'); writeDocs2StatFile('SDD') 
writeDocs2StatFile('SED'); writeDocs2StatFile('SFD'); writeDocs2StatFile('CAD'); writeDocs2StatFile('CGD'); writeDocs2StatFile('ZCD'); writeDocs2StatFile('SOD') 
writeDocs2StatFile('SND'); writeDocs2StatFile('ZVD'); writeDocs2StatFile('CBD'); writeDocs2StatFile('FUD'); writeDocs2StatFile('CDD'); writeDocs2StatFile('HPD') 
writeDocs2StatFile('IHD'); writeDocs2StatFile('SMD'); writeDocs2StatFile('CED'); writeDocs2StatFile('SQD'); writeDocs2StatFile('DCD'); writeDocs2StatFile('HGD')
writeDocs2StatFile('SHD'); writeDocs2StatFile('TMD'); writeDocs2StatFile('CCD'); writeDocs2StatFile('YBD'); writeDocs2StatFile('IBD'); writeDocs2StatFile('LRD') 
writeDocs2StatFile('CZD')

