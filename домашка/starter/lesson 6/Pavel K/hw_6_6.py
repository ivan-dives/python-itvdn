import os
path = 'D:\\dirforrange' #В виде строки храниться путь к нашей корневой папке

def obxoddir(path):
    for i in os.listdir(path): # обходим все элементы папки
        if os.path.isdir(path +'\\' + i):
            createtxt(path + '\\' + i)

def createtxt(way):
    s1 = open(str(way) +'\\'+ '1.txt', 'w')
    print(way + '.txt')
    k = 'Все права принадлежат ___ номер для связи тел...!'
    s1.write(k)
    s1.close()
    obxoddir(way)
obxoddir(path)