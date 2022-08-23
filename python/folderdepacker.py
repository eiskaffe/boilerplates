import json
import os
import shutil
import time

FOLDER_NAME = "all_files"

def get_loc(_file_):
    x = _file_.split('\\')
    x.pop()
    dir_loc = x[0]
    x.pop(0)
    for k in x:
        dir_loc = dir_loc + '/' + k
    return str(dir_loc + '/')

def printUI(_string, c = "+", v = "|", n = 78):
    print()
    print(c + "-" * n + c)
    print(v + _string.center(n) + v)
    print(c + "-" * n + c)

f = []
dirpath = []
dirnames = []
filenames = []
location = get_loc(__file__)
for (dirpath, dirnames, filenames) in os.walk(location):
    f.extend(filenames)
    break

try: os.mkdir(location + FOLDER_NAME)
except FileExistsError: dirnames.remove(FOLDER_NAME)

printUI("ALLIN FOLDER: " + location + FOLDER_NAME, n = 82)

start_time = time.time()
for index in dirnames:
    for x, y, value in os.walk(location + index):
        print("\n -= Opening " + '\x1b[1;37;40m' + x.split("/")[-1] + '\x1b[0m' + " folder =- " )
        for file in value:
            try: 
                shutil.move(location + x.split("/")[-1] + "/" + file, location + FOLDER_NAME + "/" + file)
                print('\x1b[0;32;40m' + f'Successfully moved {file}' + '\x1b[0m')
            except Exception as e: print('\x1b[1;37;41m' + f'Failed to move {location}{file} Error code: {str(e)}' + '\x1b[0m')
print(f"\nProgram finished in {'{0:.2f}'.format(time.time() - start_time)} second(s).")

input("Press ENTER to exit\n > ")