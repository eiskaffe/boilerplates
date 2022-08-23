from os import walk
from time import sleep
from random import randint

x = __file__.split('\\')
x.pop()
dir_loc = x[0]
x.pop(0)
for k in x: dir_loc = dir_loc + '/' + k
location = str(dir_loc + '/')

f = []
dirpath = []
dirnames = []
filenames = []
for (dirpath, dirnames, filenames) in walk(location):
    f.extend(filenames)
    break

try: print(filenames[randint(0, len(filenames))])
except IndexError: print("No files in root.")

sleep(3)