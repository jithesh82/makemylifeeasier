# make a backup of the current file
# looks for v1_myfile in the current directory
# save the current to file to v(1+1)_myfile
# usage: backup.py filename

import glob

# file to make back up of
filename = 'backup.py'

# find all files containing 'filename' at the end
x = glob.glob('*' + filename)
print(x)

for file in x:

