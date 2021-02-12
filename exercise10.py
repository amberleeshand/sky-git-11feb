import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

'''
python_files = []
for file in glob.glob('*'):
    python_files.append(file)
print(python_files)
'''

print(glob.glob('*'))
# TODO: use os.path.getsize to find each file's size

print(os.path.getsize('exercise10.py'))

# TODO: Add a test to only display files that are not zero length

for file in glob.glob('*'):
    if os.path.getsize(file) != 0:
        print(file)


# TODO: Remove the leading directory name(s) from each filename
#  before you print it -
# using os.path.basename()
