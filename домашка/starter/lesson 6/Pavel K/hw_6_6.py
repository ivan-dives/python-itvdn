import pathlib
import os

#PATH = pathlib.Path('D:\\dirforrange')
PATH = pathlib.Path('/home/ivan/PycharmProjects/python-itvdn/домашка/starter/lesson 6')
#path = 'D:\\dirforrange' #В виде строки храниться путь к нашей корневой папке


def obxoddir(path):
    for i in os.listdir(path): # обходим все элементы папки
        p = path / i
        if os.path.isdir(p):
            createtxt(p)


def createtxt(way):
    f = way / '1.txt'
    with open(f, 'w') as s1:
        print(f)
        k = 'Все права принадлежат ___ номер для связи тел...!'
        s1.write(k)
    obxoddir(way)


obxoddir(PATH)