import os
import time
import os



class Monkey(object):
    def __init__(self):
        self._cached_stamp = 0
        self.filename = '/Users/Heinz-MacBook/Documents/workspace/gitwue/wuepython/watch.txt'

    def ook(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            print(' File has changed, so do something...')
