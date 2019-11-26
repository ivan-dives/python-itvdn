import glob

# my_path = '/Program Files'
#
# files = glob.glob(my_path + '/**', recursive=True)
#
# print(files)

import os
import pathlib
import stat


def folders_tree(p):
    for f in os.listdir(p):
        f = p / f
        s = os.lstat(f)
        if stat.S_ISDIR(s.st_mode):
            folders_tree(f)
        else:
            print(f)


PATH = pathlib.Path(os.getcwd()) / '..'
os.chdir(PATH)
folders_tree(PATH)