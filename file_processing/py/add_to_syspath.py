import sys, os

## how to modify sys.path
## bugs to vladimir dot kulyukin at gmail dot com
## change this to your directory
my_root_dir = '/home/vladimir/Dropbox/MyShare/programming/'

sys.path.append(my_root_dir)

## add all subdirectories in my_root_dir to sys.path.
for item in os.listdir(my_root_dir):
    path = my_root_dir + item
    if os.path.isdir(path):
        sys.path.append(path)

print sys.path
