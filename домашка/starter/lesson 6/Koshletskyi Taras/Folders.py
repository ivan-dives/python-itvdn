import os

path = '/Users/taraskoshletskyi/test'


def tree(path):
    if len(os.listdir(path)) == 0:
        print(path)
    for i in os.listdir(path):
        if os.path.isfile(f'{path}/{i}'):
            print(f'{path}/{i}')
        elif os.path.isdir(f'{path}/{i}'):
            tree(f'{path}/{i}')


tree(path)

