
from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read('conftest.cfg')

for section in [ 'input', 'none' ]:
    print '%s section exists: %s' % (section, parser.has_section(section))
    for candidate in [ 'heinz1', 'service2', 'url', 'description' ]:
        print '%s.%-12s  : %s' % (section, candidate, parser.has_option(section, candidate))
    print





'''
parser = SafeConfigParser()
parser.read('conftest.cfg')

for candidate in [ 'input', 'service', 'pfad' ]:
    print '%-12s: %s' % (candidate, parser.has_section(candidate))
''' 
