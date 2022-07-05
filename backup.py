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

comments = None
if len(sys.argv) > 2:
    comments = sys.argv[2]

def sorterKey(name):
    """
    create key to sort the filenames
    sorted based on the number 11 etc in v11_myfile
    """
    # splits v11_myfile etc. at '_' 
    # find the v11 etc component by indexing to 0
    # strips v11 of v --> convert '11' to int
    name = name.split('_')[0].strip('v')
    key = int(name)
    return key

# find all files containing 'filename' at the end
filelist = glob.glob('*' + filename)
filelist_copy = filelist.copy()
filelist_copy.pop(filelist.index(filename))
filelist_copy.sort(key=sorterKey)
print('before: ', filelist_copy)

# number of previous versions 
# the list also contains actual file; hence -1
N = len(filelist) - 1

new_version_number = N + 1

newbkupname = 'v' + str(new_version_number) + '_' + \
        filename

#add comments at the top if present
if comments:
    comments = "# " + comments + "\n"
    with open(newbkupname, 'w') as f:
        f.write(comments)

# copy file: open origin file in read binary mode and read
# open new file in write binary mode and write
fcontent = open(filename, 'rb').read()
open(newbkupname, 'ab').write(fcontent)

print('\n')

# find all files containing 'filename' at the end
filelist = glob.glob('*' + filename)
filelist.pop(filelist.index(filename))
filelist.sort(key=sorterKey)
print('after: ', filelist)
