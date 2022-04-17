#!/usr/bin/env python3

# make a backup of the current file
# looks for v1_myfile in the current directory
# save the current to file to v(1+1)_myfile
# usage: backup.py filename
# backups are saved like v1_myfile, v2_myfile etc.
# with myfile containing the latest update and v2_ the previous
# version v1_ previous-previous version and so on

import glob
import sys

# file to make back up of
filename = sys.argv[1] #'backup.py' 

# find all files containing 'filename' at the end
filelist = glob.glob('*' + filename)
filelist.sort()
print('before: ', filelist)

# number of previous versions 
# the list also contains actual file; hence -1
N = len(filelist) - 1

new_version_number = N + 1

newbkupname = 'v' + str(new_version_number) + '_' + \
        filename

fcontent = open(filename, 'rb').read()
open(newbkupname, 'wb').write(fcontent)

# find all files containing 'filename' at the end
filelist = glob.glob('*' + filename)
filelist.sort()
print('after: ', filelist)
