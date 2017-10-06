#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
#from nt import rename
#from multiprocessing.pool import job_counter

path="U:\\ZZZ"
pfad_out1="U:\\ZZZ\\AAA"
pfad_out2="U:\\ZZZ\\BBB"



survey_type = ['MB','SB']

#File path for directory of interest
path = r'U:\ZZZ'

#List of all files in set directory
file_list = os.listdir(path)


for file in file_list:
    print file