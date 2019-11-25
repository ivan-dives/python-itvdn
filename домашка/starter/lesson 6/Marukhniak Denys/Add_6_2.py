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

    return

    types = os.lstat(p)
    folder = stat.S_ISDIR(types.st_mode)  # вернёт True если папка
    if folder:

        #path = path + f'\\{os.listdir(path=path)[0]}'
        path_tree(path)
        return path
    else:
        print(path)
        return

path_tree(PATH)
