import os
import pathlib
import stat

#PATH = "D:\Python\Starter"
PATH = pathlib.Path(os.getcwd()) / '..'
os.chdir(PATH)


def path_tree(p):
    for f in os.listdir(p):
        f = p / f
        s = os.lstat(f)
        if stat.S_ISDIR(s.st_mode):
            path_tree(f)
        else:
            print(f)


path_tree(PATH)
