#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import subprocess

#subprocess.call('a.py')
#subprocess.Popen( ['/usr/bin/python', '/a.py'], stdout=subprocess.PIPE )
subprocess.call( ['python', 'a.py'])
print ('ich bin fertig mit b')
