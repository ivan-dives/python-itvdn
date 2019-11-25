import os
import stat


def path_tree(path):
    types = os.lstat(path)
    folder = stat.S_ISDIR(types.st_mode)  # вернёт True если папка
    if folder:
        path = path + f'\\{os.listdir(path=path)[0]}'
        path_tree(path)
        return path
    else:
        print(path)
        return


PATH = "D:\Python\Starter"
path_tree(PATH)
