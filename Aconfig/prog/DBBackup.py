#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
'''
# ****************************
#    Configfile variablen    *
# ****************************
from configparser import SafeConfigParser
parser = SafeConfigParser()
parser.read('../cfg/configfile.cfg')    # For local use
'''

# Load the configuration file
with open('../cfg/configfile.cfg') as f:
    from configparser import SafeConfigParser
    parser = SafeConfigParser()
    sample_config = f.read()
parser = SafeConfigParser(allow_no_value=True)
parser.readfp(io.BytesIO(sample_config))

# List all contents
print("List all contents")
for section in parser.sections():
    print("Section: %s" % section)
    for options in parser.options(section):
        print("x %s:::%s:::%s" % (options,
                                  parser.get(section, options),
                                  str(type(options))))

# Print some contents
print("\nPrint some contents")
print(parser.get('other', 'use_anonymous'))  # Just get the value
print(parser.getboolean('other', 'use_anonymous'))  # You know the datatype?











exit()




items = parser.items( "pfade" )
dict = {}
for keys, values in items:
    dict.append(keys, values)
pfadelist = dict


print(pfadelist)
#print(PFAD_LOG)

exit()

'''
for section_name in parser.sections():
#    print ('Section:', section_name)
#    print ('  Options:', parser.options(section_name))
    for name, value in parser.items(section_name):
        print ('  %s = %s' % (name, value))
    print()
    
#print(PFAD_LOG)   
exit()
'''

PFAD_LOG        = parser.get('pfade', 'PFAD_LOG')
LOGFILENAME     = parser.get('pfade', 'LOGFILENAME')
Drive           = parser.get('pfade', 'Drive')
environment     = parser.get('pfade', 'environment')


# ***************************************************************
#    auslesen der config section "server" und section           *
#    services aus dem config File                               *
# ***************************************************************
#HOST        = (socket.gethostname())
items = parser.items( "databases" )
liste = []
for keyServer, valueServer in items:
    liste.append(valueServer)
serverlist = liste


print(serverlist)
print(PFAD_LOG)
print(LOGFILENAME)
print(Drive)
print(environment)




'''
items = parser.items( "services" )
listeserv = []
for keyservices, valueservices in items:
    listeserv.append(valueservices)
listeServices = listeserv

# ***************************************************************
#    check is Database Backup File exists                       *
# ***************************************************************
while not wait4Files("H:\\", "VDFS_DATA_????????_??????_T01S.BAK"):
    print "Sleeping for 60 sec"
    logger.info('Sleeping for 60 sec')
    time.sleep(60)

# ***************************************************************
#    30 min wait until the DB Backup file is closed             *
#    VDFS_DATA_????????_??????_T01S.BAK                         *
# ***************************************************************
time.sleep(1800)

# ***************************************************************
#    Stop der VDFS Services   je nach Umgebung                  *
# ***************************************************************
for service in listeServices:
    stop_service(service)
    
# ***************************************************************
#    list logfiles without Directorys                           *
# ***************************************************************
logfiles = [f for f in listdir(PFAD_LOG) if isfile(join(PFAD_LOG, f))]
logger.info('listdir to the logdirectory')

# ***************************************************************
#    Create Zip Directory for Versions > 5                      *
# ***************************************************************
os.chdir(PFAD_ARCH)
zipdir = (time.strftime("Logfiles-%Y-%m-%d"))
if exists(zipdir):
    logger.error('The Zip archive Dir allready exists, the Script allows just one run per Day')
    try:
        reboot_server(serverlist)
    except Exception,e:
        logger.error('not all Server are rebootet', exc_info=True)
        exit()
else:
    os.mkdir(zipdir)
    logger.info('ZIP Directory created for versions >5')

    for files in os.listdir(PFAD_ARCH):
        if files.endswith(".5"):
            newZip = zipfile.ZipFile(files + '.zip', 'w')
            newZip.write(files, compress_type=zipfile.ZIP_DEFLATED)
            newZip.close()
            shutil.move(files + ".zip", zipdir)

logger.info('all Files with version >5 are zipped and moved')    

# ***************************************************************
#    Log Files wrden in das log_archive Directory verschoben    *
#    und wieder als leere Files angelegt                        *
# ***************************************************************
os.chdir(PFAD_LOG)
for lFiles in logfiles:
    try:
        shutil.move(lFiles, PFAD_ARCH)
    except Exception,e:
        logger.warn('One or more logfiles allready exists in the log_archive Directory without any extensions', exc_info=True)
logger.info('Logfiles moved to the log_archive Directory')
    

try:
    for nFiles in logfiles:
        f = open(nFiles, 'w+')
        f.close()
except Exception, e:
    logger.error('IOError: [Errno 13] Permission denied: ' + nFiles + ' ', exc_info=True)

logger.info('New empty lofiles are created')

# ***************************************************************
#    LogRollover im Log_archive Directory, max 5 Versionen     *
#    und wieder als leere Files angelegt                        *
# ***************************************************************
os.chdir(PFAD_ARCH)
for ff in logfiles:
    my_logger = logging.getLogger(ff)
#    my_logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(ff, backupCount=5)
    my_logger.addHandler(handler)
    my_logger.handlers[0].doRollover()
    handler.close()
logger.info('Logfiles are rolled in the log_archive Directory')

# ***************************************************************
#    Die Temporaer angelegten logdateien werden geloescht       *
# ***************************************************************
try:
    for fFiles in logfiles:
        os.remove(fFiles)
except IOError:
    logger.error(' ', exc_info=True)

logger.info('all empty logfiles in the log_archive Directory are deletet')

# *************************************************************
#    Shutdown Slave und Fileserver                            *
# *************************************************************
try:
    reboot_server(serverlist)
except Exception,e:
    logger.error('not all Server are rebootet', exc_info=True)

'''